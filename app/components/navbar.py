from typing import Literal


class Navbar:
    def __init__(self, path: Literal["main", "project"]):
        self.path = path

    def __str__(self):
        if self.path == "main":
            return """
<!-- Google Font - Nav Logo-->
<link href="https://fonts.googleapis.com/css2?family=Playwrite+HR+Lijeva&display=swap" rel="stylesheet">
<!--Nav Style-->
<style>
    .nav .nav-item .nav-link {
        color: gray;
        font-size: calc(1.275rem);
        -webkit-appearance: none;
    }

    .nav .nav-item .nav-link:hover {
        color: var(--themeColor);
        border-width: 6px;
        border-bottom: var(--themeColor);
        border-bottom-style: solid;
    }

    .nav .nav-item .active {
        font-weight: bolder;
        border-width: 6px;
        border-bottom: black;
        border-bottom-style: solid;
        text-decoration: none;
        color: #141929;
        font-size: calc(1.275rem + 0.3vw);
        letter-spacing: 0.05em;
        -webkit-appearance: none;
    }

    .grayBlockHover {
        text-decoration: none;
        color: #1f1f1f;
    }

    .grayBlockHover:hover {
        text-decoration: none;
        color: #1f1f1f;
        background-color: #f0f0f0;
    }

    .btn-myprimary {
        background-color: var(--themeColor);
        color: #ffffff;
    }

    .btn-myprimary:hover {
        background-color: var(--secondColor);
        color: #ffffff;
    }

    .btn-outline-myprimary {
        border-color: var(--themeColor);
        color: var(--themeColor);
    }

    .btn-outline-myprimary:hover {
        border-color: var(--secondColor);
        background-color: var(--themeColor);
        color: #ffffff;
    }
    
    .navlogofont {
        font-family: "Playwrite HR Lijeva", cursive;
        font-optical-sizing: auto;
        font-weight: 400;
        font-style: normal;
    }
</style>

<nav class="navbar navbar-expand-lg navbar-light shadow p-3 fixed-top" id="nav">
    <div class="container-fluid">
        <a class="navbar-brand d-flex align-items-center flex-wrap text-white" href="/#topCover">
            <img src="/assets/file/iconDesignFile/logo.svg" class="me-3" alt="Icon of Logo" width="24px"
                height="24px"><span class="navlogofont" style="font-size: 1rem;">Liang Chin Lu</span>
        </a>
        <button class="navbar-toggler border-0 text-white" type="button" data-bs-toggle="collapse"
            data-bs-target="#navbarContentLinks" aria-controls="navbarContentLinks" aria-expanded="false"
            aria-label="Toggle navigation">
            <i class="bi bi-list-nested"></i>
        </button>
        <div class="collapse navbar-collapse" id="navbarContentLinks">
            <ul class="navbar-nav me-auto mb-lg-0 d-flex col-12 justify-content-end align-items-center">
                <li class="nav-item rounded-pill">
                    <a class="nav-link" aria-current="page" href="/projects/">所有作品</a>
                </li>
                <li class="nav-item rounded-pill">
                    <a class="nav-link" aria-current="page" href="/awards/">我的獎項</a>
                </li>
                <li class="nav-div rounded-pill">
                    <a class="nav-link text-white-50">｜</a>
                </li>
                <li class="nav-item rounded-pill">
                    <a class="nav-link" target="_blank" href="mailto:liangchinlu@gmail.com"><i class="bi bi-envelope-at-fill me-2"></i>信箱</a>
                </li>
                <li class="nav-item rounded-pill">
                    <a class="nav-link" target="_blank" href="https://www.facebook.com/tony13382/"><i class="bi bi-facebook me-2"></i>臉書</a>
                </li>
                <li class="nav-item rounded-pill">
                    <a class="nav-link" target="_blank"
                        href="https://www.linkedin.com/in/liang-chin-lu/"><i class="bi bi-linkedin me-2"></i>領英</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
"""
        elif self.path == "project":
            return """
<nav class="navbar navbar-expand-sm navbar-light shadow p-3 fixed-top" id="nav">
    <div class="container-fluid">
        <a class="navbar-brand fw-bold px-2 text-white" href="/">
            <i class="bi bi-arrow-left"></i>
        </a>
        <button class="navbar-toggler border-0 text-white" type="button" data-bs-toggle="collapse"
            data-bs-target="#navbarContentLinks" aria-controls="navbarContentLinks" aria-expanded="false"
            aria-label="Toggle navigation">
            <i class="bi bi-list-nested"></i>
        </button>
        <div class="collapse navbar-collapse" id="navbarContentLinks">
            <ul class="navbar-nav me-auto mb-lg-0 d-flex col-12 justify-content-end align-items-center">
                <li class="nav-item rounded-pill">
                    <a class="nav-link" aria-current="page" href="/">首頁</a>
                </li>
                <li class="nav-div rounded-pill">
                    <a class="nav-link text-white-50">｜</a>
                </li>
                <li class="nav-item rounded-pill">
                    <a class="nav-link" target="_blank" href="mailto:liangchinlu@gmail.com"><i class="bi bi-envelope-at-fill me-2"></i>信箱</a>
                </li>
                <li class="nav-item rounded-pill">
                    <a class="nav-link" target="_blank" href="https://www.facebook.com/tony13382/"><i class="bi bi-facebook me-2"></i>臉書</a>
                </li>
                <li class="nav-item rounded-pill">
                    <a class="nav-link" target="_blank"
                        href="https://www.linkedin.com/in/liang-chin-lu/"><i class="bi bi-linkedin me-2"></i>領英</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
"""
