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
        "slug": "marketing-research-with-ai",
        "title": "Marketing Research with AI",
        "content": "An AI powered webapp that can research marketing tactics and give you a summary of the results as well as a plan to implement.",
        "image": "icons/projects/mkt.png",
        "link": "https://github.com/piercebnance/Marketing-Trends-AI-Webapp-Tool",
        "link_label": "View on GitHub",
    },
    {
        "id": 2,
        "slug": "amazon-web-scraper",
        "title": "Amazon Web Scraper",
        "content": "A web scraper built with Python, BeautifulSoup, and ScrapingBee to extract products with discounts from Amazon.",
        "image": "icons/projects/web_scrape.png",
        "link": "https://thewonderscraper.com",
        "link_label": "View on Website",
    },
    {
        "id": 3,
        "slug": "cleanup-of-a-large-dataset",
        "title": "Cleanup of a Large Dataset",
        "content": "Project where I cleaned up and optimized a large dataset of 2400+ entries. I also performed data normalization and standardization.",
        "image": "icons/projects/db_stock.png",
        "link": "https://github.com/piercebnance/data-analyst-project---cleaning-and-exploring-a-dataset",
        "link_label": "View on GitHub",
    },
    #{
        #"id": 4,
        #"slug": "my-personal-website",
        #"title": "My Personal Website",
        #"content": "My own website! I built this from the ground up with FastAPI, Bootstrap, and Python.",
        #"image": "icons/projects/website.png",
        #"link": "https://github.com/piercedev",
        #"link_label": "View on GitHub",
    #},
    #{
        #"id": 4,
        #"slug": "mental-health-detection-using-machine-learning",
        #"title": "Mental Health Detection using Machine Learning",
        #"content": "A machine learning project aimed at detecting signs of mental health issues through analysis of user data and behavior patterns.",
        #"link": "https://github.com/piercedev",
        #"link_label": "View on GitHub",
    #}
]


@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {"posts": project_posts, "title": "Home"},
    )


@app.get("/projects", include_in_schema=False, name="projects")
def projects(request: Request):
    return templates.TemplateResponse(
        request,
        #"projects.html",
        {"posts": project_posts, "title": "Projects"},
    )


@app.get("/api/posts")
def get_posts():
    return project_posts