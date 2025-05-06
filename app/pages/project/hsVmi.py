from app.layouts.project import ProjectPage
from app.variables import ThemeColor
from app.elements import (
    Card,
    IconBlock,
    LinkButton,
    ListDiv,
    Text,
    Tool,
)


page = ProjectPage(
    title="華新 VMI 庫存管理遊戲",
    description="模擬物流系統，利用華新麗華歷史資訊來推算庫存，並依照使用者操作來預估未來的成本，協助員工規劃銷售與庫存管理。",
    startdate="2020/10",
    enddate="2020/12",
    status="closed",
    colorSet=ThemeColor().blue,
    prefix="hsVmi",
    cover="/assets/imgs/projects/hsVmi/cover.png",
    description_links=[
        LinkButton(
            content="GitHub 代碼",
            href="https://github.com/tony13382/CycuSA_VMI",
            fill=True,
            open_in_tab=True,
            icon="bi-github",
        ),
    ],
    skill_types=["pin", "dev"],
    tags=["全端開發"],
    tools=[
        Tool("Apache Tomcat (JSP)", "後端資料處理（無框架）"),
        Tool("MySQL", "SQL 資料庫設計與串接"),
        Tool("Bootstrap V4.3", "前端元件套件"),
    ],
    children=[
        Card(
            body=[
                Text("技術文件", "h3"),
                ListDiv(
                    [
                        IconBlock(
                            src="/assets/file/hsVmi/供應商庫存管理系統規格.pdf",
                            icon="bi-file-earmark-arrow-down",
                            title="系統規格書(1)",
                            subtitle="PDF",
                        ),
                        IconBlock(
                            src="/assets/file/hsVmi/VMI個案遊戲.docx",
                            icon="bi-file-earmark-arrow-down",
                            title="系統規格書(2)",
                            subtitle="DOCX",
                        ),
                        IconBlock(
                            src="/assets/file/hsVmi/VMI起始資料.xlsx",
                            icon="bi-database-down",
                            title="預設資料集(1)",
                            subtitle="XLSX",
                        ),
                        IconBlock(
                            src="/assets/file/hsVmi/VMIDATA2020.xlsx",
                            icon="bi-database-down",
                            title="預設資料集(2)",
                            subtitle="XLSX",
                        ),
                    ],
                    mt=2,
                ),
            ]
        ),
    ],
)
