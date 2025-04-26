from typing import Literal


class Html:
    def __init__(self, code: str):
        self.code = code

    def __str__(self):
        return self.code


class Image:
    def __init__(self, src: str, alt: str = "", allow_pop: bool = False):
        self.src = src
        self.alt = alt
        self.allow_pop = allow_pop

    def __str__(self):
        if self.allow_pop:
            return f"""
<a href="{self.src}" data-fancybox="gallery">
    <img src="{self.src}" class="img-fluid" alt="{self.alt}">
</a>
"""
        return f"""
<img src="{self.src}" class="img-fluid" alt="{self.alt}">
"""


class Canva:
    def __init__(self, src: str = ""):
        self.src = src

    def __str__(self) -> str:
        return f"""
<div
    style="position: relative; width: 100%; height: 0; padding-top: 56.2400%; padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 0em; margin-bottom: 0.9em; overflow: hidden; will-change: transform;">
    <iframe loading="lazy"
        style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
        src="{self.src}"
        allowfullscreen="allowfullscreen" allow="fullscreen">
    </iframe>
</div>
"""


class Link:
    def __init__(
        self,
        content: str = "",
        href: str = "",
        fill: bool = False,
        open_in_tab: bool = False,
        icon: str = "",
    ):
        self.content = content
        self.href = href
        self.fill = fill
        self.open_in_tab = open_in_tab
        self.icon = icon

    def __str__(self) -> str:
        targetText = ""
        if self.open_in_tab is True:
            targetText = 'target="_blank"'

        fill_class = "btn-outline-theme"
        if self.fill is True:
            fill_class = "btn-theme"

        return f"""
        <a href="{self.href}" type="button" {targetText} class="btn {fill_class} rounded-pill">
            <i class="bi {self.icon} me-2"></i>{self.content}
        </a>
        """


class Card:
    def __init__(self, header=None, body: list = [], footer: list = []):
        self.header = header
        self.body = body
        self.footer = footer

    def __str__(self):
        header_html = "" if self.header is None else str(self.header)
        body_html = ""
        if self.body:
            body_html += """<div class="card-body"><div class="p-2">"""
            for item in self.body:
                body_html += str(item)
            body_html += """</div></div>"""

        footer_html = ""
        if self.footer:
            footer_html += (
                """<div class="card-footer bg-transparent"><div class="p-2">"""
            )
            for item in self.footer:
                footer_html += str(item)
            footer_html += """</div></div>"""

        return f"""
<div class="card shadow rounded-basic border-0">
    {header_html}
    {body_html}
    {footer_html}
</div>
"""


class Text:
    def __init__(self, content: str, fontsize: Literal["h2", "h3", "p"] = "p"):
        self.content = content
        self.fontsize = fontsize

    def __str__(self) -> str:
        return f"""
<{self.fontsize} class="m-0 p-0">
    {self.content}
</{self.fontsize}>
"""
