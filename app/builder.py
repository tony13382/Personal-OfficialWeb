import os
from typing import List, Any
from app.layouts.project import ProjectPage
from app.pages.project import (
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
    stockCalc,
    techlife,
    trelloFinder,
    chenmko,
)
from app.pages.job import (
    y2022_Songla,
    y2023_NthuOu,
    y2023_NthuIr,
    y2023_Tiic,
    y2024_solwenAi,
)


class WebBuilder:
    def __init__(self, path: str) -> None:
        self.path = path
        self.projectWebConfigs = []
        # 确保目录存在
        os.makedirs(path, exist_ok=True)

    def addPage(self, newProject: Any):
        self.projectWebConfigs.append(newProject)

    def addPages(self, newProjects: List[Any]):
        self.projectWebConfigs.extend(newProjects)

    def getPages(self):
        return self.projectWebConfigs

    def build(self):
        for page in self.projectWebConfigs:
            file_path = self.path + f"{page.prefix}.html"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(str(page))
                print(f"Output to html Successful. File: {file_path}")


projectBuilder = WebBuilder("projects/")
jobBuilder = WebBuilder("jobs/")

projectBuilder.addPages(
    [
        trelloFinder.page,
        chenmko.page,
        songla.page,
        mindReader.page,
        hsCloudMeetingManage.page,
        hsVmi.page,
        pincakeAi.page,
        stockCalc.page,
        foodome.page,
        noDrinkNoDrunk.page,
        oneDayLover.page,
        jobAnalytics2020.page,
        digitalOcean.page,
        techlife.page,
    ]
)


jobBuilder.addPages(
    [
        y2022_Songla.page,
        y2023_NthuOu.page,
        y2023_NthuIr.page,
        y2023_Tiic.page,
        y2024_solwenAi.page,
    ]
)
