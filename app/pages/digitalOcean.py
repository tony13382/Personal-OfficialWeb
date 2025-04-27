from app.layouts.project import ProjectPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    DivBar,
    Link,
    Text,
    Tool,
)


page = ProjectPage(
    title="數位海洋知識專案",
    description="ML 亮進 的個人知識庫資訊統整並線上公開，高效分享資訊與蒐集到的資源。",
    startdate="2022/05",
    enddate="2022/05",
    status="closed",
    colorSet=ThemeColor().orange,
    prefix="digitalOcean",
    cover="/assets/imgs/digitalOcean/cover.png",
    description_links=[
        Link(
            content="專案網址（datastudio）",
            href="https://meowlu.notion.site/12e7c67f7f2d47249f0111882d932663",
            open_in_tab=True,
            icon="bi-window-sidebar",
        )
    ],
    tags=["數位內容"],
    tools=[
        Tool("Notion", "內容管理與發佈"),
    ],
    children=[
        Card(
            body=[
                Text("為何要開展計畫？", "h3"),
                Text(
                    "數位海洋專案源自於作者「ML」的個人知識庫，在大學期間由於有積累一些常用資源，因此常常會進行分享，但是由於分享資源越來越多且沒有一個系統性的統整，因此知識如同碎片一般，要找尋時不太容易，因此建立了這個計畫，將以往資訊打通，建立一個統一的方式分享資訊與蒐集到的資源。"
                ),
                DivBar(),
                Text("這項計畫的知識從何而來？", "h3"),
                Text(
                    "這項計畫的知識目前有三個來源，第一個是網路上的網頁擷取，第二個是個人筆記，第三個則是投稿內容，觀看者可以利用投稿提供知識或資源給平台方審核，經審核後即可在網站中發現。由於許多的知識來源來自於網絡，因此本網站若從網路上收錄的資訊均會標示來源地址，而著作權歸屬也歸原網站，此網站只會整理資訊與精煉出重點，但個人筆記與心法之著作權歸作者所有，而投稿之文章也代表同意本平台方可以進行內容發佈。"
                ),
            ]
        )
    ],
)
