import os
from app.builder.jobs import jobBuilder
from app.builder.projects import projectBuilder
from app.builder.skill import skillBuilder
import app.builder.projects_home as projects_homeBuilder
import app.builder.awards as awardsBuilder

import app.builder.home as homeBuilder


projectBuilder.build()
jobBuilder.build()
skillBuilder.build()
os.makedirs("projects", exist_ok=True)
projects_homeBuilder.build()
os.makedirs("awards", exist_ok=True)
awardsBuilder.build()
homeBuilder.build()
