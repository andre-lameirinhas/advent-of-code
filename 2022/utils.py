import os


def get_data_path(src_file: str, data_file) -> str:
    return os.path.join(os.path.dirname(src_file), data_file)
