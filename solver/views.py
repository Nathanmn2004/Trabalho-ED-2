import csv
import os
from django.shortcuts import render

# Caminho do arquivo CSV
CSV_PATH = os.path.join(os.path.dirname(__file__), 'data/sudoku.csv')

# Função para carregar a tabela de busca do CSV
def load_lookup_table():
    lookup_table = {}
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
