from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from utils import main_with_params
from pathlib import Path
import json
import time

app = FastAPI()

@app.get("/api/v1/vacancies")
def read_root_api(text: str, tech: str, count: int):
    if count < 1 or count > 100:
        return {"detail": "Bad Request", "error": "Count cannot be greater than 100"}
    data = main_with_params(vacancy_title=text, technology=tech, area=113, per_page=count)
    return {"vacancies": data["vacancies"], "stats": data["stats"], "vacancy_title": text, "resultID": data["resultID"]}

@app.get("/api/v1/last")
def get_last_data():
    vacancies = []
    technologies = []
    results_dir = Path("results")
    if not results_dir.exists() or not results_dir.is_dir():
        return {"vacancies": [], "technologies": []}
    for p in results_dir.iterdir():
        if p.is_file():
            latest_file = p.name
            file_path = results_dir / latest_file
            with file_path.open("r", encoding="utf-8") as f:
                content = json.loads(f.read())
                vacancy_title = content.get("vacancy_title", "").lower()
                technology_name = content.get("stats", "").get("technology", "").lower()
                if vacancy_title not in vacancies:
                    vacancies.append(vacancy_title)
                if technology_name not in technologies:
                    technologies.append(technology_name)
    return {"vacancies": vacancies, "technologies": technologies}

@app.get("/api/v1/results")
def list_results():
    results_dir = Path("results")
    if not results_dir.exists() or not results_dir.is_dir():
        return {"files": []}
    files = [p.name.split('.json')[0] for p in results_dir.iterdir() if p.is_file()]
    files.sort()
    return {"files": files}

@app.get("/api/v1/results/{filename}")
def get_result(filename: str):
    file_path = Path("results") / (filename + ".json")
    if not file_path.exists() or not file_path.is_file():
        return {"detail": "Not Found", "error": "Result does not exist"}
    with file_path.open("r", encoding="utf-8") as f:
        content = json.loads(f.read())
    return {"time": {"raw": float(filename), "formatted": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(filename)))}, "result": content}

app.mount("/", StaticFiles(directory="static",html = True), name="static")
app.mount("/results", StaticFiles(directory="results"), name="results")
