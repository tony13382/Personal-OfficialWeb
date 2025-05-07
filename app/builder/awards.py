from app.layouts.awards import page


def build():
    with open(f"awards/index.html", "w", encoding="utf-8") as f:
        f.write(page)
        print("Output to html Successful. File: awards/index.html")
