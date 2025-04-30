from app.layouts.job import JobPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    DivBar,
    Image,
    LinkButton,
    ListDiv,
    ListStr,
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
    children=[
        Card(
            header=Image("/assets/imgs/project/trelloFinder/cover.png"),
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
                DivBar(),
                Text("模糊文本搜尋算法", bold=True),
                ListStr(
                    [
                        "使用 Sentence-BERT (SBERT) 技術進行文本向量化方面具有豐富經驗。透過 SBERT 技術，我能夠將文本轉換為密集的向量表示，進而實現更精確的相似性計算和文本匹配。",
                        "在多個專案中負責維運 Milvus 向量資料庫。我能夠靈活地配置、調整和優化 Milvus，以確保系統在處理大規模向量資料時的穩定性和高效性。",
                        "善於將自然語言處理 (NLP) 技術與搜尋算法相結合，以提供更精確和全面的搜索結果，從而提高系統的用戶體驗。",
                    ]
                ),
                Text("Flask API 開發", bold=True),
                ListStr(
                    [
                        "設計和實現了基於 Flask 框架的 API，為計劃案發系統提供了穩定且靈活的後端服務。",
                        "透過遵循最佳實踐和優化代碼結構，我確保 API 的可擴展性和易於維護。",
                        "撰寫原子測試與技術相關文件，確保系統可以妥善的交接。",
                    ]
                ),
                DivBar(),
                LinkButton("專案網址", "/projects/trelloFinder.html"),
            ],
            footer=[
                ListDiv(
                    [
                        Text("# API 開發", "span"),
                        Text("# 資訊佇列系統", "span"),
                        Text("# LLM 應用", "span"),
                        Text("# 文本探勘", "span"),
                        Text("# Webhook 串接", "span"),
                        Text("# SBERT", "span"),
                        Text("# Milvus", "span"),
                    ],
                    grid_layout=False,
                )
            ],
        ),
    ],
)
