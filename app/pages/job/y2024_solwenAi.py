from app.layouts.job import JobPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    DivBar,
    ListDiv,
    Text,
)


page = JobPage(
    title="AI 工程師",
    description="Solwen AI（偉利科技子公司）",
    startdate="2024/08",
    enddate="Present",
    colorSet=ThemeColor().green,
    prefix="2024_SolwenAi",
    cover="/assets/imgs/jobs/2024_SolwenAi/cover.png",
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
            footer=[
                ListDiv(
                    [
                        Text("# 語音合成開發", "span"),
                        Text("# Azure", "span"),
                        Text("# API 開發", "span"),
                        Text("# ORM", "span"),
                    ],
                    grid_layout=False,
                )
            ],
        ),
        Card(
            body=[
                Text("Solwen RAG For Business", "h4"),
                Text("2024/08 ~ 2024/11"),
                DivBar(),
                Text(
                    "基於 FastAPI 框架規劃建構與`開發開發企業 AI 知識庫問答系統`。"
                    "深度與 AI 工程師合作，將 LangChain 生成文本工作流整合進系統。"
                ),
            ],
            footer=[
                ListDiv(
                    [
                        Text("# API 開發", "span"),
                        Text("# 後端開發", "span"),
                        Text("# ORM", "span"),
                        Text("# PGVector", "span"),
                    ],
                    grid_layout=False,
                )
            ],
        ),
    ],
)
