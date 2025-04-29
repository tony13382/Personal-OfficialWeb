from app.layouts.job import JobPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    DivBar,
    ListDiv,
    ListStr,
    Text,
)


page = JobPage(
    title="研究實習生",
    description="清華大學校務研究中心",
    startdate="2022/09",
    enddate="2023/01",
    colorSet=ThemeColor().purple,
    prefix="2023_NthuIr",
    cover="/assets/imgs/jobs/2023_NthuIr/cover.png",
    children=[
        Card(
            body=[
                Text("研究實習生", "h4"),
                Text("2022/09 ~ 2023/01"),
                DivBar(),
                Text(
                    "利用 Gephi、Excel、Python 處理`約 3000 筆`資料建立課程圖譜，找出不同課程與系所的連結程度。"
                ),
                Text(
                    "使用 SBERT 模型進行文本向量化分析校園內不同領域的課程相似度，整理並利用校園課綱資料進行`分群分析`。"
                ),
                DivBar(),
                Text("非結構化文本分析", bold=True),
                ListStr(
                    [
                        "在校務研究中心運用先進的文本處理技術，從各種校園相關資料源中擷取、清理和整理大量的文本資料，確保資料品質以及適合後續的分析。",
                        "處理文本資料時，我使用了 SBERT（Sentence-BERT）模型來進行文本向量化。這有助於將課程資訊轉換為數值表示，使其更易於進行相關的量化分析。",
                        "利用我對文本分析技術的熟悉，我能夠分析和評估校園內不同領域的能力表現，幫助決策者了解哪些領域能力優勢以及可能需要進一步發展的領域。",
                    ]
                ),
            ],
            footer=[
                ListDiv(
                    [
                        Text("# 資料搜集／前處理", "span"),
                        Text("# 文字探勘", "span"),
                        Text("# 文本分析", "span"),
                    ],
                    grid_layout=False,
                )
            ],
        ),
    ],
)
