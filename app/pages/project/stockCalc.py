from app.layouts.project import ProjectPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    DivBar,
    FileLink,
    Html,
    Image,
    LinkButton,
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
    cover="/assets/imgs/project/stockCalc/cover.png",
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
    tags=["介面設計", "產品規劃", "前端開發"],
    tools=[
        Tool("UIKit v2", "前端樣式庫"),
        Tool("JavaScript", "邏輯計算與 Dom 交互"),
    ],
    children=[
        Card(
            header=Image(
                "/assets/imgs/project/stockCalc/priceCalc.png", "試算交易手續費"
            ),
            body=[Text("試算交易手續費", "h3")],
        ),
        Card(
            header=Image(
                "/assets/imgs/project/stockCalc/trendCalc.png", "預估漲跌目標股價"
            ),
            body=[Text("預估漲跌目標股價", "h3")],
        ),
        Card(
            header=Image(
                "/assets/imgs/project/stockCalc/quickCalc.png", "快速加減計算"
            ),
            body=[Text("快速加減計算", "h3")],
        ),
    ],
)
