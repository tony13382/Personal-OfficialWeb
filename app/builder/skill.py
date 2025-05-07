from app.builder.basic import WebBuilder
from app.pages.skill.develope import page as develope
from app.pages.skill.design import page as design
from app.pages.skill.plan import page as plan
from app.pages.skill.other import page as other

skillBuilder = WebBuilder("skills/")

skillBuilder.addPages(
    [
        develope,
        design,
        plan,
        other,
    ]
)
