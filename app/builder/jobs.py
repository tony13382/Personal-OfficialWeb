from app.builder.basic import WebBuilder
from app.pages.job import allJobs

jobBuilder = WebBuilder("jobs/")

jobBuilder.addPages(allJobs)
