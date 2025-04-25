import os
import sys


def get_resource_path(relative_path):
   try:
      base_path = sys._MEIPASS
   except Exception:
      base_path = os.path.abspath(".")
   return os.path.join(base_path, relative_path)

IMG = {
    'aceitar': get_resource_path('img/aceitar.png'),
    'login': get_resource_path('img/login.png'),
    'senha': get_resource_path('img/senha.png'),
    'acessar': get_resource_path('img/acessar.png'),
    'calendario': get_resource_path('img/calendario.png'),
    'calendario2': get_resource_path('img/calendario2.png'),
    'avancar': get_resource_path('img/avancar.png'),
    'tipo': get_resource_path('img/tipo.png'),
    'procontribanco': get_resource_path('img/procontribanco.png'),
    'pendente': get_resource_path('img/pendente.png'),
    'compromisso': get_resource_path('img/compromisso.png'),
    'nenhum': get_resource_path('img/nenhum.png'),
    'subtipo': get_resource_path('img/subtipo.png'),
    'defesaprocon': get_resource_path('img/DEFESAPROCON.png'),
    '3pontos': get_resource_path('img/3pontos.png'),
    'editar': get_resource_path('img/editar.png'),
    'atrasada': get_resource_path('img/atrasada.png'),
    'atrasado': get_resource_path('img/atrasado.png'),
    'vencido': get_resource_path('img/vencido.png'),
    'subatrasado': get_resource_path('img/subatrasado.png'),
    'salvar': get_resource_path('img/salvar.png'),
    'prazo': get_resource_path('img/prazo.png'),
    'atrasadoprocon': get_resource_path('img/atrasadoprocon.png'),

}


POSITION = {
    'pesquisar': (620, 378),
    'cookie': (1767, 972),
    'data1': (219, 477),
    'data2': (186, 536),
    'clique': (672, 627),
    'adiantar': (726, 603),
    'trocar': (905, 408)
}
