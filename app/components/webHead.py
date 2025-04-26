class Head:
    def __init__(
        self,
        title: str = "",
        description: str = "",
        cover: str = "/assets/MetaTagCover.png",
        link: str = "/",
    ):
        self.title = title
        self.description = description
        self.cover = cover
        self.link = link

    def __str__(self):
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
            <meta property="og:image:width" content="386px" />
            <meta property="og:image:height" content="386px" />
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
        </head>
        """
