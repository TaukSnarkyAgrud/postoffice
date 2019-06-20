from src.ConcurrentRun import ConcurrentRun
from src.PostmanIO import PostmanIO


def main():
    api_key = "dcc58ac7a9bf4e339b58deb82f39d443"

    id_load = PostmanIO()
    id_load.import_from_json("..\\lib\\IDs.json")

    collections = id_load.content["workspace"]["collections"]
    environments = id_load.content["workspace"]["environments"]
    ConcurrentRun(api_key, [collections[-1]], [environments[-1]])


if __name__ == "__main__":
    main()
