from typing import List, Literal, Optional, Tuple
from app.components.webHead import Head
from app.components.navbar import Navbar
from app.components.footer import Footer
from app.elements import Card, Link, Score, Image, Text


class ProjectPage:
    def __init__(
        self,
        title: str,
        startdate: str,
        enddate: str,
        status: Literal["running", "closed"],
        colorSet: Tuple,  # ThemeColor
        prefix: str,
        cover: str = "/assets/MetaTagCover.png",
        description: Optional[str] = None,
        subdescription: Optional[str] = None,
        tags: Optional[List[str]] = None,
        description_links: Optional[List[Link]] = None,
        scores: Optional[List[Score]] = None,
        children: Optional[List[Card]] = None,
    ):
        self.title = title
        self.startdate = startdate
        self.enddate = enddate
        self.status = status
        self.colorSet = colorSet
        self.prefix = prefix
        self.cover = cover
        self.description = description
        self.subdescription = subdescription
        self.tags = tags or []
        self.desc_links = description_links or []
        self.scores = scores or []
        self.children = children or []

    def __str__(self):

        head_html = str(
            Head(
                title=self.title,
                description=self.description,
                cover=self.cover,
                link="/projects/" + self.prefix,
            )
        )

        theme_color, second_color = self.colorSet

        navbar_html = str(Navbar(path="project"))

        items_html = ""
        for item in self.children:
            items_html += str(item)

        status_html = ""
        if self.status == "running":
            status_html = """<span class="badge bg-success rounded-pill mb-3 fs-5">專案持續維護中</span>"""
        elif self.status == "closed":
            status_html = """<span class="badge bg-secondary rounded-pill mb-3 fs-5">專案關閉</span>"""

        description_html = ""
        if self.description:
            description_html = f"""
<p class="mb-2 notoFont msf-info-s">
    {self.description}
</p>
"""

        subdesc_html = ""
        if self.subdescription:
            subdesc_html = f"""
<hr class="my-2" style="opacity:10%;">
<p class="color-mytheme fw-bold my-3">
    {self.subdescription}
</p>
"""

        tags_html = ""
        if self.tags:
            tags_html = """<hr class="my-2" style="opacity:10%;"><div class="fs-5 text-black pt-3">"""
            for tag in self.tags:
                tags_html += f"""<span class="badge bg-mytheme text-dark rounded-pill overflow-hidden me-2"># {tag}</span>"""
            tags_html += "</div>"

        desc_link_html = ""
        if self.desc_links:
            for link in self.desc_links:
                desc_link_html = desc_link_html + str(link) + "\n"

        meta_card = Card()
        if self.cover:
            meta_card.header = Image(self.cover, "Cover Image")
        if self.scores:
            meta_card.body = [
                Text("專案成就", "h3"),
            ]
            for score in self.scores:
                meta_card.body.append(
                    Score(
                        name=score.name,
                        group=score.group,
                        score=score.score,
                    )
                )

        content_html = ""
        if self.children:
            for item in self.children:
                content_html = content_html + str(item) + "\n"

        return f"""
<!doctype html>
<html lang="zh-Hant-TW">

{head_html}

<body class="bg-mytheme">
	<style>
		:root {{
			--themeColor: {theme_color};
			--secondColor: {second_color};
		}}

		.bg-mytheme {{
			color: var(--secondColor);
			position: relative;
			letter-spacing: 0.02rem;
			z-index: 10;
		}}

		.bg-mytheme::before {{
			content: "";
			position: absolute;
			top: 0;
			left: 0;
			width: 100%;
			height: 100%;
			background: var(--themeColor);
			opacity: 0.2;
			z-index: -1;
		}}

		.color-mytheme {{
			color: var(--themeColor);
		}}
	</style>
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
				style="background: linear-gradient(0deg, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.7)); backdrop-filter: blur(20px);">
			</div>
			<div class="d-flex align-items-center pb-2 position-relative" style="width: 100%;min-height: 240px;">
				<div class="container">
					<div class="col-12">
						<h1 class="text-center fw-bold text-white notoFont">{self.title}</h1>
						<p class="text-center fw-bold text-white m-0 notoFont">
                            {self.startdate} ~ {self.enddate}
                        </p>
					</div>
				</div>
			</div>
		</div>
		<div class="container" style="margin-top: -160px; min-height: 100vh;">
			<div class="row position-relative d-flex align-items-start">
				<div class="col-lg-4 col-12 pb-5 sticky-lg-top " style="padding-top: 92px;">
					<div class="card shadow p-3 bg-body rounded-basic">
						<div class="card-body">
							{status_html}
							{description_html}
							{subdesc_html}
							{tags_html}
							<div class="d-grid gap-2 mt-4">
								{desc_link_html}
							</div>

						</div>
					</div>
				</div>
				<div class="col-lg-8 col-12 pb-5 d-grid gap-5">
					<div style="height: calc(92px - 3rem);" class="d-none d-lg-block"></div>
					{str(meta_card)}
                    {content_html}
				</div>
			</div>
		</div>

	</div>
	{str(Footer())}
</body>

</html>
"""
