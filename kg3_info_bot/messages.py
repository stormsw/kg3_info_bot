from os import path
import pkg_resources


def msg_reader(message:str):
    filename = path.join('resources',f"{message}.md")
    return pkg_resources.resource_string('kg3_info_bot',filename).decode()
