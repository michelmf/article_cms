terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.13.0"
    }
  }
}

provider "azurerm" {
  features {
    key_vault {
      purge_soft_delete_on_destroy = false
    }
  }
}

resource "azurerm_resource_group" "article_cms_rg" {
  name     = ""
  location = "eastus"
}

resource "azurerm_storage_account" "article_cms_st" {

}