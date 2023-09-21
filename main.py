from uuid import uuid4
from fastapi import FastAPI, Response, status

from schema import PessoaSchema

def app() -> FastAPI:
    app = FastAPI()

    @app.post("/pessoas", status_code=status.HTTP_201_CREATED)
    async def add(pessoa: PessoaSchema, response: Response):
        pessoa.id = uuid4()
        response.headers["Location"] = f"/pessoas/{pessoa.id}"
        return pessoa

    @app.post("/pessoas/{id}", status_code=status.HTTP_200_OK)
    async def get(id: uuid4, response: Response):
        response.headers["Location"] = f"/pessoas/{id}"
        return {"id": id}
    
    return app

if __name__ == "__main__":
    app()
