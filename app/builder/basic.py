import os
from typing import List, Any


class WebBuilder:
    def __init__(self, path: str) -> None:
        self.path = path
        self.pages = []
        # 确保目录存在
        os.makedirs(path, exist_ok=True)

    def addPage(self, newPage: Any):
        self.pages.append(newPage)

    def addPages(self, newPages: List[Any]):
        self.pages.extend(newPages)

    def getPages(self):
        return self.pages

    def build(self):
        for page in self.pages:
            file_path = self.path + f"{page.prefix}.html"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(str(page))
                print(f"Output to html Successful. File: {file_path}")
