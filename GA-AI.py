import random
import string

# Target yang ingin dicapai
target = "FAHRI"

# Populasi awal
initial_population = ["Futop", "Sania", "Hirup", "Horas"]

# Fungsi fitness
def fitness(individual):
    # Fitness adalah jumlah karakter yang cocok dengan target
    return sum(1 for a, b in zip(individual, target) if a == b)

# Seleksi orang tua berdasarkan fitness
def select_parents(population):
    # Pemilihan orang tua secara acak berdasarkan fitness
    parents = random.choices(population, weights=[fitness(ind) for ind in population], k=2)
    return parents

# Crossover (reproduksi)
def crossover(parents):
    # Pilih titik crossover acak
    crossover_point = random.randint(1, len(target) - 1)
    
    # Proses crossover menghasilkan dua anak
    child1 = parents[0][:crossover_point] + parents[1][crossover_point:]
    child2 = parents[1][:crossover_point] + parents[0][crossover_point:]
    return child1, child2

# Mutasi
def mutate(individual, mutation_rate):
    # Mutasi individual dengan tingkat mutasi yang ditentukan
    mutated_individual = ""
    for char in individual:
        if random.random() < mutation_rate:
            # Jika memutasi, ganti karakter dengan acak
            mutated_individual += random.choice(string.ascii_uppercase)
        else:
            mutated_individual += char
    return mutated_individual

# Algoritma genetika
generations = 100
mutation_rate = 0.1

for generation in range(generations):
    next_population = []
    for _ in range(len(initial_population) // 2):
        # Seleksi orang tua
        parents = select_parents(initial_population)
        
        # Crossover
        child1, child2 = crossover(parents)
        
        # Mutasi
        child1 = mutate(child1, mutation_rate)
        child2 = mutate(child2, mutation_rate)
        
        next_population.extend([child1, child2])

    initial_population = next_population
    best_individual = max(initial_population, key=fitness)

    print(f"Generasi {generation + 1}: {best_individual} (Fitness: {fitness(best_individual)})")

    if best_individual == target:
        print(f"Target '{target}' tercapai pada generasi ke-{generation + 1}!")
        break
