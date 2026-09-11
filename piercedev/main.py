from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

project_posts: list[dict] = [
    {
        "id": 1,
        "title": "Marketing Research with AI",
        "content": "An AI powered webapp that can research marketing tactics and give you a summary of the results as well as a plan to implement.",
    },
    {
        "id": 2,
        "title": "Amazon Web Scraper",
        "content": "A web scraper built with Python, BeautifulSoup, and ScrapingBee to extract products with discounts from Amazon.",
    },
    {
        "id": 3,
        "title": "Cleanup of a Large Dataset",
        "content": "Intro project where I cleaned up and optimized a large dataset of 2400+ entries, removing duplicates, null values, and irrelevant data. I also performed data normalization and standardization to prepare the dataset for analysis.",
    }
]


@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {"posts": project_posts, "title": "Home"},
    )


@app.get("/api/posts")
def get_posts():
    return project_posts