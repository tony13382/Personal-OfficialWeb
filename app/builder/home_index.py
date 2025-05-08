from app.layouts.home import full_html


def build():
    with open(f"index.html", "w", encoding="utf-8") as f:
        f.write(full_html)
        print("Output to html Successful. File: index.html")
