"""
Diagrams.py
Generate the infrastructure's diagram of the CMS article project.
"""
from diagrams import Cluster, Diagram

from diagrams.azure.compute import AppServices
from diagrams.azure.database import SQLDatabases
from diagrams.azure.storage import StorageAccounts

with Diagram("CMS Article Project", show=False) as diagram:

    with Cluster("          Resource Group Name: rg_article_cms          "):

        with Cluster("     Compute Services     "):
            compute = AppServices("cms_app_service")

        with Cluster("     Storage Services     "):
            databases = [
                SQLDatabases("cms_sql_database"),
                StorageAccounts("cms_storage_account")
            ]

            compute >> databases
            compute << databases

# Create the diagram
diagram