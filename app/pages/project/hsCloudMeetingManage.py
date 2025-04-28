from app.layouts.project import ProjectPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    DivBar,
    FileLink,
    Image,
    LinkButton,
    ListDiv,
    Text,
    Tool,
)


page = ProjectPage(
    title="華新雲會議管理系統",
    description="大學系統分析專案，利用 mongodb 與 jisti 提供使用者線上開會與開會管理的解決方案，除了基本網頁通知，也串接了信箱系統，以確保用戶信息不漏接。",
    subdescription="擔任：CTO, Product Designer<br>負責：軟體架構設計、產品介面設計、軟體開發、技術總負責人",
    startdate="2020/09",
    enddate="2021/01",
    status="closed",
    colorSet=ThemeColor().purple,
    prefix="hsCloudMeetingManage",
    cover="/assets/imgs/project/hsCloudMeetingManage/cover.png",
    description_links=[
        LinkButton(
            content="GitHub 代碼",
            href="https://github.com/tony13382/CycuSA-MeetManagement",
            fill=True,
            open_in_tab=True,
            icon="bi-github",
        ),
        LinkButton(
            content="Figma 設計界面稿",
            href="https://www.figma.com/design/TFvrAIjw0xeTr0HIvw942d/-2020-SA-%E8%B3%87%E7%AE%A1%E4%B8%89%E4%B9%99_%E7%AC%AC%E5%85%AD%E7%B5%84_%E8%8F%AF%E6%96%B0%E9%9B%B2%E6%9C%83%E8%AD%B0%E7%AE%A1%E7%90%86%E7%B3%BB%E7%B5%B1%E8%A8%AD%E8%A8%88%E6%AA%94",
            open_in_tab=True,
            icon="bi-window-sidebar",
        ),
    ],
    tags=["介面設計", "產品規劃", "全端開發"],
    tools=[
        Tool("Figma", "UI & Prototype"),
        Tool("Node.js", "後端資料處理"),
        Tool("mongoDB", "NoSQL 資料庫"),
        Tool("Jitsi Meet", "線上會議後端系統"),
        Tool("Bootstrap V4.3", "前端框架"),
        Tool("handlebars", "前端模板採用"),
    ],
    children=[
        Card(
            header=Image(
                "/assets/imgs/project/hsCloudMeetingManage/ad.png", "Ad Cover", True
            ),
        ),
        Card(
            body=[
                Text("DFD 設計", "h3"),
                DivBar(),
                Image(
                    "/assets/imgs/project/hsCloudMeetingManage/dfdL0.png",
                    "DFD 設計 1",
                    True,
                ),
                DivBar(),
                Image(
                    "/assets/imgs/project/hsCloudMeetingManage/dfdL1.png",
                    "DFD 設計 2",
                    True,
                ),
                ListDiv(
                    [
                        FileLink(
                            src="https://drive.google.com/file/d/1svdIQLUVO5-AF-cirV8XNvexPLyFgCc0/view",
                            icon="bi-file-earmark-arrow-down",
                            title="系統規格書",
                            subtitle="PDF",
                        ),
                        FileLink(
                            src="https://www.figma.com/design/TFvrAIjw0xeTr0HIvw942d/-2020-SA-%E8%B3%87%E7%AE%A1%E4%B8%89%E4%B9%99_%E7%AC%AC%E5%85%AD%E7%B5%84_%E8%8F%AF%E6%96%B0%E9%9B%B2%E6%9C%83%E8%AD%B0%E7%AE%A1%E7%90%86%E7%B3%BB%E7%B5%B1%E8%A8%AD%E8%A8%88%E6%AA%94",
                            icon="bi-window-sidebar",
                            title="Figma 設計界面稿",
                            subtitle="Figma",
                        ),
                    ],
                    mt=4,
                ),
            ]
        ),
        Card(
            header=Image(
                "/assets/imgs/project/hsCloudMeetingManage/erModel.png",
                "ER Model",
                True,
            ),
            body=[Text("ER Model", "h3")],
        ),
    ],
)
