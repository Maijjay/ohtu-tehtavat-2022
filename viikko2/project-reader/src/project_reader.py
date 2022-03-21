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



        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        tmp = toml.loads(content)
        name = tmp["tool"]["poetry"]["name"]
        description = tmp["tool"]["poetry"]["description"]
        dependencies = tmp["tool"]["poetry"]["dependencies"]
        dev_dependencies = tmp["tool"]["poetry"]["dev-dependencies"]
        projekti = Project(name, description, dependencies, dev_dependencies)
        
        
        return projekti
