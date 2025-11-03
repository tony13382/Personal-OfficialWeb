from typing import List, Literal, Optional, Tuple

from app.components.webHead import Head
from app.components.navbar import Navbar
from app.components.footer import Footer
from app.elements import (
    Card,
    DivBar,
    Html,
    LinkButton,
    ListDiv,
    ListStr,
    Score,
    Image,
    Text,
    Tool,
)


class JobPage:
    def __init__(
        self,
        title: str,
        startdate: str | None,
        enddate: str | None,
        colorSet: Tuple,  # ThemeColor
        prefix: str,
        cover: str = "/assets/MetaTagCover.png",
        job_name: Optional[str] = None,
        description: Optional[ListStr] = None,
        children: Optional[List[Card]] = None,
    ):
        self.title = title
        self.startdate = startdate
        self.enddate = enddate
        self.colorSet = colorSet
        self.prefix = prefix
        self.cover = cover
        self.job_name = job_name
        self.description = description
        self.children = children or []

    def __str__(self):

        head_html = str(
            Head(
                title=self.title,
                description=self.job_name,
                cover=self.cover,
                link="/jobs/" + self.prefix,
                colorSet=self.colorSet,
            )
        )

        navbar_html = str(Navbar(path="project"))

        time_str = ""
        if self.startdate and self.enddate:
            time_str = f"{self.startdate} ~ {self.enddate}"
        elif self.startdate is None and self.enddate is None:
            time_str = "---"
        elif self.startdate:
            time_str = f"{self.startdate} ~ Present"
        elif self.enddate:
            time_str = f"~ {self.enddate}"


        items_html = ""
        for item in self.children:
            items_html += str(item)

        job_name_html = ""
        if self.job_name:
            job_name_html = f"""{self.job_name}"""

        cover_html = str(Image(self.cover, "Cover Image"))

        description_html = ""
        if self.description:
            description_html = str(Card(body=[self.description]))

        content_html = ""
        if self.children:
            for item in self.children:
                content_html = content_html + str(item) + "\n"

        f_color, s_color = self.colorSet
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
            style="padding: 80px 0px;width: 100%; background: url({self.cover}); background-repeat:no-repeat;background-size:cover; background-attachment: local;">
            <div class="position-absolute top-0 start-0 w-100 h-100"
                style="background: linear-gradient(0deg, {f_color}80, {s_color}90); backdrop-filter: blur(80px);">
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
        <div class="container" style="margin-top: -160px; min-height: 100vh;">
            <div class="row position-relative d-flex align-items-start">
                <div class="col-lg-4 col-12 pb-5 sticky-lg-top " style="padding-top: 92px;">
                    <div class="card shadow bg-body border-0 rounded-basic">
                        {cover_html}
                        <div class="card-body p-4 text-center">
                            <p class="text-center fw-bold m-0 pb-2 fs-5 notoFont">
                                {job_name_html}
                            </p>
                            {time_str}
                        </div>
                    </div>
                </div>
                <div class="col-lg-8 col-12 pb-5 d-grid gap-5">
                    <div style="height: calc(92px - 3rem);" class="d-none d-lg-block"></div>
                    {description_html}
                    {content_html}
                </div>
            </div>
        </div>

    </div>
    {str(Footer())}
</body>

</html>
"""
