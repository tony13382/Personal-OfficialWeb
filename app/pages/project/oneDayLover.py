from app.layouts.project import ProjectPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    IconBlock,
    Image,
    LinkButton,
    Text,
    Tool,
)


page = ProjectPage(
    title="一日情人後端",
    description="大學專案，基於 JSP 所建構商城後端（純資料庫交互，無金流，具備後台）。",
    subdescription="擔任：後端工程師<br>負責：後端開發",
    startdate="2020/09",
    enddate="2021/01",
    status="closed",
    colorSet=ThemeColor().red,
    prefix="oneDayLover",
    cover="/assets/imgs/projects/oneDayLover/cover.png",
    description_links=[
        LinkButton(
            content="GitHub・前端版本",
            href="https://github.com/ziyihong/ziyihong.github.io",
            open_in_tab=True,
            icon="bi-github",
        ),
        LinkButton(
            content="GitHub・JSP 版本",
            href="https://github.com/ziyihong/ziyihong.github.io/tree/master/final",
            open_in_tab=True,
            icon="bi-github",
        ),
    ],
    tags=["後端開發"],
    tools=[
        Tool("Apache Tomcat", "後端處理"),
        Tool("MySQL", "資料庫交互與設計"),
    ],
    children=[
        Card(
            header=Image(
                "/assets/imgs/projects/oneDayLover/er-model.png", "ER-Modal", True
            ),
            body=[
                Text("ER Model", "h3"),
                IconBlock(
                    title="SQL File （預設資料庫）",
                    subtitle=".SQL",
                    src="/assets/file/oneDayLover/mydata.sql",
                    icon="bi-table",
                ),
                IconBlock(
                    title="ZIP File （JSP 程式碼備份）",
                    subtitle="ZIP",
                    src="https://drive.google.com/file/d/1SFD0cc5bJYFFNuvxcoyXMdBAoDrOWUFh/view",
                    icon="bi-file-earmark-arrow-down",
                ),
            ],
        )
    ],
)
