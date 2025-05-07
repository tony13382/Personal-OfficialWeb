from app.components.navbar import Navbar
from app.components.footer import Footer
from app.components.person_card import PersonCard, MoreModal
from app.components.webHead import Head
from app.layouts.project import ProjectPage
from app.variables import ThemeColor
from app.builder.projects import projectBuilder


def convert_project(project: ProjectPage) -> str:
    tag_code = ""
    if project.tags:
        tag_code += """<div class="card-footer bg-transparent border-0 pb-3"><div class="fs-5 text-black pt-3">"""
        for tag in project.tags:
            tag_code += f"""<span class="badge bg-mytheme text-black me-1 rounded-pill overflow-hidden">{tag}</span>"""
        tag_code += """</div></div>"""
    single_code = f"""
    <div class="col-12 col-md-6 col-lg-6 p-2"><a href="/projects/{project.prefix}.html" class="text-decoration-none">
                <div class="card hoverShadow hoverBigger h-100 border-0 rounded-basic"><img
                        src="{project.cover}" class="card-img-top lozad" alt="..."
                        data-src="/assets/imgs/general/imageLoading.svg" data-loaded="true">
                    <div class="card-body">
                        <h5 class="card-title text-dark">{project.title}</h5>
                        <p class="card-text text-dark">{project.description}</p>
                    </div>
                    {tag_code}
                </div>
            </a></div>
"""
    return single_code


projects_html = ""
projects = projectBuilder.getPages()
if projects:
    projects_html += """
<div class="row d-flex align-items-stretch g-2">
"""
    for project in projects:
        projects_html += convert_project(project)

    projects_html += """
</div>
"""

page = f"""
<!doctype html>
<html lang="zh-Hant-TW">
    {Head(
        title="所有作品",
        description="這是我的所有作品，包含了我在學校的專題、實習的專案、以及我自己開發的專案。",
        cover="/assets/imgs/index/cover.jpg",
        link="/projects",
        colorSet=ThemeColor().natural,
    )}
<body class="bg-mytheme">

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
                            所有作品
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
                <div style="height: 92px;" class="d-none d-lg-block"></div>
                <div style="margin-top: -92px;padding-top: 92px;">
                    {projects_html}
                </div>
            </div>
        </div>
    </div>

    {str(MoreModal())}

    {str(Footer())}
</body>

</html>
"""
