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
        self.purple: Tuple[str, str] = ("#303150", "#4C4E80")
        self.pink: Tuple[str, str] = ("#804C78", "#653A5E")
        self.natural: Tuple[str, str] = ("#373737", "#2B2B2B")

    def get_color(self, name: str, is_dark: bool = False) -> str:
        """获取指定名称的颜色值

        Args:
            name: 颜色名称
            is_dark: 是否获取深色版本

        Returns:
            str: 颜色值
        """
        if name == "home":
            return self.home_color[1] if is_dark else self.home_color[0]
        if name == "natural":
            return self.natural[1] if is_dark else self.natural[0]

        if name in self.__dict__:
            return self.__dict__[name][1] if is_dark else self.__dict__[name][0]

        raise ValueError(f"Unknown color name: {name}")
