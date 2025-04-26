from app.layouts.project import ProjectPage
from app.pages import trelloFinder


class WebBuilder:
    def __init__(self) -> None:
        self.projectWebConfigs = []

    def addProject(self, newProject: ProjectPage):
        self.projectWebConfigs.append(newProject)


builder = WebBuilder()

builder.addProject(trelloFinder.page)
