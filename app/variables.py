from typing import Literal, Tuple


class ThemeColor:
    """颜色主题类，用于管理应用的颜色方案"""

    def __init__(self):
        # 每个颜色包含 (浅色, 深色) 两个版本
        self.home_color: Tuple[str, str] = ("#7c6e69", "#49413d")
        self.red: Tuple[str, str] = ("#804C4C", "#503030")
        self.orange: Tuple[str, str] = ("#805F4C", "#503C30")
        self.yellow: Tuple[str, str] = ("#807E4C", "#6F6D42")
        self.green: Tuple[str, str] = ("#4C8077", "#30504A")
        self.blue: Tuple[str, str] = ("#4C6D80", "#304450")
        self.purple: Tuple[str, str] = ("#727196", "#555474")
        self.pink: Tuple[str, str] = ("#804C78", "#653A5E")
        self.natural: Tuple[str, str] = ("#555555", "#2B2B2B")


GapClass = {
    "nano": "gap-0",
    "small": "gap-1",
    "regular": "gap-2",
    "large": "gap-4",
}


class GapSet:
    def __init__(self, size: Literal["nano", "small", "regular", "large"] = "regular"):
        self.size = size

    def __str__(self) -> str:
        match self.size:
            case "nano":
                return "gap-0"
            case "small":
                return "gap-1"
            case "regular":
                return "gap-2"
            case "large":
                return "gap-4"


class SpaceSet:
    def __init__(
        self,
        m:int | None = None,
        mx: int | None = None,
        my: int | None = None,
        mt: int | None = None,
        mb: int | None = None,
        ms: int | None = None,
        me: int | None = None,
        p:int | None = None,
        px: int | None = None,
        py: int | None = None,
        pt: int | None = None,
        pb: int | None = None,
        ps: int | None = None,
        pe: int | None = None,
    ):
        self.m = m
        self.mx = mx
        self.my = my
        self.mt = mt
        self.mb = mb
        self.ms = ms
        self.me = me
        self.p = p
        self.px = px
        self.py = py
        self.pt = pt
        self.pb = pb
        self.ps = ps
        self.pe = pe

    def __str__(self) -> str:
        margin_class = ""
        margin_class += f"m-{self.m} " if self.m is not None else ""
        margin_class += f"mx-{self.mx} " if self.mx is not None else ""
        margin_class += f"my-{self.my} " if self.my is not None else ""
        margin_class += f"mt-{self.mt} " if self.mt is not None else ""
        margin_class += f"mb-{self.mb} " if self.mb is not None else ""
        margin_class += f"ms-{self.ms} " if self.ms is not None else ""
        margin_class += f"me-{self.me} " if self.me is not None else ""

        padding_class = ""
        padding_class += f"p-{self.p} " if self.p is not None else ""
        padding_class += f"px-{self.px} " if self.px is not None else ""
        padding_class += f"py-{self.py} " if self.py is not None else ""
        padding_class += f"pt-{self.pt} " if self.pt is not None else ""
        padding_class += f"pb-{self.pb} " if self.pb is not None else ""
        padding_class += f"ps-{self.ps} " if self.ps is not None else ""
        padding_class += f"pe-{self.pe} " if self.pe is not None else ""

        return f"{margin_class}{padding_class}".strip()
