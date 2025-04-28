from app.layouts.project import ProjectPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    DivBar,
    Image,
    LinkButton,
    Text,
    Tool,
)


page = ProjectPage(
    title="No Drink No Drunk",
    description="大學開發專案，純 HTML5 & CSS3 製作酒類銷售網頁。",
    subdescription="擔任：網站設計師<br>負責：網站介面設計、前端開發、RWD 實作",
    startdate="2020/09",
    enddate="2021/01",
    status="closed",
    colorSet=ThemeColor().orange,
    prefix="noDrinkNoDrunk",
    cover="/assets/imgs/project/noDrinkNoDrunk/cover.png",
    description_links=[
        LinkButton(
            content="專案網址・純前端展示",
            href="https://tony13382.github.io/CycuWebDesign-FinalWeb/pages/products.html",
            fill=True,
            open_in_tab=True,
            icon="bi-cloud",
        ),
        LinkButton(
            content="GitHub 專案・前端版本",
            href="https://github.com/tony13382/CycuWebDesign-FinalWeb",
            open_in_tab=True,
            icon="bi-github",
        ),
        LinkButton(
            content="GitHub 專案・JSP 版本",
            href="https://github.com/tony13382/CycuWebDesign-JspWeb",
            open_in_tab=True,
            icon="bi-github",
        ),
    ],
    tags=["程式開發"],
    tools=[
        Tool("Figma", "UI Design"),
        Tool("HTML5 & CSS3", "前端"),
        Tool("Bootstrap v3", "前端介面工具"),
    ],
    children=[
        Card(
            body=[
                Text("系統介面", "h3"),
                DivBar("nano", opacity=0),
                Image(
                    "/assets/imgs/project/noDrinkNoDrunk/nodrinkIndex.jpeg",
                    "Home Page",
                    True,
                ),
                Image(
                    "/assets/imgs/project/noDrinkNoDrunk/info.png",
                    "Wine Info Page",
                    True,
                ),
                Image(
                    "/assets/imgs/project/noDrinkNoDrunk/list.png",
                    "Shopping List Page",
                    True,
                ),
                Image(
                    "/assets/imgs/project/noDrinkNoDrunk/knowledge.png",
                    "Wine Knowledge Page",
                    True,
                ),
            ],
        )
    ],
)
