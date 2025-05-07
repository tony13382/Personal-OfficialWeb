from typing import List, Optional, Tuple

from pydantic import BaseModel
from app.components.webHead import Head
from app.components.navbar import Navbar
from app.components.footer import Footer
from app.components.person_card import PersonCard, MoreModal
from app.elements import Card, DivBar, Html, ListDiv, ListStr, Text
from app.layouts.project import ProjectPage
from app.layouts.job import JobPage


class SkillItem(BaseModel):
    title: str
    description: str
    icon: str


class SkillsGroup(BaseModel):
    icon: str
    title: str
    children: List[SkillItem] = []


class Certificate(BaseModel):
    title: str
    company: str
    tags: List[str] = []


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


def convert_job(job: JobPage) -> str:
    firstColor, secondColor = job.colorSet
    return f"""
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


def convert_certificate(certificate: Certificate) -> str:
    tags = ""
    if certificate.tags:
        tags += """<div class="card-footer p-3 pb-2 pt-0 bg-white border-0"><p class="col-12 mb-0">"""
        for tag in certificate.tags:
            tags += f"""<span class="badge rounded-pill bg-mytheme text-dark p-2 me-2 overflow-hidden"># {tag}</span>"""
        tags += """</p></div>"""
    return f"""
<div class="col-12 text-black">
    <div class="card rounded-inline-basic">
        <div class="card-body">
            <div class="row">
                <div class="col">
                    <b>{certificate.title}</b>
                    <p class="mb-0">{certificate.company}</p>
                </div>
            </div>
        </div>
        {tags}
    </div>
</div>
"""


class SkillPage:
    def __init__(
        self,
        title: str,
        colorSet: Tuple,  # ThemeColor
        prefix: str,
        cover: str = "/assets/MetaTagCover.png",
        icon: str = "bi-person",
        description: Optional[ListStr] = None,
        skill_group: Optional[List[SkillsGroup]] = None,
        projects: Optional[List[ProjectPage]] = None,
        jobs: Optional[List[JobPage]] = None,
        certificate: Optional[List[Certificate]] = None,
    ):
        self.title = title
        self.colorSet = colorSet
        self.prefix = prefix
        self.cover = cover
        self.icon = icon
        self.description = description
        self.skill_group = skill_group or []
        self.projects = projects or []
        self.jobs = jobs or []
        self.certificate = certificate or []

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
<div class="col-12 col-md-6 col-lg-6 d-flex align-items-stretch skill-card">
    <div class="card d-flex mt-1 flex-fill rounded-inline-basic">
        <div class="card-body d-inline-flex align-items-center">
            <div class="d-inline-block">
                <div style="width: 40px; height: 40px;" class="">
                    <img src="{item.icon}" class="img-fluid p-1" alt="{item.title} Icon">
                </div>
            </div>
            <div class="ps-3 d-inline-flex flex-column">
                <p class="p-0 m-0 fw-bold">{item.title}</p>
                <p class="p-0 m-0">{str(item.description)}</p>
            </div>
        </div>
    </div>
</div>
"""
                skill_tools_html += """</div>"""

        skill_card = Card(
            body=[
                Text("技能組", "h3"),
                DivBar(),
                ListDiv([Html(skill_tools_html)], gap_size="large"),
            ],
        )

        projects_html = ""
        if self.projects:
            projects_html += """

        <div class="row">
            <div class="col-12"><h3 class="pb-2 px-2">相關作品</h3></div>
        </div>
        <div class="row d-flex align-items-stretch g-2">
"""
            for project in self.projects:
                projects_html += convert_project(project)

            projects_html += """
        </div>
    """

        job_html = ""
        if self.jobs:
            job_content = ""
            for job in self.jobs:
                job_content += convert_job(job)
            job_html = Card(
                body=[
                    Text("相關工作經歷", "h3"),
                    ListDiv([Html(job_content)], gap_size="large"),
                ],
                body_gap_size="large",
            )

        certificate_html = ""
        if self.certificate:
            certificate_content = ""
            for cert in self.certificate:
                certificate_content += convert_certificate(cert)
            certificate_html = Card(
                body=[
                    Text("相關證照", "h3"),
                    ListDiv([Html(certificate_content)], gap_size="large", mt=2),
                ],
            )
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
                        <h1 style="letter-spacing: 0.4em; line-height: 150%; color: #FFFFFF;" class="text-center">
                            {self.title}
                        </h1>
                    </div>
                </div>
            </div>
        </div>
        <div class="container pb-5 text-black" style="margin-top: -160px; min-height: 100vh;">
            <div class="row position-relative d-flex align-items-start">
                <div class="col-lg-3 col-12 pb-5 sticky-lg-top " style="padding-top: 92px;">
                    {str(PersonCard())}
                    <div class="card shadow bg-body border-0 rounded-basic">
                        <div class="card-body p-4">
                            {str(self.description)}
                        </div>
                    </div>
                </div>
                <div class="col-lg-9 col-12 pb-5 d-grid gap-5">
                    <div style="height: calc(92px - 3rem);" class="d-none d-lg-block"></div>
                    {str(skill_card)}
                    {job_html}
                    {certificate_html}
                </div>
            </div>
            {projects_html}
        </div>
    </div>

    

    {str(Footer())}

    {str(MoreModal())}
</body>

</html>
"""
