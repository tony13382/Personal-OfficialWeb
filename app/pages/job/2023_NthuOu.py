from app.layouts.job import JobPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    DivBar,
    Image,
    LinkButton,
    Text,
)


page = JobPage(
    title="系統開發工程師",
    description="國立清華大學（國科會）",
    startdate="2023/07",
    enddate="2024/07",
    colorSet=ThemeColor().purple,
    prefix="2023_NthuOu",
    cover="/assets/imgs/jobs/2023_NthuOu/cover.png",
    tags=["LLM 應用", "文本探勘", "資訊佇列系統", "Webhook 串接", "API 開發"],
    children=[
        Card(
            header=Image("/assets/imgs/trelloFinder/cover.png"),
            body=[
                Text("Trello 知識小幫手 2.0", "h4"),
                Text("2023/07 ~ 2024/07"),
                DivBar(),
                Text(
                    "使用了SBERT（Sentence-BERT）模型進行文本向量化。結合 Milvus 向量資料庫。在確保資料搜索準確性的情形下`減少資源推薦運算時間（1 分鐘 → 3 秒）`"
                ),
                Text(
                    "使用 Flask 模組建立 WebAPIs，將系統與 Trello Webhook 進行結合，重構流程大幅減少整體系統獲取資料速度`1分鐘→ 50毫秒。`"
                ),
            ],
            footer=[LinkButton("專案網址", "/projects/trelloFinder.html")],
        ),
    ],
)
