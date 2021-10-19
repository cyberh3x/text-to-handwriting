import pywhatkit
from utility.primary import getUserProfilePath, directoryExist, makeDirectory
from utility.date import getCurrentTimestamp


class Converter:
    def __init__(self, text: str, save_to: str = None, color: tuple = (0, 0, 0)):
        self.text = text
        path = "Text-To-Handwriting/{timestamp}.png"
        user_profile_path = getUserProfilePath()
        if not directoryExist(user_profile_path):
            makeDirectory(user_profile_path)
        self.save_to = getUserProfilePath(path.format(timestamp=getCurrentTimestamp())) if save_to is None else save_to
        self.color = color

    def convert(self):
        pywhatkit.text_to_handwriting(self.text, save_to=self.save_to, rgb=self.color)
        return self.save_to
