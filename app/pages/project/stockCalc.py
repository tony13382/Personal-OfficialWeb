from app.layouts.project import ProjectPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    DivBar,
    HtmlCarousel,
    IconBlock,
    Html,
    Image,
    LinkButton,
    ListDiv,
    Score,
    Text,
    Tool,
    UiImageCarousel,
    Youtube,
)


page = ProjectPage(
    title="MeowLu Stock - 股票試算小工具",
    description="輕鬆好用的股票交易試算工具",
    startdate="2020/10",
    enddate="NOW",
    status="running",
    colorSet=ThemeColor().red,
    prefix="stockCalc",
    pin=True,
    cover="/assets/imgs/projects/stockCalc/cover.png",
    description_links=[
        LinkButton(
            content="服務網址",
            href="https://stockcal.lianglu.uk/",
            open_in_tab=True,
            icon="bi-window-sidebar",
        ),
        LinkButton(
            content="GitHub 專案",
            href="https://github.com/tony13382/Tools-StockCal",
            open_in_tab=True,
            icon="bi-github",
        ),
    ],
    skill_types=["pin", "dev"],
    tags=["介面設計", "產品規劃", "前端開發"],
    tools=[
        Tool("UIKit v2", "前端元件套件"),
        Tool("JavaScript", "邏輯計算與 Dom 交互"),
    ],
    children=[
        Card(
            header=Image(
                "/assets/imgs/projects/stockCalc/priceCalc.png",
                "試算交易手續費",
                allow_pop=True,
                rounded=True,
            ),
            body=[
                Text("試算交易手續費", "h3"),
            ],
        ),
        Card(
            header=Image(
                "/assets/imgs/projects/stockCalc/trendCalc.png",
                "預估漲跌目標股價",
                allow_pop=True,
                rounded=True,
            ),
            body=[
                Text("預估漲跌目標股價", "h3"),
            ],
        ),
        Card(
            header=Image(
                "/assets/imgs/projects/stockCalc/quickCalc.png",
                "快速加減計算",
                allow_pop=True,
                rounded=True,
            ),
            body=[
                Text("快速加減計算", "h3"),
            ],
        ),
    ],
)
