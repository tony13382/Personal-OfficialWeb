from app.builder.jobs import jobBuilder
from app.builder.projects import projectBuilder
from app.builder.skill import skillBuilder
import app.builder.home as homeBuilder
import app.builder.projects_home as projects_homeBuilder

projectBuilder.build()
jobBuilder.build()
skillBuilder.build()
homeBuilder.build()
projects_homeBuilder.build()
