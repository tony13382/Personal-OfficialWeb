from app.layouts.project import ProjectPage
from app.variables import SpaceSet, ThemeColor
from app.elements import (
    Card,
    DivBar,
    HtmlCarousel,
    IconBlock,
    Html,
    Image,
    LinkButton,
    ListDiv,
    Score,
    Tab,
    TabItem,
    Text,
    Tool,
    UiImageCarousel,
    Youtube,
)


page = ProjectPage(
    title="Songla 音樂智慧創作小幫手",
    description="哼唱即可作曲，讓創作音樂不再是遙不可及的夢想",
    subdescription="擔任：CTO, Product Designer<br>負責：軟體架構設計、產品介面設計、UX 優化、簡報設計",
    startdate="2022/01",
    enddate="2023/09",
    status="closed",
    colorSet=ThemeColor().green,
    prefix="songla",
    pin=True,
    cover="/assets/imgs/projects/songla/cover.png",
    description_links=[
        LinkButton(
            content="公司網站（封存）",
            href="https://tony13382.github.io/Songla-OfficialWeb/",
            open_in_tab=True,
            icon="bi-building",
        ),
        LinkButton(
            content="Figma 原型展示連結",
            href="https://www.figma.com/proto/4oTSzb5vE1VzRp7nYXCYiy/202112---SL--%E8%BB%9F%E9%AB%94%E5%88%9D%E7%A8%BF%E5%9C%96?node-id=321-262&t=BiEbxhMaInIN0bkG-1&starting-point-node-id=321:262",
            open_in_tab=True,
            icon="bi-phone",
        ),
    ],
    skill_types=["pin", "design"],
    tags=["介面設計", "產品規劃", "UX 優化"],
    scores=[
        Score("通過教育部青年署 U-start 創新創業第一階段計畫", "取得 50 萬資金"),
        Score("2021 全國大專校院智慧創新暨跨域整合創作競賽", "佳作"),
        Score("2021 桃園新創之星創天下實作競賽", "佳作"),
    ],
    tools=[
        Tool("Figma", "UI 設計與產品原型設計"),
        Tool("PowerPoint", "資訊設計與簡報文案編輯"),
        Tool("Notion", "企業時程控管、檔案管理、多團隊協作系統"),
    ],
    children=[
        Card(
            header=Youtube("https://www.youtube.com/embed/QMBos6hJSsg"),
            body=[
                Text(
                    "即時行樂「 Song la -音樂創作智慧小幫手」，是一款`結合社群功能的音樂創作手機軟體`，藉由哼唱人聲，系統能夠根據旋律智慧編曲，將編曲樂器轉換成 275 種不同音色，並且產出樂譜，錄製曲子上傳至分享平台，完成屬於使用者獨創的曲子，達到音樂創作直覺化、音色呈現多元化、樂譜產生自動化、音樂傳播數位化等效益，「即時行樂 Song la」 讓創作音樂不再是遙不可及的夢想，幫助更多人跨入音樂創作的世界，讓腦中的新創意能夠具體化展現在生活中。"
                ),
            ],
        ),
        Card(
            body=[
                Text("產品架構「公開版」", "h3"),
                DivBar(),
                Image(
                    "/assets/imgs/projects/songla/systemFrame2.png", "產品架構 1", True
                ),
                DivBar(),
                Image(
                    "/assets/imgs/projects/songla/systemFrame.png", "產品架構 2", True
                ),
            ],
            body_gap_size="large",
        ),
        Card(
            header=UiImageCarousel(
                [
                    "/assets/imgs/projects/songla/UI01.png",
                    "/assets/imgs/projects/songla/UI02.png",
                    "/assets/imgs/projects/songla/UI03.png",
                    "/assets/imgs/projects/songla/UI04.png",
                ]
            ),
            body=(
                [
                    Text("Figma 原型展示連結", "h3"),
                    IconBlock(
                        src="https://www.figma.com/proto/4oTSzb5vE1VzRp7nYXCYiy/202112---SL--%E8%BB%9F%E9%AB%94%E5%88%9D%E7%A8%BF%E5%9C%96?node-id=306-8&t=BiEbxhMaInIN0bkG-1",
                        icon="bi-phone",
                        title="Figma 原型展示連結",
                        subtitle="Figma",
                    ),
                ]
            ),
            body_gap_size="large",
        ),
        Card(
            body=[
                Text("導航列設計", "h3"),
                DivBar(),
                Image("/assets/imgs/projects/songla/ux/Navbar.png", "導航列設計"),
                DivBar(),
                Tab(
                    [
                        TabItem(
                            title="探索",
                            content=ListDiv(
                                [
                                    DivBar(),
                                    Html(
                                        """
<div class="py-4">
    <p class="m-0 fs-4 text-center">根據用戶訪談，有</p>
    <p class="m-0 fs-3 text-center">高達<span class="px-1 text-projectSonglaPrimary fw-bold" style="font-size:5rem;"> 89</span>
        <span class="fw-bold text-projectSonglaPrimary pe-1">%</span>的用戶
    </p>
    <p class="m-0 fs-4 text-center">認為沒有靈感阻礙了他們創作</p>
</div>
"""
                                    ),
                                    DivBar(),
                                    Text("在`探索`我們可以", "h4"),
                                    ListDiv(
                                        [
                                            IconBlock(
                                                title="利用風格篩選的音樂，透過他人作品找尋靈感",
                                                icon="bi-crosshair2",
                                            ),
                                            IconBlock(
                                                title="精選與你相關的熱門音樂，了解你創作的最新趨勢",
                                                icon="bi-fire",
                                            ),
                                            IconBlock(
                                                title="瀏覽社群，聆聽朋友的作品來思考作品",
                                                icon="bi-share-fill",
                                            ),
                                        ],
                                        space=SpaceSet(mt=2),
                                    ),
                                ]
                            ),
                        ),
                        TabItem(
                            title="動態",
                            content=ListDiv(
                                [
                                    DivBar(),
                                    Html(
                                        """
<div class="py-4">
    <p class="m-0 fs-4 text-center">根據用戶訪談</p>
    <p class="m-0 fs-3 text-center">有<span class="ps-1 text-projectSonglaPrimary fw-bold" style="font-size: 5rem;">2/3</span>
        <span class="fw-bold text-projectSonglaPrimary pe-1">以上</span>的用戶
    </p>
    <p class="m-0 fs-4 text-center">對於<span class="mx-1 fw-bold">社群＋音樂</span>提出支持</p>
</div>
"""
                                    ),
                                    DivBar(),
                                    Text("因此在`動態`中我們提供社群相關屬性", "h4"),
                                    ListDiv(
                                        [
                                            IconBlock(
                                                title="音樂創作挑戰",
                                                subtitle="你可以發起自訂主題或風格的創作挑戰，當然也可以加入其他人的競賽，用作品來交流！",
                                                icon="bi-flag-fill",
                                            ),
                                            IconBlock(
                                                title="分享音樂作品",
                                                subtitle="分享你喜愛的音樂作品，讓你的追隨者也能聽見你聽到的好聲音。",
                                                icon="bi-headphones",
                                            ),
                                            IconBlock(
                                                title="生活照片紀錄",
                                                subtitle="與追隨者分享生活或者也能發布活動消息，讓你與你的追隨者更進一步互動。",
                                                icon="bi-image-fill",
                                            ),
                                            IconBlock(
                                                title="文章",
                                                subtitle="你可以分享心情、活動，可以用文字表達的都可以書寫。",
                                                icon="bi-pencil-fill",
                                            ),
                                        ],
                                        space=SpaceSet(mt=2),
                                    ),
                                ]
                            ),
                        ),
                        TabItem(
                            title="錄音室",
                            content=ListDiv(
                                [
                                    DivBar(),
                                    Text(
                                        "即時行樂 Songla `結合音樂創作功能與社群`功能，使用者不需會任何樂器或樂理知識，只要會哼唱就能透過產品的「`智慧編曲`」功能完成屬於自己的音樂，並且上傳至即時行樂分享平台或下載保存至手機，`大幅降低創作所需門檻`。"
                                    ),
                                    ListDiv(
                                        [
                                            IconBlock(
                                                title="音樂創作",
                                                subtitle="打開Songla 錄音室，按下錄音鍵開始哼唱旋律。",
                                                icon="bi-mic",
                                            ),
                                            IconBlock(
                                                title="智慧編曲",
                                                subtitle="交給 Songla 讓 AI 幫你編出獨一無二的曲子。",
                                                icon="bi-stars",
                                            ),
                                            IconBlock(
                                                title="選擇音色",
                                                subtitle="從 275 種音色裡面任選喜歡音色演奏自己的創作。",
                                                icon="bi-music-note-list",
                                            ),
                                            IconBlock(
                                                title="瀏覽樂譜",
                                                subtitle="Songla 幫你編寫樂譜，誰說需要樂理才能當音樂家？",
                                                icon="bi-file-earmark-music",
                                            ),
                                            IconBlock(
                                                title="與世界共享",
                                                subtitle="按下分享鍵，讓自己的音樂跟來自世界各地的朋友們分享吧！",
                                                icon="bi-box-arrow-right",
                                            ),
                                        ],
                                        space=SpaceSet(mt=2),
                                    ),
                                ]
                            ),
                        ),
                        TabItem(
                            title="點數",
                            content=ListDiv(
                                [
                                    DivBar(),
                                    Image(
                                        "/assets/imgs/projects/songla/laCoin.png",
                                        "點數用途",
                                        rounded=True,
                                    ),
                                    DivBar(),
                                    Text("在`點數`我們可以", "h4"),
                                    ListDiv(
                                        [
                                            IconBlock(
                                                title="蒐集樂幣",
                                                icon="bi-collection",
                                            ),
                                            IconBlock(
                                                title="轉換樂幣",
                                                icon="bi-arrow-repeat",
                                            ),
                                            IconBlock(
                                                title="消費樂幣",
                                                icon="bi-wallet",
                                            ),
                                        ],
                                        space=SpaceSet(mt=2),
                                    ),
                                ]
                            ),
                        ),
                    ]
                ),
            ]
        ),
        Card(
            body=[
                Text("音樂封面照", "h3"),
                DivBar(),
                HtmlCarousel(
                    [
                        ListDiv(
                            [
                                Text("寬版音樂封面照", "h4"),
                                Image(
                                    "/assets/imgs/projects/songla/ux/Music Wider.png"
                                ),
                                Text(
                                    "多用於需要給予較多資訊內容的場景，如：工作室、搜尋結果。"
                                ),
                                DivBar(),
                                Text(
                                    "`呈現內容包含：`<br>音樂標題、封面照片、封面照片、音樂介紹、音樂分類、音樂長度、播放次數、授權方式。"
                                ),
                            ]
                        ),
                        ListDiv(
                            [
                                Text("標準音樂封面照", "h4"),
                                Image("/assets/imgs/projects/songla/ux/Music List.png"),
                                Text(
                                    "運用於預設場景，如：首頁推播音樂、分類排行榜、搜尋預覽。"
                                ),
                                DivBar(),
                                Text(
                                    "`呈現內容包含：`<br>音樂標題、封面照片、封面照片、音樂分類、音樂長度、播放次數、授權方式。"
                                ),
                            ]
                        ),
                        ListDiv(
                            [
                                Text("窄版音樂封面照", "h4"),
                                Image("/assets/imgs/projects/songla/ux/Music Thin.png"),
                                Text(
                                    "多用於不重於資訊內容的場景，如：社群附加音樂、播放紀錄。"
                                ),
                                DivBar(),
                                Text(
                                    "`呈現內容包含：`<br>音樂標題、音樂長度、播放次數。"
                                ),
                            ]
                        ),
                    ]
                ),
            ],
        ),
        Card(
            body=[
                Text("設計上的思考", "h3"),
                DivBar(),
                Tab(
                    [
                        TabItem(
                            title="色彩",
                            content=str(
                                ListDiv(
                                    [
                                        DivBar(),
                                        Image(
                                            "/assets/imgs/projects/songla/ux/colortheme.png",
                                            "設計色彩系統",
                                            max_width=400,
                                        ),
                                        Text("運用多彩色系營造活潑的感覺", center=True),
                                    ],
                                    gap_size="large",
                                )
                            ),
                        ),
                        TabItem(
                            title="蒙版漸層背景設計",
                            content=str(
                                ListDiv(
                                    [
                                        DivBar(),
                                        Image(
                                            "/assets/imgs/projects/songla/ux/colorBG.png",
                                            "蒙版漸層背景設計",
                                            max_width=400,
                                        ),
                                        Text("運用漸層營造立體的感覺", center=True),
                                    ],
                                    gap_size="large",
                                )
                            ),
                        ),
                        TabItem(
                            title="圖示設計",
                            content=str(
                                ListDiv(
                                    [
                                        DivBar(),
                                        Image(
                                            "/assets/imgs/projects/songla/ux/iconpack.png",
                                            "圖示設計",
                                            max_width=400,
                                        ),
                                        Text(
                                            "依據漸層色設計風格結合主色調與圖標進行融合成為獨一無二的專屬圖標",
                                            center=True,
                                        ),
                                        Text(
                                            "上述所述圖標取得於 IconPark 釋出之開源圖標庫、官方 Material Icons 與呂亮進本人設計，",
                                            center=True,
                                        ),
                                    ],
                                    gap_size="large",
                                )
                            ),
                        ),
                    ]
                ),
            ]
        ),
    ],
)
