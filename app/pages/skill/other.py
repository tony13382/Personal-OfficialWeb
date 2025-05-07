from app.elements import ListStr, Text
from app.layouts.skill import Certificate, SkillPage, SkillsGroup, SkillItem
from app.variables import ThemeColor

from app.pages.project import digitalOcean, techlife

from app.pages.job import y2023_Tiic

page = SkillPage(
    title="其他技能",
    colorSet=ThemeColor().pink,
    prefix="other",
    icon="bi-bag",
    cover="/assets/imgs/skills/design/cover.png",
    description=ListStr(
        [
            "社群行銷",
            "商業思維",
            "使用者研究",
        ]
    ),
    skill_group=[
        SkillsGroup(
            title="行銷相關",
            icon="bi-bag",
            children=[
                SkillItem(
                    title="OBS",
                    description="直播架設與實務操作（FB & Youtube）",
                    icon="/assets/imgs/appIcons/obs.png",
                ),
                SkillItem(
                    title="Google Ads",
                    description="廣告操作",
                    icon="/assets/imgs/appIcons/googleAds.png",
                ),
                SkillItem(
                    title="社群行銷",
                    description="社群經營與維護",
                    icon="/assets/imgs/appIcons/social.png",
                ),
            ],
        ),
        SkillsGroup(
            title="內容管理 CMS",
            icon="bi-file-earmark-medical",
            children=[
                SkillItem(
                    title="Wordpress",
                    description="網頁架設與管理",
                    icon="/assets/imgs/appIcons/wordpress.png",
                ),
            ],
        ),
    ],
    projects=[
        digitalOcean.page,
        techlife.page,
    ],
    jobs=[y2023_Tiic.page],
    certificate=[
        Certificate(
            title="Google Analytics (分析) 個人認證",
            company="Google",
            tags=["行銷", "數位行銷", "資料分析", "GA4", "SEO"],
        ),
        Certificate(
            title="Google 基礎行銷資格認證",
            company="Google",
            tags=["行銷", "數位行銷"],
        ),
    ],
)
