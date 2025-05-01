from typing import Tuple


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
        self.purple: Tuple[str, str] = ("#4C4E80", "#303150")
        self.pink: Tuple[str, str] = ("#804C78", "#653A5E")
        self.natural: Tuple[str, str] = ("#555555", "#2B2B2B")


GapClass = {
    "nano": "gap-0",
    "small": "gap-1",
    "regular": "gap-2",
    "large": "gap-4",
}
