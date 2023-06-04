from django.urls import path
from escola.views import ListaMatriculasAluno, ListaAlunosMatriculados

urlpatterns = [
    path('aluno/<int:pk>/matriculas', ListaMatriculasAluno.as_view(),
         name="lista_matriculas_aluno"),
    path('curso/<int:pk>/matriculas', ListaAlunosMatriculados.as_view(),
         name='lista_alunos_matriculados_curso')
]
