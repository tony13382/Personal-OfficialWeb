from pydantic import BaseModel
from typing import Any, List, Literal
from uuid import uuid4
from app.variables import GapClass


class Canva:
    def __init__(self, src: str = ""):
        self.src = src

    def __str__(self) -> str:
        return f"""
<div
    style="position: relative; width: 100%; height: 0; padding-top: 56.2400%; padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 0em; margin-bottom: 0em; overflow: hidden; will-change: transform;">
    <iframe loading="lazy"
        style="position: absolute; width: 100%; height: calc( 100% + 1px ); top: -1px; left: 0; border: none; padding: 0;margin: 0;"
        src="{self.src}"
        allowfullscreen="allowfullscreen" allow="fullscreen">
    </iframe>
</div>
"""


class Card:
    def __init__(
        self,
        header=None,
        body: list = [],
        footer: list = [],
        body_gap_size: Literal["nano", "small", "regular", "large"] = "regular",
        footer_gap_size: Literal["nano", "small", "regular", "large"] = "regular",
    ):
        self.header = header
        self.body = body
        self.footer = footer
        self.body_gap_size = body_gap_size
        self.footer_gap_size = footer_gap_size

    def __str__(self):
        header_html = ""
        if self.header:
            header_html += "<div>"
            header_html += str(self.header)
            header_html += "</div>"

        body_html = ""
        if self.body:
            body_html += f"""<div class="card-body"><div class="p-2 d-grid {GapClass[self.body_gap_size]}">"""
            for item in self.body:
                body_html += str(item)
            body_html += """</div></div>"""

        footer_html = ""
        if self.footer:
            footer_html += f"""<div class="card-footer bg-transparent"><div class="p-2 d-grid {GapClass[self.body_gap_size]}">"""
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


class AccordionItem(BaseModel):
    title: str
    items: List[Any]
    expanded: bool = False


class AccordionBlock:
    def __init__(self, items: List[AccordionItem]):
        self.items = items

    def __str__(self) -> str:
        random_id = f"c{uuid4().hex[0:6]}"
        index_id = 0

        accordion_html = f"""<div class="accordion" id="accordion{random_id}">"""

        for item in self.items:
            index_id += 1
            # 修正條件判斷：expanded 為 True 時不應該有 collapsed 類
            expanded_class = "" if item.expanded is True else "collapsed"
            expanded_value = "true" if item.expanded is True else "false"
            show_class = "show" if item.expanded is True else ""

            tab_content = ""
            for ele in item.items:
                tab_content += str(ele)

            accordion_html += f"""
<div class="accordion-item">
    <h2 class="accordion-header">
        <button class="accordion-button {expanded_class}" type="button" 
            data-bs-toggle="collapse" data-bs-target="#{random_id}Collapse_{index_id}" 
            aria-expanded="{expanded_value}" aria-controls="{random_id}Collapse_{index_id}">
            {item.title}
        </button>
    </h2>
    <div id="{random_id}Collapse_{index_id}" 
        class="accordion-collapse collapse {show_class}">
        <div class="accordion-body">
            {tab_content}
        </div>
    </div>
</div>
"""

        accordion_html += """</div>"""
        return accordion_html


class Div:
    def __init__(
        self,
        child,
        mt: int = None,
        md: int = None,
        ms: int = None,
        me: int = None,
    ) -> None:
        self.child = child
        self.mt = mt
        self.md = md
        self.ms = ms
        self.me = me

    def __str__(self) -> str:
        margin_class = ""
        margin_class += f"mt-{self.mt} " if self.mt else ""
        margin_class += f"mt-{self.md} " if self.md else ""
        margin_class += f"mt-{self.ms} " if self.ms else ""
        margin_class += f"mt-{self.me} " if self.me else ""

        return f"""
<div class="{margin_class}">
    {self.child}
</div>
"""


class DivBar:
    def __init__(self, space: Literal["nano", "mini", "regular", "wide"] = "regular"):
        self.space = space

    def __str__(self):
        margin_class = {
            "nano": "my-0",
            "mini": "my-1",
            "regular": "my-2",
            "wide": "my-3",
        }

        return f"""
<hr class="{margin_class[self.space]}">
"""


class FileLink:
    def __init__(
        self, src="", icon="", title: str = None, subtitle: str = None
    ) -> None:
        self.src = src
        self.icon = icon
        self.title = title
        self.subtitle = subtitle

    def __str__(self) -> str:
        title_html = (
            f"""<p class="m-0 fw-bold">{self.title}</p>""" if self.title else ""
        )
        subtitle_html = (
            f"""<p class="m-0 opacity-50">{self.subtitle}</p>"""
            if self.subtitle
            else ""
        )
        return f"""
<a href="{self.src}" type="button" target="_blank" class="text-decoration-none">
    <div class="card rounded-inline-basic">
        <div class="card-body d-flex p-2 align-items-center">
            <div class="col-auto">
                <div class="d-flex align-items-center justify-content-center fs-4 rounded-inline-basic text-white" style="background-color: var(--themeColor); width:56px; height:56px;">
                <i class="bi {self.icon}"></i>
                </div>
            </div>
            <div class="col ps-3 text-dark">
                {title_html}
                {subtitle_html}
            </div>
        </div>
    </div>
</a>
"""


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


class ListDiv:
    def __init__(
        self,
        children: list = [],
        gap_size: Literal["nano", "small", "regular", "large"] = "regular",
        mt: int = None,
        md: int = None,
        ms: int = None,
        me: int = None,
    ):
        self.children = children
        self.gap_size = gap_size
        self.mt = mt
        self.md = md
        self.ms = ms
        self.me = me

    def __str__(self) -> str:
        content_html = ""

        margin_class = ""
        margin_class += f"mt-{self.mt} " if self.mt else ""
        margin_class += f"mt-{self.md} " if self.md else ""
        margin_class += f"mt-{self.ms} " if self.ms else ""
        margin_class += f"mt-{self.me} " if self.me else ""

        for item in self.children:
            content_html += str(item)
        return f"""
<div class="d-grid {GapClass[self.gap_size]} {margin_class}">
{content_html}
</div>
"""


class Score:
    def __init__(self, name: str, score: str, group: str = None):
        self.name = name
        self.group = group
        self.score = score

    def __str__(self) -> str:
        group_html = ""
        if self.group:
            group_html = f"""<span class="d-inline-block">{self.group}</span>"""
        return f"""
<div class="row notoFont px-1">
    <div class="col-12 p-2">
        <ul class="list-group list-group-flush">
            <li class="list-group-item px-0">
                <p class="m-0 msf-info-s">{self.name}・{group_html}</p>
                <p class="m-0 pt-1 fw-bold fs-4 color-mytheme">{self.score}</p>
            </li>
        </ul>
    </div>
</div>
"""


class Text:
    def __init__(
        self,
        content: str,
        fontsize: Literal["h2", "h3", "p", "span"] = "p",
        bold: bool = False,
    ):
        self.content = content
        self.fontsize = fontsize
        self.bold = bold

    def __str__(self) -> str:
        fw_class = "fw-bold" if self.bold is True else ""

        if self.fontsize == "span":
            return f"""
<span class="badge bg-mytheme text-dark {fw_class} rounded-pill overflow-hidden fs-6">{self.content}</span>
"""
        return f"""
<{self.fontsize} class="m-0 p-0 {fw_class}">
    {self.content}
</{self.fontsize}>
"""
