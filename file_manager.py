import json
import os


def read_state(path):
    """JSON 파일을 UTF-8로 읽어서 데이터를 돌려줘요"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_state(path, data):
    """데이터를 UTF-8 JSON 파일로 저장해요"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def backup_broken_file(path):
    """망가진 파일을 .bak 이름으로 옮겨서 보관해요"""
    backup_path = path + ".bak"
    os.replace(path, backup_path)
    return backup_path