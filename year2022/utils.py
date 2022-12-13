from os.path import join, dirname


def get_data_path(src_file: str, data_file: str) -> str:
    return join(dirname(src_file), data_file)
