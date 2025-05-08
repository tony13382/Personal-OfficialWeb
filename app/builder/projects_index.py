import os
from app.layouts.projects_index import page


def build():
    os.makedirs("projects", exist_ok=True)
    with open(f"projects/index.html", "w", encoding="utf-8") as f:
        f.write(page)
        print("Output to html Successful. File: projects/index.html")
