from os import getenv

def get_env_var(key):
    return getenv(key)


def get_bool_env_var(key):
    return bool(getenv(key))


def get_list_env_var(key):
    return getenv(key).split(',')


def get_int_env_var(key):
    return int(getenv(key))
