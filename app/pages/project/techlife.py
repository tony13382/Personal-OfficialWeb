from app.layouts.project import ProjectPage
from app.variables import GapSet, SpaceSet, ThemeColor
from app.elements import (
    AccordionItem,
    AccordionBlock,
    Card,
    Canva,
    IconBlock,
    LinkButton,
    Score,
    Text,
    Tool,
    Youtube,
)


page = ProjectPage(
    title="TechLife 讓科技充滿生活 - Photopea 講師",
    description="因應網路時代，教育孩子具備資訊素養與科技應用能力，能為未來發展打下堅實基礎。",
    startdate="2021/10",
    enddate="2021/12",
    status="closed",
    colorSet=ThemeColor().green,
    prefix="techlife",
    pin=True,
    cover="/assets/imgs/projects/techlife/cover.png",
    description_links=[
        LinkButton(
            content="企劃書網址",
            href="https://drive.google.com/file/d/1eniB4QHWWV2XpCchNALeQpDLl1XQkiVT/view",
            open_in_tab=True,
            icon="bi-file-earmark-arrow-down",
        )
    ],
    skill_types=["pin", "plan", "other"],
    tags=["教案設計", "PowerPoint 設計"],
    tools=[
        Tool("Photopea", "修圖"),
        Tool("Powerpoint", "教案設計"),
    ],
    scores=[Score("1092 中原大學資管系資訊管理競賽", "第一名")],
    children=[
        Card(
            body=[
                Text(
                    "`方案名稱`：TechLife 讓科技充滿生活<br>`團隊名稱`：中原資管總動員<br>`服務日期`：2021 年 6 月 11～12 日<br>`預計服務地點及對象`：台東縣延平鄉桃源國小（15～20 位小朋友）"
                ),
                IconBlock(
                    title="教案文件",
                    subtitle="PDF (Google Drive)",
                    src="https://drive.google.com/file/d/1eniB4QHWWV2XpCchNALeQpDLl1XQkiVT/view?usp=sharing",
                ),
            ],
            body_gap=GapSet("large"),
        ),
        Card(
            header=Youtube("https://www.youtube.com/embed/mOWnXJHIqIY"),
            body=[
                Text("教案：圖像創作不設限", "h3"),
                IconBlock(
                    title="圖像創作不設限",
                    subtitle="PPT 教案",
                    src="https://docs.google.com/presentation/d/1dCqidx20eRnYCjTZqa0tZ0-m0BvxnJFC/edit#slide=id.p1",
                    icon="bi-file-earmark-ppt",
                ),
                AccordionBlock(
                    [
                        AccordionItem(
                            title="圖像創作不設限（簡報資源預覽）",
                            items=[
                                Canva("https://www.canva.com/design/DAG35mSwP18/DR5c7o5yWyfYZ3jgg3RnGg/view?embed")
                            ],
                            body_space=SpaceSet(p=0)
                        )
                    ]
                )
            ],
            body_gap=GapSet("large"),
        ),
        Card(
            header=Youtube("https://www.youtube.com/embed/R_vsL1NFWN8"),
            body=[
                Text("教案：10 分鐘學會製作 Linebot", "h3"),
                IconBlock(
                    title="快樂農場​",
                    subtitle="PPT 教案",
                    src="https://docs.google.com/presentation/d/1caNefhQInRqCu8LZLcUChf4yaCZgMC41/edit#slide=id.p1",
                    icon="bi-file-earmark-ppt",
                ),
                AccordionBlock(
                    [
                        AccordionItem(
                            title="快樂農場​（簡報資源預覽）",
                            items=[
                                Canva("https://www.canva.com/design/DAG3_U2O5UM/7BineOJpAOxa4MRyZv8opA/view?embed")
                            ],
                            body_space=SpaceSet(p=0)
                        )
                    ]
                )
            ],
            body_gap=GapSet("large"),
        ),
    ],
)
