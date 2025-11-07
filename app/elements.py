from pydantic import BaseModel
from typing import Any, List, Literal, Union
from uuid import uuid4
from app.variables import GapClass, GapSet, SpaceSet


def string_formator(text: str):
    # return text
    parts = text.split("`")
    result = ""
    for i, part in enumerate(parts):
        if i % 2 == 0:
            result += part
        else:
            result += f'<span class="text-highlight">{part}</span>'
    # 如果原本字串最後是 ` 結尾，會多一個空的 part，這邊不用特別處理
    return result


class Element:
    """Base class for elements."""

    pass


class Canva(Element):
    def __init__(self, src: str = ""):
        # 如果最後是 `/view` 則填充成 `/view?embed`，如果最後是 `/view?embed` 則不修改
        if src.endswith("/view"):
            self.src = src + "?embed"
        else:
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


class Card(Element):
    def __init__(
        self,
        header=None,
        body: list = None,
        footer: list = None,
        body_gap: GapSet = None,
        footer_gap: GapSet = None,
        has_shadow: bool = True,
        space: SpaceSet = None,
    ):
        self.header = header
        self.body = [] if body is None else body
        self.footer = [] if footer is None else footer

        if body_gap is None:
            self.body_gap = GapSet("regular")
        else:
            self.body_gap = body_gap

        self.footer_gap = footer_gap
        if space is None:
            self.space = SpaceSet("regular")
        else:
            self.space = space
        self.has_shadow = has_shadow
        self.space = space

    def __str__(self):
        header_html = ""
        if self.header:
            header_html += "<div>"
            header_html += str(self.header)
            header_html += "</div>"

        body_html = ""
        if self.body:
            body_html += f"""<div class="card-body"><div class="p-2 d-grid {str(self.body_gap)}">"""
            for item in self.body:
                body_html += str(item)
            body_html += """</div></div>"""

        footer_html = ""
        if self.footer:
            footer_html += f"""<div class="card-footer bg-transparent"><div class="p-2 d-grid {str(self.footer_gap)}">"""
            for item in self.footer:
                footer_html += str(item)
            footer_html += """</div></div>"""

        shadow_class = "shadow" if self.has_shadow else ""
        return f"""
<div class="card {shadow_class} {str(self.space)} rounded-basic border-0">
    {header_html}
    {body_html}
    {footer_html}
</div>
"""


class AccordionItem(BaseModel):
    model_config = {"arbitrary_types_allowed": True}
    title: str
    items: List[Element]
    expanded: bool = False
    body_space: SpaceSet = None


class AccordionBlock(Element):
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

            gap_class = "" if item.body_space is None else str(item.body_space)

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
        <div class="accordion-body {gap_class}"">
            {tab_content}
        </div>
    </div>
</div>
"""

        accordion_html += """</div>"""
        return accordion_html


class Columns(Element):
    def __init__(
        self, gap_size: int = 0, cols_of_row: int = 0, children: List[Any] = None
    ):
        self.gap_size = gap_size
        self.cols_of_row = cols_of_row
        self.children = children if children is not None else []
        self.min_cols = 12
        self.sm_cols = 12 // self.cols_of_row if self.cols_of_row > 0 else 12
        self.md_cols = 12 // self.cols_of_row if self.cols_of_row > 0 else 12
        self.lg_cols = 12 // self.cols_of_row if self.cols_of_row > 0 else 12
        self.xl_cols = 12 // self.cols_of_row if self.cols_of_row > 0 else 12
        self.xxl_cols = 12 // self.cols_of_row if self.cols_of_row > 0 else 12

    def __str__(self) -> str:
        col_class = f"col-{self.min_cols} col-sm-{self.sm_cols} col-md-{self.md_cols} col-lg-{self.lg_cols} col-xl-{self.xl_cols} col-xxl-{self.xxl_cols}"
        html = ""
        if self.children:
            html += f"""<div class="row g-{self.gap_size}">"""
            for item in self.children:
                if self.cols_of_row > 0:
                    col_class = f"{col_class}"
                else:
                    col_class = "col-12"
                html += f"""<div class="{col_class}">{str(item)}</div>"""
            html += "</div>"
        return html


class Div(Element):
    def __init__(
        self,
        child,
        mt: int = None,
        mb: int = None,
        ms: int = None,
        me: int = None,
    ) -> None:
        self.child = child
        self.mt = mt
        self.mb = mb
        self.ms = ms
        self.me = me

    def __str__(self) -> str:
        margin_class = ""
        margin_class += f"mt-{self.mt} " if self.mt else ""
        margin_class += f"mb-{self.mb} " if self.mb else ""
        margin_class += f"ms-{self.ms} " if self.ms else ""
        margin_class += f"me-{self.me} " if self.me else ""

        return f"""
<div class="{margin_class}">
    {self.child}
</div>
"""


class DivBar(Element):
    def __init__(
        self,
        space: Literal["nano", "mini", "regular", "wide"] = "regular",
        opacity: float = 0.15,
    ):
        self.space = space
        self.opacity = opacity

    def __str__(self):
        margin_class = {
            "nano": "my-0",
            "mini": "my-1",
            "regular": "my-2",
            "wide": "my-3",
        }

        return f"""
<hr class="{margin_class[self.space]}" style="opacity:{self.opacity}">
"""


class Html(Element):
    def __init__(self, code: str):
        self.code = code

    def __str__(self):
        return self.code


class HtmlCarousel(Element):
    def __init__(self, blocks: Union[List[str], List[Any]]):
        self.blocks = blocks

    def __str__(self) -> str:
        random_id = f"c{uuid4().hex[0:6]}"
        index_id = 0
        blocksLen = len(self.blocks)

        carousel_html = ""
        for block in self.blocks:
            if index_id == 0:
                carousel_html += f"""
<div class="carousel__slide is-selected" data-index="{index_id}">
    {str(block)}
</div>
                """
            else:
                carousel_html += f"""
<div class="carousel__slide" data-index="{index_id}" aria-hidden="true">
    {block}
</div>
"""

            index_id += 1

        ol_html = """<ol class="carousel__dots">"""
        for i in range(blocksLen):
            if i == 0:
                ol_html += f"""<li class="carousel__dot is-selected" data-page="{i}" role="button" tabindex="0" title="Go to slide #{i + 1}"></li>"""
            else:
                ol_html += f"""<li class="carousel__dot" data-page="{i}" role="button" tabindex="0" title="Go to slide #{i + 1}"></li>"""
        ol_html = """</ol>"""
        script_html = f"""
<script>
    const uiCarousel_{random_id} = new Carousel(document.querySelector("#uiCarouse_{random_id}"), {{
        // 配置選項
        autoplay: true,
        autoplaySpeed: 1000, // 每張圖片展示 1000 毫秒，即 1 秒
        infinite: true
    }});
</script>
"""

        return f"""
<div id="uiCarouse_{random_id}" class="carousel has-dots is-draggable mt-3 mb-5">
    <div class="carousel__viewport">
        <div class="carousel__track" style="transform: translate3d(171px, 0px, 0px) scale(1);">
        {carousel_html}
        </div>
    </div>
    <div class="carousel__nav"><button title="Next slide" class="carousel__button is-next" tabindex="0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" tabindex="-1"><path d="M9 3l9 9-9 9"></path></svg></button><button title="Previous slide" class="carousel__button is-prev" tabindex="0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" tabindex="-1"><path d="M15 3l-9 9 9 9"></path></svg></button></div>
</div>
{script_html}
"""


class IconBlock(Element):
    def __init__(
        self,
        title: str = None,
        subtitle: str = None,
        src: str = "",
        icon: str = "bi-file-earmark-arrow-down",
    ) -> None:
        self.src = src
        self.icon = icon
        self.title = title
        self.subtitle = subtitle

    def __str__(self) -> str:
        title_html = ""
        if self.title:
            title_html = (
                f"""<p class="m-0 fw-bold">{string_formator(self.title)}</p>"""
                if self.title
                else ""
            )
        subtitle_html = ""
        if self.subtitle:
            subtitle_html = (
                f"""<p class="m-0 opacity-50">{string_formator(self.subtitle)}</p>"""
                if self.subtitle
                else ""
            )
        link_h_start = ""
        link_h_end = ""
        fileLink_css = ""
        if self.src != "":
            link_h_start = f"""<a href="{self.src}" type="button" target="_blank" class="text-decoration-none">"""
            link_h_end = "</a>"
            fileLink_css = "file-links"
        # RETURN HTML
        return f"""
{link_h_start}
    <div class="card rounded-inline-basic {fileLink_css}">
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
{link_h_end}
"""


class Image(Element):
    def __init__(
        self,
        src: str,
        alt: str = "",
        allow_pop: bool = False,
        max_width: int = None,
        rounded: bool = False,
    ):
        self.src = src
        self.alt = alt
        self.allow_pop = allow_pop
        self.max_width = max_width
        self.rounded = rounded

    def __str__(self):
        max_width_style = ""
        if self.max_width:
            max_width_style = f"""style="width:100%; max-width: {self.max_width}px;" """
        rounded_class = "rounded-inline-basic" if self.rounded else ""
        if self.allow_pop:
            return f"""
<a href="{self.src}" data-fancybox="gallery" class="mx-auto {rounded_class}">
    <img src="{self.src}" class="img-fluid mx-auto" alt="{self.alt}"  {max_width_style}>
</a>
"""
        return f"""
<div class="d-block mx-auto text-center">
    <img src="{self.src}" class="img-fluid mx-auto {rounded_class}" alt="{self.alt}" {max_width_style}>
</div>
"""


class ImageCarousel(Element):
    def __init__(self, images: List[Image]) -> None:
        self.images = images

    def __str__(self) -> str:
        random_id = f"c{uuid4().hex[0:6]}"
        index_id = 0

        inner_html = ""
        for image in self.images:
            active_class = "active" if index_id == 0 else ""
            index_id += 1
            inner_html += f"""
<div class="carousel-item {active_class}">
    <a href="{image.src}" data-fancybox="gallery">
        <img src="{image.src}" class="img-fluid" alt="{image.alt}">
    </a>
</div>
"""

        return f"""
<div id="{random_id}" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
        {inner_html}
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#{random_id}" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#{random_id}" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
    </button>
</div>
"""


class LinkButton(Element):
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


class ListStr(Element):
    def __init__(self, items: List[str]) -> None:
        self.items = items

    def __str__(self):
        return_html = """<ul class="ps-3 m-0 lh-lg">"""
        for item in self.items:
            return_html += f"""<li>{string_formator(item)}</li>"""
        return_html += """</ul>"""
        return return_html


class ListDiv(Element):
    def __init__(
        self,
        children: list = None,
        gap: SpaceSet = None,
        layout: Literal["grid", "flex", "inline"] = "grid",
        space: SpaceSet = None,
    ):
        self.children = children if children is not None else []
        self.gap = gap if gap is not None else SpaceSet("regular")
        self.layout = layout
        self.space = space if space is not None else ""

    def __str__(self) -> str:
        content_html = ""

        display_class = f"d-{self.layout}"
        if self.layout == "flex":
            display_class += " flex-wrap"
        for item in self.children:
            content_html += str(item)
        return f"""
<div class="{display_class} {str(self.gap)} {str(self.space)}">
{content_html}
</div>
"""


class Score(Element):
    def __init__(self, name: str, score: str, group: str = None):
        self.name = name
        self.group = group
        self.score = score

    def __str__(self) -> str:
        group_html = ""
        if self.group:
            group_html = f"""・<span class="d-inline-block">{self.group}</span>"""
        return f"""
<div class="row notoFont px-1">
    <div class="col-12 p-2">
        <ul class="list-group list-group-flush">
            <li class="list-group-item px-0">
                <p class="m-0 msf-info-s">{self.name}{group_html}</p>
                <p class="m-0 pt-1 fw-bold fs-4 text-theme">{self.score}</p>
            </li>
        </ul>
    </div>
</div>
"""


class TabItem(BaseModel):
    title: str
    content: str | Any


class Tab(Element):
    def __init__(self, data: List[TabItem]):
        self.data = data
        pass

    def __str__(self) -> str:
        random_id = f"c{uuid4().hex[0:6]}"
        index_id = 0
        ul_html = f"""<div class="overflow-auto"><ul class="nav nav-pills flex-nowrap" id="pills-tab-{random_id}" role="tablist" style="white-space: nowrap;">"""
        for item in self.data:
            if index_id == 0:
                ul_html += f""" 
                <li class="nav-item" role="presentation">
                    <button class="nav-link active" id="pills-{random_id}-{item.title.replace(" ", "-")}-tab" data-bs-toggle="pill" data-bs-target="#pills-{random_id}-{item.title.replace(" ", "-")}" type="button" role="tab" aria-controls="pills-{random_id}-{item.title.replace(" ", "-")}" aria-selected="true">{item.title}</button>
                </li>"""
            else:
                ul_html += f""" 
                <li class="nav-item" role="presentation">
                    <button class="nav-link" id="pills-{random_id}-{item.title.replace(" ", "-")}-tab" data-bs-toggle="pill" data-bs-target="#pills-{random_id}-{item.title.replace(" ", "-")}" type="button" role="tab" aria-controls="pills-{random_id}-{item.title.replace(" ", "-")}" aria-selected="false">{item.title}</button>
                </li>"""
            index_id += 1
        ul_html += """</ul></div>"""
        index_id = 0
        ul_html += f"""<div class="tab-content" id="pills-{random_id}-tabContent">"""
        for item in self.data:
            if index_id == 0:
                ul_html += f""" 
                <div class="tab-pane fade show active" id="pills-{random_id}-{item.title.replace(" ", "-")}" role="tabpanel" aria-labelledby="pills-{random_id}-{item.title.replace(" ", "-")}-tab" tabindex="0">
                    {str(item.content)}
                </div>"""
            else:
                ul_html += f""" 
                <div class="tab-pane fade" id="pills-{random_id}-{item.title.replace(" ", "-")}" role="tabpanel" aria-labelledby="pills-{random_id}-{item.title.replace(" ", "-")}-tab" tabindex="0">
                    {str(item.content)}
                </div>"""
            index_id += 1
        ul_html += """</div>"""
        return ul_html


class Text(Element):
    def __init__(
        self,
        content: str,
        fontsize: Literal["h2", "h3", "h4", "p", "span"] = "p",
        bold: bool = False,
        center: bool = False,
        pill_type: bool = False,
    ):
        self.content = content
        self.fontsize = fontsize
        self.bold = bold
        self.center = center
        self.pill_type = pill_type

    def __str__(self) -> str:
        fw_class = "fw-bold" if self.bold is True else ""
        center_class = "text-center" if self.center is True else ""

        id_code = ""
        if self.fontsize in ["h2", "h3", "h4"]:
            id_code = f"""id='{self.content.replace(" ", "_").replace("`", "")}'"""

        content_html = f"""
            <{self.fontsize} class="m-0 p-0 {fw_class} {center_class}" {id_code}>
                {string_formator(self.content)}
            </{self.fontsize}>
        """

        if self.pill_type:
            return f"""
<span class="badge bg-mytheme text-dark {fw_class} {center_class} rounded-pill overflow-hidden fs-6" {id_code}>
    {content_html}
</span>
"""
        else:
            return content_html


class Tool(Element):
    def __init__(self, name: str, action: str):
        self.name = name
        self.action = action

    def __str__(self) -> str:
        return (
            "<div class='col-12 col-sm-6'>"
            + str(
                ListDiv(
                    children=[Text(self.name, bold=True), Text(self.action)],
                    gap=SpaceSet("nano"),
                )
            )
            + "</div>"
        )


class UiImageCarousel(Element):
    def __init__(self, images: List[str]):
        self.images = images

    def __str__(self) -> str:
        random_id = f"c{uuid4().hex[0:6]}"
        index_id = 0
        imagesLen = len(self.images)

        carousel_html = ""
        for image in self.images:
            if index_id == 0:
                carousel_html += f"""
<div class="carousel__slide is-selected" data-index="{index_id}"><img data-lazy-src="{image}" data-fancybox="{image}" class="d-block w-100 rounded-inline-basic" alt="{index_id + 1}" src="{image}"></div>
                """
            else:
                carousel_html += f"""
<div class="carousel__slide" data-index="{index_id}" aria-hidden="true"><img data-lazy-src="{image}" data-fancybox="{image}" class="d-block w-100 rounded-inline-basic" alt="{index_id + 1}" src="{image}"></div>
"""

            index_id += 1

        ol_html = """<ol class="carousel__dots">"""
        for i in range(imagesLen):
            if i == 0:
                ol_html += f"""<li class="carousel__dot is-selected" data-page="{i}" role="button" tabindex="0" title="Go to slide #{i + 1}"></li>"""
            else:
                ol_html += f"""<li class="carousel__dot" data-page="{i}" role="button" tabindex="0" title="Go to slide #{i + 1}"></li>"""
        ol_html = """</ol>"""
        script_html = f"""
<script>
    const uiCarousel_{random_id} = new Carousel(document.querySelector("#uiCarouse_{random_id}"), {{
        // 配置選項
        autoplay: true,
        autoplaySpeed: 1000, // 每張圖片展示 1000 毫秒，即 1 秒
        infinite: true
    }});
</script>
"""

        return f"""
<div id="uiCarouse_{random_id}" class="carousel has-dots is-draggable mt-3 mb-5">
    <div class="carousel__viewport">
        <div class="carousel__track" style="transform: translate3d(171px, 0px, 0px) scale(1);">
        {carousel_html}
        </div>
    </div>
    <div class="carousel__nav"><button title="Next slide" class="carousel__button is-next" tabindex="0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" tabindex="-1"><path d="M9 3l9 9-9 9"></path></svg></button><button title="Previous slide" class="carousel__button is-prev" tabindex="0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" tabindex="-1"><path d="M15 3l-9 9 9 9"></path></svg></button></div>
</div>
{script_html}
"""


class Youtube(Element):
    def __init__(self, src="") -> None:
        self.src = src

    def __str__(self) -> str:
        return f"""
<div class="ratio ratio-16x9">
    <iframe width="560" height="315" src="{self.src}"
        title="YouTube video player"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen=""></iframe>
</div>
"""
