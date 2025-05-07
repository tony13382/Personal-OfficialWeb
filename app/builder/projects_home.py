from app.layouts.projects import page


def build():
    with open(f"projects/index.html", "w", encoding="utf-8") as f:
        f.write(page)
        print("Output to html Successful. File: index.html")
