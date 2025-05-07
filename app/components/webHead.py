from typing import Tuple

from app.variables import ThemeColor


class Head:
    def __init__(
        self,
        title: str = "",
        description: str = "",
        cover: str = "/assets/MetaTagCover.png",
        link: str = "/",
        colorSet: Tuple = ThemeColor().natural,
    ):
        self.title = title
        self.description = description
        self.cover = cover
        self.link = link
        self.colorSet = colorSet

    def __str__(self):
        theme_color, second_color = self.colorSet
        return f"""
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="Description" CONTENT="{self.description}">
    <!-- Facebook Opengraph -->
    <meta property="og:url" content="{self.link}" />
    <meta property="og:type" content="website" />
    <meta property="og:title" content="{self.title}" />
    <meta property="og:description" content="{self.description}" />
    <meta property="og:image" content="{self.cover}" />
    <meta property="og:image:alt" content="{self.title}" />
    <meta property="og:image:type" content="{self.cover}" />
    <meta property="og:image:width" content="1200px" />
    <meta property="og:image:height" content="630px" />
    <!-- End Facebook Opengraph -->
    <title>{self.title}・呂亮進</title>
    <link rel="Shortcut Icon" type="image/x-icon" href="/favicon.png" />

    <!-- Self CSS -->
    <link rel="stylesheet" href="/assets/stylesheets/myself.css">
    <link rel="stylesheet" href="/assets/stylesheets/all.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" />
    <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css"
        integrity="sha384-AYmEC3Yw5cVb3ZcuHtOA93w35dYTsvhLPVnYs9eStHfGJvOvKxVfELGroGkvsg+p" crossorigin="anonymous" />
    <!-- End of Self CSS -->
    <!-- Fancyapp (Image Box)-->
    <!-- CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fancyapps/ui@4/dist/fancybox.css" />
    <!-- JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/@fancyapps/ui@4/dist/fancybox.umd.js"></script>
    <!-- End of Fancyapp (Image Box)-->
    <style>
        :root {{
            --themeColor: {theme_color};
            --secondColor: {second_color};
        }}

        .bg-mytheme {{
            background: {second_color}15;
            color: {second_color};
        }}
        

        .text-theme {{
            color: var(--themeColor);
        }}
        .text-secondTheme {{
            color: var(--secondColor);
        }}

        .text-highlight {{
            color: var(--themeColor);
            margin: 0 2px;
            padding: 0 4px;
            font-weight: 800;
            background: linear-gradient(to top, {theme_color}40 30%, transparent 30%);
            background-position: bottom;
            background-repeat: no-repeat;
            background-size: 100% 100%; /* 使背景覆蓋文字 */
        }}
        .grayBlockHover {{
            text-decoration: none;
            color: #1f1f1f;
        }}

        .grayBlockHover:hover {{
            text-decoration: none;
            color: #1f1f1f;
            background-color: #f0f0f0;
        }}
        
    </style>
    <style>
        .carousel__nav .carousel__button {{
            background-color: #FFFFFF;
            box-shadow: 0 6px 12px -2px rgb(50 50 93 / 25%), 0 3px 7px -3px rgb(0 0 0 / 30%);
        }}

        .carousel__nav .carousel__button:hover {{
            background-color: #f9f9f9;
            box-shadow: 0 6px 12px -2px rgb(50 50 93 / 25%), 0 3px 7px -3px rgb(0 0 0 / 30%);
        }}
    </style>
</head>
        """
