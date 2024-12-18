import csv
from time import process_time


# Aqui é uma função que eu crio o nó passando os parametros para o construtor da classe Node 
class Node:
    def __init__(self, problem, solution):
        self.problem = problem
        self.solution = solution
        self.next = None

# Aqui é uma classe de gerenecia da Lista, onde eu posso inserir, procurar e transpor para o inicio o Nó desejado
class LinkedList:
    def __init__(self):
        self.head = None

    # Método utilizado para inserir o Nó na lista, é importante observar que essa inserção só ocorre normalmente 
    # no início da execução do programa, mas pode ser utilizado em momentos posteriores
    def insert(self, problem, solution):
        new_node = Node(problem, solution)
        new_node.next = self.head
        self.head = new_node

    # Neste método eu utilizo uma busca linear para buscar o problema do sudoku desejado e transporto ele para o início da lista
    def search_and_transpose(self, problem):
        # Verifico se o no que eu procuro está na primeira posição (cabeça)
        if self.head:
            if self.head.problem == problem:
             return self.head
            
            # Inicio as variáveis anterior e atual com os respectivos nós
            prev = None
            current = self.head

            # Executo meu loop para percorrer a lista e encontrar o problema desejado
            while current and current.problem != problem:
                prev = current
                current = current.next

            if not current:  # Aqui eu verifico se o Nó atual não está presente na lista e retorno 'None'
                return None

            # Aqui é realizada a transposição do no atual para a primeira posição da lista e realizado o retorno do Nó
            if prev:
                prev.next = current.next
                current.next = self.head
                self.head = current
                return current

            
        else:
            print("Lista Vazia")
            return None


       
"""  # Método para exibir os primeiros 10 elementos (opcional, para depuração)
    def display(self):
        current = self.head
        count = 0
        while current and count < 10:  # Limitar a exibição para os primeiros 10 elementos
            print(f"Problem: {current.problem}, Solution: {current.solution}")
            current = current.next
            count += 1
"""

def main():
    # Inicializar a lista encadeada
    linked_list = LinkedList()

    # Contador para acompanhar inserções
    counter = 0

    # Medir o tempo de CPU para carregar os dados
    start_time = process_time()

    # Ler o arquivo CSV
    with open('data\\sudoku.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            problem, solution = row[0], row[1]
            linked_list.insert(problem, solution)  # Inserir na cabeça

            # Incrementar o contador
            counter += 1

            # Imprimir "1 milhão" a cada 1 milhão de inserções
            if counter % 1_000_000 == 0:
                print(f"\n{counter} inserções concluídas!")

    end_time = process_time()

    # Mostrar o tempo total de carregamento
    print(f"\n\nTempo de CPU para carregar a lista encadeada: {end_time - start_time:.6f} segundos")

    def processamento():
        # Iniciar o contador de tempo de CPU para a busca
        search_start_time = process_time()

        result = linked_list.search_and_transpose(search_problem)

        # Parar o contador de tempo de CPU para a busca
        search_end_time = process_time()

        if result:
            print(f"\nProblema encontrado e movido para o início:\nProblem: {result.problem} \nSolution: {result.solution}")
        else:
            print("\nProblema não encontrado.")

        # Mostrar o tempo de execução da busca
        print(f"\nTempo de CPU para busca e transposição: {search_end_time - search_start_time:.7f} segundos")
 
    while True:
        search_problem = input("Digite o problema a ser buscado ou (0) para sair: ")
        if not search_problem.isdigit():
            print("Erro: O problema deve conter apenas números. Tente novamente.")
            continue
        if search_problem == '0':
            print("Saindo...")
            break
        else:
            processamento()
            

      

if __name__ == "__main__":
    main()
