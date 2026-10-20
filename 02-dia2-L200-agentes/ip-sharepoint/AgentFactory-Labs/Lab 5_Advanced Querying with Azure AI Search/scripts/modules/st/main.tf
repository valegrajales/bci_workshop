locals {
  network_rules_bypass = ["AzureServices"]
}

resource "azurerm_storage_account" "st" {
  name                     = var.storage_account_name             # Storage account name
  location                 = var.location            # Location from the resource group
  resource_group_name      = var.resource_group_name # Resource group name
  account_tier             = "Standard"              # Performance tier
  account_replication_type = "LRS"                   # Locally-redundant storage replication
}

resource "azurerm_role_assignment" "storage_contributor" {
  scope                = azurerm_storage_account.st.id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = var.principal_id
}

