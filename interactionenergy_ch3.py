# Calculate the component energy  interactions (Electrostatic and dispersion)  between Ibuprofen and the amino acids  in the active site of Cox2
# data : the crucial amino acids : Asp, Glu, Ser, Thr, Tyr, His, Leu, Phe
# Electrostatic components [-5.2, -4.8, -3.6, -2.7, -4.3, -1.9, -3.1, -4.0]
# Dispersion components [-1.5, -2.0, -0.9, -1.1, -2.3, -0.7, -1.8, -2.1]

amino_acids = ["Asp", "Glu", "Ser", "Thr", "Tyr", "His", "Leu", "Phe"] #Amino acids
electrostatic_energies = [-5.2, -4.8, -3.6, -2.7, -4.3, -1.9, -3.1, -4.0]
dispersion_energies = [-1.5, -2.0, -0.9, -1.1, -2.3, -0.7, -1.8, -2.1]

#total energy for each amino acid
total_energies = []
for i in range(len(amino_acids)):
    total_energy = electrostatic_energies[i] + dispersion_energies[i]
    total_energies.append(total_energy)
    print(f"Total interaction energy for {amino_acids[i]}: {total_energy:.2f} kcal/mol")

#total enenry
total_sum = sum(total_energies)
print(f"\nTotal sum of interaction energies: {total_sum:.2f} kcal/mol")

# average energy
average_energy = total_sum / len(amino_acids)
print(f"Average interaction energy: {average_energy:.2f} kcal/mol")
