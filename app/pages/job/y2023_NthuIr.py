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
    job_name="清華大學校務研究中心",
    startdate="2022/09",
    enddate="2023/01",
    colorSet=ThemeColor().purple,
    prefix="2023_NthuIr",
    cover="/assets/imgs/jobs/2023_NthuIr/cover.png",
    description=ListStr(
        [
            "清理與整理`約 3000 筆`複合式資料，確保資料品質以及適合後續的分析。",
            "使用`SBERT（Sentence-BERT）模型`向量化文本，使其更易於進行相關的量化分析。",
            "利用 Gephi、Excel、Python 處理`約 3000 筆`資料建立課程圖譜，透過視覺化工具找出不同課程與系所的連結程度。",
        ]
    ),
    children=[
        Card(
            body=[
                Text("研究實習生", "h4"),
                Text("2022/09 ~ 2023/01"),
                DivBar(),
                ListStr(
                    [
                        "在校務研究中心運用文本處理技術，從各種校園相關資料源中擷取、清理和整理`約 3000 筆`複合式資料，確保資料品質以及適合後續的分析。",
                        "使用 SBERT（Sentence-BERT）模型來進行文本向量化。這有助於將課程資訊轉換為數值表示，使其更易於進行相關的量化分析。",
                        "使用`分群分析技術將相似的課程和系所進行分組`，從而更好地理解校園內不同領域的關聯性。",
                        "使用`Gephi 可視化工具`將分析結果轉化為易於理解的圖形和報告，幫助校務研究中心更好地理解和傳達研究結果。",
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
