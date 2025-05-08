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
    job_name="Solwen AI（新創）",
    startdate="2024/08",
    enddate="Present",
    colorSet=ThemeColor().natural,
    prefix="2024_SolwenAi",
    cover="/assets/imgs/jobs/2024_SolwenAi/cover.png",
    description=ListStr(
        [
            "專注於`開發與整合 AI 解決方案`，提升企業的運營效率與競爭力。",
            "負責設計、實現和維護 AI 系統，並確保其性能和可靠性。",
            "將 `AI 技術轉為 API 服務`並結合 `Docker Compose 自動部署`於 Linode 伺服器。",
            "專注於多模態模型的開發與應用，結合`語音識別、自然語言處理和計算機視覺`等技術，實現多種應用場景。",
            "持續學習和研究最新的 AI 技術和趨勢，為企業提供前瞻性的技術建議。",
        ]
    ),
    children=[
        Card(
            body=[
                Text("巨匠英語口說 AI 學習系統", "h4"),
                Text("2024/11 ~ Now"),
                DivBar(),
                ListStr(
                    [
                        "開發專注於英語學習的 AI 對話系統，具有`自動對話`、`偏題偵測`等功能。",
                        "結合`火山雲`語音合成技術，實現了高品質的語音合成效果，使聲音更自然。",
                        "針對對話內容結合 `Azure 語音評分工具`，提供詳細的對話與綜合報告，幫助用戶了解自己的口說表現。",
                    ]
                ),
            ],
            footer=[
                ListDiv(
                    [
                        Text("# 語音合成開發", "span", pill_type=True),
                        Text("# Azure", "span", pill_type=True),
                        Text("# API 開發", "span", pill_type=True),
                        Text("# ORM", "span", pill_type=True),
                    ],
                    layout="flex",
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
                        Text("# LLM 視覺多模態", "span", pill_type=True),
                        Text("# Streamlit", "span", pill_type=True),
                    ],
                    layout="flex",
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
                        "建立自動化 CI/CD 流程，結合 Docker Compose 部署搭配 alembic 進行資料庫版本控制，確保系統的穩定性與一致性。",
                    ]
                ),
            ],
            footer=[
                ListDiv(
                    [
                        Text("# API 開發", "span", pill_type=True),
                        Text("# OpenAI Whisper", "span", pill_type=True),
                        Text("# 火山雲語音合成", "span", pill_type=True),
                    ],
                    layout="flex",
                )
            ],
        ),
        Card(
            header=Image("/assets/imgs/projects/enterpriseKnowledgeBase/cover.png"),
            body=[
                Text("Solwen RAG For Business", "h4"),
                Text("2024/08 ~ 2024/11"),
                DivBar(),
                ListStr(
                    [
                        "基於 FastAPI 框架規劃建構與`開發企業 AI 知識庫問答系統`。",
                        "深度與 AI 工程師合作，`整合 LangChain`工作流進系統。",
                        "使用 alembic 進行`資料庫版本控制`，確保資料庫結構的穩定性與一致性。",
                        "使用 PGVector 進行文本向量化管理，並結合`PostgreSQL`資料庫進行資料存儲與檢索。",
                        "使用`Docker`進行容器化部署，確保系統的可擴展性與穩定性。",
                        "使用 FastAPI `開發 RESTful API`，實現了高效的資料存取與處理。",
                    ]
                ),
            ],
            footer=[
                ListDiv(
                    [
                        Text("# API 開發", "span", pill_type=True),
                        Text("# 自動化部署", "span", pill_type=True),
                        Text("# PGVector 整合", "span", pill_type=True),
                    ],
                    layout="flex",
                )
            ],
        ),
    ],
)
