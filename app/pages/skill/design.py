from app.elements import ListStr
from app.layouts.skill import SkillPage, SkillsGroup, SkillItem
from app.variables import ThemeColor

import app.pages.project as projectPages
import app.pages.job as jobPages

page = SkillPage(
    title="設計技能・專精資訊設計",
    colorSet=ThemeColor().purple,
    prefix="design",
    cover="/assets/imgs/skills/design/cover.png",
    icon="bi-phone",
    description=ListStr(
        [
            "熟悉 UI/UX 設計流程",
            "具備使用者研究與需求分析能力",
            "擅長資訊視覺化設計",
            "精通 Figma、Adobe XD 等設計工具",
            "精通簡報製作",
        ]
    ),
    skill_group=[
        SkillsGroup(
            title="產品設計",
            icon="bi-phone",
            children=[
                SkillItem(
                    title="Figma",
                    description="UI Design／平面設計",
                    icon="/assets/imgs/appIcons/figma.png",
                ),
                SkillItem(
                    title="Adobe XD",
                    description="UI/UX 設計",
                    icon="/assets/imgs/appIcons/xd.png",
                ),
            ],
        ),
        SkillsGroup(
            title="資訊傳達",
            icon="bi-easel",
            children=[
                SkillItem(
                    title="資訊設計",
                    description="整理資訊並傳遞給受眾",
                    icon="/assets/imgs/appIcons/thinkFlow.png",
                ),
                SkillItem(
                    title="PowerPoint",
                    description="簡報設計",
                    icon="/assets/imgs/appIcons/powerpoint.png",
                ),
                SkillItem(
                    title="Canva",
                    description="簡報設計／平面設計",
                    icon="/assets/imgs/appIcons/canva.png",
                ),
                SkillItem(
                    title="Photoshop",
                    description="圖片設計",
                    icon="/assets/imgs/appIcons/photoshop.png",
                ),
                SkillItem(
                    title="Premiere",
                    description="影片剪輯",
                    icon="/assets/imgs/appIcons/premiere.png",
                ),
            ],
        ),
    ],
    projects=[
        projectPages.songla,
        projectPages.mindReader,
        projectPages.hsCloudMeetingManage,
        projectPages.pincakeAi,
        projectPages.foodome,
    ],
    jobs=[
        jobPages.y2022_Songla,
        jobPages.y2019_CycuEdu,
    ],
)
