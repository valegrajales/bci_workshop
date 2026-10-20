// Recursos COMPARTIDOS del laboratorio BCI Foundry Training Day (scope: resource group).
// Azure AI Search (un solo servicio con el índice normativa-austral), Log Analytics y Application Insights.
// Los participantes solo leen el índice (Search Index Data Reader); los instructores lo crean y administran.
targetScope = 'resourceGroup'

param location string = 'eastus2'

@description('Región de Azure AI Search (puede diferir si la región principal no tiene capacidad).')
param searchLocation string = location
@description('Object ID del grupo de participantes.')
param participantsGroupObjectId string
@description('Object ID del grupo de instructores.')
param instructorsGroupObjectId string

@allowed([
  'basic'
  'standard'
])
param searchSku string = 'basic'

param tags object = {}

var suffix = take(uniqueString(resourceGroup().id), 5)
var searchName = 'bcilab-search-${suffix}'

var roleSearchIndexDataReader = '1407120a-92aa-4202-b7e9-c0e197c71c8f'
var roleSearchIndexDataContributor = '8ebe5a00-799e-43f5-93ac-243d3dce84a7'
var roleSearchServiceContributor = '7ca78c08-252a-4471-8644-bb5ff32d4ba0'

resource search 'Microsoft.Search/searchServices@2024-06-01-preview' = {
  name: searchName
  location: searchLocation
  tags: tags
  sku: {
    name: searchSku
  }
  properties: {
    replicaCount: 1
    partitionCount: 1
    hostingMode: 'default'
    semanticSearch: 'standard'
    disableLocalAuth: false
    authOptions: {
      aadOrApiKey: {
        aadAuthFailureMode: 'http401WithBearerChallenge'
      }
    }
    publicNetworkAccess: 'enabled'
  }
}

resource law 'Microsoft.OperationalInsights/workspaces@2023-09-01' = {
  name: 'bcilab-law-${suffix}'
  location: location
  tags: tags
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: 30
  }
}

resource appi 'Microsoft.Insights/components@2020-02-02' = {
  name: 'bcilab-appi-${suffix}'
  location: location
  tags: tags
  kind: 'web'
  properties: {
    Application_Type: 'web'
    WorkspaceResourceId: law.id
    DisableLocalAuth: false
  }
}

resource raParticipantsRead 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(search.id, participantsGroupObjectId, roleSearchIndexDataReader)
  scope: search
  properties: {
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', roleSearchIndexDataReader)
    principalId: participantsGroupObjectId
    principalType: 'Group'
  }
}

resource raInstructorsData 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(search.id, instructorsGroupObjectId, roleSearchIndexDataContributor)
  scope: search
  properties: {
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', roleSearchIndexDataContributor)
    principalId: instructorsGroupObjectId
    principalType: 'Group'
  }
}

resource raInstructorsService 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(search.id, instructorsGroupObjectId, roleSearchServiceContributor)
  scope: search
  properties: {
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', roleSearchServiceContributor)
    principalId: instructorsGroupObjectId
    principalType: 'Group'
  }
}

output searchName string = search.name
output searchEndpoint string = 'https://${search.name}.search.windows.net'
output appInsightsName string = appi.name
output appInsightsConnectionString string = appi.properties.ConnectionString
