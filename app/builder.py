from app.layouts.project import ProjectPage
from app.pages import (
    digitalOcean,
    foodome,
    hsCloudMeetingManage,
    hsVmi,
    jobAnalytics2020,
    mindReader,
    noDrinkNoDrunk,
    oneDayLover,
    pincakeAi,
    songla,
    techlife,
    trelloFinder,
    chenmko,
)
import os


class WebBuilder:
    def __init__(self, path: str) -> None:
        self.path = path
        self.projectWebConfigs = []
        # 确保目录存在
        os.makedirs(path, exist_ok=True)

    def addProject(self, newProject: ProjectPage):
        self.projectWebConfigs.append(newProject)

    def getProjects(self):
        return self.projectWebConfigs

    def build(self):
        for page in self.projectWebConfigs:
            file_path = self.path + f"{page.prefix}.html"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(str(page))
                print(f"Output to html Successful. File: {file_path}")


builder = WebBuilder("static/")

builder.addProject(trelloFinder.page)
builder.addProject(chenmko.page)
builder.addProject(songla.page)
builder.addProject(mindReader.page)
builder.addProject(hsCloudMeetingManage.page)
builder.addProject(hsVmi.page)
builder.addProject(pincakeAi.page)
builder.addProject(foodome.page)
builder.addProject(noDrinkNoDrunk.page)
builder.addProject(oneDayLover.page)
builder.addProject(jobAnalytics2020.page)
builder.addProject(digitalOcean.page)
builder.addProject(techlife.page)
