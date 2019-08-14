import os.path

import requests

from src.PostmanIO import PostmanIO


class PAPI:
    GetWorkspacesURL = "https://api.getpostman.com/workspaces"
    GetCollectionsURL = "https://api.getpostman.com/collections"
    GetEnvironmentsURL = "https://api.getpostman.com/environments"
    API_key = None

    def __init__(self, api_key):
        self.SO_frontend_current = "4690258-a923c87c-3760-473c-892c-e7e1096d09c7"
        self.SO_admin_current = "4690258-ac0a63d3-f6ed-4b41-921e-2a3706751eb3"
        self.API_key = api_key
        self.workspaces = None
        self.get_workspaces()
        self.collections = None
        self.get_collections()
        self.environments = None
        self.get_environments()

    def get_workspaces(self):
        if os.path.exists("../lib/workspaces.json"):
            po = PostmanIO()
            po.import_from_json("../lib/workspaces.json")
            return po.content
        else:
            self.update_workspaces()
            return

    def get_request_workspaces(self):
        return self.get_request_generic(self.GetWorkspacesURL)

    def get_workspace(self, workspace_uid):
        url = self.GetWorkspacesURL + "/" + workspace_uid
        return self.get_request_generic(url)

    def get_collections(self):
        if os.path.exists("../lib/collections.json"):
            po = PostmanIO()
            po.import_from_json("../lib/collections.json")
            return po.content
        else:
            self.update_collections()
            return

    def get_request_collections(self):
        return self.get_request_generic(self.GetCollectionsURL)

    def get_collection(self, collection_uid):
        url = self.GetCollectionsURL + "/" + collection_uid
        return self.get_request_generic(url)

    def get_environments(self):
        if os.path.exists("../lib/environments.json"):
            po = PostmanIO()
            po.import_from_json("../lib/environments.json")
            return po.content
        else:
            self.update_environments()
            return

    def get_request_environments(self):
        return self.get_request_generic(self.GetEnvironmentsURL)

    def get_request_generic(self, url):
        r = requests.get(url=url, headers={"X-Api-Key": self.API_key})
        return r.json()

    def export_workspaces(self):
        po = PostmanIO()
        po.export_to_json(self.workspaces, "../lib/workspaces.json")

    def export_collections(self):
        po = PostmanIO()
        po.export_to_json(self.collections, "../lib/collections.json")

    def export_environments(self):
        po = PostmanIO()
        po.export_to_json(self.environments, "../lib/environments.json")

    def update_environments(self):
        self.environments = self.get_request_environments()
        self.export_environments()
        return

    def update_collections(self):
        self.collections = self.get_request_collections()
        self.export_collections()
        return

    def update_workspaces(self):
        self.workspaces = self.get_request_workspaces()
        self.export_workspaces()

    def get_smooth_operators_current_prod(self):
        full_object = self.get_smooth_operators_current()
        collections = []
        for collection in full_object['workspace']['collections']:
            if collection['uid'] is self.SO_admin_current or self.SO_frontend_current:
                collections.append(collection)
        environments = []
        for environment in full_object['workspace']['environments']:
            if environment['uid'] is self.SO_environment_prod:
                environments.append(environment)
        return collections, environments
