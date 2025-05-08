import os
from app.builder.jobs import jobBuilder
from app.builder.projects import projectBuilder
from app.builder.skill import skillBuilder
import app.builder.projects_index as projects_homeBuilder
import app.builder.awards as awardsBuilder

import app.builder.home_index as homeBuilder


projectBuilder.build()
jobBuilder.build()
skillBuilder.build()
projects_homeBuilder.build()
awardsBuilder.build()
homeBuilder.build()
