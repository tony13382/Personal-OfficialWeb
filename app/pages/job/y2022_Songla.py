from app.layouts.job import JobPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    Div,
    DivBar,
    Image,
    LinkButton,
    ListDiv,
    ListStr,
    Text,
)


page = JobPage(
    title="產品設計師／技術總管",
    job_name="即時行樂有限公司（新創）",
    startdate="2022/01",
    enddate="2023/09",
    colorSet=ThemeColor().green,
    prefix="2022_Songla",
    cover="/assets/imgs/jobs/2022_Songla/cover.png",
    description=ListStr(
        [
            "建立企業原子設計系統，`協助企業建立一致的設計風格`，包括排版、用色和字體。",
            "`設計提案簡報`協助企業向政府與投資者精準傳達企業資訊。",
            "利用 Figma 進行`產品與原型設計`，提升企業對外溝通效率。",
            "利用資訊設計能力設計 UI，透過訪談用戶需求`設計產品功能`，並`與工程師協作`開發產品。",
        ]
    ),
    children=[
        Card(
            header=Image("/assets/imgs/projects/songla/cover.png"),
            body=[
                Text("產品設計師／技術總管", "h4"),
                Text("2022/01 ~ 2023/09"),
                DivBar(),
                ListStr(
                    [
                        "設計提案簡報協助企業向政府與投資者精準傳達企業資訊，最終團隊`通過教育部青年署 U-start 創新創業第一階段計畫`。",
                        "利用資訊設計能力設計 UI，透過訪談 5名用戶需求於 Figma 進行產品設計，`建立企業原子設計系統設計`並完成產品 MVP。",
                    ]
                ),
            ],
            footer=[LinkButton("專案網址", "/projects/songla.html")],
        ),
        Card(
            body=[
                Text("軟體介面設計", "h4"),
                DivBar(),
                ListDiv(
                    [
                        ListStr(
                            [
                                "使用 Figma 建利`高品質、交互式的軟體原型`。這使得整個設計過程更具有靈活性，能夠輕鬆地與團隊進行協作和討論，同時也能更好地呈現我對產品界面的想法。",
                                "深度參與制定商業目標以及軟體功能需求。將`設計融合進整個產品生態系統中`，確保用戶體驗與公司的整體戰略目標保持一致。",
                                "重視使用者的反饋，並將其視為優化產品的關鍵因素。通過與用戶進行緊密的合作、測試和反思，設計出更符合他們期望和需求的界面，從而提高產品的可用性和滿意度。",
                            ]
                        ),
                    ]
                ),
            ],
            footer=[
                ListDiv(
                    [
                        Text("# UI 設計", "span"),
                        Text("# 資訊設計", "span"),
                    ],
                    grid_layout=False,
                ),
            ],
        ),
        Card(
            body=[
                Text("簡報設計工作", "h4"),
                DivBar(),
                ListDiv(
                    [
                        Text("簡報規劃", bold=True),
                        ListStr(
                            [
                                "受眾分析：在簡報前`定義簡報受眾`、主述內容與載體。",
                                "內容規劃：分析受眾`期望內容`、提高簡報與聽眾的連結性、其中專注於受眾利益與需求並`思考對象需要甚麼`，將既有資料提出洞察。",
                                "簡報設計：基於`簡報場景`、`目標用戶`微調字體大小與設計母版，確保簡報在不同設備上都能正常顯示。",
                            ]
                        ),
                    ]
                ),
                ListDiv(
                    [
                        Text("簡報設計", bold=True),
                        ListStr(
                            [
                                "視覺化設計：使用圖表、圖形和圖片來增強簡報的可視性和吸引力，並`幫助觀眾更好地理解數據`。",
                                "利用轉化簡報動畫，`引導觀眾的視線流動`，讓他們能夠更好地理解簡報的內容。",
                                "簡報設計的關鍵在於`視覺化設計`，這不僅僅是為了美觀，更是為了讓觀眾能夠更好地理解和記住簡報的內容。",
                                "設計系統訂製：為企業建立一致的設計風格，包括排版、用色和字體。",
                            ]
                        ),
                    ]
                ),
            ],
            footer=[
                ListDiv(
                    [
                        Text("# 資訊設計", "span"),
                        Text("# 原子設計", "span"),
                    ],
                    grid_layout=False,
                ),
            ],
        ),
    ],
)
