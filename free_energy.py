
# Exercise: Calculating and Analyzing Gibbs Free Energy for 12 Ligands
# The Gibbs Free Energy of 12 ligands interacting with a specific protein is given.
# The goal is to calculate the total energy, average energy, and identify the ligand with the lowest energy.

# List of ligands and their Gibbs Free Energy values
ligands = ["Ligand1", "Ligand2", "Ligand3", "Ligand4", "Ligand5", "Ligand6", 
           "Ligand7", "Ligand8", "Ligand9", "Ligand10", "Ligand11", "Ligand12"]
gibbs_energies = [-35.2, -40.1, -37.5, -33.8, -42.0, -39.3, -36.7, -31.4, -38.2, -40.7, -34.6, -39.0]

# 1. Print the list of ligands and their Gibbs Free Energy values
for i in range(len(ligands)):
    print(f"{ligands[i]}: Gibbs Free Energy = {gibbs_energies[i]} kcal/mol")

# 2. Calculate the total Gibbs Free Energy
total_energy = sum(gibbs_energies)
print(f"\nTotal Gibbs Free Energy: {total_energy} kcal/mol")

# 3. Calculate the average Gibbs Free Energy
average_energy = total_energy / len(gibbs_energies)
print(f"Average Gibbs Free Energy: {average_energy:.2f} kcal/mol")

# 4. Find the ligand with the lowest Gibbs Free Energy
min_energy = min(gibbs_energies)
min_index = gibbs_energies.index(min_energy)
print(f"Ligand with the lowest Gibbs Free Energy: {ligands[min_index]} ({min_energy} kcal/mol)")