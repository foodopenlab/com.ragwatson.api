from typing import List
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field


from titanic.app.james_controller import JamesController
from doro.app.doro_director import DoroDirector


app = FastAPI(title="Foodopenlab Main Page ")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)   

    
@app.get("/")
def read_root():
    return {"message": "FAST API 메인 페이지", "docs": "/docs"}


@app.get("/titanic/data")
def read_titanic_data():
    james = JamesController()
    return james.get_data().to_dict(orient="records")


@app.get("/titanic/count")
def read_titanic_count():
    james = JamesController()
    return james.get_count().to_dict(orient="records")


@app.get("/titanic/model")
def read_titanic_model():
    controller= JamesController()
    model_name = controller.get_model_name_and_accuracy()
    return JSONResponse(content=jsonable_encoder(model_name))   


@app.get("/titanic/tree")
def read_titanic_tree():
    james = JamesController()
    return {"has_decision_tree_model": james.has_decision_tree_model()}


@app.get("/doro/data")
def read_doro_data():
    return DoroDirector().get_data().to_dict(orient="records")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
