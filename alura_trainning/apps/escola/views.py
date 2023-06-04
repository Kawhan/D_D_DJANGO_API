from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer
from escola.serializer import MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosCursoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AlunosViewSet(viewsets.ModelViewSet):
    """  Exibindo todos os alunos e alunas """

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    """  Exibindo todos os cursos """

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculasViewsSet(viewsets.ModelViewSet):
    """ Exibindo todas as matriculas nos cursos """

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaMatriculasAluno(generics.ListAPIView):
    """ Listando as matriculas de um aluno ou aluna """

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaAlunosMatriculados(generics.ListAPIView):
    """ Listando os alunos e alunas matriculados em curso """

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaAlunosMatriculadosCursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
