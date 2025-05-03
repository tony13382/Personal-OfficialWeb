from app.builder.jobs import jobBuilder
from app.builder.projects import projectBuilder
from app.components.footer import Footer
from app.components.navbar import Navbar


projectBuilder.getPages()

set_projects_js = ""
for project in projectBuilder.getPages():
    set_projects_js += f"""
    {{
        name: "{project.title}",
        cover: "{project.cover}",
        beforeLoadingCover: "",
        link: "{f"/projects/{project.prefix}.html"}",
        tags: {project.tags},
        description: "{project.description}",
        projectType: {project.skill_types},
    }},
    """


head_html = """
<!doctype html>
<html lang="zh-Hant-TW">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="Description" CONTENT="關於呂亮進">
    <!-- Facebook Opengraph -->
    <meta property="og:url" content="https://lianglu.uk/" />
    <meta property="og:type" content="website" />
    <meta property="og:title" content="關於呂亮進" />
    <meta property="og:description" content="一位多領域背景的產品創造者." />
    <meta property="og:image" content="/assets/MetaTagCover.png" />
    <meta property="og:image:alt" content="亮進・產品創造者" />
    <meta property="og:image:type" content="image/png" />
    <meta property="og:image:width" content="1200px" />
    <meta property="og:image:height" content="630px" />
    <!-- End Facebook Opengraph -->
    <title>呂亮進・一位多領域背景的產品創造者</title>
    <link rel="Shortcut Icon" type="image/x-icon" href="/assets/favicon.png" />
    <!--Start Load CSS-->
    <link rel="stylesheet" href="/assets/stylesheets/myself.css">
    <link rel="stylesheet" href="/assets/stylesheets/all.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" />
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" />
    <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css"
        integrity="sha384-AYmEC3Yw5cVb3ZcuHtOA93w35dYTsvhLPVnYs9eStHfGJvOvKxVfELGroGkvsg+p" crossorigin="anonymous" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@100;400;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Emoji&display=swap" rel="stylesheet">
    <!-- Google Font - Nav Logo-->
    <link href="https://fonts.googleapis.com/css2?family=Playwrite+HR+Lijeva&display=swap" rel="stylesheet">

    <!--GA Ana-->
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-165132NHTH"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        gtag('js', new Date());

        gtag('config', 'G-165132NHTH');
    </script>


    <!-- Add: Vue.js Suppot-->
    <script type="importmap">
        {"imports": {
            "vue": "/assets/script/vue.esm-browser.js"
        }}
    </script>

    <script>
        // 定義作品集資料格式
        const set_type = [
            {
                id: "pin",
                title: "⭐ 精選專案",
                html_icon: "<i class='bi bi-star-fill pe-2'></i>精選專案"
            },
            {
                id: "analysis",
                title: "📊 數據/文本分析",
                html_icon: "<i class='bi bi-bar-chart-fill pe-2'></i>數據／文本分析"
            },
            {
                id: "dev",
                title: "💻 程式開發",
                html_icon: "<i class='bi-terminal-fill pe-2'></i>程式開發"
            },
            {
                id: "design",
                title: "🎨 設計",
                html_icon: "<i class='bi bi-vector-pen pe-2'></i>設計"
            },
            {
                id: "plan",
                title: "🖊️ 企劃",
                html_icon: "<i class='bi-file-earmark-medical-fill pe-2'></i>企劃"
            },
            {
                id: "other",
                title: "🗃️ 其他",
                html_icon: "<i class='bi bi-three-dots pe-2'></i>其他"
            }
        ]
        // 作品集資料
        const set_projects = [
"""
head_html += set_projects_js
head_html += """
    ]
    </script>
</head>
"""

navbar_html = str(Navbar("main"))


jobBuilder.getPages()

job_html = ""
for job in jobBuilder.getPages():
    job_html += f"""
<a href="/jobs/{job.prefix}.html" class="text-decoration-none text-black">
    <div class="card pb-2 rounded-inline-basic hoverShadow">
        <div class="card-body pb-1">
            <div class="d-flex align-items-center flex-wrap">
                <p class="mb-0 flex-fill fs-5 fw-bold">{job.title}</p>
                <p class="mb-0 opacity-50 ">{job.startdate} ～ {job.enddate}</p>
            </div>
            <div class="">
                <div class="d-flex align-items-center flex-wrap">
                    <p class="mb-0 me-2">{job.job_name.replace("<br>", "")}</p>
                </div>
            </div>
            <div class="">
                <hr style="opacity: 0.1;">
                {str(job.description)}
            </div>
        </div>
    </div>
</a>
    """

footer_html = str(Footer())

themeColor = "#7c6e69"
secondColor = "#49413d"
theme_html = f"""
<style>
    :root {{
        --themeColor: {themeColor};
        --secondColor: {secondColor};
    }}

    body {{
        background-color: #E8E1E5 !important;
    }}

    .bg-my-projects {{
        background-color: #ececec !important;
    }}

    .navlogofont {{
        font-family: "Playwrite HR Lijeva", cursive;
        font-optical-sizing: auto;
        font-weight: 400;
        font-style: normal;
    }}

    .text-highlight {{
        color: var(--secondColor);
        margin: 0 2px;
        padding: 0 4px;
        font-weight: 800;
        background: linear-gradient(to top, {themeColor}40 30%, transparent 30%);
        background-position: bottom;
        background-repeat: no-repeat;
        background-size: 100% 100%; /* 使背景覆蓋文字 */
    }}
</style>
"""

full_html = (
    head_html
    + """
<body>
    """
    + theme_html
    + navbar_html
    + """
    <a class="fixed-bottom text-decoration-none" onclick="toTop()" id="toTopBtn"
        style="display:none; z-index: 1000; right:16px; bottom:40px; left: auto;">
        <div class="rounded-circle d-inline-flex shadow-lg p-2 rounded toTopBtn">
            <div class="fs-4 d-flex align-items-center flex-wrap justify-content-center text-white"
                style="width: 48px; height: 48px;">
                <i class="bi bi-chevron-up text-decoration-none d-flex"></i>
            </div>
        </div>
    </a>
    <script src="/assets/script/scroll.js"></script>
    <div style="
            padding: 80px 0px; 
            background: linear-gradient(0deg, rgba(49, 40, 38, 0.89), rgba(45, 38, 30, 0.95)), url(assets/imgs/index/homeCover.jpg); 
            background-size: cover;
            min-height: 90vh;
            align-items: center;
            display: grid;" id="topCover">
        <div class="text-white" style="padding: 5rem 2rem;">
            <div class="container">
                <div class="row">
                    <div class="col-12 d-grid gap-4">
                        <h1 style="letter-spacing: 0.4em; line-height: 150%; color: #FFFFFF;" class="">
                            具多領域能力的網頁全端工程師
                        </h1>
                        <div class="card rounded-basic animate__animated animate__fadeInUp"
                            style="background-color: #fcefeab9;">
                            <div class="row card-body">
                                <div class="col-auto">
                                    <div class="d-inline-flex justify-content-center align-items-center fs-4"
                                        style="width: 48px; height: 48px; border-radius: 1.0rem; background-color: var(--secondColor);">
                                        <i class="bi bi-phone"></i>
                                    </div>
                                </div>
                                <div class="col text-black ps-1">
                                    <p class="fw-bold mb-0">設計</p>
                                    <p class="mt-1 mb-0" style="letter-spacing: 0.1rem;">
                                        熟悉用戶體驗設計，並具有大量資料視覺化設計經驗，能夠提供有效的方案解決需求。
                                    </p>
                                </div>
                            </div>
                        </div>
                        <div class="card rounded-basic animate__animated animate__fadeInUp"
                            style="background-color: #fcefeab9;">
                            <div class="row card-body">
                                <div class="col-auto">
                                    <div class="d-inline-flex justify-content-center align-items-center fs-4"
                                        style="width: 48px; height: 48px; border-radius: 1.0rem; background-color: var(--secondColor);">
                                        <i class="bi bi-code-slash"></i>
                                    </div>
                                </div>
                                <div class="col text-black ps-1">
                                    <p class="fw-bold mb-0">開發</p>
                                    <p class="mt-1 mb-0" style="letter-spacing: 0.1rem;">
                                        專精於網頁領域全端開發，具有多項專案開發經驗，能建立完整架構的前後端網頁。
                                    </p>
                                </div>
                            </div>
                        </div>
                        <div class="card rounded-basic animate__animated animate__fadeInUp"
                            style="background-color: #fcefeab9;">
                            <div class="row card-body">
                                <div class="col-auto">
                                    <div class="d-inline-flex justify-content-center align-items-center fs-4"
                                        style="width: 48px; height: 48px; border-radius: 1.0rem; background-color: var(--secondColor);">
                                        <i class="bi bi-database"></i>
                                    </div>
                                </div>
                                <div class="col text-black ps-1">
                                    <p class="fw-bold mb-0">數據分析</p>
                                    <p class="mt-1 mb-0" style="letter-spacing: 0.1rem;">
                                        具有大量數據處理以及分析經驗，擅長結合資訊設計並進行分析，讓數據帶來價值。
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="container" style="margin-top: -160px;">
        <div class="row position-relative d-flex align-items-start">
            <div class="col-lg-3 col-12 pb-4 sticky-lg-top " style="padding-top: 92px; z-index: 999;">
                <div class="card shadow rounded-basic">
                    <div class="card-body p-4">
                        <div class="col-12">
                            <div class="d-flex justify-content-center">
                                <img src="/assets/imgs/index/myHead.webp" alt="my personal picture" width="120px"
                                    class="bordre-1 rounded-circle">
                            </div>
                            <h2 class="fs-4 text-SkyHeavyBlue text-center mt-2">
                                呂亮進
                            </h2>
                            <p class="text-center text-black-50">後端開發／AI 工程師</p>
                        </div>
                        <div class="d-grid gap-2">
                            <a target="_blank" type="button" class="btn btn-myprimary rounded-pill"
                                href="/assets/file/rv/RV(Data_Science).pdf">
                                我的履歷
                            </a>
                            <a type="button" class="btn btn-outline-myprimary rounded-pill" data-bs-toggle="modal"
                                data-bs-target="#shareModel" data-bs-toggle="popover" data-bs-trigger="hover focus"
                                data-bs-content="QR Code" data-bs-placement="bottom">聯絡我
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-9 col-12 pb-4">
                <div style="height: 92px;" class="d-none d-lg-block"></div>
                <!--自介-->
                <div class="card shadow rounded-basic border-0">
                    <img src="/assets/imgs/index/profile_cover.jpg" class="card-img-top" alt="header image.">
                    <div class="p-2">
                        <div class="card-body lh-lg" id="about">
                            <div class="row">
                                <div class="col-12">
                                    <p class="card-text pb-2 px-2">
                                        我是一位對<span
                                            class="halfHightLightBg">產品開發充滿熱情</span>且擁有設計開發與行銷經驗的專業人士。我享受挑戰和開發新產品的過程，擁有將商業設計與開發相結合的能力，並具備參與多項專案的經驗。
                                    </p>
                                    <p class="card-text pb-2 px-2">
                                        我喜歡不斷挑戰自己並參與新產品的開發。從商業設計到開發的一條龍產品規劃經驗讓我能夠全方位地理解並滿足用戶需求。我注重細節，能夠平衡創新和實用性，並致力於創造出優質的產品。我具有良好的問題解決能力和分析能力，在高壓環境下能夠保持冷靜並迅速找到解決方案。
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- 工作優勢 -->
                <div class="card shadow mt-4 border-0 rounded-basic">
                    <div class="card-body pb-0 lh-lg" id="about">
                        <div class="col-12">
                            <h3 class="pt-2 fw-bold" style="letter-spacing: 4px;">與我合作的<span
                                    style="color: #ea81b0;">優勢</span></h3>
                        </div>
                    </div>
                    <div class="card-body px-0 py-0 pb-3 mx-3 lh-lg">
                        <div class="d-grid gap-3 pt-2">
                            <div class="card rounded-basic border-0" style="background-color: #f8eff6ca;">
                                <div class="row card-body">
                                    <div class="col-auto">
                                        <div class="d-inline-flex justify-content-center align-items-center fs-4 text-white"
                                            style="width: 52px; height: 52px; border-radius: 1rem; background-color: #755e70;">
                                            <i class="bi bi-card-checklist"></i>
                                        </div>
                                    </div>
                                    <div class="col ps-1 text-black">
                                        <p class="fw-bold mb-0">全方位產品開發能力</p>
                                        <p class="mt-1 mb-0" style="letter-spacing: 0.1rem;">
                                            具備<span
                                                class="halfHightLightBg">商業設計到開發的一條龍產品規劃</span>經驗，能夠全面理解並滿足用戶需求。我注重於需求整合打造優質的產品。
                                        </p>
                                    </div>
                                </div>
                            </div>
                            <div class="card rounded-basic border-0" style="background-color: #f8eff6ca;">
                                <div class="row card-body">
                                    <div class="col-auto">
                                        <div class="col-auto">
                                            <div class="d-inline-flex justify-content-center align-items-center fs-4 text-white"
                                                style="width: 52px; height: 52px; border-radius: 1rem; background-color: #755e70;">
                                                <i class="bi bi-patch-question"></i>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col ps-1 text-black">
                                        <p class="fw-bold mb-0">強大的問題解決能力</p>
                                        <p class="mt-1 mb-0" style="letter-spacing: 0.1rem;">
                                            具備優秀的問題分析和實作能力。在高壓環境下，我能夠透過<span
                                                class="halfHightLightBg">以終為始與資源盤點</span>迅速找到解決方案並且在挑戰過程中不斷成長。
                                        </p>
                                    </div>
                                </div>
                            </div>
                            <div class="card rounded-basic border-0" style="background-color: #f8eff6ca;">
                                <div class="row card-body">
                                    <div class="col-auto">
                                        <div class="col-auto">
                                            <div class="d-inline-flex justify-content-center align-items-center fs-4 text-white"
                                                style="width: 52px; height: 52px; border-radius: 1rem; background-color: #755e70;">
                                                <i class="bi bi-person-lines-fill"></i>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col ps-1 text-black">
                                        <p class="fw-bold mb-0">多元技能背景</p>
                                        <p class="mt-1 mb-0" style="letter-spacing: 0.1rem;">
                                            擁有資訊管理和學習科學與科技研究所的學位，<span
                                                class="halfHightLightBg">多元的校園經驗與創業經歷</span>相結合使我能夠結合技術和理解使用者需求來開發產品。精通多種程式語言，能夠進行<span
                                                class="halfHightLightBg">全端開發</span>並擁有<span
                                                class="halfHightLightBg">介面設計和資料視覺化</span>的專業技能。
                                        </p>
                                    </div>
                                </div>
                            </div>
                            <div class="card rounded-basic border-0" style="background-color: #f8eff6ca;">
                                <div class="row card-body">
                                    <div class="col-auto">
                                        <div class="col-auto">
                                            <div class="d-inline-flex justify-content-center align-items-center fs-4 text-white"
                                                style="width: 52px; height: 52px; border-radius: 1rem; background-color: #755e70;">
                                                <i class="bi bi-briefcase"></i>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col ps-1 text-black">
                                        <p class="fw-bold mb-0">豐富合作經驗</p>
                                        <p class="mt-1 mb-0" style="letter-spacing: 0.1rem;">
                                            具備良好的團隊合作能力，能夠有效溝通和協調。<span
                                                class="halfHightLightBg">多次擔任管理職與協調者角色</span>，善於與團隊成員合作，共同努力實現目標。我相信良好的團隊合作能讓計畫走得更長遠。
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- 工作經歷 -->
                <div class="card shadow mt-4 rounded-basic">
                    <div class="card-body lh-lg" id="about">
                        <div class="row">
                            <div class="col-12 pb-3">
                                <h3 class="pt-2 fw-bold" style="letter-spacing: 4px;">工作<span
                                        style="color: #ea81b0;">經歷</span></h3>
                            </div>
                            <div class="col-12 d-grid gap-3 bordre-1">
                                """
    + job_html
    + """
                            </div>
                        </div>
                    </div>
                </div>
                <!--學歷-->
                <div class="card shadow mt-4 rounded-basic">
                    <div class="card-body lh-lg" id="about">
                        <div class="row">
                            <div class="col-12">
                                <h3 class="pt-2 fw-bold" style="letter-spacing: 4px;">學歷</h3>
                            </div>
                        </div>
                        <div class="row d-grid gap-3 mt-3">
                            <div class="col-12">
                                <div class="card rounded-inline-basic">
                                    <div class="card-body">
                                        <div class="row">
                                            <div class="col">
                                                <b>國立清華大學</b>
                                                <p class="mb-0">學習科學與科技研究所</p>
                                            </div>
                                            <div class="col-auto">
                                                <p class="mb-0 opacity-50">2022/07～2024/07</p>
                                            </div>
                                        </div>
                                        <div class="row">
                                            <div class="col">
                                                <hr class="my-2" style="opacity:10%;">
                                                <p class="mb-0">論文：</p>
                                                <ol class="mb-0" style="padding-left: 22px;">
                                                    <li>在自主學習環境比較不同提示策略對大型語言模型回應的影響</li>
                                                    <li>使用自然語言技術建構自主學習資源推薦系統</li>
                                                </ol>
                                                <hr class="my-2" style="opacity:10%;">
                                                <div class="d-flex flex-wrap align-items-center mt-3">
                                                    <p class="mb-0 me-2">相關專案：</p>
                                                    <a href="projects/trelloFinder.html"
                                                        class="btn btn-outline-myprimary px-2 py-1 my-1 me-2 rounded-pill"
                                                        style="font-size: 0.75rem;">
                                                        Trello 知識小幫手 2.0
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="card-footer bg-white">
                                        <p class="mt-1 mb-0">
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 mt-1 me-1 overflow-hidden">#
                                                教育</span>
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 mt-1 me-1 overflow-hidden">#
                                                科技</span>
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 mt-1 me-1 overflow-hidden">#
                                                自然語言分析</span>
                                        </p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="card rounded-inline-basic">
                                    <div class="card-body">
                                        <div class="row">
                                            <div class="col">
                                                <b>中原大學</b>
                                                <p class="mb-0">資訊管理系</p>
                                            </div>
                                            <div class="col-auto">
                                                <p class="mb-0 opacity-50">2019/07～2022/07</p>
                                            </div>
                                        </div>
                                        <div class="row">
                                            <div class="col">
                                                <hr class="my-2" style="opacity:10%;">
                                                <div class="d-flex flex-wrap align-items-center mt-3">
                                                    <p class="mb-0 me-2">相關專案：</p>
                                                    <a href="projects/mindReader.html"
                                                        class="btn btn-outline-myprimary px-2 py-1 my-1 me-2 rounded-pill"
                                                        style="font-size: 0.75rem;">
                                                        MindReader 與你心譯相通
                                                    </a>
                                                    <a href="projects/hsCloudMeetingManage.html"
                                                        class="btn btn-outline-myprimary px-2 py-1 my-1 me-2 rounded-pill"
                                                        style="font-size: 0.75rem;">
                                                        華新雲會議管理系統
                                                    </a>
                                                    <a href="projects/hsVmi.html"
                                                        class="btn btn-outline-myprimary px-2 py-1 my-1 me-2 rounded-pill"
                                                        style="font-size: 0.75rem;">
                                                        華新 VMI 庫存管理遊戲
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="card-footer bg-white">
                                        <p class="mt-1 mb-0">
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 mt-1 me-1 overflow-hidden">#
                                                開發</span>
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 mt-1 me-1 overflow-hidden">#
                                                資料庫</span>
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 mt-1 me-1 overflow-hidden">#
                                                數據分析</span>
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!--資格認證-->
                <div class="card shadow mt-4 rounded-basic">
                    <div class="card-body lh-lg" id="about">
                        <div class="row">
                            <div class="col-12">
                                <h3 class="pt-2 fw-bold" style="letter-spacing: 4px;">資格認證</h3>
                            </div>
                        </div>
                        <div class="row d-grid gap-3 mt-3">
                            <div class="col-12">
                                <div class="card rounded-inline-basic">
                                    <div class="card-body">
                                        <div class="row">
                                            <div class="col">
                                                <b>Google Data Analytics Professional Certificate</b>
                                                <p class="mb-0">Google (Coursera)</p>
                                            </div>
                                            <div class="col-auto">
                                                <p class="mb-0 opacity-50">2021</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="card-footer p-3 pb-1 bg-white">
                                        <p class="col-12 mb-0">
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 me-2 overflow-hidden">#
                                                Python</span>
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 me-2 overflow-hidden">#
                                                Excel</span>
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 me-2 overflow-hidden">#
                                                SQL</span>
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 me-2 overflow-hidden">#
                                                資料搜集／前處理</span>
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 me-2 overflow-hidden">#
                                                資料視覺化</span>
                                        </p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="card rounded-inline-basic">
                                    <div class="card-body">
                                        <div class="row">
                                            <div class="col">
                                                <b>IBM Data Visualization & Dashboard Essentials</b>
                                                <p class="mb-0">IBM (Coursera)</p>
                                            </div>
                                            <div class="col-auto">
                                                <p class="mb-0 opacity-50">2021</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="card-footer p-3 pb-1 bg-white">
                                        <p class="col-12 mb-0">
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 me-2 overflow-hidden">#
                                                Python</span>
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 me-2 overflow-hidden">#
                                                Excel</span>
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 me-2 overflow-hidden">#
                                                IBM Cognos</span>
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 me-2 overflow-hidden">#
                                                SQL</span>
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 me-2 overflow-hidden">#
                                                資料視覺化</span>
                                        </p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="card rounded-inline-basic">
                                    <div class="card-body">
                                        <div class="row">
                                            <div class="col">
                                                <b>Google Analytics (分析) 個人認證</b>
                                                <p class="mb-0">Google</p>
                                            </div>
                                            <div class="col-auto">
                                                <p class="mb-0 opacity-50">2021</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="card-footer p-3 pb-1 bg-white">
                                        <p class="col-12 mb-0">
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 me-2 overflow-hidden">#
                                                行銷</span>
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 me-2 overflow-hidden">#
                                                數位行銷</span>
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 me-2 overflow-hidden">#
                                                資料分析</span>
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 me-2 overflow-hidden">#
                                                GA4</span>
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 me-2 overflow-hidden">#
                                                SEO</span>
                                        </p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="card rounded-inline-basic">
                                    <div class="card-body">
                                        <div class="row">
                                            <div class="col">
                                                <b>Google 基礎行銷資格認證</b>
                                                <p class="mb-0">Google</p>
                                            </div>
                                            <div class="col-auto">
                                                <p class="mb-0 opacity-50">2021</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="card-footer p-3 pb-1 bg-white">
                                        <p class="col-12 mb-0">
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 me-2 overflow-hidden">#
                                                行銷</span>
                                            <span
                                                class="badge rounded-pill bg-mytheme text-dark p-2 me-2 overflow-hidden">#
                                                數位行銷</span>
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </div>
    <!--技能組-->
    <div class="container pb-5">
        <div class="row">
            <div class="col-12">
                <!--技能組-->
                <div class="card shadow my-4 rounded-basic">
                    <div class="card-body">
                        <div class="row ms-navbar fs-4" id="skills" style="margin-top: -92px;padding-top: 92px;">
                            <div class="col-12">
                                <ul class="nav mb-2 align-items-end flex-nowrap overflow-auto" id="products-tabs"
                                    role="tablist" style="margin-left: -0.25rem;">
                                    <li class="nav-item me-3 ">
                                        <a class="nav-link px-1 py-0 text-nowrap active" id="skill-develope-tab"
                                            data-bs-toggle="pill" data-bs-target="#skill-develope" type="button"
                                            role="tab" aria-controls="skill-develope" aria-selected="true">開發技能</a>
                                    </li>
                                    <li class="nav-item me-3">
                                        <a class="nav-link px-1 py-0 text-nowrap" id="skill-dataScience-tab"
                                            data-bs-toggle="pill" data-bs-target="#skill-dataScience" type="button"
                                            role="tab" aria-controls="skill-dataScience"
                                            aria-selected="false">數據分析技能</a>
                                    </li>
                                    <li class="nav-item me-3">
                                        <a class="nav-link px-1 py-0 text-nowrap" id="skill-design-tab"
                                            data-bs-toggle="pill" data-bs-target="#skill-design" type="button"
                                            role="tab" aria-controls="skill-design" aria-selected="false">設計相關技能</a>
                                    </li>
                                    <li class="nav-item me-3 ">
                                        <a class="nav-link px-1 py-0 text-nowrap" id="skill-other-tab"
                                            data-bs-toggle="pill" data-bs-target="#skill-other" type="button" role="tab"
                                            aria-controls="skill-develope" aria-selected="false">其他技能</a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <div class="tab-content" id="pills-tabContent">
                            <!--開發技能-->
                            <div class="tab-pane fade show active" id="skill-develope" role="tabpanel"
                                aria-labelledby="skill-develope-tab" tabindex="0">
                                <p class="mb-1 mt-2 notoFont lh-lg">
                                    全端皆可開發，主要發力於 <span class="halfHightLightBg">網站領域</span>，對於 APIs
                                    串接與架設皆已有相關實務經驗，能整合各式套件協助企業完成產品開發。
                                </p>
                                <hr class="my-3" style="opacity: 0.10;">
                                <div class="row" style="margin: 0rem -0.25rem;">
                                    <div class="col-12 p-1">
                                        <p class="fs-5 m-0">
                                            <i class='bi bi-laptop px-2'></i> 前端
                                        </p>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/pythonPackage/streamlit.png"
                                                            class="img-fluid p-1" alt="ChatGPT（LLM） Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Streamlit</p>
                                                    <p class="p-0 m-0">Python 介面快速部署</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/html.png" class="img-fluid p-1"
                                                            alt="HTML5 Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">HTML5 & CSS3</p>
                                                    <p class="p-0 m-0">前端設計</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/bootstrapV5.png"
                                                            class="img-fluid p-1" alt="BS5 Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Bootstrap</p>
                                                    <p class="p-0 m-0">網頁切版</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/javascript.png"
                                                            class="img-fluid p-1" alt="JS Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">JavaScript</p>
                                                    <p class="p-0 m-0">DOM 物件操作與變化</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/react.png" class="img-fluid p-1"
                                                            alt="React Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">React</p>
                                                    <p class="p-0 m-0">前端開發</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/vue.png" class="img-fluid p-1"
                                                            alt="VueJS Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Vue.js</p>
                                                    <p class="p-0 m-0">前端開發</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/flutter.png"
                                                            class="img-fluid p-1" alt="flutter Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Flutter</p>
                                                    <p class="p-0 m-0">APP 開發</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="row" style="margin: 0rem -0.25rem;">
                                    <div class="col-12 p-1">
                                        <p class="fs-5 m-0 pt-4">
                                            <i class='bi bi-terminal px-2'></i>後端
                                        </p>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/fastapi.png"
                                                            class="img-fluid p-2" alt="Milvus Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">FastAPI</p>
                                                    <p class="p-0 m-0">API 開發</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/pythonPackage/flask.png"
                                                            class="img-fluid p-1" alt="python Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Python</p>
                                                    <p class="p-0 m-0">Flask APIs 開發實務／資料庫串接</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/apacheTomcat.png"
                                                            class="img-fluid p-1" alt="JSP Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Java Server Page</p>
                                                    <p class="p-0 m-0">Tomcat 後端程式／MySQL 交互</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/nodejs.png"
                                                            class="img-fluid p-1" alt="NodeJs Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">NodeJs</p>
                                                    <p class="p-0 m-0">APIs 建立／網頁後端</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/php.png" class="img-fluid"
                                                            alt="NodeJs Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">php</p>
                                                    <p class="p-0 m-0">網頁後端</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="row" style="margin: 0rem -0.25rem;">
                                    <div class="col-12 p-1 pt-4">
                                        <p class="fs-5 m-0">
                                            <i class='bi bi-database px-2'></i>資料庫
                                        </p>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/postgreSQL.png"
                                                            class="img-fluid p-2" alt="MySQL Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">PostgreSQL（pgvector）</p>
                                                    <p class="p-0 m-0">SQL語法／關聯資料表設計</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/mysql.png" class="img-fluid p-1"
                                                            alt="MySQL Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">MySQL</p>
                                                    <p class="p-0 m-0">SQL語法／關聯資料表設計</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/mongodb.png"
                                                            class="img-fluid p-1" alt="MongoDB Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">MongoDB</p>
                                                    <p class="p-0 m-0">資料檔查詢／與後端進行交互</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/firebase.png"
                                                            class="img-fluid p-1" alt="Firebase Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Firebase</p>
                                                    <p class="p-0 m-0">資料檔查詢／與後端進行交互</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/milvus.png"
                                                            class="img-fluid p-1" alt="Milvus Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Milvus (Vector Database)</p>
                                                    <p class="p-0 m-0">向量資料庫管理</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="row" style="margin: 0rem -0.25rem;">
                                    <div class="col-12 p-1 pt-4">
                                        <p class="fs-5 m-0">
                                            <i class='bi bi-boxes px-2'></i>模型
                                        </p>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/chatgpt.png"
                                                            class="img-fluid p-1" alt="ChatGPT（LLM） Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">ChatGPT (LLM)</p>
                                                    <p class="p-0 m-0">Fine-tuning、提示詞工程、系統串接</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/anthropic.png"
                                                            class="img-fluid p-1" alt="Anthropic (LLM) Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Anthropic (LLM)</p>
                                                    <p class="p-0 m-0">提示詞工程、系統串接</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/chatgpt.png"
                                                            class="img-fluid p-1" alt="ChatGPT（LLM） Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Whisper (OpenAI)</p>
                                                    <p class="p-0 m-0">語音轉文字、語音合成</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/volcengine.png"
                                                            class="img-fluid p-2" alt="SBERT Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">火山雲</p>
                                                    <p class="p-0 m-0">語音轉文字、語音合成</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/azure.png" class="img-fluid p-1"
                                                            alt="SBERT Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Azure LUIS</p>
                                                    <p class="p-0 m-0">NLP 自然語言處理／文字意圖訓練與分析</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/sbert.png" class="img-fluid p-1"
                                                            alt="SBERT Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Sentence-BERT</p>
                                                    <p class="p-0 m-0">文本向量化處理與微調</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="row" style="margin: 0rem -0.25rem;">
                                    <div class="col-12 p-1">
                                        <p class="fs-5 m-0 pt-4">
                                            <i class='bi bi-braces-asterisk px-2'></i>其他
                                        </p>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/docker.png"
                                                            class="img-fluid p-1" alt="Java Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Docker</p>
                                                    <p class="p-0 m-0">Docker 封裝／部署</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/java.png" class="img-fluid p-1"
                                                            alt="Java Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Java</p>
                                                    <p class="p-0 m-0">程式設計</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/git.png" class="img-fluid p-1"
                                                            alt="Git Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Git</p>
                                                    <p class="p-0 m-0">版本控制</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/rabbit_mq.png"
                                                            class="img-fluid p-1" alt="rabbit_mq Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">RabbitMQ</p>
                                                    <p class="p-0 m-0">API 訊息佇列處理系統</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/xampp.svg" class="img-fluid p-1"
                                                            alt="rabbit_mq Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">XAMPP</p>
                                                    <p class="p-0 m-0">部署與配置 Server</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!--數據分析技能-->
                            <div class="tab-pane fade" id="skill-dataScience" role="tabpanel"
                                aria-labelledby="skill-dataScience-tab" tabindex="0">
                                <p class="mb-1 mt-2 notoFont lh-lg">
                                    可協助資料清理與自動化爬蟲取得所需資料，並熟悉利用各式工具將結構化的資料進行視覺化，在非結構化的資料則專注於
                                    <span class="halfHightLightBg">文字探勘</span>
                                    領域，藉由各式分析讓非結構化文字也能對企業帶來新洞察與效益。
                                </p>
                                <hr class="my-3" style="opacity: 0.10;">
                                <div class="row" style="margin: 0rem -0.25rem;">
                                    <div class="col-12 p-1">
                                        <p class="fs-5 m-0">
                                            <i class='bi bi-database px-2'></i>資料搜集／前處理
                                        </p>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/excel.png" class="img-fluid p-1"
                                                            alt="Excel Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Excel</p>
                                                    <p class="p-0 m-0">數據分析／清理／視覺化</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/pyhon.png" class="img-fluid p-1"
                                                            alt="Python Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Python</p>
                                                    <p class="p-0 m-0">Requests & BS4 爬蟲</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/pyhon.png" class="img-fluid p-1"
                                                            alt="Python Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Python</p>
                                                    <p class="p-0 m-0">pandas / Firebase 交互</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/rStudio.png"
                                                            class="img-fluid p-1" alt="R Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">R</p>
                                                    <p class="p-0 m-0">Tidyverse 資料清理、視覺化</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/googleAnalytics.png"
                                                            class="img-fluid p-1" alt="GA Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Google Analytics</p>
                                                    <p class="p-0 m-0">後台操作與資料搜集</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="row" style="margin: 0rem -0.25rem;">
                                    <div class="col-12 p-1">
                                        <p class="fs-5 m-0 pt-4">
                                            <i class='bi bi-file-earmark-bar-graph px-2'></i>資料視覺化
                                        </p>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/data_studio.svg"
                                                            class="img-fluid p-1" alt="Google Data Studio Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Google Data Studio</p>
                                                    <p class="p-0 m-0">數據視覺化</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/powerBi.png"
                                                            class="img-fluid p-1" alt="powerBi Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Poewr BI</p>
                                                    <p class="p-0 m-0">數據視覺化</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/ibmCognos.png"
                                                            class="img-fluid p-1" alt="IBM Cognos Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">IBM Cognos</p>
                                                    <p class="p-0 m-0">數據視覺化</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/ggplot2.png"
                                                            class="img-fluid p-1" alt="Python Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">ggplot2 (Python)</p>
                                                    <p class="p-0 m-0">數據視覺化</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!--設計相關技能-->
                            <div class="tab-pane fade" id="skill-design" role="tabpanel"
                                aria-labelledby="skill-design-tab" tabindex="0">
                                <p class="mb-1 mt-2 notoFont lh-lg">
                                    擅長於 <span class="halfHightLightBg">UI&UX 產品設計</span>，藉由設計的方式將產品概念轉化成可想像的實際產品。
                                    除此之外在<span
                                        class="halfHightLightBg">資料視覺化</span>，也擁有相關技術與經驗，藉由設計的方式將繁雜的資訊以組織有架構且易於吸收的方式傳達給受眾。
                                </p>
                                <hr class="my-3" style="opacity: 0.10;">
                                <div class="row" style="margin: 0rem -0.25rem;">
                                    <div class="col-12 p-1">
                                        <p class="fs-5 m-0">
                                            <i class='bi bi-phone px-2'></i>產品設計
                                        </p>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/figma.png" class="img-fluid p-1"
                                                            alt="Figma Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Figma</p>
                                                    <p class="p-0 m-0">UI Design／平面設計</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/xd.png" class="img-fluid p-1"
                                                            alt="Adobe XD Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Adobe XD</p>
                                                    <p class="p-0 m-0">UI Design</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="row" style="margin: 0rem -0.25rem;">
                                    <div class="col-12 p-1">
                                        <p class="fs-5 m-0 pt-4">
                                            <i class='bi bi-easel px-2'></i>資訊傳達
                                        </p>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/thinkFlow.png"
                                                            class="img-fluid p-1" alt="thinkFlow Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">資訊設計</p>
                                                    <p class="p-0 m-0">整理資訊並傳遞給受眾</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/powerpoint.png"
                                                            class="img-fluid p-1" alt="PPT Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">PowerPoint</p>
                                                    <p class="p-0 m-0">簡報設計</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/canva.png" class="img-fluid p-1"
                                                            alt="Canva Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Canva</p>
                                                    <p class="p-0 m-0">簡報設計／平面設計</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/photoshop.png"
                                                            class="img-fluid p-1" alt="PS Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Photoshop</p>
                                                    <p class="p-0 m-0">圖片設計</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/premiere.png"
                                                            class="img-fluid p-1" alt="PR Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Premiere</p>
                                                    <p class="p-0 m-0">影片剪輯</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!--其他技能-->
                            <div class="tab-pane fade" id="skill-other" role="tabpanel"
                                aria-labelledby="skill-other-tab" tabindex="0">
                                <p class="mb-1 mt-2 notoFont lh-lg">
                                    其他技能能輔助產品製作與發展、技能組橫跨
                                    <span class="halfHightLightBg">行銷、商業思維</span> 。
                                </p>
                                <hr class="my-3" style="opacity: 0.10;">
                                <div class="row" style="margin: 0rem -0.25rem;">
                                    <div class="col-12 p-1">
                                        <p class="fs-5 m-0">
                                            <i class='bi bi-bag px-2'></i>行銷相關
                                        </p>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/obs.png" class="img-fluid p-1"
                                                            alt="OBS Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">OBS</p>
                                                    <p class="p-0 m-0">直播架設與實務操作（FB & Youtube）</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/googleAds.png"
                                                            class="img-fluid p-1" alt="G Ads Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Google Ads</p>
                                                    <p class="p-0 m-0">廣告操作</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/social.png"
                                                            class="img-fluid p-1" alt="Social Marketing Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">社群行銷</p>
                                                    <p class="p-0 m-0">社群經營與維護</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="row" style="margin: 0rem -0.25rem;">
                                    <div class="col-12 p-1">
                                        <p class="fs-5 m-0 pt-4">
                                            <i class='bi bi-file-earmark-medical px-2'></i>內容管理 CMS
                                        </p>
                                    </div>
                                    <div class="col-12 col-md-6 col-lg-4 p-2 d-flex align-items-stretch">
                                        <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
                                            <div class="card-body d-inline-flex align-items-center">
                                                <div class="d-inline-block">
                                                    <div style="width: 64px; height: 64px;" class="">
                                                        <img src="/assets/imgs/appIcons/wordpress.png"
                                                            class="img-fluid p-1" alt="Wordpress Icon">
                                                    </div>
                                                </div>
                                                <div class="ps-3 d-inline-flex flex-column">
                                                    <p class="p-0 mb-2 fw-bold">Wordpress</p>
                                                    <p class="p-0 m-0">網頁架設與管理</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- 作品集 -->
    <div id="myProjects" class="" style="padding-top: 92px; margin-top: -92px;">
        <div class="pt-3 bg-my-projects">
            <div class="container">
                <div class="row ms-navbar">
                    <div class="col-12">
                        <h2 class="mb-4 mt-5" style="margin-left: -4px;">作品集</h2>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="pb-5 bg-my-projects">
        <div class="container" id="project_board">
            <div class="row">
                <div class="col-12">
                    <div class="col-12">
                        <ul class="nav mb-3 align-items-end flex-nowrap overflow-auto" id="products-tabs" role="tablist"
                            style="margin-left: -0.25rem;">
                            <li class="nav-item me-3" v-for="(typetag, index) in type_list" :key="typetag.id">
                                <a class="nav-link px-1 py-0 text-nowrap" v-bind:id="'products-' + typetag.id + '-tab' "
                                    v-bind:data-bs-target="'#products-' + typetag.id "
                                    v-bind:aria-controls="'products-' + typetag.id"
                                    :aria-selected="index === 0 ? 'true' : 'false'" :class="{'active': index === 0}"
                                    data-bs-toggle="pill" type="button" role="tab" aria-selected="false"
                                    v-html="typetag.html_icon">{{typetag.title}}</a>
                            </li>
                            <li class="nav-item me-3">
                                <a class="nav-link px-1 py-0 text-nowrap" id="products-all-tab" data-bs-toggle="pill"
                                    data-bs-target="#products-all" type="button" role="tab" aria-controls="products-all"
                                    aria-selected="false">
                                    <i class='bi bi-boxes pe-2'></i>所有作品
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="tab-content" id="pills-tabContent">
                <div class="tab-pane fade" v-for="(typetag, index) in type_list" v-bind:id="'products-' + typetag.id"
                    v-bind:aria-labelledby="'products-' + typetag.id + '-tab'" :class="{'show active': index === 0}"
                    role="tabpanel" tabindex="0">
                    <div class="row d-flex align-items-stretch">
                        <div class="col-12 col-md-6 col-lg-4 p-2" v-for="project in filteredProjects(typetag.id)">
                            <a :href="project.link" class="text-decoration-none">
                                <div class="card hoverShadow hoverBigger h-100 border-0 rounded-basic">
                                    <img :src="project.beforeLoadingCover" class="card-img-top lozad" alt="..."
                                        :data-src="project.cover">
                                    <div class="card-body">
                                        <h5 class="card-title text-dark">{{ project.name }}</h5>
                                        <p class="card-text text-dark">{{ project.description }}</p>
                                    </div>
                                    <div class="card-footer bg-transparent border-0 pb-3">
                                        <div class="fs-5 text-black pt-3">
                                            <span class="badge bg-mytheme text-black me-1 rounded-pill overflow-hidden"
                                                v-for="tag in project.tags">{{ tag }}</span>
                                        </div>
                                    </div>
                                </div>
                            </a>
                        </div>
                    </div>
                </div>
                <!--所有作品-->
                <div class="tab-pane fade" id="products-all" role="tabpanel" aria-labelledby="products-all-tab"
                    tabindex="0">
                    <div class="row d-flex align-items-stretch">
                        <div class="col-12 col-md-6 col-lg-4 p-2" v-for="project of projects_list">
                            <a :href="project.link" class="text-decoration-none">
                                <div class="card hoverShadow hoverBigger h-100 border-0 rounded-basic">
                                    <img v-bind:src="project.beforeLoadingCover" class="card-img-top lozad" alt="..."
                                        v-bind:data-src="project.cover">
                                    <div class="card-body">
                                        <h5 class="card-title text-dark">
                                            {{project.name}}
                                        </h5>
                                        <p class="card-text text-dark">
                                            {{project.description}}
                                        </p>
                                    </div>
                                    <div class="card-footer bg-transparent border-0 pb-3">
                                        <div class="fs-5 text-black pt-3">
                                            <span class="badge bg-mytheme text-black me-1 rounded-pill overflow-hidden"
                                                v-for="tag in project.tags">{{tag}}</span>
                                        </div>
                                    </div>
                                </div>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <script type="module">
            import { createApp, ref } from 'vue';

            createApp({
                setup() {
                    const projects_list = ref(set_projects); // 初始化項目列表
                    const type_list = ref(set_type); // 初始化類型列表

                    // 定義過濾項目的函數
                    const filteredProjects = (typeId) => {
                        return projects_list.value.filter(project => project.projectType.includes(typeId));
                    };

                    return {
                        projects_list,
                        type_list,
                        filteredProjects,
                    };
                },
            }).mount('#project_board');

            // 當 document 準備好後執行 run_lazad
            document.addEventListener('DOMContentLoaded', () => {
                run_lazad()
            });
        </script>

    </div>
    <!-- Modal -->
    <div class="modal fade" id="shareModel" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
        aria-labelledby="shareModelLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered p-2" style="max-width: 800px;">
            <div class="modal-content rounded-basic">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="shareModelLabel">聯絡我</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body h-auto">
                    <div class="row">
                        <div class="col-12 col-md-6">
                            <div class="d-grid gap-2 text" style="font-size: 1.2rem;">
                                <a class="text-decoration-none grayBlockHover rounded text-dark p-2"
                                    href="mailto:liangchinlu@gmail.com" target="_blank">
                                    <div class="d-flex flex-row align-items-center px-2 py-2 rounded-inline-basic">
                                        <div class="d-flex align-items-center justify-content-center fs-3 rounded-circle"
                                            style="height: 48px; width: 48px; background-color: #b5f5ec; color: #08979c;">
                                            <i class="bi bi-envelope-fill"></i>
                                        </div>
                                        <div class="ms-3 fs-6">
                                            <p class="m-0 fw-bolder">Email</p>
                                            <p class="m-0 text-black-50">liangchinlu@gmail.com</p>
                                        </div>
                                    </div>
                                </a>
                                <a class="text-decoration-none grayBlockHover rounded text-dark p-2"
                                    href="https://www.facebook.com/tony13382/" target="_blank">
                                    <div class="d-flex flex-row align-items-center px-2 py-2 rounded-inline-basic">
                                        <div class="d-flex align-items-center justify-content-center fs-3 rounded-circle"
                                            style="height: 48px; width: 48px; background-color: #bae0ff; color: #0958d9;">
                                            <i class="bi bi-facebook"></i>
                                        </div>
                                        <div class="ms-3 fs-6">
                                            <p class="m-0 fw-bolder">Facebook</p>
                                            <p class="m-0 text-black-50">呂亮進 （양진）</p>
                                        </div>
                                    </div>
                                </a>
                                <a class="text-decoration-none grayBlockHover rounded text-dark p-2"
                                    href="https://www.instagram.com/liang_chin_ml/" target="_blank">
                                    <div class="d-flex flex-row align-items-center px-2 py-2 rounded-inline-basic">
                                        <div class="d-flex align-items-center justify-content-center fs-3 rounded-circle"
                                            style="height: 48px; width: 48px; background-color: #efdbff; color: #531dab;">
                                            <i class="bi bi-instagram"></i>
                                        </div>
                                        <div class="ms-3 fs-6">
                                            <p class="m-0 fw-bolder">Instagram</p>
                                            <p class="m-0 text-black-50">@liang_chin_ml</p>
                                        </div>
                                    </div>
                                </a>
                                <a class="text-decoration-none grayBlockHover rounded text-dark p-2"
                                    href="https://www.linkedin.com/in/liang-chin-lu" target="_blank">
                                    <div class="d-flex flex-row align-items-center px-2 py-2 rounded-inline-basic">
                                        <div class="d-flex align-items-center justify-content-center fs-3 rounded-circle"
                                            style="height: 48px; width: 48px; background-color: #d6e4ff; color: #1d39c4;">
                                            <i class="bi bi-linkedin"></i>
                                        </div>
                                        <div class="ms-3 fs-6">
                                            <p class="m-0 fw-bolder">LinkedIn</p>
                                            <p class="m-0 text-black-50">呂亮進 (Liang-Chin,Lu)</p>
                                        </div>
                                    </div>
                                </a>
                            </div>
                        </div>
                        <div class="col-12 col-md-6">
                            <div class="d-grid gap-2 text" style="font-size: 1.2rem;">
                                <a class="text-decoration-none grayBlockHover rounded text-dark p-2"
                                    href="https://github.com/tony13382" target="_blank">
                                    <div class="d-flex flex-row align-items-center px-2 py-2 rounded-inline-basic">
                                        <div class="d-flex align-items-center justify-content-center fs-3 rounded-circle"
                                            style="height: 48px; width: 48px; background-color: #f5f5f5; color: #262626;">
                                            <i class="bi bi-github"></i>
                                        </div>
                                        <div class="ms-3 fs-6">
                                            <p class="m-0 fw-bolder">GitHub</p>
                                            <p class="m-0 text-black-50">tony13382</p>
                                        </div>
                                    </div>
                                </a>
                                <a class="text-decoration-none grayBlockHover rounded text-dark p-2"
                                    href="https://meowlu.notion.site/Liang-Chin-ML-12e7c67f7f2d47249f0111882d932663"
                                    target="_blank">
                                    <div class="d-flex flex-row align-items-center px-2 py-2 rounded-inline-basic">
                                        <div class="d-flex align-items-center justify-content-center fs-3 rounded-circle"
                                            style="height: 48px; width: 48px; background-color: #fff1b8; color: #d48806;">
                                            <i class="bi bi-journal-bookmark-fill"></i>
                                        </div>
                                        <div class="ms-3 fs-6">
                                            <p class="m-0 fw-bolder">Notion 知識站</p>
                                            <p class="m-0 text-black-50">數位海洋．ML個人學習庫</p>
                                        </div>
                                    </div>
                                </a>
                                <a class="text-decoration-none grayBlockHover rounded text-dark p-2"
                                    href="https://learn.lianglu.uk/" target="_blank">
                                    <div class="d-flex flex-row align-items-center px-2 py-2 rounded-inline-basic">
                                        <div class="d-flex align-items-center justify-content-center fs-3 rounded-circle"
                                            style="height: 48px; width: 48px; background-color: #ffd6e7; color: #c41d7f;">
                                            <i class="bi bi-bookmark-heart-fill"></i>
                                        </div>
                                        <div class="ms-3 fs-6">
                                            <p class="m-0 fw-bolder">知識推薦獲取來源</p>
                                            <p class="m-0 text-black-50">IG／YT／FB／Mail／Web</p>
                                        </div>
                                    </div>
                                </a>
                                <a class="text-decoration-none grayBlockHover rounded text-dark p-2"
                                    href="http://portaly.cc/liang_chin_ml" target="_blank">
                                    <div class="d-flex flex-row align-items-center px-2 py-2 rounded-inline-basic">
                                        <div class="d-flex align-items-center justify-content-center fs-3 rounded-circle"
                                            style="height: 48px; width: 48px; background-color: #d9f7be; color: #389e0d;">
                                            <i class="bi bi-three-dots"></i>
                                        </div>
                                        <div class="ms-3 fs-6">
                                            <p class="m-0 fw-bolder">更多資訊</p>
                                            <p class="m-0 text-black-50">呂亮進 (portaly.cc)</p>
                                        </div>
                                    </div>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="modal-footer d-flex ">
                    <button type="button" class="btn btn-dark w-100 rounded-pill" data-bs-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>

    """
    + footer_html
    + """

    <!-- Optional JavaScript; choose one of the two! -->
    <!-- Option 1: Bootstrap Bundle with Popper -->
    <!--<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous">
        </script>-->
    <script src="/assets/script/bootstrap.bundle.min.js"></script>
    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
    -->

    <!-- <script language="javascript" type="text/javascript"
        src="https://cdnjs.cloudflare.com/ajax/libs/wow/1.1.2/wow.min.js">
        </script>
    <script>
        var wow = new WOW({
            boxClass: 'delayshowanimate', // 要套用WOW.js縮需要的動畫class(預設是wow)
            animateClass: 'animate__animated', // 要"動起來"的動畫(預設是animated, 因此如果你有其他動畫library要使用也可以在這裡調整)
            offset: 0, // 距離顯示多遠開始顯示動畫 (預設是0, 因此捲動到顯示時才出現動畫)
            mobile: true, // 手機上是否要套用動畫 (預設是true)
            live: true, // 非同步產生的內容是否也要套用 (預設是true, 非常適合搭配SPA)
            callback: function (box) {
                // 當每個要開始時, 呼叫這裡面的內容, 參數是要開始進行動畫特效的element DOM
            },
            scrollContainer: null // 可以設定成只套用在某個container中捲動才呈現, 不設定就是整個視窗
        });
        wow.init();
    </script> -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/2.0.2/anime.min.js"></script>
    <!-- <script>
        // Wrap every letter in a span
        var textWrapper = document.querySelector('.ml12');
        textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

        anime.timeline({
            loop: false
        })
            .add({
                targets: '.ml12 .letter',
                translateX: [40, 0],
                translateZ: 0,
                opacity: [0, 1],
                easing: "easeOutExpo",
                duration: 1200,
                delay: (el, i) => 500 + 30 * i
            })
    </script> -->

    <script type="text/javascript" src="/assets/script/lozad.min.js"></script>
    <script>
        function run_lazad() {
            const observer = lozad(); // lazy loads elements with default selector as '.lozad'
            observer.observe();
        }
        run_lazad();
    </script>
</body>

</html>
"""
)
