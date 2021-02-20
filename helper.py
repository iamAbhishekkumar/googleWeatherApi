import re


def inner_html(element):
    return element[0].decode_contents()


def remove_tags(string: str):
    return re.sub('<(.*?)>+', "", string)


# def errorHtml():
#     return {
#         "status": 0,
#         "response": "error",
#     }
