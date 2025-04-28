from app.layouts.job import JobPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    DivBar,
    Text,
)


page = JobPage(
    title="AI 工程師",
    description="Solwen AI（偉利科技子公司）",
    startdate="2024/08",
    enddate="Present",
    colorSet=ThemeColor().green,
    prefix="2024_solwenAi",
    cover="/assets/imgs/jobs/2024_solwenAi/cover.png",
    tags=["LLM 應用", "API 開發", "後端開發", "ORM", "PGVector"],
    children=[
        Card(
            body=[
                Text("巨匠英語口說 AI 學習系統", "h4"),
                Text("2024/11 ~ Now"),
                DivBar(),
                Text(
                    "開發`英語口說學習系統`，提供語音即時對話結合語言模型與 Azure 工具，生成口說評估報表生成與輸出功能。"
                ),
            ],
        ),
        Card(
            body=[
                Text("Solwen RAG For Business", "h4"),
                Text("2024/08 ~ 2024/11"),
                DivBar(),
                Text(
                    "基於 FastAPI 框架規劃建構與`開發開發企業 AI 知識庫問答系統`，深度與 AI 工程師合作，將 LangChain 生成文本工作流整合進系統。"
                ),
            ]
        ),
    ],
)
