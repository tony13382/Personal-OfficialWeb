from typing import List, Optional, Tuple

from pydantic import BaseModel
from app.components.webHead import Head
from app.components.navbar import Navbar
from app.components.footer import Footer
from app.elements import Card, Html, Image, ListStr
from app.layouts.project import ProjectPage


class SkillItem(BaseModel):
    title: str
    description: str
    icon: str


class SkillsGroup(BaseModel):
    icon: str
    title: str
    children: List[SkillItem] = []


def convert_project(project: ProjectPage) -> str:
    tag_code = ""
    if project.tags:
        tag_code += """<div class="card-footer bg-transparent border-0 pb-3"><div class="fs-5 text-black pt-3">"""
        for tag in project.tags:
            tag_code += f"""<span class="badge bg-mytheme text-black me-1 rounded-pill overflow-hidden">{tag}</span>"""
        tag_code += """</div></div>"""
    single_code = f"""
    <div class="col-12 col-md-6 col-lg-4 p-2"><a href="/projects/{project.prefix}.html" class="text-decoration-none">
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


class SkillPage:
    def __init__(
        self,
        title: str,
        colorSet: Tuple,  # ThemeColor
        prefix: str,
        cover: str = "/assets/MetaTagCover.png",
        description: Optional[ListStr] = None,
        skill_group: Optional[List[SkillsGroup]] = None,
        projects: Optional[List[ProjectPage]] = None,
    ):
        self.title = title
        self.colorSet = colorSet
        self.prefix = prefix
        self.cover = cover
        self.description = description
        self.skill_group = skill_group or []
        self.projects = projects or []

    def __str__(self):

        head_html = str(
            Head(
                title=self.title,
                description=f"{self.title} 的技能介紹頁面。",
                cover=self.cover,
                link="/skills/" + self.prefix,
                colorSet=self.colorSet,
            )
        )

        navbar_html = str(Navbar(path="project"))

        skill_tools_html = ""
        if self.skill_group:
            skill_tools_html += """
<style>
.skill-card .card-footer {
    opacity: 0;
    max-height: 0;
    overflow: hidden;
    padding: 0;
    transition: opacity 0.3s ease, max-height 0.3s ease;
}

.skill-card:hover .card-footer {
    opacity: 1;
    padding: 0.5rem 1rem;
    max-height: 100px;
}
</style>
"""
            for group in self.skill_group:
                skill_tools_html += """<div class="row g-3">"""
                skill_tools_html += f"""\
<div class="col-12 px-3">
    <p class="fs-5 m-0">
        <i class="bi {group.icon} me-2"></i> {group.title}   
    </p>
</div>    
"""
                for item in group.children:
                    skill_tools_html += f"""\
<div class="col-12 col-md-6 col-lg-4 d-flex align-items-stretch skill-card">
    <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
        <div class="card-body d-inline-flex align-items-center">
            <div class="d-inline-block">
                <div style="width: 40px; height: 40px;" class="">
                    <img src="{item.icon}" class="img-fluid p-1" alt="{item.title} Icon">
                </div>
            </div>
            <div class="ps-3 d-inline-flex flex-column">
                <p class="p-0 m-0 fw-bold">{item.title}</p>
            </div>
        </div>
        <div class="card-footer bg-transparent">
            <p class="p-0 m-0">{str(item.description)}</p>
        </div>
    </div>
</div>
"""
                skill_tools_html += """</div>"""

        skill_card = str(Card(body=[Html(skill_tools_html)], body_gap_size="large"))

        project_html = ""
        if self.projects:
            project_html += """

        <div class="row">
            <div class="col-12"><h3 class="pb-2 px-2">作品集</h3></div>
        </div>
        <div class="row d-flex align-items-stretch g-2">
"""
            for project in self.projects:
                project_html += convert_project(project)

            project_html += """
        </div>
    """

        return f"""
<!doctype html>
<html lang="zh-Hant-TW">
{head_html}
<body class="bg-mytheme">
    {navbar_html}
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
    
    <div>
        <div class="position-relative"
            style="padding: 80px 0px;width: 100%; background: url({self.cover}); background-repeat:no-repeat;background-size:cover; background-attachment: fixed;">
            <div class="position-absolute top-0 start-0 w-100 h-100"
                style="background: linear-gradient(0deg, rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.5)); backdrop-filter: blur(40px);">
            </div>
            <div class="d-flex align-items-center pb-2 position-relative" style="width: 100%;min-height: 240px;">
                <div class="container">
                    <div class="col-12">
                        <h1 class="text-center fw-bold text-white notoFont">{self.title}</h1>
                    </div>
                </div>
            </div>
        </div>
        <div class="container pb-5" style="margin-top: -160px; min-height: 100vh;">
            <div class="row position-relative d-flex align-items-start">
                <div class="col-lg-4 col-12 pb-5 sticky-lg-top " style="padding-top: 92px;">
                    <div class="card shadow bg-body border-0 rounded-basic">
                        {str(Image(self.cover, "Cover Image"))}
                        <div class="card-body p-4">
                            <p class="fw-bold m-0 pb-2 fs-5 notoFont">
                                {str(self.description)}
                            </p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-8 col-12 pb-5 d-grid gap-5">
                    <div style="height: calc(92px - 3rem);" class="d-none d-lg-block"></div>
                    {skill_card}
                </div>
            </div>
            {project_html}
        </div>
    </div>

    

    {str(Footer())}
</body>

</html>
"""
