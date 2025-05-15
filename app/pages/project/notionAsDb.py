from app.layouts.project import ProjectPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    IconBlock,
    Image,
    ImageCarousel,
    LinkButton,
    ListDiv,
    ListStr,
    Text,
    Tool,
)


page = ProjectPage(
    title="知識庫與書籤。Notion As DB 實驗專案",
    description="基於 Notion API, Github Action, Cloudflare Pages 所打造的靜態網頁",
    startdate="2022/03",
    enddate="NOW",
    status="running",
    colorSet=ThemeColor().natural,
    prefix="notionAsDb",
    pin=True,
    cover="/assets/imgs/projects/notionAsDb/cover.png",
    skill_types=["pin", "dev"],
    tags=["網站架設", "Notion", "靜態網頁"],
    description_links=[
        LinkButton("亮進的精選書籤", "https://bm.lianglu.uk/"),
        LinkButton("知識推薦獲取來源", "https://learn.lianglu.uk/"),
    ],
    tools=[
        Tool("Notion", "靜態網頁資料庫"),
        Tool("Github Action", "自動化部署"),
        Tool("Cloudflare Pages", "靜態網頁部署"),
    ],
    children=[
        Card(
            header=Image("/assets/imgs/projects/notionAsDb/workflow.png"),
            body=[
                Text("工作流程", "h3"),
                ListDiv(
                    [
                        IconBlock(
                            title="步驟ㄧ：建置 Notion 資料庫", icon="bi-1-circle"
                        ),
                        IconBlock(
                            title="步驟二：於`Cloudflare Page`透過腳本連線 Notion 生成靜態檔案",
                            icon="bi-2-circle",
                        ),
                        IconBlock(
                            title="步驟三：部署`html`靜態網頁", icon="bi-3-circle"
                        ),
                        IconBlock(
                            title="背景任務：每 20 分鐘透過`Cloudflare Hook`執行生成腳本",
                            subtitle="處理圖片路徑更新限制",
                            icon="bi-clock-history",
                        ),
                    ]
                ),
            ],
            body_gap_size="large",
        ),
    ],
)
