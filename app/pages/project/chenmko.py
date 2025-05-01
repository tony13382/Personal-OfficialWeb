from app.layouts.project import ProjectPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    Image,
    ImageCarousel,
    ListDiv,
    ListStr,
    Text,
    Tool,
)


page = ProjectPage(
    title="Chenmko 全端網頁開發內容",
    description="Chenmko 企業委託專案，根據客戶提供的設計圖和需求，為企業提供一個完整的官網和後台系統管理產品。",
    startdate="2023/03",
    enddate="2023/06",
    status="closed",
    colorSet=ThemeColor().blue,
    prefix="chenmko",
    cover="/assets/imgs/project/chenmko/cover.png",
    tags=["網站架設", "資料庫設計", "前端開發", "後端開發"],
    tools=[
        Tool("Bootstrap", "RWD 切版與前端介面開發"),
        Tool("php", "後端開發（無框架）"),
        Tool("PostgreSQL", "資料庫設計與管理"),
        Tool("ckeditor", "內容編輯工具"),
    ],
    children=[
        Card(
            header=Image(
                src="/assets/imgs/project/chenmko/cover.webp",
                alt="委託封面圖",
            ),
            body=[
                Text("根據企業的設計圖打造官網和後台系統管理產品。"),
                ListStr(
                    [
                        "技術前端採用 bootstrap 打造出響應式 (RWD) 網頁，確保網站在不同設備上能夠良好地顯示。",
                        "後端採用 php 語言打造，以便後續系統交接「企業要求」。",
                        "網站內容採用英語、日語與繁體中文，確保企業的目標受眾能夠理解網站的內容。",
                    ]
                ),
                Text(
                    "總之，專案的目標是為企業打造一個高效、易用、且能夠展示企業資訊的官網和後台系統便於管理產品與資訊。"
                ),
            ],
        ),
        Card(
            body=[
                Text("後端・Banner 圖片管理", "h3"),
                ImageCarousel(
                    [
                        Image(
                            "/assets/imgs/project/chenmko/banner_manage_2.webp",
                            "Banner 圖片管理 - Modal Show",
                        ),
                        Image(
                            "/assets/imgs/project/chenmko/banner_manage_1.webp",
                            "Banner 圖片管理 - Home",
                        ),
                    ]
                ),
                Text(
                    "這個工具擁有一個簡單的介面，讓您輕鬆地瀏覽您的輪播圖片，並且可以直接進行新增或刪除。您可以使用這個工具上傳新的輪播圖片，也可以隨時刪除您不需要的圖片，讓您的網站上的輪播圖片保持最新和最適合的內容。"
                ),
            ],
            body_gap_size="large",
        ),
        Card(
            body=[
                Text("後端・公司資訊管理", "h3"),
                Image(
                    src="/assets/imgs/project/chenmko/comp_manage.webp",
                    alt="後端・公司資訊管理",
                    allow_pop=True,
                ),
                Text(
                    "提供了管理企業相關資訊的功能，例如企業基本資料、聯絡方式。透過這個系統，企業可以方便地管理自己的資訊，同時也可以提供更多的資訊給客戶與潛在客戶。"
                ),
                Text(
                    "除了基本的企業資訊管理功能外，這個解決方案還結合了 Bootstrap 的 Switches 功能，讓企業可以直觀選擇是否在聯絡我們頁面與 footer 顯示相關資訊。這個自定義顯示開關功能可以提供更多彈性，讓企業可以更好地控制自己的資訊展示。"
                ),
            ],
            body_gap_size="large",
        ),
        Card(
            body=[
                Text("後端・公司沿革資訊管理", "h3"),
                Image(
                    src="/assets/imgs/project/chenmko/comp_history.webp",
                    alt="後端・公司沿革資訊管理",
                    allow_pop=True,
                ),
                Text(
                    "對於企業內容管理者來說，擁有一個易於使用且功能強大的編輯界面是非常重要的。為滿足此需求，我選擇 ckeditor 工具來滿足此需求。"
                ),
                Text(
                    "使用 ckeditor，企業內容管理者可以輕鬆地創建、編輯和格式化網站上的內容，而不需要具備任何編程技能。ckeditor 的簡潔而直觀的界面使得它易於使用，即使是初學者也能夠快速上手。"
                ),
            ],
            body_gap_size="large",
        ),
        Card(
            body=[
                Text("後端・分類表格欄位管理", "h3"),
                Image(
                    src="/assets/imgs/project/chenmko/table_cols.webp",
                    alt="後端・分類表格欄位管理",
                    allow_pop=True,
                ),
                Text(
                    "系統採用開關功能，以讓管理者輕鬆地自訂產品欄位，讓產品展示更具彈性和效果。因為不同產品分類可能需要不同的欄位，而此設計能讓您直覺地開關欄位，以確保只有相關屬性會顯示出來。"
                ),
                Text(
                    "此設計只顯示您需要的欄位。使得產品顯示更專注，更直觀，更容易讓客戶了解。"
                ),
                Text(
                    "在此設計中，您可以在不同的產品分類之間進行快速的欄位切換。我們的開關功能會自動隱藏不需要的欄位，以確保您只看到與您的產品分類相關的欄位。"
                ),
            ],
            body_gap_size="large",
        ),
        Card(
            body=[
                Text("後端・產品管理", "h3"),
                Image(
                    src="/assets/imgs/project/chenmko/products_edit_1.webp",
                    alt="後端・產品管理1",
                    allow_pop=True,
                ),
                Text(
                    "為協助內容管理者更快速便捷地編輯類別產品和欄位。在側邊提供快速切換功能，使管理者可以輕鬆地切換並管理不同的內容。此工具可有效節省時間和提高工作效率。"
                ),
                Text(
                    "使用此工具，內容管理者可以輕鬆地編輯產品和欄位，而不必花費過多的時間在繁瑣的切換操作上。"
                ),
                Image(
                    src="/assets/imgs/project/chenmko/products_edit_2.webp",
                    alt="後端・產品管理2",
                    allow_pop=True,
                ),
                Text(
                    "根據所屬分類動態調整顯示欄位，讓內容管理者在填寫內容時不會被非顯示的欄位干擾。"
                ),
                Text(
                    "這個內容管理系統的設計是為了讓內容管理者更加輕鬆地填寫內容，不顯示該類別關閉的欄位選項，讓內容管理者能夠更加專注於內容本身。"
                ),
            ],
            body_gap_size="large",
        ),
        Card(
            header=Image(
                "/assets/imgs/project/chenmko/db_ErModel.png", "ER Modal Table", True
            ),
            body=[
                Text("資料架構設計（ER-Model）", "h3"),
                ListDiv(
                    children=[
                        Text(
                            "關聯資料表設計思路：",
                            bold=True,
                        ),
                        ListDiv(
                            [
                                Text(
                                    "在一個網站的開發中，遇到了一個困難：不同分類的產品需要不同的欄位進行描述，而這些欄位的數量和內容是不同的，因此無法在單一的產品資料表中完成描述。為了解決這個問題，採用了一個新的設計方法。"
                                ),
                                Text(
                                    """
我設計了三個資料表： `cols_html`、`products`和`category`。<br>
`cols_html` 用來存放欄位資料，`products` 用來存放產品資料，`category` 用來存放產品分類資料。
"""
                                ),
                                Text(
                                    """
此外，團隊還設計了兩個關聯資料表：`products_col_link`和`cols_congfigs`。<br>
其中，`products_col_link` 用來關聯產品和欄位，
`cols_congfigs` 用來定義每個分類所需要啟用的欄位。
"""
                                ),
                                Text(
                                    "當用戶需要查詢某個分類的產品時，系統會根據分類檢索產品和欄位資料。接著，系統會動態生成SQL語句，根據所需欄位進行查詢。最終，系統會將查詢結果呈現在前端頁面上。"
                                ),
                                Text(
                                    "通過這種設計方法，團隊成功地解決了不同分類產品欄位描述的問題。這種方法不僅提高了系統的可擴展性和可維護性，還能夠有效地處理複雜的查詢需求。在實際的應用中，這個設計還能夠進一步擴展，滿足更多複雜的需求。"
                                ),
                            ]
                        ),
                    ],
                    mt=3,
                ),
                ListDiv(
                    children=[
                        Text(
                            "需求：",
                            bold=True,
                        ),
                        ListStr(
                            [
                                "各個分類會有不一樣的資料表欄位",
                                "每個分類會對應多樣商品",
                                "單頁最多呈現 50 樣商品（需分頁）",
                                "單頁最多呈現 50 樣商品（需分頁）",
                                "可根據資訊排序所有商品",
                                "欄位資料為數字與文字混合（需要進行數字大小排序）",
                                "跨分類資料檢索",
                            ]
                        ),
                    ],
                    mt=3,
                ),
                ListDiv(
                    children=[
                        Text(
                            "執行：",
                            bold=True,
                        ),
                        ListStr(
                            [
                                "設計三個資料表存放欄位 `cols_html`、產品 `products`、分類 `category`",
                                "設計 `products_col_link` ：存放欄位資料、`cols_congfigs`：每個分類所需要啟用的欄位",
                                "透過分類檢索產品與欄位、動態生成 SQL ，最後透過 INNER JOIN / GROUP（聚合）、SUBSTRING / ORDER(排序)彙整成一張產品資料表",
                            ]
                        ),
                    ],
                    mt=3,
                ),
                ListDiv(
                    children=[
                        Text(
                            "獨立資料表：",
                            bold=True,
                        ),
                        ListStr(
                            [
                                "company：企業資訊紀錄",
                                "banner：首頁 banner 圖片管理",
                                "backend_psw_config：後台加密後密碼驗證",
                                "company_history：企業沿革資訊管理",
                            ]
                        ),
                    ],
                    mt=3,
                ),
            ],
        ),
    ],
)
with open(f"test.html", "w", encoding="utf-8") as f:
    f.write(str(page))
    print("Output to html Successful.")
