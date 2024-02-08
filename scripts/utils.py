from pathlib import Path
import bson
import git
import os

from constants import LATEST_BACKUP_DATE
from constants import Databases, Auth


def _convert_collection(database, collection):
    repo = git.Repo('.', search_parent_directories=True)
    base = repo.working_tree_dir
    dir = f"{base}/db-backups/{LATEST_BACKUP_DATE}/"
    return f"{dir}/{database.value}_{collection.value}"


def get_collections():
    for i in os.listdir():
        if i.endswith(".bson"):
            yield Path(i).stem


def get_data(database, collection):
    db_collection = _convert_collection(database, collection)
    filename = f"{db_collection}.bson"
    with open(filename, "rb") as f:
        bson_data = bson.decode_all(f.read())
        return bson_data


if __name__ == "__main__":
    print(get_data(Databases.AUTH, Auth.INFO))