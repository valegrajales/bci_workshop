resource "azurerm_cognitive_account" "openai" {
  name                          = var.azopenai_name
  kind                          = "OpenAI"
  sku_name                      = "S0"
  location                      = var.location
  resource_group_name           = var.resource_group_name
  public_network_access_enabled = true
  custom_subdomain_name         = var.azopenai_name
}

# Deploy models into Azure OpenAI

resource "azurerm_cognitive_deployment" "embedding" {
  name                 = "text-embedding-ada-002"
  cognitive_account_id = azurerm_cognitive_account.openai.id
  rai_policy_name      = "Microsoft.Default"
  model {
    format  = "OpenAI"
    name    = "text-embedding-ada-002"
    version = "2"
  }
  sku {
    name     = "GlobalStandard"
    capacity = 100
  }
}

resource "azurerm_cognitive_deployment" "gpt4o" {
  name                 = "gpt4o"
  cognitive_account_id = azurerm_cognitive_account.openai.id
  rai_policy_name      = "Microsoft.Default"
  model {
    format  = "OpenAI"
    name    = "gpt-4o"
    version = "2024-05-13"
  }
  sku {
    name     = "GlobalStandard"
    capacity = 20
  }
}

# Set role assignment for OpenAI

resource "azurerm_role_assignment" "openai_user" {
  scope                = azurerm_cognitive_account.openai.id
  role_definition_name = "Cognitive Services OpenAI User"
  principal_id         = var.principal_id
}


