from app.layouts.job import JobPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    DivBar,
    Image,
    LinkButton,
    ListDiv,
    ListStr,
    Text,
)


page = JobPage(
    title="中原大學資管系",
    job_name="中原大學資管系（學校）",
    startdate="2019/07",
    enddate="2022/07",
    colorSet=ThemeColor().blue,
    prefix="2019_CycuEdu",
    cover="/assets/imgs/jobs/2019_CycuEdu/cover.png",
    description=ListStr(
        [
            "`UI/UX` 設計與產品原型開發 (Figma)。",
            "全端`網頁開發`：(Bootstrap, Node.js, mongoDB, Apache Tomcat, MySQL, RWD設計)。",
            "`API 開發`與系統整合：(Django, Flask, RESTful API)。",
            "`資料處理與視覺化`：Excel 資料清理, Data Studio 儀表板。",
            "`多媒體內容製作`：Premiere Pro 影片剪輯, Photopea 教學。",
            "`行銷企劃與市場分析`：安索夫矩陣, STP 策略, 行銷 4P。",
            "`專案競賽`經驗與`簡報呈現`能力。",
        ]
    ),
    children=[
        Card(
            header=Image("/assets/imgs/projects/mindReader/cover.png"),
            body=[
                Text("MindReader 與你心譯相通", "h4"),
                Text("2019/11 ~ 2020/12"),
                DivBar(),
                ListStr(
                    [
                        "結合用戶分析需求並使用 Figma `設計產品原型`。",
                        "基於 `Azure LUIS` 技術分析文本意圖與結構，並結合 Firebase 字詞庫微調用戶輸入文本。",
                        "基於 Django 框架`開發 LineBot`，實現即時的對話與互動。",
                        "使用 Flask 框架`開發 RESTful API`，實現了高效的資料存取與處理。",
                    ]
                ),
                DivBar(),
                Text("獲獎記錄：", bold=True),
                ListStr(
                    [
                        "2021 大專校院資訊應用服務創新競賽・Azure 雲端組 `第三名`",
                        "2021 大專校院資訊應用服務創新競賽・資訊應用組 `佳作`",
                        "中原大學資管系 110 學年度資訊管理畢業專題競賽 `第一名`",
                        "109 學年度中原大學資管系資訊管理專題初賽 `第二名`",
                    ]
                ),
                DivBar(),
                LinkButton("專案網址", "/projects/mindReader"),
            ],
            footer=[
                ListDiv(
                    [
                        Text("# Azure", "span", pill_type=True),
                        Text("# API 開發", "span", pill_type=True),
                        Text("# NLP", "span", pill_type=True),
                    ],
                    layout="flex",
                )
            ],
        ),
        Card(
            header=Image("/assets/imgs/projects/hsCloudMeetingManage/cover.png"),
            body=[
                Text("華新雲會議管理系統", "h4"),
                Text("2020/09 ~ 2021/01"),
                DivBar(),
                ListStr(
                    [
                        "結合用戶分析需求並使用 Figma `設計產品原型`。",
                        "使用 `Node.js` 與 `mongoDB` 開發後端系統，實現了高效的資料存取與處理。",
                        "使用 `Jitsi Meet` 建構線上會議。",
                        "使用 `Bootstrap` 建構出 RWD 網頁介面。",
                    ]
                ),
                DivBar(),
                LinkButton("專案網址", "/projects/hsCloudMeetingManage"),
            ],
            footer=[
                ListDiv(
                    [
                        Text("# 介面設計", "span", pill_type=True),
                        Text("# 全端開發", "span", pill_type=True),
                    ],
                    layout="flex",
                )
            ],
        ),
        Card(
            header=Image("/assets/imgs/projects/hsVmi/cover.png"),
            body=[
                Text("華新 VMI 庫存管理遊戲", "h4"),
                Text("2020/10 ~ 2020/12"),
                DivBar(),
                ListStr(
                    [
                        "使用 `Apache Tomcat (Java Page)` 與 `MySQL` 開發模擬物流系統。",
                        "使用 `Bootstrap` 建構出 RWD 網頁介面。",
                    ]
                ),
                DivBar(),
                LinkButton("專案網址", "/projects/hsVmi"),
            ],
            footer=[
                ListDiv(
                    [
                        Text("# 全端開發", "span", pill_type=True),
                    ],
                    layout="flex",
                )
            ],
        ),
        Card(
            header=Image("/assets/imgs/projects/techlife/cover.png"),
            body=[
                Text("TechLife・Photopea 講師", "h4"),
                Text("2021/10 ~ 2021/12"),
                DivBar(),
                ListStr(
                    [
                        "錄製 `Photopea` 的教學影片，並設計教學大綱並設計活動。",
                        "使用 `Premiere Pro` 剪輯影片微調節奏並加上字幕。",
                    ]
                ),
                DivBar(),
                Text("獲獎記錄：", bold=True),
                ListStr(
                    [
                        "1092 中原大學資管系資訊管理競賽 `第一名`",
                    ]
                ),
                DivBar(),
                LinkButton("專案網址", "/projects/techlife"),
            ],
            footer=[
                ListDiv(
                    [
                        Text("# 教案設計", "span", pill_type=True),
                        Text("# 簡報設計", "span", pill_type=True),
                        Text("# 影音剪輯", "span", pill_type=True),
                    ],
                    layout="flex",
                )
            ],
        ),
        Card(
            header=Image("/assets/imgs/projects/foodome/cover.png"),
            body=[
                Text("食材外送專家 - Foodome", "h4"),
                Text("2020/07 ~ 2020/08"),
                DivBar(),
                ListStr(
                    [
                        "結合用戶分析需求並使用 Figma `設計產品原型`。",
                        "作為行銷策劃人員，主要負責`市場分析、安索夫矩陣、STP 策略和行銷 4P` 等工作。",
                    ]
                ),
                DivBar(),
                LinkButton("專案網址", "/projects/foodome"),
            ],
            footer=[
                ListDiv(
                    [
                        Text("# 全端開發", "span", pill_type=True),
                    ],
                    layout="flex",
                )
            ],
        ),
        Card(
            header=Image("/assets/imgs/projects/noDrinkNoDrunk/cover.png"),
            body=[
                Text("No Drink No Drunk", "h4"),
                Text("2020/09 ~ 2021/01"),
                DivBar(),
                ListStr(
                    [
                        "結合用戶分析需求並使用 Figma `設計產品原型`。",
                        "使用 `Bootstrap` 建構出 RWD 網頁介面。",
                        "利用 `Github Pages` 靜態部署前端網頁。",
                    ]
                ),
                DivBar(),
                LinkButton("專案網址", "/projects/noDrinkNoDrunk"),
            ],
            footer=[
                ListDiv(
                    [
                        Text("# UI 設計", "span", pill_type=True),
                        Text("# RWD 設計", "span", pill_type=True),
                        Text("# 前端開發", "span", pill_type=True),
                    ],
                    layout="flex",
                )
            ],
        ),
        Card(
            header=Image("/assets/imgs/projects/jobAnalytics2020/cover.png"),
            body=[
                Text("2020 年台灣各行業別員工薪資統計分析", "h4"),
                Text("2022/05 ~ 2022/05"),
                DivBar(),
                ListStr(
                    [
                        "從政府資料開放平台中獲取資料，並使用 `Excel` 進行資料清理與整合。",
                        "使用 `Data Studio` 製作儀表板，線上部署成可操作網頁。",
                        "使用 `Powerpoint` 並利用資訊設計能力建構簡報。",
                    ]
                ),
                DivBar(),
                LinkButton("專案網址", "/projects/jobAnalytics2020"),
            ],
            footer=[
                ListDiv(
                    [
                        Text("# 資料清理", "span", pill_type=True),
                        Text("# 資料視覺化", "span", pill_type=True),
                        Text("# 簡報設計", "span", pill_type=True),
                    ],
                    layout="flex",
                )
            ],
        ),
        Card(
            header=Image("/assets/imgs/projects/oneDayLover/cover.png"),
            body=[
                Text("一日情人後端", "h4"),
                Text("2020/10 ~ 2020/12"),
                DivBar(),
                ListStr(
                    [
                        "使用 `Apache Tomcat (Java Page)` 與 `MySQL` 開發商城。",
                        "使用 `Bootstrap` 建構出 RWD 網頁介面。",
                    ]
                ),
                DivBar(),
                LinkButton("專案網址", "/projects/oneDayLover"),
            ],
            footer=[
                ListDiv(
                    [
                        Text("# 後端開發", "span", pill_type=True),
                    ],
                    layout="flex",
                )
            ],
        ),
    ],
)
