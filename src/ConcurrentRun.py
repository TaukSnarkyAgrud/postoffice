import threading
import os

from src.PostmanIO import PostmanIO


class ConcurrentRun:
    currentWorkspaceObject = ()
    results = []
    current_log_directory = None

    def __init__(self, api_key, collections_list, environments_list):
        self.io_control = PostmanIO()
        self.io_control.change_working_directory("C:/Users/aaldridge/PycharmProjects/post_office/LogFiles")
        self.api_key = api_key
        self.currentWorkspaceObject = (collections_list, environments_list)
        self.execute_each_collection_sequentially_but_concurrent_across_environments(self.currentWorkspaceObject)
        self.log_interpreter()

    @staticmethod
    def run_command(cmd):
        os.system(cmd)

    @staticmethod
    def build_execution_phrase(output_filename, collection_uid, environment_uid, api_key):
        execute_phrase_preamble = "newman run --reporters cli,json --reporter-json-export"
        execute_phrase_collection = "https://api.getpostman.com/collections/"
        execute_phrase_environment = "-e https://api.getpostman.com/environments/"
        execute_phrase_api_key = "?apikey="
        full_phrase = execute_phrase_preamble + " " + output_filename + ".json " + execute_phrase_collection + \
            collection_uid + execute_phrase_api_key + api_key + " " + execute_phrase_environment + \
            environment_uid + execute_phrase_api_key + api_key + " > " + output_filename + ".txt"
        return full_phrase

    def execute_each_collection_sequentially_but_concurrent_across_environments(self, workspace):
        collections = workspace[0]
        environments = workspace[1]

        self.current_log_directory = self.io_control.create_log_file()
        for collection in collections:
            print("Starting a batch")

            for environment in environments:
                output_file_name = collection['name'] + "_" + environment['name']
                self.results.append(output_file_name + ".json")
                execution_phrase = self.build_execution_phrase(output_file_name, collection['uid'], environment['uid'],
                                                               self.api_key)
                t = threading.Thread(name=output_file_name, target=self.run_command(execution_phrase))
                t.start()
                t.join()

            print("Done with that batch")

    def log_interpreter(self):
        print("Interpreting run: ...")
        collection_failures = 0
        for file in self.results:
            ingest = PostmanIO()
            ingest.import_from_json(".\\" + file)
            if not ingest.content["run"]["failures"]:
                print(file + " had no failures")
            else:
                collection_failures += 1
        print("\n\n--------------------------------------RESULTS--------------------------------------")
        print(self.current_log_directory)
        if collection_failures == 0:
            print("\n\nALL COLLECTIONS PASS!!")
        else:
            print("\n\nFailures detected")
        pass
