from app.builder.jobs import jobBuilder
from app.builder.projects import projectBuilder
from app.builder.skill import skillBuilder
from app.components.footer import Footer
from app.components.navbar import Navbar
from app.components.person_card import PersonCard, MoreModal
from app.layouts.project import ProjectPage

projectBuilder.getPages()


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
</head>
"""

navbar_html = str(Navbar("main"))


jobBuilder.getPages()

job_html = ""
for job in jobBuilder.getPages():
    firstColor, secondColor = job.colorSet
    job_html += f"""
<style>
.jobCard-{job.prefix}:hover {{
    border: 1px solid {firstColor};
    background-color: {firstColor}20;
}}
</style>
<a href="/jobs/{job.prefix}.html" class="text-decoration-none text-black">
    <div class="card pb-2 rounded-inline-basic hoverShadow jobCard-{job.prefix}">
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


skill_html = ""
for skill in skillBuilder.getPages():
    firstColor, secondColor = skill.colorSet
    skill_html += f"""
    <style>
    .skillCard-{skill.prefix} {{
        border: 0px;
        background-color: {firstColor}10;
    }}
    .skillCard-{skill.prefix}:hover {{
        border: 1px solid {firstColor};
    }}
    </style>
    <div class="col-12 col-md-6 d-grid">
        <a href="/skills/{skill.prefix}.html" class="text-decoration-none text-black">
            <div class="card rounded-inline-basic h-100 hoverShadow skillCard-{skill.prefix}">
                <div class="card-body">
                    <div class="d-inline-flex justify-content-center align-items-center fs-4 text-white" style="width: 52px; height: 52px; border-radius: 1rem; background-color: {firstColor};">
                        <i class="bi {skill.icon}"></i>
                    </div>
                    <p class="m-0 mt-2 fw-bold" style="color: {firstColor};">{skill.title}</p>
                    <hr style="opacity: 0.1;" class="my-2">
                    {str(skill.description)}
                </div>
            </div>
        </a>
    </div>
"""


def convert_project(project: ProjectPage) -> str:
    tag_code = ""
    if project.tags:
        tag_code += """<div class="card-footer bg-transparent border-0 pb-3"><div class="fs-5 text-black pt-3">"""
        for tag in project.tags:
            tag_code += f"""<span class="badge bg-mytheme text-black me-1 rounded-pill overflow-hidden">{tag}</span>"""
        tag_code += """</div></div>"""
    single_code = f"""
    <div class="col-12 col-md-6 col-lg-4 p-2">
        <a href="/projects/{project.prefix}.html" class="text-decoration-none text-dark">
            <div class="card hoverShadow hoverBigger h-100 border-0 rounded-basic"><img
                    src="{project.cover}" class="card-img-top lozad" alt="..."
                    data-src="/assets/imgs/general/imageLoading.svg" data-loaded="true">
                <div class="card-body">
                    <h5 class="card-title">{project.title}</h5>
                    <p class="card-text">{project.description}</p>
                </div>
                {tag_code}
            </div>
        </a>
    </div>
"""
    return single_code


projects_html = ""
projects = projectBuilder.getPages()
if projects:
    pin_projects = []
    for project in projects:
        if project.pin:
            pin_projects.append(project)

    for project in pin_projects:
        projects_html += convert_project(project)


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

    .bg-mytheme {{
        background: {secondColor}15;
    }}
    .text-theme {{
        color: var(--themeColor);
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
            background-repeat:no-repeat;background-size:cover; background-attachment: local;
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
                """
    + str(PersonCard())
    + """
            </div>
            <div class="col-lg-9 col-12 pb-5">
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
                <!-- 專業技能 -->
                <div class="card shadow mt-4 border-0 rounded-basic">
                    <div class="card-body lh-lg" id="about">
                        <div class="col-12">
                            <h3 class="py-2 fw-bold" style="letter-spacing: 4px;">我的<span
                                    style="color: #ea81b0;">專業技能</span></h3>
                        </div>
                        <div class="row g-3">
                            """
    + skill_html
    + f"""
                        </div>
                    </div>
                </div>
                <!-- 工作經歷 -->
                <div class="card shadow mt-4 rounded-basic">
                    <div class="card-body lh-lg" id="about">
                        <div class="row">
                            <div class="col-12 pb-3">
                                <h3 class="pt-2 fw-bold" style="letter-spacing: 4px;">個人<span
                                        style="color: #ea81b0;">經歷</span></h3>
                            </div>
                            <div class="col-12 d-grid gap-3 bordre-1">
                                """
    + job_html
    + f"""
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
                        <h2 class="mb-2 mt-5" style="margin-left: -4px;">精選作品集</h2>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="pb-5 bg-my-projects">
        <div class="container" id="project_board">
            <div class="row d-flex align-items-stretch">
                {projects_html}
                <div class="col-12 p-2">
                    <a href="/projects/index.html" class="text-decoration-none text-black">
                        <div class="card hoverShadow hoverBigger h-100 border-0 rounded-basic">
                            <div class="card-body">
                                <p class="card-text text-center">查看更多作品</p>
                            </div>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </div>

    """
    + str(MoreModal())
    + footer_html
    + """
    <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/2.0.2/anime.min.js"></script>
</body>

</html>
"""
)
