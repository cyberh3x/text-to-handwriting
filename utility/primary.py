import os


def getUserProfilePath(suffix: str = "Text-To-Handwriting"):
    return os.path.expanduser(os.sep.join(["~", suffix]))


def directoryExist(path):
    return os.path.exists(os.path.join(os.getcwd(), path))


def makeDirectory(path):
    return os.mkdir(path)
