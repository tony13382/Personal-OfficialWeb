from app.builder.basic import WebBuilder
from app.pages.project import allProjects

projectBuilder = WebBuilder("projects/")

projectBuilder.addPages(allProjects)
