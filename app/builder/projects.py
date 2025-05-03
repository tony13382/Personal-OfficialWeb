from app.builder.basic import WebBuilder
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

projectBuilder = WebBuilder("projects/")


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
