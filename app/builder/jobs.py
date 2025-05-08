from app.builder.basic import WebBuilder
from app.pages.job import (
    y2024_SolwenAi,
    y2023_Tiic,
    y2022_NthuIlst,
    y2023_NthuIr,
    y2022_Songla,
    y2019_CycuEdu,
)

jobBuilder = WebBuilder("jobs/")

jobBuilder.addPages(
    [
        y2024_SolwenAi.page,
        y2023_Tiic.page,
        y2023_NthuIr.page,
        y2022_NthuIlst.page,
        y2022_Songla.page,
        y2019_CycuEdu.page,
    ]
)
