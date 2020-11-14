
from modules import *


def res_olx(user_input):
    for i in olx(user_input):
        return(' '.join(i))
        return i


def res_pracuj(user_input):
    for i in pracuj(user_input):
        return(' '.join(i))


def res_gumtree(user_input):
    for i in gumtree(user_input):
        return(' '.join(i))


def res_all(user_input):
    for i in pracuj(user_input):
        return(' '.join(i))
    for i in gumtree(user_input):
        return(' '.join(i))
    for i in olx(user_input):
        return(' '.join(i))
