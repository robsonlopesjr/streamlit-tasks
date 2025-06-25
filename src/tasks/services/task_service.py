from tasks.schemas.task_schema import TaskCreate, TaskUpdate
from tasks.repositories import task_repository
from typing import List
from database.connection import SessionLocal


def listar_tarefas(usuario_id: str) -> List:
    db = SessionLocal()
    try:
        return task_repository.get_by_user(db, usuario_id)
    finally:
        db.close()


def criar_tarefa(dados: TaskCreate):
    db = SessionLocal()
    try:
        if not dados.task.strip():
            raise ValueError("A descrição da tarefa não pode estar vazia.")
        return task_repository.create(db, dados)
    finally:
        db.close()


def atualizar_tarefa(task_id: str, dados: TaskUpdate):
    db = SessionLocal()
    try:
        task = task_repository.update(db, task_id, dados)
        if not task:
            raise ValueError("Tarefa não encontrada.")
        return task
    finally:
        db.close()


def excluir_tarefa(task_id: str):
    db = SessionLocal()
    try:
        task = task_repository.delete(db, task_id)
        if not task:
            raise ValueError("Tarefa não encontrada.")
        return task
    finally:
        db.close()
