from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from api.providers.page import (
    PageProvider,
    ExplorePageData,
    ExplorePageDataItem,
)


router = APIRouter(prefix="/explore", tags=["explore"])


page_provider = PageProvider()


@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):

    # pretend we got these ids from reading S3
    datasets = [1, 2, 3, 4, 5]

    data = ExplorePageData(
        title="datasets",
        items=[ExplorePageDataItem(name=ds, url=f"datasets/{ds}") for ds in datasets],
    )

    return page_provider.render_explore_page(request=request, data=data)


@router.get("/datasets/{dataset_id}", response_class=HTMLResponse)
async def read_item(request: Request, dataset_id: str):

    # pretend we got these ids from reading S3
    dataset_objects = [10, 11, 12, 13, 14]

    data = ExplorePageData(
        title="dataset_objects",
        items=[
            ExplorePageDataItem(name=dso, url=f"{dataset_id}/dataset_objects/{dso}")
            for dso in dataset_objects
        ],
    )

    return page_provider.render_explore_page(request=request, data=data)


@router.get(
    "/datasets/{dataset_id}/dataset_objects/{dataset_object_id}",
    response_class=HTMLResponse,
)
async def read_item(request: Request, dataset_id: str, dataset_object_id: str):

    # pretend we got these file names from reading S3
    files = ["summary.html", "frequency.html"]

    data = ExplorePageData(
        title="files",
        items=[
            ExplorePageDataItem(name=f, url=f"{dataset_object_id}/files/{f}")
            for f in files
        ],
    )

    return page_provider.render_explore_page(request=request, data=data)
