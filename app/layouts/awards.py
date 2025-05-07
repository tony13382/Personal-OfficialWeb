from app.components.navbar import Navbar
from app.components.footer import Footer
from app.components.person_card import PersonCard, MoreModal
from app.components.webHead import Head
from app.layouts.project import ProjectPage
from app.variables import ThemeColor
from app.builder.projects import projectBuilder


def convert_project(project: ProjectPage, delay_times: float) -> str:
    awards_code = ""
    index = 0
    if project.scores:
        for score in project.scores:
            if index != 0:
                awards_code += """<hr class="my-2">"""
            index += 1
            awards_code += f"""
<div class="col my-autor">
    <p class="card-text m-0 fw-bold">
        {score.name}{f"・{score.group}" if score.group else ""}
    </p>
    <p class="card-text m-0 text-theme fs-4 fw-bold">
        {score.score}
    </p>
</div>
"""
    single_code = f"""
<div class="card shadow rounded-basic animate__animated animate__fadeInUp" style="animation-delay: {delay_times}s;">
    <div class="card-body lh-lg pt-1 pb-2" id="about">
        <div class="row">
            <div class="col align-self-center">
                <p class="m-0 text-secondary fs-5">{project.title}</p>
            </div>
            <div class="col-auto">
                <a href="../projects/{project.prefix}.html" class="btn btn-outline-theme rounded-pill my-2">相關專案</a>
            </div>
        </div>
        <hr class="mt-1 mb-2">
        <div class="row">
            {awards_code}
        </div>
    </div>
</div>
"""
    return single_code


projects_html = ""
projects = projectBuilder.getPages()

if projects:
    delay_sec = 0
    had_score = []
    for project in projects:
        if project.scores:
            had_score.append(project)
    for project in had_score:
        projects_html += convert_project(project, delay_sec)
        delay_sec += 0.2

script = """    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/2.0.2/anime.min.js"></script>

    <script type="text/javascript" src="/assets/script/lozad.min.js"></script>
    <script>
        function run_lazad() {
            const observer = lozad(); // lazy loads elements with default selector as '.lozad'
            observer.observe();
        }
        run_lazad();
    </script>
    """

page = f"""
<!doctype html>
<html lang="zh-Hant-TW">
    {Head(
        title="我的獎項",
        description="關於我的榮譽獎項",
        cover="/assets/imgs/index/cover.jpg",
        link="/projects",
        colorSet=ThemeColor().orange,
    )}
<body class="bg-mytheme">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" />
    
    {Navbar("project")}

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
            background: linear-gradient(0deg, rgba(49, 40, 38, 0.89), rgba(45, 38, 30, 0.95)), url(/assets/imgs/index/cover.jpg);
            background-size: cover;
            min-height: 20vh;
            align-items: center;
            display: grid;">
        <div class="text-white" style="padding: 5rem 2rem;">
            <div class="container">
                <div class="row">
                    <div class="col-12 d-grid gap-4">
                        <h1 style="letter-spacing: 0.4em; line-height: 150%; color: #FFFFFF;" class="text-center">
                            我的獎項
                        </h1>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="container pb-5" style="margin-top: -160px;">
        <div class="row position-relative d-flex align-items-start">
            <div class="col-lg-3 col-12 pb-4 sticky-lg-top " style="padding-top: 92px; z-index: 999;">
                {str(PersonCard())}
            </div>
            <div class="col-lg-9 col-12 pb-4">
                <div style="height:92px;" class="d-none d-lg-block"></div>
                <div class=" d-grid gap-4" style="margin-top: -92px; padding-top:92px;">
                    {projects_html}
                </div>
            </div>
        </div>
    </div>

    {str(MoreModal())}

    {str(Footer())}

    {script}
</body>

</html>
"""
