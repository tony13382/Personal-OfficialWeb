from app.elements import ListStr, Text
from app.layouts.skill import Certificate, SkillPage, SkillsGroup, SkillItem
from app.variables import ThemeColor

from app.pages.project import (
    trelloFinder,
    pincakeAi,
    jobAnalytics2020,
    techlife,
    foodome,
)
from app.pages.job import y2023_NthuIr, y2023_NthuOu, y2023_Tiic

page = SkillPage(
    title="數據分析與企劃",
    colorSet=ThemeColor().blue,
    prefix="plan",
    cover="/assets/imgs/skills/plan/cover.png",
    icon="bi-map",
    description=ListStr(
        [
            "熟悉資料清理流程",
            "擅長 Excel 分析",
            "Python 爬蟲處理",
            "精通 pandas 操作",
            "熟用 R 語言整理",
            "GA 數據收集分析",
            "使用 BI 工具將資料可視化",
        ]
    ),
    skill_group=[
        SkillsGroup(
            title="資料搜集／前處理",
            icon="bi-database",
            children=[
                SkillItem(
                    title="Excel",
                    description="UI Design／平面設計",
                    icon="/assets/imgs/appIcons/figma.png",
                ),
                SkillItem(
                    title="BeautifulSoup",
                    description="網頁逆向分析與 BS4 爬蟲",
                    icon="/assets/imgs/appIcons/pyhon.png",
                ),
                SkillItem(
                    title="Python Pandas",
                    description="資料整理與分析",
                    icon="/assets/imgs/appIcons/pyhon.png",
                ),
                SkillItem(
                    title="R",
                    description="Tidyverse 資料清理、視覺化",
                    icon="/assets/imgs/appIcons/rStudio.png",
                ),
                SkillItem(
                    title="Google Analytics",
                    description="後台操作與資料搜集",
                    icon="/assets/imgs/appIcons/googleAnalytics.png",
                ),
            ],
        ),
        SkillsGroup(
            title="資料視覺化",
            icon="bi-file-earmark-bar-graph",
            children=[
                SkillItem(
                    title="Google Data Studio",
                    description="數據視覺化",
                    icon="/assets/imgs/appIcons/data_studio.svg",
                ),
                SkillItem(
                    title="Poewr BI",
                    description="數據視覺化",
                    icon="/assets/imgs/appIcons/powerBi.png",
                ),
                SkillItem(
                    title="IBM Cognos",
                    description="數據視覺化",
                    icon="/assets/imgs/appIcons/ibmCognos.png",
                ),
                SkillItem(
                    title="ggplot2 (Python)",
                    description="數據視覺化",
                    icon="/assets/imgs/appIcons/ggplot2.png",
                ),
            ],
        ),
    ],
    projects=[
        trelloFinder.page,
        pincakeAi.page,
        jobAnalytics2020.page,
        techlife.page,
        foodome.page,
    ],
    jobs=[
        y2023_NthuIr.page,
        y2023_NthuOu.page,
        y2023_Tiic.page,
    ],
    certificate=[
        Certificate(
            title="Google Data Analytics Professional Certificate",
            company="Google (Coursera)",
            tags=["Python", "Excel", "SQL", "資料搜集／前處理", "資料視覺化"],
        ),
        Certificate(
            title="IBM Data Visualization & Dashboard Essentials",
            company="IBM (Coursera)",
            tags=["Python", "Excel", "IBM Cognos", "SQL", "資料視覺化"],
        ),
    ],
)
