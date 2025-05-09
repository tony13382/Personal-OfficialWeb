from app.components.project_card import ProjectCard
from app.layouts.job import JobPage
from app.variables import ThemeColor
from app.elements import (
    ListDiv,
    ListStr,
)
import app.pages.project as projectPages

page = JobPage(
    title="中原資管學士",
    job_name="中原大學<br>（資訊管理系）",
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
        ProjectCard(
            project=projectPages.mindReader,
            memo=ListDiv(
                [
                    ListStr(
                        [
                            "結合用戶分析需求並使用 Figma `設計產品原型`。",
                            "基於 `Azure LUIS` 技術分析文本意圖與結構，並結合 Firebase 字詞庫微調用戶輸入文本。",
                            "基於 Django 框架`開發 LineBot`，實現即時的對話與互動。",
                            "使用 Flask 框架`開發 RESTful API`，實現了高效的資料存取與處理。",
                        ]
                    ),
                ]
            ),
        ),
        ProjectCard(
            project=projectPages.hsCloudMeetingManage,
            memo=ListDiv(
                [
                    ListStr(
                        [
                            "結合用戶分析需求並使用 Figma `設計產品原型`。",
                            "使用 `Node.js` 與 `mongoDB` 開發後端系統，實現了高效的資料存取與處理。",
                            "使用 `Jitsi Meet` 建構線上會議。",
                            "使用 `Bootstrap` 建構出 RWD 網頁介面。",
                        ]
                    ),
                ]
            ),
        ),
        ProjectCard(
            project=projectPages.hsVmi,
            memo=ListDiv(
                [
                    ListStr(
                        [
                            "使用 `Apache Tomcat (Java Page)` 與 `MySQL` 開發模擬物流系統。",
                            "使用 `Bootstrap` 建構出 RWD 網頁介面。",
                        ]
                    ),
                ]
            ),
        ),
        ProjectCard(
            project=projectPages.techlife,
            memo=ListDiv(
                [
                    ListStr(
                        [
                            "錄製 `Photopea` 的教學影片，並設計教學大綱並設計活動。",
                            "使用 `Premiere Pro` 剪輯影片微調節奏並加上字幕。",
                        ]
                    ),
                ]
            ),
        ),
        ProjectCard(
            project=projectPages.foodome,
            memo=ListDiv(
                [
                    ListStr(
                        [
                            "結合用戶分析需求並使用 Figma `設計產品原型`。",
                            "作為行銷策劃人員，主要負責`市場分析、安索夫矩陣、STP 策略和行銷 4P` 等工作。",
                        ]
                    ),
                ]
            ),
        ),
        ProjectCard(
            project=projectPages.noDrinkNoDrunk,
            memo=ListDiv(
                [
                    ListStr(
                        [
                            "結合用戶分析需求並使用 Figma `設計產品原型`。",
                            "使用 `Bootstrap` 建構出 RWD 網頁介面。",
                            "利用 `Github Pages` 靜態部署前端網頁。",
                        ]
                    ),
                ]
            ),
        ),
        ProjectCard(
            project=projectPages.jobAnalytics2020,
            memo=ListDiv(
                [
                    ListStr(
                        [
                            "從政府資料開放平台中獲取資料，並使用 `Excel` 進行資料清理與整合。",
                            "使用 `Data Studio` 製作儀表板，線上部署成可操作網頁。",
                            "使用 `Powerpoint` 並利用資訊設計能力建構簡報。",
                        ]
                    ),
                ]
            ),
        ),
        ProjectCard(
            project=projectPages.oneDayLover,
            memo=ListDiv(
                [
                    ListStr(
                        [
                            "使用 `Apache Tomcat (Java Page)` 與 `MySQL` 開發商城。",
                            "使用 `Bootstrap` 建構出 RWD 網頁介面。",
                        ]
                    ),
                ]
            ),
        ),
    ],
)
