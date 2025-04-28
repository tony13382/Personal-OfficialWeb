from app.layouts.project import ProjectPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    DivBar,
    FileLink,
    Html,
    Image,
    Link,
    Score,
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
    cover="/assets/imgs/songla/cover.png",
    description_links=[
        Link(
            content="公司社群網站",
            href="https://linkby.tw/Songla",
            open_in_tab=True,
            icon="bi-building",
        )
    ],
    tags=["介面設計", "產品規劃", "UX 優化"],
    scores=[
        Score("通過教育部青年署 U-start 創新創業第一階段計畫", "取得 50 萬資金"),
        Score("2021 全國大專校院智慧創新暨跨域整合創作競賽", "佳作"),
        Score("2021 桃園新創之星創天下實作競賽", "佳作"),
    ],
    tools=[
        Tool("Figma", "UI & Prototype"),
        Tool("Notion", "時程控管、檔案管理"),
        Tool("PowerPoint", "簡報視覺與編排"),
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
                Image("/assets/imgs/songla/systemFrame2.png", "產品架構 1", True),
                DivBar(),
                Image("/assets/imgs/songla/systemFrame.png", "產品架構 2", True),
            ],
            body_gap_size="large",
        ),
        Card(
            header=UiImageCarousel(
                [
                    "/assets/imgs/songla/UI01.png",
                    "/assets/imgs/songla/UI02.png",
                    "/assets/imgs/songla/UI03.png",
                    "/assets/imgs/songla/UI04.png",
                ]
            ),
            body=(
                [
                    Text("Figma 原型展示連結", "h3"),
                    FileLink(
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
                Image("/assets/imgs/songla/ux/Navbar.png", "導航列設計"),
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
                Html(
                    """
<div class="row">
    <div class="d-flex d-flex align-items-center">
        <p class="m-0 fs-4">在</p>
        <p class="m-0 fs-4 ms-0 me-1 align-items-center d-flex">
            <img src="/assets/imgs/songla/ux/icon-home.svg" width="48px">
            <b>探索</b>
        </p>
        <p class="m-0 fs-4">我們可以</p>
    </div>
</div>
<div class="row d-flex align-items-stretch">
    <div class="col-6 col-md-6 p-2">
        <div class="card h-100 rounded-inline-basic">
            <div class="card-body pb-4">
                <p class="fs-1 m-0 text-success pb-2"><i class="bi bi-crosshair2"></i></p>
                <p class="m-0">利用風格篩選的音樂，透過他人作品找尋靈感</p>
            </div>
        </div>
    </div>
    <div class="col-6 col-md-6 p-2">
        <div class="card h-100 rounded-inline-basic">
            <div class="card-body pb-4">
                <p class="fs-1 m-0 text-danger pb-2"><i class="bi bi-fire"></i></p>
                <p class="m-0">精選與你相關的熱門音樂，了解你創作的最新趨勢</p>
            </div>
        </div>
    </div>
    <div class="col-6 col-md-6 p-2">
        <div class="card h-100 rounded-inline-basic">
            <div class="card-body pb-4">
                <p class="fs-1 m-0 text-info pb-2"><i class="bi bi-share-fill"></i></p>
                <p class="m-0">瀏覽社群，聆聽朋友的作品來思考作品</p>
            </div>
        </div>
    </div>
    <div class="col-6 col-md-6 p-2">
        <div class="card h-100 rounded-inline-basic">
            <div class="card-body pb-4">
                <p class="fs-1 m-0 text-warning pb-2"><i class="bi bi-search"></i></p>
                <p class="m-0">利用風格篩選的音樂，透過他人作品找尋靈感</p>
            </div>
        </div>
    </div>
</div>
"""
                ),
            ]
        ),
        Card(
            body=[
                Text("音樂社群設計", "h3"),
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
                Html(
                    """
<div class="row">
    <div class="d-flex d-flex align-items-center my-3">
        <p class="m-0 fs-4">因此在</p>
        <p class="m-0 fs-4 ms-0 me-1 align-items-center d-flex">
            <img src="/assets/imgs/songla/ux/icon-social.svg" class="p-1" width="48px">
            <b>動態</b>
        </p>
        <p class="m-0 fs-4">中我們提供社群相關屬性</p>
    </div>
    <div class="col-12 col-md-6 d-flex p-2">
        <div class="card flex-fill rounded-inline-basic">
            <div class="card-body">
                <p class="fs-1 m-0 text-success pb-2"><i class="bi bi-flag-fill"></i></p>
                <p class="m-0 mb-2 fw-bold">音樂創作挑戰</p>
                <p class="m-0">你可以發起自訂主題或風格的創作挑戰，當然也可以加入其他人的競賽，用作品來交流！</p>
            </div>
        </div>
    </div>
    <div class="col-12 col-md-6 d-flex p-2">
        <div class="card flex-fill rounded-inline-basic">
            <div class="card-body">
                <p class="fs-1 m-0 text-danger pb-2"><i class="bi bi-headphones"></i></p>
                <p class="m-0 mb-2 fw-bold">分享音樂作品</p>
                <p class="m-0">分享你喜愛的音樂作品，讓你的追隨者也能聽見你聽到的好聲音。</p>
            </div>
        </div>
    </div>
    <div class="col-12 col-md-6 d-flex p-2">
        <div class="card flex-fill rounded-inline-basic">
            <div class="card-body">
                <p class="fs-1 m-0 text-info pb-2"><i class="bi bi-image-fill"></i></p>
                <p class="m-0 mb-2 fw-bold">生活照片紀錄</p>
                <p class="m-0">與追隨者分享生活或者也能發布活動消息，讓你與你的追隨者更進一步互動。</p>
            </div>
        </div>
    </div>
    <div class="col-12 col-md-6 d-flex p-2">
        <div class="card flex-fill rounded-inline-basic">
            <div class="card-body">
                <p class="fs-1 m-0 text-warning pb-2"><i class="bi bi-pencil-fill"></i></p>
                <p class="m-0 mb-2 fw-bold">文章</p>
                <p class="m-0">你可以分享心情、活動，可以用文字表達的都可以書寫。</p>
            </div>
        </div>
    </div>
</div>
"""
                ),
            ]
        ),
        Card(
            body=[
                Html(
                    """
<div class="row">
    <p class="fs-4 col-12">
        <img src="/assets/imgs/songla/ux/icon-record.svg" width="48px">
        <b>錄音室</b>
    </p>
</div>
<div class="row notoFont">
    <div class="col-12">
        <p class="fs-5 lh-lg">即時行樂Song
            la結合音樂創作功能與社群功能，使用者不需會任何樂器或樂理知識，只要會哼唱就能透過產品的「智慧編曲」功能完成屬於自己的音樂，並且上傳至即時行樂分享平台或下載保存至手機，大幅降低創作所需門檻。
        </p>
        <div class="row">
            <div class="col-12 mb-3">
                <div class="card rounded-inline-basic">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-auto fs-3 text-center d-flex justify-content-center align-items-center ps-3">
                                <i class="bi bi-mic"></i>
                            </div>
                            <div class="col">
                                <p class="m-0 mb-2 fw-bold">
                                    音樂創作
                                </p>
                                <p class="m-0">
                                    打開Songla 錄音室，按下錄音鍵開始哼唱旋律。
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-12 mb-3">
                <div class="card rounded-inline-basic">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-auto fs-3 text-center d-flex justify-content-center align-items-center ps-3">
                                <i class="bi bi-stars"></i>
                            </div>
                            <div class="col">
                                <p class="m-0 mb-2 fw-bold">
                                    智慧編曲
                                </p>
                                <p class="m-0">
                                    交給 Song la 讓 AI 幫你編出獨一無二的曲子。
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-12 mb-3">
                <div class="card rounded-inline-basic">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-auto fs-3 text-center d-flex justify-content-center align-items-center ps-3">
                                <i class="bi bi-music-note-list"></i>
                            </div>
                            <div class="col">
                                <p class="m-0 mb-2 fw-bold">
                                    選擇音色
                                </p>
                                <p class="m-0">
                                    從275種音色裡面任選喜歡音色演奏自己的創作。
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-12 mb-3">
                <div class="card rounded-inline-basic">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-auto fs-3 text-center d-flex justify-content-center align-items-center ps-3">
                                <i class="bi bi-file-earmark-music"></i>
                            </div>
                            <div class="col">
                                <p class="m-0 mb-2 fw-bold">
                                    瀏覽樂譜
                                </p>
                                <p class="m-0">
                                    Song la 幫你編寫樂譜，誰說需要樂理才能當音樂家？
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
                                <i class="bi bi-box-arrow-right"></i>
                            </div>
                            <div class="col">
                                <p class="m-0 mb-2 fw-bold">
                                    與世界共享
                                </p>
                                <p class="m-0">
                                    按下分享鍵，讓自己的音樂跟來自世界各地的朋友們分享吧！
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
"""
                )
            ]
        ),
        Card(
            header=Image("/assets/imgs/songla/laCoin.png", "點數用途"),
            body=[
                Html(
                    """
<div class="row">
    <div class="col-12">
        <div class="d-flex d-flex align-items-center pb-3">
            <p class="m-0 fs-4">在</p>
            <p class="m-0 fs-4 ms-0 me-1 align-items-center d-flex">
                <img src="/assets/imgs/songla/ux/icon-coins.svg" width="48px">
                <b>點數</b>
            </p>
            <p class="m-0 fs-4">我們可以</p>
        </div>
    </div>
    <div class="d-flex col-12 mt-1">
        <div class="card col-12 my-1 rounded-inline-basic">
            <div class="card-body">
                <p class="fs-5 m-0">
                    <i class="bi bi-collection-fill ms-1 me-3 text-info"></i>蒐集樂幣
                </p>
            </div>
        </div>
    </div>
    <div class="d-flex col-12 mt-1">
        <div class="card col-12 my-1 rounded-inline-basic">
            <div class="card-body">
                <p class="fs-5 m-0">
                    <i class="bi bi-arrow-repeat ms-1 me-3 text-warning"></i>轉換樂幣
                </p>
            </div>
        </div>
    </div>
    <div class="d-flex col-12 mt-1">
        <div class="card col-12 my-1 rounded-inline-basic">
            <div class="card-body">
                <p class="fs-5 m-0">
                    <i class="bi bi-wallet-fill ms-1 me-3 text-danger"></i>消費樂幣
                </p>
            </div>
        </div>
    </div>
</div>
"""
                )
            ],
        ),
        Card(
            body=[
                Text("音樂封面照", "h3"),
                DivBar(),
                Html(
                    """
<div class="row justify-content-center align-items-center">
    <div class="col-12 col-md-6 py-2 d-flex justify-content-center">
        <img data-src="/assets/imgs/songla/ux/Music Wider.png" class="card-img-top lozad" alt="songla app song list" src="/assets/imgs/songla/ux/Music Wider.png" data-loaded="true">
    </div>
    <div class="col-12 col-md-6 py-3">
        <h5 class="card-title fw-bold">寬版音樂封面照</h5>
        <p class="card-text msf-info-s">
            呈現內容包含：<br>音樂標題、封面照片、封面照片、音樂介紹、音樂分類、音樂長度、播放次數、授權方式。
        </p>
        <div class="msf-heightlight">
            多用於需要給予較多資訊內容的場景，如：工作室、搜尋結果。
        </div>
    </div>
</div>
"""
                ),
                DivBar(),
                Html(
                    """
<div class="row justify-content-center align-items-center">
    <div class="col-12 col-md-6 py-2 d-flex justify-content-center">
        <img data-src="/assets/imgs/songla/ux/Music List.png" class="card-img-top lozad" alt="songla app song list" src="/assets/imgs/songla/ux/Music List.png" data-loaded="true">
    </div>
    <div class="col-12 col-md-6 py-3">
        <h5 class="card-title fw-bold">標準音樂封面照</h5>
        <p class="card-text msf-info-s">
            呈現內容包含：<br>音樂標題、封面照片、封面照片、音樂分類、音樂長度、播放次數、授權方式。
        </p>
        <div class="msf-heightlight">
            運用於預設場景，如：首頁推播音樂、分類排行榜、搜尋預覽。
        </div>
    </div>
</div>
"""
                ),
                DivBar(),
                Html(
                    """
<div class="row justify-content-center align-items-center">
    <div class="col-12 col-md-6 py-2 d-flex justify-content-center">
        <img data-src="/assets/imgs/songla/ux/Music Thin.png" class="card-img-top lozad" alt="songla app song list" src="/assets/imgs/songla/ux/Music Thin.png" data-loaded="true">
    </div>
    <div class="col-12 col-md-6 py-3">
        <h5 class="card-title fw-bold">窄版音樂封面照</h5>
        <p class="card-text msf-info-s">
            呈現內容包含：<br>音樂標題、音樂長度、播放次數。
        </p>
        <div class="msf-heightlight">
            多用於不重於資訊內容的場景，如：社群附加音樂、播放紀錄。
        </div>
    </div>
</div>
"""
                ),
            ]
        ),
        Card(
            body=[
                Text("設計色彩", "h3", bold=True),
                DivBar(),
                Image(
                    "/assets/imgs/songla/ux/colortheme.png",
                    "設計色彩系統",
                    max_width=400,
                ),
                Text("運用多彩色系營造活潑的感覺", center=True),
            ],
            body_gap_size="large",
        ),
        Card(
            body=[
                Text("蒙版漸層背景設計", "h3", bold=True),
                DivBar(),
                Image(
                    "/assets/imgs/songla/ux/colorBG.png",
                    "蒙版漸層背景設計",
                    max_width=400,
                ),
                Text("運用漸層營造立體的感覺", center=True),
            ],
            body_gap_size="large",
        ),
        Card(
            body=[
                Text("圖示設計", "h3", bold=True),
                DivBar(),
                Image(
                    "/assets/imgs/songla/ux/iconpack.png",
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
            body_gap_size="large",
        ),
    ],
)
