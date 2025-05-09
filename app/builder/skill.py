from app.builder.basic import WebBuilder
from app.pages.skill import allPages

skillBuilder = WebBuilder("skills/")

skillBuilder.addPages(allPages)
