from typing import Optional
from pydantic import UUID4, BaseModel, constr

from datetime import date


class PessoaSchema(BaseModel):
    id: Optional[UUID4] = None
    apelido: constr(max_length=32)
    nome: constr(max_length=100)
    nascimento: date
    stack: Optional[list[constr(max_length=32)]] = None
