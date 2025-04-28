from app.layouts.job import JobPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    DivBar,
    Image,
    LinkButton,
    ListStr,
    Text,
)


page = JobPage(
    title="產品設計師／技術總管",
    description="即時行樂有限公司（新創）",
    startdate="2022/01",
    enddate="2023/09",
    colorSet=ThemeColor().green,
    prefix="2022_songla",
    cover="/assets/imgs/jobs/2022_songla/cover.png",
    tags=["資訊設計", "提案", "UI 設計", "系統規劃"],
    children=[
        Card(
            header=Image("/assets/imgs/songla/cover.png"),
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
                DivBar(),
                Text("軟體介面設計", bold=True),
                ListStr(
                    [
                        "使用 Figma 這一優秀的設計工具來創建高品質、交互式的軟體原型。這使得整個設計過程更具有靈活性，能夠輕鬆地與團隊進行協作和討論，同時也能更好地呈現我對產品界面的想法。",
                        "我深度參與制定商業目標以及軟體功能需求。這讓我能夠將設計融合進整個產品生態系統中，確保用戶體驗與公司的整體戰略目標保持一致。",
                        "我非常重視使用者的反饋，並將其視為優化產品的關鍵因素。通過與用戶進行緊密的合作、測試和反思，我能夠設計出更符合他們期望和需求的界面，從而提高產品的可用性和滿意度。",
                    ]
                ),
                DivBar(),
                Text("軟體規劃、設計、開發", bold=True),
                ListStr(
                    [
                        "建立企業形象網頁。我使用了現代化的設計風格、符合最佳用戶體驗的介面設計和直觀的導航結構，以確保網站能夠有效地展示公司的核心價值和產品特色。",
                        "深入研究音樂理論和人工智能相關技術，協助設計了一個優秀的音樂生成系統。這個系統能夠根據用戶哼唱的旋律，自動生成與之匹配的音樂內容",
                    ]
                ),
                DivBar(),
                Text("簡報設計", bold=True),
                ListStr(
                    [
                        "我深信言簡意賅的原則。我會針對聽眾選擇最重要的資料和信息，以清晰簡明的方式呈現，避免信息過於冗長或混淆。",
                        "我精通使用各種視覺化工具和技巧，將不同資料轉化為生動有趣且易於理解的圖表和圖形。這有助於觀眾迅速抓住重要信息，從而更好地理解我所呈現的內容。",
                        "為了確保簡報的一致性和專業性，我替公司設計視覺識別指南，使用統一的字體、色彩和排版風格。這有助於確保我所設計的每一份簡報都代表著公司的形象和價值觀。",
                    ]
                ),
            ],
            footer=[LinkButton("專案網址", "/projects/songla.html")],
        ),
    ],
)
