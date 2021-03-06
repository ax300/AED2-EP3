import json
import sys
import matplotlib.pyplot as plt


sys.setrecursionlimit(10000) # Aumenta o limite padrão de recursões, se não dá erro. 
population = {}
visited = []
component_size = []


def componente_conex(): # Percorre os componentes conexos
    global population, component_size, count
    
    for k, v in population.items():
        if v[0] == False:
            count = 0
            dfs(k)
            component_size.append(count)


def dfs(k): # Busca em profundidade
    global population, count
    population[k][0] = True
    count += 1
    for adjacente in population[k][1]:
        if population[adjacente][0] == False:
            dfs(adjacente)

def add_person(v_ori, v_dest): # Cria o lista de adjacencia 
    global population

    if v_ori in population: # Se o no ja existe
        if v_dest not in population[v_ori][1]:
            population[v_ori][1].append(v_dest)
    else: # Se o no eh novo
        population[v_ori] = [False, [v_dest]] # O false indica que o vértice ainda não foi visitado
    
def plot():
    x_array = []
    y_array = []
    size_components = {}

    for x in component_size: 
        if x not in size_components:      
            size_components[x] = 1
        else:
            size_components[x] += 1

    for k, v in size_components.items():
        x_array.append(k)
        y_array.append(v)

    plt.bar(x_array, y_array)
    plt.xlabel('Tamanho da componente')
    plt.ylabel('Nº de componentes')
    plt.xticks(rotation='vertical')
    plt.show()


if __name__ == "__main__":
    
    with open('cenario3.txt') as f:

        v = f.readline().replace('\n', '')
        e = f.readline().replace('\n', '')

        for l in f.readlines():
            v_ori, v_dest = l.replace('\n', '').split(' ')
            add_person(v_ori, v_dest)
            add_person(v_dest, v_ori) # Adiciona a volta também para fazer um grafo não direcionado
    
    componente_conex()
    # print(population)
    # print(component_size)
    plot()