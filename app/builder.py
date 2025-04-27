from app.layouts.project import ProjectPage
from app.pages import (
    foodome,
    hsCloudMeetingManage,
    hsVmi,
    jobAnalytics2020,
    mindReader,
    noDrinkNoDrunk,
    oneDayLover,
    pincakeAi,
    songla,
    trelloFinder,
    chenmko,
)


class WebBuilder:
    def __init__(self) -> None:
        self.projectWebConfigs = []

    def addProject(self, newProject: ProjectPage):
        self.projectWebConfigs.append(newProject)


builder = WebBuilder()

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
