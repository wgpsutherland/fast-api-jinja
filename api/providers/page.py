from dataclasses import dataclass

from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="api/templates")


@dataclass
class ExplorePageData:
    title: str
    items: list["ExplorePageDataItem"]


@dataclass
class ExplorePageDataItem:
    name: str
    url: str


class PageProvider:
    def render_explore_page(self, request: Request, data: ExplorePageData):
        return templates.TemplateResponse(
            "explore.html",
            {"request": request, "data": data},
        )
