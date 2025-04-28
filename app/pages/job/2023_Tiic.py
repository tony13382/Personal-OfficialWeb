from app.layouts.job import JobPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    DivBar,
    Image,
    ListStr,
    Text,
)


page = JobPage(
    title="行銷部組長／行銷部 CRM 組幹部",
    description="TIIC 台灣實習影響力社群（TYCIA 臺灣青年職涯創新協會）",
    startdate="2023/03",
    enddate="2024/02",
    colorSet=ThemeColor().green,
    prefix="2023_Tiic",
    cover="/assets/imgs/jobs/2023_Tiic/cover.png",
    tags=["領導", "行銷規劃"],
    children=[
        Card(
            header=Image("/assets/imgs/jobs/2023_Tiic/tiic3.webp"),
            body=[
                Text("行銷部組長", "h4"),
                Text("2023/03 ~ 2024/02"),
                DivBar(),
                Text("組長職務 - 團隊與行銷策略管理", bold=True),
                ListStr(
                    [
                        "建立團隊社群策略，帶領 3 位夥伴執行企劃，`吸引 280 人加入社群`。",
                        "`管理 13 位學員`的培訓進度，帶領學員進行內部培訓。",
                    ]
                ),
            ],
        ),
        Card(
            header=Image("/assets/imgs/jobs/2023_Tiic/tiic1.webp"),
            body=[
                Text("行銷部組長", "h4"),
                Text("2023/03 ~ 2024/02"),
                DivBar(),
                Text("組長職務 - 團隊與行銷策略管理", bold=True),
                ListStr(
                    [
                        "建立團隊社群策略，帶領 3 位夥伴執行企劃，`吸引 280 人加入社群`。",
                        "`管理 13 位學員`的培訓進度，帶領學員進行內部培訓。",
                    ]
                ),
            ],
        ),
    ],
)
