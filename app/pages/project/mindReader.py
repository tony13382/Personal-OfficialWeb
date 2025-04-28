from app.layouts.project import ProjectPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    Div,
    DivBar,
    FileLink,
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
    title="MindReader 與你心譯相通",
    description="透過文本分析技術微調用戶輸入文本，經由技術精準的表達出文字中所包含的情感和意思，減少生活上的誤會。",
    subdescription="擔任：CTO, Product Designer<br>負責：軟體架構設計、產品介面設計、資料庫設計、軟體開發、技術管理",
    startdate="2019/11",
    enddate="2020/12",
    status="closed",
    colorSet=ThemeColor().orange,
    prefix="mindReader",
    cover="/assets/imgs/mindReader/cover.png",
    description_links=[
        LinkButton(
            content="專案網址",
            href="https://github.com/tony13382/MindReader-MVP",
            open_in_tab=True,
            icon="bi-github",
        )
    ],
    tags=["介面設計", "產品規劃", "UX 優化"],
    scores=[
        Score("2021 大專校院資訊應用服務創新競賽", "佳作", "資訊應用組"),
        Score("2021 大專校院資訊應用服務創新競賽", "第三名", "Azure 雲端組"),
        Score("中原大學資管系 110 學年度資訊管理畢業專題競賽", "第一名"),
        Score("109 學年度中原大學資管系資訊管理專題初賽", "第二名"),
        Score("110 年中原大學高教深耕學生解決企業問題研究團隊計畫", "佳作"),
    ],
    tools=[
        Tool("Figma", "UI & Prototype"),
        Tool("Bootstrap V5.0", "前端框架"),
        Tool("Azure LUIS", "NLP 自然語言處理、文字意圖分析"),
        Tool("Firebase", "NoSQL 資料庫交互"),
        Tool("Flask", "伺服器 API 建置"),
        Tool("Django", "LineBot Server"),
        Tool("Jieba", "NLP處理、斷詞"),
        Tool("OpenCC", "文字處理（簡繁轉換）"),
    ],
    children=[
        Card(
            header=Youtube("https://www.youtube.com/embed/VzLFWFRzGh8"),
            body=[
                Text(
                    "相信使用過通訊軟體的人都曾遇到過這些問題：說話詞不達意和因感受不到對方情緒而造成誤會，這是因為每個人對訊息文字的解讀都有所不同，嚴重時甚至會導致人際關係上的破裂。為了解決以上這些問題，我們想出了一種輔助聊天的應用程式。它能幫助人們精準的表達出文字中所包含的情感和意思，從而減少誤會的發生，讓文字變得更有溫度，就算隔著螢幕，也能感覺像是面對面談話一般。"
                ),
            ],
        ),
        Card(
            body=[
                Text("產品優勢", "h3"),
                ListDiv(
                    [
                        Div(Text("客製化對話情境", "span", bold=True)),
                        Text(
                            "為聊天對象設定角色定位並打造出專屬於你的客製化說話情境。希望能藉此系統為使用者雙方都帶來舒適的聊天體驗，不會因為是透過文字傳遞訊息而有所誤會甚至是產生衝突，解決文字訊息中無法確切傳遞出情感的問題。"
                        ),
                    ],
                    "nano",
                ),
                ListDiv(
                    [
                        Div(Text("聊天話題不間斷", "span", bold=True)),
                        Text(
                            "為了讓使用者能將話題不斷地延續下去，系統能透過過往的聊天紀錄去分析用戶間有所共鳴的話題，並結合當下的時事推薦給你。除了共鳴的話題之外，系統也會推薦各種不同領域的熱門話題，並附上一段開頭語句，讓你成為話題高手，聊天不間斷。"
                        ),
                    ],
                    "nano",
                ),
                ListDiv(
                    [
                        Div(Text("個人化智慧提醒", "span", bold=True)),
                        Text(
                            "人們常需要將已經安排好的行程再次手動輸入到手機行事曆中，費時又費力，利用系統的功能一鍵加入，便利又快速。智慧提醒能在最即時和適當的時間推播個人化的資訊，如:本日行程、天氣、股市的波動等等。讓MindReader替你安排好，使你輕鬆沒煩惱，成為你專屬的智慧秘書。"
                        ),
                    ],
                    "nano",
                ),
            ],
            body_gap_size="large",
        ),
        Card(
            body=[
                Text("產品架構", "h3"),
                DivBar(),
                Image(
                    "/assets/imgs/mindReader/systemFrame.png",
                    "MindReader's system design",
                    True,
                ),
                DivBar(),
                Image(
                    "/assets/imgs/mindReader/systemFrame2.png",
                    "MindReader's system design",
                    True,
                ),
            ]
        ),
        Card(
            header=UiImageCarousel(
                [
                    "/assets/imgs/mindReader/keybroad01.png",
                    "/assets/imgs/mindReader/keybroad02.png",
                    "/assets/imgs/mindReader/keybroad03.png",
                    "/assets/imgs/mindReader/keybroad04.png",
                ]
            ),
            body=(
                [
                    Text("設計理念", "h3"),
                    Text("介面設計貼近原生鍵盤體驗，唯一記得的事就是`輸入`"),
                    ListDiv(
                        [
                            FileLink(
                                title="Figma 原型展示連結",
                                subtitle="Figma",
                                src="https://www.figma.com/proto/Tk1mSaUpLrBxUdHbHQvtQd/%5B2021-MR%5D-APP-Design?page-id=0%3A1&node-id=58%3A3277&viewport=241%2C48%2C0.14&scaling=scale-down&starting-point-node-id=58%3A3277&show-proto-sidebar=1",
                                icon="bi-phone-fill",
                            ),
                            FileLink(
                                title="MVP 網頁",
                                subtitle="GitHub",
                                src="https://github.com/tony13382/MindReader-MVP/",
                                icon="bi-github",
                            ),
                        ],
                        mt=3,
                    ),
                ]
            ),
        ),
        Card(
            header=Image("/assets/imgs/mindReader/apiFlow (1).jpg", "API Flow", True),
            body=[
                Text("輸入文本轉換流程", "h3"),
                Html(
                    """
<div class="d-grid gap-3">
    <div class="col-12">
        <div class="card rounded-inline-basic">
            <div class="card-body">
                <div class="row">
                    <div class="col-auto fs-3 text-center d-flex justify-content-center align-items-center ps-3">
                        <i class="bi bi-keyboard"></i>
                    </div>
                    <div class="col d-flex align-items-center ps-3">
                        <p class="m-0">
                            用戶輸入（鍵盤攔截）
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="col-12">
        <div class="card rounded-inline-basic">
            <div class="card-body">
                <div class="row">
                    <div class="col-auto fs-3 text-center d-flex justify-content-center align-items-center ps-3">
                        <i class="bi bi-hdd-network"></i>
                    </div>
                    <div class="col d-flex align-items-center ps-3">
                        <p class="m-0">
                            鍵盤利用 Web APIs 將文字傳送至 <span class="fw-bold">MindReader
                                Core</span>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="col-12">
        <div class="card rounded-inline-basic">
            <div class="card-body">
                <div class="row">
                    <div class="col-auto fs-3 text-center d-flex justify-content-center align-items-center ps-3">
                        <i class="bi bi-line"></i>
                    </div>
                    <div class="col d-flex align-items-center ps-3">
                        <p class="m-0">
                            <span class="fw-bold">Line Bot</span> 抓取用戶 ID
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="col-12">
        <div class="card rounded-inline-basic">
            <div class="card-body">
                <div class="row">
                    <div class="col-auto fs-3 text-center d-flex justify-content-center align-items-center ps-3">
                        <i class="bi bi-arrow-repeat"></i>
                    </div>
                    <div class="col d-flex align-items-center ps-3">
                        <p class="m-0">
                            根據 ID 與文字進行轉換
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="col-12">
        <div class="card rounded-inline-basic">
            <div class="card-body">
                <div class="row">
                    <div class="col-auto fs-3 text-center d-flex justify-content-center align-items-center ps-3">
                        <i class="bi bi-send"></i>
                    </div>
                    <div class="col d-flex align-items-center ps-3">
                        <p class="m-0">
                            傳送轉譯後文字
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="col-12">
        <div class="card rounded-inline-basic">
            <div class="card-body">
                <div class="row">
                    <div class="col-auto fs-3 text-center d-flex justify-content-center align-items-center ps-3">
                        <i class="bi bi-hdd-network"></i>
                    </div>
                    <div class="col d-flex align-items-center ps-3">
                        <p class="m-0">
                            接收使用者以外的回饋文字
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="col-12">
        <div class="card rounded-inline-basic">
            <div class="card-body">
                <div class="row">
                    <div class="col-auto fs-3 text-center d-flex justify-content-center align-items-center ps-3">
                        <i class="bi bi-database-down"></i>
                    </div>
                    <div class="col d-flex align-items-center ps-3">
                        <p class="m-0">
                            <span class="fw-bold">錄入資料</span> 進行評分
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
"""
                ),
            ],
            body_gap_size="large",
        ),
    ],
)
