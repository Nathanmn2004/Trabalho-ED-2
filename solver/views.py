import csv
import os
from django.shortcuts import render


#IMPLEMENTAÇÃO DO DICIONÁRIO
class MyDict:
    def __init__(self):
        # Inicializa as listas para armazenar chaves e valores
        self.keys = []
        self.values = []

    def __setitem__(self, key, value):
        # Adiciona uma chave e seu valor
        if key in self.keys:
            index = self.keys.index(key)
            self.values[index] = value  # Atualiza o valor se a chave já existir
        else:
            self.keys.append(key)
            self.values.append(value)

    def __getitem__(self, key):
        # Retorna o valor associado à chave
        if key in self.keys:
            index = self.keys.index(key)
            return self.values[index]
        else:
            raise KeyError(f"Chave {key} não encontrada")

    def __delitem__(self, key):
        # Deleta a chave e o valor associados
        if key in self.keys:
            index = self.keys.index(key)
            del self.keys[index]
            del self.values[index]
        else:
            raise KeyError(f"Chave {key} não encontrada")

    def __contains__(self, key):
        # Verifica se a chave está no dicionário
        return key in self.keys

    def get(self, key, default=None):
        # Retorna o valor associado à chave ou o valor padrão se não encontrado
        if key in self.keys:
            index = self.keys.index(key)
            return self.values[index]
        return default

    def __repr__(self):
        # Representação do dicionário para impressão
        return '{' + ', '.join(f'{k}: {v}' for k, v in zip(self.keys, self.values)) + '}'
#FIM DA IMPLEMENTAÇÃO DO DICIONÁRIO


# Caminho do arquivo CSV
CSV_PATH = os.path.join(os.path.dirname(__file__), 'data/sudoku.csv')

# Função para carregar a tabela de busca do CSV
def load_lookup_table():
    lookup_table = MyDict()
    try:
        with open(CSV_PATH, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 2:
                    puzzle = row[0].strip()
                    solution = row[1].strip()
                    lookup_table[puzzle] = solution
    except Exception as e:
        print(f"Erro ao carregar o CSV: {e}")
    return lookup_table

# Carrega a tabela de busca na inicialização
LOOKUP_TABLE = load_lookup_table()

# Função principal para lidar com a interface
def solve_puzzle(request):
    solution = None
    puzzle_input = None

    if request.method == 'POST':
        puzzle_input = request.POST.get('puzzle', '').strip()
        solution = LOOKUP_TABLE.get(puzzle_input, 'Não encontrada')

    return render(request, 'solver/solve.html', {
        'solution': solution,
        'puzzle_input': puzzle_input,
    })
