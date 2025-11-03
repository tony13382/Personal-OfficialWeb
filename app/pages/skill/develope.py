from app.elements import ListStr, Text
from app.layouts.skill import Certificate, SkillPage, SkillsGroup, SkillItem
from app.variables import ThemeColor

import app.pages.project as projectPages
import app.pages.job as jobPages

page = SkillPage(
    title="AI 系統開發／自然語言處理",
    colorSet=ThemeColor().red,
    prefix="develope",
    icon="bi-code-slash",
    cover="/assets/imgs/skills/develope/cover.png",
    description=ListStr(
        [
            "精通大型語言模型應用與整合",
            "掌握前後端全棧開發",
            "擅長建構網頁式 AI 應用程式",
            "擅長資料庫結構設計與優化",
            "具備用戶友好界面設計經驗",
            "快速適應多種開發工具與環境",
        ]
    ),
    skill_group=[
        SkillsGroup(
            title="前端",
            icon="bi-laptop",
            children=[
                SkillItem(
                    title="Streamlit",
                    description="Python Web 介面",
                    icon="/assets/imgs/icons/Streamlit.svg",
                ),
                SkillItem(
                    title="React",
                    description="前端開發",
                    icon="/assets/imgs/icons/React.svg",
                ),
                SkillItem(
                    title="Vue",
                    description="前端開發",
                    icon="/assets/imgs/icons/Vue.svg",
                ),
                SkillItem(
                    title="HTML5 & CSS3",
                    description="前端設計",
                    icon="/assets/imgs/icons/HTML5.svg",
                ),
                SkillItem(
                    title="Bootstrap",
                    description="網頁切版",
                    icon="/assets/imgs/icons/Bootstrap.svg",
                ),
                SkillItem(
                    title="TailwindCSS",
                    description="客製化網頁樣式",
                    icon="/assets/imgs/icons/Tailwind.svg",
                ),
                SkillItem(
                    title="Flutter",
                    description="APP 開發",
                    icon="/assets/imgs/icons/Flutter.svg",
                ),
            ],
        ),
        SkillsGroup(
            title="後端",
            icon="bi-terminal",
            children=[
                SkillItem(
                    title="FastAPI",
                    description="API 開發",
                    icon="/assets/imgs/icons/FastAPI.svg",
                ),
                SkillItem(
                    title="Python Flask",
                    description="API 開發實務／資料庫串接",
                    icon="/assets/imgs/icons/Flask.svg",
                ),
                SkillItem(
                    title="NextJs",
                    description="API 開發串接／網頁後端",
                    icon="/assets/imgs/icons/NextJs.svg",
                ),
                SkillItem(
                    title="NodeJs",
                    description="APIs 建立／網頁後端",
                    icon="/assets/imgs/icons/NodeJs.svg",
                ),
                SkillItem(
                    title="Java Server Page",
                    description="Tomcat 後端／資料庫串接",
                    icon="/assets/imgs/icons/JavaServerPage.svg",
                ),
                SkillItem(
                    title="php",
                    description="網頁後端",
                    icon="/assets/imgs/icons/Php.svg",
                ),
                SkillItem(
                    title="Ruby On Rails",
                    description="MVC 網頁開發",
                    icon="/assets/imgs/icons/RubyOnRails.svg",
                ),
            ],
        ),
        SkillsGroup(
            title="資料庫",
            icon="bi-database",
            children=[
                SkillItem(
                    title="PostgreSQL（pgvector）",
                    description="關聯式＆向量 資料庫",
                    icon="/assets/imgs/icons/PostgreSQL.svg",
                ),
                SkillItem(
                    title="Milvus",
                    description="向量資料庫管理",
                    icon="/assets/imgs/icons/Milvus.svg",
                ),
                SkillItem(
                    title="MySQL",
                    description="SQL語法／資料表設計",
                    icon="/assets/imgs/icons/MySQL.svg",
                ),
                SkillItem(
                    title="MongoDB",
                    description="非關聯式資料庫",
                    icon="/assets/imgs/icons/MongoDB.svg",
                ),
                SkillItem(
                    title="Firebase",
                    description="線上非關聯式資料庫",
                    icon="/assets/imgs/icons/Firebase.svg",
                ),
                SkillItem(
                    title="SQLite",
                    description="微型資料庫",
                    icon="/assets/imgs/icons/SQLite.svg",
                ),
                SkillItem(
                    title="Redis",
                    description="快取資料庫",
                    icon="/assets/imgs/icons/Redis.svg",
                ),
            ],
        ),
        SkillsGroup(
            title="模型與雲服務",
            icon="bi-boxes",
            children=[
                SkillItem(
                    title="ChatGPT",
                    description="提示詞工程／微調／SDK 串接",
                    icon="/assets/imgs/icons/ChatGPT.svg",
                ),
                SkillItem(
                    title="Anthropic (LLM)",
                    description="提示詞工程、SDK 串接",
                    icon="/assets/imgs/icons/Anthropic.svg",
                ),
                SkillItem(
                    title="火山雲",
                    description="語音轉文字、語音合成",
                    icon="/assets/imgs/icons/火山雲.svg",
                ),
                SkillItem(
                    title="Azure",
                    description="自然語言處理／語音合成",
                    icon="/assets/imgs/icons/Azure.svg",
                ),
                SkillItem(
                    title="Sentence-BERT",
                    description="文本向量化處理與微調",
                    icon="/assets/imgs/icons/HuggingFace.svg",
                ),
            ],
        ),
        SkillsGroup(
            title="部署與自動化",
            icon="bi-hdd-network",
            children=[
                SkillItem(
                    title="Docker",
                    description="容器化技術／封裝／部署",
                    icon="/assets/imgs/icons/Docker.svg",
                ),
                SkillItem(
                    title="Cloudflare",
                    description="Worker／DNS",
                    icon="/assets/imgs/icons/Cloudflare.svg",
                ),
                SkillItem(
                    title="GitHub Actions",
                    description="自動化部署",
                    icon="/assets/imgs/icons/GitHub.svg",
                ),
                SkillItem(
                    title="Linode",
                    description="雲端部屬",
                    icon="/assets/imgs/icons/Linode.svg",
                ),
                SkillItem(
                    title="APP Script",
                    description="自動化任務與排程",
                    icon="/assets/imgs/icons/AppScript.svg",
                ),
            ],
        ),
        SkillsGroup(
            title="其他",
            icon="bi-braces-asterisk",
            children=[
                SkillItem(
                    title="Java",
                    description="程式設計",
                    icon="/assets/imgs/icons/Java.svg",
                ),
                SkillItem(
                    title="C#",
                    description="程式設計",
                    icon="/assets/imgs/icons/CSharp.svg",
                ),
                SkillItem(
                    title="RabbitMQ",
                    description="訊息佇列處理系統",
                    icon="/assets/imgs/icons/RabbitMQ.svg",
                ),
                SkillItem(
                    title="Git",
                    description="版本控制",
                    icon="/assets/imgs/icons/Git.svg",
                ),
            ],
        ),
    ],
    projects=[
        projectPages.trelloFinder,
        projectPages.notionAsDb,
        projectPages.chenmko,
        projectPages.mindReader,
        projectPages.hsCloudMeetingManage,
        projectPages.hsVmi,
        projectPages.stockCalc,
        projectPages.noDrinkNoDrunk,
        projectPages.oneDayLover,
    ],
    jobs=[
        jobPages.y2024_SolwenAi,
        jobPages.y0000_Developer,
        jobPages.y2023_NthuIr,
        jobPages.y2022_NthuIlst,
        jobPages.y2019_CycuEdu,
    ],
    certificate=[
        Certificate(
            title="Google Data Analytics Professional Certificate",
            company="Google (Coursera)",
            tags=["Python", "Excel", "SQL", "資料搜集／前處理", "資料視覺化"],
        ),
        Certificate(
            title="IBM Data Visualization & Dashboard Essentials",
            company="IBM (Coursera)",
            tags=["Python", "Excel", "IBM Cognos", "SQL", "資料視覺化"],
        ),
    ],
)
