from app.components.project_card import ProjectCard
from app.layouts.job import JobPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    Image,
    ListDiv,
    ListStr,
)
import app.pages.project as projectPages

page = JobPage(
    title="接案經驗",
    job_name="AI 系統開發／全端網頁開發",
    startdate=None,
    enddate=None,
    colorSet=ThemeColor().natural,
    prefix="developer",
    cover="/assets/imgs/jobs/0000_Developer/cover.png",
    description=ListStr(
        [
            "`前端`：Bootstrap, Tailwind CSS",
            "`後端`：FastAPI, Flask, Node.js, Apache Tomcat, Ruby on rails",
            "`DB`：PostgreSQL, MySQL, MongoDB, Firebase"
        ]
    ),
    children=[
        Card(
            header=Image(src="/assets/imgs/projects/fileTaggerWeb/Cover.png"),
            body=[
                ListStr([
                    "PostgreSQL 作為核心資料庫，存處所有標籤資料，並搭配 alembic 管理資料庫",
                    "前端採用 Jinja2 模版語言，並搭配 Bootstrap 打造 RWD 響應式網頁",
                    "後端採用 fastapi 確保多併發安全執行",
                    "Docker Compose 部屬，杜絕環境干擾",
                ])
            ],
        ),
        ProjectCard(
            project=projectPages.chenmko,
            memo=ListDiv(
                [
                    ListStr(
                        [
                            "基於 php 與 PostgreSQL 打造包含 產品、公告、企業資訊的管理系統",
                            "特殊資料表設計`動態調整產品欄位顯示`",
                            "使用 Bootstrap 打造 RWD 響應式網頁"
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
                            "涵蓋設計與全端開發工作",
                            "基於 Node.js＋Jitsi Meet 作為會議系統後端核心",
                            "結合 Bootstrap 打造 RWD 響應式網頁"
                        ]
                    ),
                ]
            ),
        ),
        ProjectCard(
            project=projectPages.hsVmi,
            memo=None,
        ),
    ],
)
