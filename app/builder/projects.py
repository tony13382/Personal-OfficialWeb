from app.builder.basic import WebBuilder
from app.pages.project.trelloFinder import page as trelloFinder
from app.pages.project.chenmko import page as chenmko
from app.pages.project.songla import page as songla
from app.pages.project.mindReader import page as mindReader
from app.pages.project.hsCloudMeetingManage import page as hsCloudMeetingManage
from app.pages.project.hsVmi import page as hsVmi
from app.pages.project.pincakeAi import page as pincakeAi
from app.pages.project.stockCalc import page as stockCalc
from app.pages.project.foodome import page as foodome
from app.pages.project.noDrinkNoDrunk import page as noDrinkNoDrunk
from app.pages.project.oneDayLover import page as oneDayLover
from app.pages.project.jobAnalytics2020 import page as jobAnalytics2020
from app.pages.project.digitalOcean import page as digitalOcean
from app.pages.project.techlife import page as techlife

projectBuilder = WebBuilder("projects/")

projectBuilder.addPages(
    [
        trelloFinder,
        chenmko,
        songla,
        mindReader,
        hsCloudMeetingManage,
        hsVmi,
        pincakeAi,
        stockCalc,
        foodome,
        noDrinkNoDrunk,
        oneDayLover,
        jobAnalytics2020,
        digitalOcean,
        techlife,
    ]
)
