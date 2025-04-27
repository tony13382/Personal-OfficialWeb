from app.layouts.project import ProjectPage
from app.variables import ThemeColor
from app.elements import (
    AccordionBlock,
    AccordionItem,
    Canva,
    Card,
    Div,
    DivBar,
    FileLink,
    Html,
    Image,
    ImageCarousel,
    Link,
    ListDiv,
    ListStr,
    Score,
    Text,
    Tool,
    UiImageCarousel,
    Youtube,
)


page = ProjectPage(
    title="2020 年台灣各行業別員工薪資統計分析",
    description="大學專案，利用政府公開資訊分析職場，提供學子未來工作的預期薪資的參考資訊。",
    subdescription="負責：簡報設計、儀表板製作、資料清理與整合",
    startdate="2022/05",
    enddate="2022/05",
    status="closed",
    colorSet=ThemeColor().blue,
    prefix="jobAnalytics2020",
    cover="/assets/imgs/jobAnalytics2020/cover.png",
    description_links=[
        Link(
            content="專案網址（datastudio）",
            href="https://datastudio.google.com/s/rcRR2G3x4VI",
            open_in_tab=True,
            icon="bi-window-sidebar",
        )
    ],
    tags=["資料清理", "資料視覺化", "簡報設計"],
    tools=[
        Tool("Data Studio", "資料視覺化（儀表板製作）"),
        Tool("Powerpoint", "簡報設計"),
    ],
    children=[
        Card(
            body=[
                Text("系統資訊", "h3"),
                FileLink(
                    title="網站網址",
                    subtitle="datastudio",
                    src="https://datastudio.google.com/s/rcRR2G3x4VI",
                    icon="bi-window-sidebar",
                ),
                ListDiv(
                    [
                        Text(
                            "數據來源：政府資料開放平台中的受雇員工人數、每人每月薪資，總共有17個獨立工作表，是依照職業類別區分，包含醫療保健業、金融與保險業等，都包含在我們這次分析範圍內。"
                        ),
                        DivBar(),
                        Text(
                            "資料的欄位：年度、職類別、行業別、受僱員工人數、總薪資、經常性薪資、非經常性薪資，總共 7 個欄位。而這次總資料筆數達到了 13,644 筆"
                        ),
                    ]
                ),
            ],
            body_gap_size="large",
        ),
        Card(
            body=[
                Text("期中見解報告", "h3"),
                Html(
                    """
<div class="ratio ratio-4x3 overflow-hidden rounded-basic">
    <iframe src="https://www.slideshare.net/slideshow/embed_code/key/HBCM3uQ0iF0fNr" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="margin-bottom:5px; max-width: 100%;" allowfullscreen="">
    </iframe>
</div>
"""
                ),
                FileLink(
                    title="下載檔案",
                    subtitle="Google Slide",
                    src="https://docs.google.com/presentation/d/1fL7nC1nQda0PS9qcBswW9wU4Kmc1ME93/edit?usp=sharing&ouid=106449819474178509805&rtpof=true&sd=true",
                ),
            ],
            body_gap_size="large",
        ),
        Card(
            body=[
                Text("期末見解報告", "h3"),
                Html(
                    """
<div class="ratio ratio-4x3 overflow-hidden rounded-basic">
    <iframe src="https://www.slideshare.net/slideshow/embed_code/key/1ZyhDhZmEU41MY" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="margin-bottom:5px; max-width: 100%;" allowfullscreen="">
    </iframe>
</div>
"""
                ),
                FileLink(
                    title="下載檔案",
                    subtitle="Google Slide",
                    src="https://docs.google.com/presentation/d/1ff073pwGJFImE-1LVw6L2gE-2OFpwGi3/edit?usp=share_link&ouid=106449819474178509805&rtpof=true&sd=true",
                ),
            ],
            body_gap_size="large",
        ),
        Card(
            header=ListDiv(
                [
                    Div(Text("線上 Demo", "h3"), mt=4, ms=3, mb=3),
                    Html(
                        """
<div class="ratio ratio-4x3">
    <iframe src="https://datastudio.google.com/embed/reporting/48a45ac6-cf4f-4016-aed5-7680e097c616/page/JfGqC" frameborder="0" style="border:0" allowfullscreen=""></iframe>
</div>
"""
                    ),
                ]
            )
        ),
    ],
)
