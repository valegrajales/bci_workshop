// Asigna Cognitive Services User a un participante/instructor sobre SU cuenta Foundry ya desplegada.
// Lo usa Add-RolCognitiveServicesUser.ps1 para el entorno existente (sin redesplegar participante.bicep,
// que pisaría el SKU de gpt-5.6-luna repartido por Add-Modelo.ps1).
// El nombre de la asignación es el mismo que en participante.bicep -> ambos son idempotentes entre sí.
targetScope = 'resourceGroup'

@description('Nombre de la cuenta Foundry (AIServices) del grupo de recursos.')
param accountName string

@description('Object ID (Entra) del usuario o grupo.')
param participantObjectId string

@allowed([
  'User'
  'Group'
])
param principalType string = 'User'

var roleCognitiveServicesUser = 'a97b65f3-24c7-4388-baec-2e87135dc908'

resource account 'Microsoft.CognitiveServices/accounts@2025-04-01-preview' existing = {
  name: accountName
}

resource raCognitiveServicesUser 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(account.id, participantObjectId, roleCognitiveServicesUser)
  scope: account
  properties: {
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', roleCognitiveServicesUser)
    principalId: participantObjectId
    principalType: principalType
  }
}

output roleAssignmentId string = raCognitiveServicesUser.id
