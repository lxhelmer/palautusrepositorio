from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        taulu = toml.loads(content)
        print ("########")
        for key , value in taulu.items():
            print (key, value)
        print ("\n")
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(taulu["tool"]["poetry"]["name"], taulu["tool"]["poetry"]["description"],taulu["tool"]["poetry"]["dependencies"], taulu["tool"]["poetry"]["dev-dependencies"])
