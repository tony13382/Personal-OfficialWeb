from app.layouts.job import JobPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    DivBar,
    Image,
    ListDiv,
    ListStr,
    Text,
)


page = JobPage(
    title="行銷部組長／行銷部 CRM 組幹部",
    job_name="TIIC 台灣實習影響力社群<br>（TYCIA 臺灣青年職涯創新協會）",
    startdate="2023/03",
    enddate="2024/02",
    colorSet=ThemeColor().green,
    prefix="2023_Tiic",
    cover="/assets/imgs/jobs/2023_Tiic/cover.png",
    description=ListStr(
        [
            "擔任行銷部組長，負責團隊與行銷策略管理。",
            "協助團隊進行內部培訓，並管理學員的培訓進度。",
            "負責行銷部的社群經營與用戶體驗優化，提升用戶留存率。",
        ]
    ),
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
                        "建立團隊社群策略，帶領 3 位夥伴執行企劃，`吸引 280 人加入社群`，擴大團隊影響力。",
                        "管理 `13 位學員`的培訓進度，帶領學員進行內部培訓。",
                    ]
                ),
            ],
            footer=[
                ListDiv(
                    [
                        Text("# 領導力", "span"),
                        Text("# 教育培訓", "span"),
                    ],
                    grid_layout=False,
                )
            ],
        ),
        Card(
            header=Image("/assets/imgs/jobs/2023_Tiic/tiic1.webp"),
            body=[
                Text("行銷部組長", "h4"),
                Text("2023/03 ~ 2024/02"),
                DivBar(),
                Text("DC 社群管理與用戶體驗優化", bold=True),
                ListStr(
                    [
                        "深入了解 Discord 社群成員的需求、偏好和痛點，並從中收集寶貴的反饋。",
                        "分析前代 Discord 用戶旅程，並從中分析出可以優化的部分並執行。",
                        "與不同部門和團隊的協作，針對內部部門需求訂做 Discord 功能。",
                        "擔任 Discord 社群管理者，負責招募、培訓和指導社群志願者，確保社群運營順利且高效。",
                    ]
                ),
                DivBar(),
                Text("提升用戶留存", bold=True),
                ListStr(
                    [
                        "開發並執行社群策略，包括吸引新用戶、留住現有用戶和促進用戶參與。",
                        "制定並實施用戶激勵計劃，以增加用戶參與度和忠誠度。",
                    ]
                ),
            ],
            footer=[
                ListDiv(
                    [
                        Text("# 社群經營", "span"),
                        Text("# 行銷", "span"),
                    ],
                    grid_layout=False,
                )
            ],
        ),
        Card(
            body=[
                Text("證書", "h4"),
                DivBar(),
                Image("/assets/imgs/jobs/2023_Tiic/tiic4.webp", rounded=True),
                Image("/assets/imgs/jobs/2023_Tiic/tiic2.webp", rounded=True),
            ]
        ),
    ],
)
