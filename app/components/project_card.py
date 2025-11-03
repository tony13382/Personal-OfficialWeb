from app.elements import Card, DivBar, Element, Image, LinkButton, ListDiv, ListStr, Text
from app.layouts.project import ProjectPage
from app.variables import SpaceSet


class ProjectCard:
    def __init__(self, project: ProjectPage, memo: Element | None):
        self.project = project
        self.memo = memo

    def __str__(self):
        tag_array = []
        for tag in self.project.tags:
            tag_array.append(
                Text(f"# {tag}", "span", pill_type=True),
            )
        return_card = Card(
            header=Image(self.project.cover),
            body=[
                Text(self.project.title, "h4"),
                Text(f"{self.project.startdate} ~ {self.project.enddate}"),
            ],
        )
        if self.memo:
            return_card.body.extend(
                [
                    DivBar(),
                    self.memo,
                ]
            )

        if self.project.scores:
            return_card.body.append(DivBar())
            return_card.body.append(Text("獲獎記錄：", bold=True))
            score_texts = []

            for score in self.project.scores:
                group_text = ""
                if score.group:
                    group_text = f"・{score.group}"
                score_texts.append(f"{score.name}{group_text} `{score.score}`")
            return_card.body.append(ListStr(score_texts))

        return_card.body.extend(
            [
                DivBar(),
                ListDiv(
                    [LinkButton("專案網址", f"/projects/{self.project.prefix}")],
                    space=SpaceSet(mt=2),
                ),
            ],
        )

        if tag_array:
            return_card.footer = [
                ListDiv(
                    tag_array,
                    layout="flex",
                )
            ]
        return str(return_card)
