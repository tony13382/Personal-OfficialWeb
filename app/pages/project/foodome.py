from app.layouts.project import ProjectPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    HtmlCarousel,
    IconBlock,
    Image,
    LinkButton,
    ListDiv,
    Text,
    Tool,
)


page = ProjectPage(
    title="食材外送專家 - Foodome",
    description="本產品提供客戶食譜教學的服務，並且以銷售食材為主要的收入來源。",
    subdescription="擔任：Product Designer, 行銷策劃<br>負責：產品介面設計、行銷企劃",
    startdate="2020/07",
    enddate="2020/08",
    status="closed",
    colorSet=ThemeColor().purple,
    prefix="foodome",
    cover="/assets/imgs/projects/foodome/cover.png",
    description_links=[
        LinkButton(
            content="企劃書網址",
            href="https://drive.google.com/file/d/1cK0o97WPkW5v2Z6mb2eFtH3JYOkN6VJ8/view",
            open_in_tab=True,
            icon="bi-cloud",
        ),
    ],
    skill_types=["design", "plan"],
    tags=["介面設計", "企劃書製作"],
    tools=[
        Tool("Figma", "UI Design"),
        Tool("Word", "企劃書撰寫"),
    ],
    children=[
        Card(
            body=[
                Text("專案文檔", "h3"),
                ListDiv(
                    [
                        IconBlock(
                            title="系統規格書",
                            subtitle="PDF",
                            icon="bi-file-earmark-arrow-down",
                            src="https://drive.google.com/file/d/1cK0o97WPkW5v2Z6mb2eFtH3JYOkN6VJ8/view",
                        ),
                        IconBlock(
                            title="Figma 設計界面稿",
                            subtitle="Figma",
                            icon="bi-window-sidebar",
                            src="https://www.figma.com/proto/5cHIjh7jgfmHkaxREPKY3D/-2020-%E8%A1%8C%E9%8A%B7%E7%AE%A1%E7%90%86--Foodome-Prototype?node-id=4-288&scaling=min-zoom",
                        ),
                    ]
                ),
            ],
            body_gap_size="large",
        ),
        Card(
            header=HtmlCarousel(
                [
                    ListDiv(
                        [
                            Text("1", "h4", center=True, pill_type=True),
                            Image(
                                "/assets/imgs/projects/foodome/ui01.png",
                                "UI 01",
                                True,
                                max_width=320,
                            ),
                            Text(
                                "快速的提供用戶食譜的教學可以減輕煮菜的徬徨，並且吸引用戶，增加購買食材意願，因此觀賞食譜在這項軟體中佔有極高的優先級，於是我們設計在標準的導航欄上方放置了觀賞食譜的按鈕，而客戶除了使用觀賞食譜的按鈕以外也可以進行客服一對一問答，快速解決客人的問題。"
                            ),
                        ],
                        gap_size="large",
                    ),
                    ListDiv(
                        [
                            Text("2", "h4", center=True, pill_type=True),
                            Image(
                                "/assets/imgs/projects/foodome/ui02.png",
                                "UI 02",
                                True,
                                max_width=320,
                            ),
                            Text(
                                "在商品詳細頁的時候，除了會提供普通的商品說明，還會提供產品圖增加購買慾，並且在底下一方塊來提供所用到的食材，方便讓消費者了解說會購買到哪些食材。"
                            ),
                        ],
                        gap_size="large",
                    ),
                    ListDiv(
                        [
                            Text("3", "h4", center=True, pill_type=True),
                            Image(
                                "/assets/imgs/projects/foodome/ui03.png",
                                "UI 03",
                                True,
                                max_width=320,
                            ),
                            Text(
                                "在運送詳情頁的時候，除了會附上你所購買的食材明細之外，還會有即時路況讓你看看你現在的食材運輸到那裡，以方便使用者進行規劃。"
                            ),
                        ],
                        gap_size="large",
                    ),
                    ListDiv(
                        [
                            Text("4", "h4", center=True, pill_type=True),
                            Image(
                                "/assets/imgs/projects/foodome/ui04.png",
                                "UI 04",
                                True,
                                max_width=320,
                            ),
                            Text(
                                "在食材影片教學的影片下方，會提供快速大綱以供選擇，只要點選文字就會自動的將影片跳轉到文字所標註的時間點，讓使用者可以快速依照文字找到所需要的部分進行觀看。"
                            ),
                        ],
                        gap_size="large",
                    ),
                ]
            )
        ),
    ],
)
