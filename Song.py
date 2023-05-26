import re
import requests

class Song:
    def __init__(self, name, artist, rank,album_img):
        self._name = name
        self.rank = rank
        self._artist = artist
        self.album_img = album_img

    def get_name(self):
        return self._name

    def get_rank(self):
        return self.rank

    def get_artist(self):
        return self._artist

    def set_name(self, name):
        self._name = name

    def set_rank(self, rank):
        self.rank = rank

    def set_artist(self, artist):
        self._artist = artist

    def get_album_img(self):
        return self.album_img


