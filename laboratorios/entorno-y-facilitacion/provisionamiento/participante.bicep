// Entorno de laboratorio BCI Foundry Training Day: UN participante = UN resource group.
// Despliega (scope: resource group): cuenta Foundry (AIServices) + proyecto + deployments de chat y embeddings,
// roles del participante y un presupuesto con alertas. NO crea usuarios (lo hace Provision-Lab.ps1).
// Basado en infrastructure-setup-bicep/40-basic-agent-setup de microsoft-foundry/foundry-samples.
targetScope = 'resourceGroup'

@description('Número del participante, por ejemplo 01.')
param participantNumber string

@description('Object ID (Entra) del usuario o grupo participante.')
param participantObjectId string
@allowed([
  'User'
  'Group'
])
param principalType string = 'User'

@description('Región. Debe tener cuota para los modelos.')
param location string = 'eastus2'

@description('Modelo de chat y su versión.')
param chatModelName string = 'gpt-5-mini'
param chatModelVersion string = '2025-08-07'
@description('Capacidad en miles de TPM (GlobalStandard).')
param chatCapacity int = 10

@description('Modelo principal de los laboratorios (cuota limitada: ver Add-Modelo.ps1 para el reparto entre GlobalStandard y DataZoneStandard).')
param lunaModelName string = 'gpt-5.6-luna'
param lunaModelVersion string = '2026-07-09'
param lunaCapacity int = 4
@allowed([
  'GlobalStandard'
  'DataZoneStandard'
])
param lunaSkuName string = 'GlobalStandard'

@description('Modelo de embeddings (Día 2).')
param embeddingModelName string = 'text-embedding-3-small'
param embeddingModelVersion string = '1'
param embeddingCapacity int = 10

@description('Presupuesto mensual del RG en USD (solo alerta, no bloquea).')
param budgetAmount int = 10
@description('Primer día del mes de inicio del presupuesto (formato ISO).')
param budgetStartDate string = '2026-10-01T00:00:00Z'
@description('Correos que reciben las alertas del presupuesto.')
param budgetContactEmails array = []

param tags object = {}

var suffix = take(uniqueString(resourceGroup().id), 5)
var accountName = 'bcilab${participantNumber}-${suffix}'

// Foundry User: dataActions de CognitiveServices/* (agentes, modelos, Document Intelligence, Speech...).
var roleFoundryUser = '53ca6127-db72-4b80-b1b0-d745d6d5456d'
var roleReader = 'acdd72a7-3385-48ef-bd42-f606fba81ae7'

resource account 'Microsoft.CognitiveServices/accounts@2025-04-01-preview' = {
  name: accountName
  location: location
  tags: tags
  sku: {
    name: 'S0'
  }
  kind: 'AIServices'
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    allowProjectManagement: true
    customSubDomainName: accountName
    networkAcls: {
      defaultAction: 'Allow'
      virtualNetworkRules: []
      ipRules: []
    }
    publicNetworkAccess: 'Enabled'
    disableLocalAuth: true
  }
}

resource project 'Microsoft.CognitiveServices/accounts/projects@2025-04-01-preview' = {
  parent: account
  name: 'lab-${participantNumber}'
  location: location
  tags: tags
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    description: 'Proyecto de laboratorio BCI Foundry Training Day (participante ${participantNumber})'
    displayName: 'Lab ${participantNumber}'
  }
}

resource chatDeployment 'Microsoft.CognitiveServices/accounts/deployments@2024-10-01' = {
  parent: account
  name: chatModelName
  sku: {
    name: 'GlobalStandard'
    capacity: chatCapacity
  }
  properties: {
    model: {
      name: chatModelName
      format: 'OpenAI'
      version: chatModelVersion
    }
  }
  dependsOn: [
    project
  ]
}

resource lunaDeployment 'Microsoft.CognitiveServices/accounts/deployments@2024-10-01' = {
  parent: account
  name: lunaModelName
  sku: {
    name: lunaSkuName
    capacity: lunaCapacity
  }
  properties: {
    model: {
      name: lunaModelName
      format: 'OpenAI'
      version: lunaModelVersion
    }
  }
  dependsOn: [
    chatDeployment
  ]
}

resource embeddingDeployment 'Microsoft.CognitiveServices/accounts/deployments@2024-10-01' = {
  parent: account
  name: embeddingModelName
  sku: {
    name: 'GlobalStandard'
    capacity: embeddingCapacity
  }
  properties: {
    model: {
      name: embeddingModelName
      format: 'OpenAI'
      version: embeddingModelVersion
    }
  }
  dependsOn: [
    lunaDeployment
  ]
}

resource raFoundryUser 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(resourceGroup().id, participantObjectId, roleFoundryUser)
  properties: {
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', roleFoundryUser)
    principalId: participantObjectId
    principalType: principalType
  }
}

resource raReader 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(resourceGroup().id, participantObjectId, roleReader)
  properties: {
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', roleReader)
    principalId: participantObjectId
    principalType: principalType
  }
}

resource budget 'Microsoft.Consumption/budgets@2023-05-01' = if (!empty(budgetContactEmails)) {
  name: 'presupuesto-lab-${participantNumber}'
  properties: {
    category: 'Cost'
    amount: budgetAmount
    timeGrain: 'Monthly'
    timePeriod: {
      startDate: budgetStartDate
    }
    notifications: {
      actual50: {
        enabled: true
        operator: 'GreaterThan'
        threshold: 50
        thresholdType: 'Actual'
        contactEmails: budgetContactEmails
      }
      actual80: {
        enabled: true
        operator: 'GreaterThan'
        threshold: 80
        thresholdType: 'Actual'
        contactEmails: budgetContactEmails
      }
      actual100: {
        enabled: true
        operator: 'GreaterThan'
        threshold: 100
        thresholdType: 'Actual'
        contactEmails: budgetContactEmails
      }
    }
  }
}

output accountName string = account.name
output projectName string = project.name
output accountEndpoint string = account.properties.endpoint
output projectEndpoint string = 'https://${account.name}.services.ai.azure.com/api/projects/${project.name}'
output chatDeployment string = chatDeployment.name
output lunaDeployment string = lunaDeployment.name
output embeddingDeployment string = embeddingDeployment.name

