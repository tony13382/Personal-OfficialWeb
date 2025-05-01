from app.layouts.job import JobPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    DivBar,
    Image,
    ListDiv,
    ListStr,
    Text,
)


page = JobPage(
    title="AI 工程師",
    description="Solwen AI（偉利科技子公司）",
    startdate="2024/08",
    enddate="Present",
    colorSet=ThemeColor().natural,
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
            header=Image("/assets/imgs/projects/longtengInvoice/cover.png"),
            body=[
                Text("龍騰發票視覺處理系統", "h4"),
                Text("2025/02 ~ Now"),
                DivBar(),
                ListStr(
                    [
                        "利用`多模態模型`進行發票影像處理，結合`OCR 與 LLM`技術，實現發票資料的自動化處理與分析。",
                        "系統能夠自動識別發票上的文字、數字和圖像，並將其轉換為結構化的數據格式，從而提高了發票處理的效率和準確性。",
                        "使用`Streamlit`開發前端介面，提供用戶友好的操作界面，並實現了即時的數據可視化與編輯功能。",
                    ]
                ),
            ],
            footer=[
                ListDiv(
                    [
                        Text("# LLM 視覺多模態", "span"),
                        Text("# Streamlit", "span"),
                    ],
                    grid_layout=False,
                )
            ],
        ),
        Card(
            header=Image("/assets/imgs/projects/pandaChinese/cover.png"),
            body=[
                Text("Panda Chinese・中文口說 AI 學習系統", "h4"),
                Text("2024/11 ~ 2025/03"),
                DivBar(),
                ListStr(
                    [
                        "開發特定主題的 AI 對話系統，具有`自動對話`、`偏題偵測`等功能。",
                        "結合`火山雲`語音合成技術，實現了高品質的語音合成效果，使聲音更自然。",
                        "針對對話內容提供詳細的報告，幫助用戶了解自己的口說表現。",
                        "基於`FastAPI`框架開發，實現了高效的 API 接口，並基於併發測試持續優化。",
                    ]
                ),
            ],
            footer=[
                ListDiv(
                    [
                        Text("# OpenAI", "span"),
                        Text("# API 開發", "span"),
                        Text("# FastAPI", "span"),
                        Text("# 火山雲語音合成", "span"),
                    ],
                    grid_layout=False,
                )
            ],
        ),
        Card(
            header=Image("/assets/imgs/projects/enterpriseKnowledgeBase/cover.png"),
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
