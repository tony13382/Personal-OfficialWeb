import sys
import os

print("=== sys.path ===")
for p in sys.path:
    print(p)
print("=== app/pages/job 目錄內容 ===")
print(os.listdir("app/pages/job"))
print("=============================")

from app.builder.jobs import jobBuilder
from app.builder.projects import projectBuilder
import app.builder.home as homeBuilder

projectBuilder.build()
jobBuilder.build()
homeBuilder.build_home()
