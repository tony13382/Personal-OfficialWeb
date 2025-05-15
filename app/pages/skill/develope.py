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
                    icon="/assets/imgs/appIcons/pythonPackage/streamlit.png",
                ),
                SkillItem(
                    title="React",
                    description="前端開發",
                    icon="/assets/imgs/appIcons/react.png",
                ),
                SkillItem(
                    title="Vue",
                    description="前端開發",
                    icon="/assets/imgs/appIcons/vue.png",
                ),
                SkillItem(
                    title="JavaScript",
                    description="DOM 物件操作與變化",
                    icon="/assets/imgs/appIcons/javascript.png",
                ),
                SkillItem(
                    title="HTML5 & CSS3",
                    description="前端設計",
                    icon="/assets/imgs/appIcons/html.png",
                ),
                SkillItem(
                    title="Bootstrap",
                    description="網頁切版",
                    icon="/assets/imgs/appIcons/bootstrapV5.png",
                ),
                SkillItem(
                    title="Flutter",
                    description="APP 開發",
                    icon="/assets/imgs/appIcons/flutter.png",
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
                    icon="/assets/imgs/appIcons/fastapi.png",
                ),
                SkillItem(
                    title="Python Flask",
                    description="API 開發實務／資料庫串接",
                    icon="/assets/imgs/appIcons/pythonPackage/flask.png",
                ),
                SkillItem(
                    title="NodeJs",
                    description="APIs 建立／網頁後端",
                    icon="/assets/imgs/appIcons/nodejs.png",
                ),
                SkillItem(
                    title="Java Server Page",
                    description="Tomcat 後端／串接 MySQL",
                    icon="/assets/imgs/appIcons/apacheTomcat.png",
                ),
                SkillItem(
                    title="php",
                    description="網頁後端",
                    icon="/assets/imgs/appIcons/php.png",
                ),
            ],
        ),
        SkillsGroup(
            title="資料庫",
            icon="bi-database",
            children=[
                SkillItem(
                    title="PostgreSQL（pgvector）",
                    description="關聯與向量綜合資料庫",
                    icon="/assets/imgs/appIcons/postgreSQL.png",
                ),
                SkillItem(
                    title="Milvus",
                    description="向量資料庫管理",
                    icon="/assets/imgs/appIcons/milvus.png",
                ),
                SkillItem(
                    title="MySQL",
                    description="SQL語法／關聯資料表設計",
                    icon="/assets/imgs/appIcons/mysql.png",
                ),
                SkillItem(
                    title="MongoDB",
                    description="非關聯式資料庫",
                    icon="/assets/imgs/appIcons/mongodb.png",
                ),
                SkillItem(
                    title="Firebase",
                    description="線上非關聯式資料庫",
                    icon="/assets/imgs/appIcons/firebase.png",
                ),
            ],
        ),
        SkillsGroup(
            title="模型",
            icon="bi-boxes",
            children=[
                SkillItem(
                    title="ChatGPT",
                    description="提示詞工程、API 串接、Fine-tuning",
                    icon="/assets/imgs/appIcons/chatgpt.png",
                ),
                SkillItem(
                    title="Anthropic (LLM)",
                    description="提示詞工程、API 串接",
                    icon="/assets/imgs/appIcons/anthropic.png",
                ),
                SkillItem(
                    title="Whisper (OpenAI)",
                    description="語音轉文字、API 串接",
                    icon="/assets/imgs/appIcons/chatgpt.png",
                ),
                SkillItem(
                    title="火山雲",
                    description="語音轉文字、語音合成",
                    icon="/assets/imgs/appIcons/volcengine.png",
                ),
                SkillItem(
                    title="Azure",
                    description="自然語言處理／意圖訓練分析／語音合成",
                    icon="/assets/imgs/appIcons/azure.png",
                ),
                SkillItem(
                    title="Sentence-BERT",
                    description="文本向量化處理與微調",
                    icon="/assets/imgs/appIcons/sbert.png",
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
                    icon="/assets/imgs/appIcons/java.png",
                ),
                SkillItem(
                    title="Docker",
                    description="容器化技術／封裝／部署",
                    icon="/assets/imgs/appIcons/docker.png",
                ),
                SkillItem(
                    title="RabbitMQ",
                    description="API 訊息佇列處理系統",
                    icon="/assets/imgs/appIcons/rabbit_mq.png",
                ),
                SkillItem(
                    title="Git",
                    description="版本控制",
                    icon="/assets/imgs/appIcons/git.png",
                ),
                SkillItem(
                    title="GitHub Actions",
                    description="CI/CD 自動化部署",
                    icon="/assets/imgs/appIcons/github.png",
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
