from tasks.schemas.task_schema import TaskCreate, TaskUpdate
from tasks.services import task_service


def carregar_tarefas_do_usuario(user_id: str):
    return task_service.listar_tarefas(user_id)


def criar_tarefa(data, descricao, is_finished, user_id):
    nova = TaskCreate(
        date=data,
        task=descricao,
        is_finished=is_finished,
        user_id=user_id
    )
    return task_service.criar_tarefa(nova)


def salvar_edicao(task_id, data, descricao, is_finished):
    atualizada = TaskUpdate(
        date=data,
        task=descricao,
        is_finished=is_finished
    )
    return task_service.atualizar_tarefa(task_id, atualizada)


def excluir_tarefa(task_id):
    return task_service.excluir_tarefa(task_id)
