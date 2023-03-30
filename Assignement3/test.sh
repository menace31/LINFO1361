#!/bin/bash

# Nombre de fois que l'on veut exécuter le programme
num_executions=1

rm statistique.txt
touch statistique.txt




# Chemin du programme à exécuter
chemin_programme="python pontu_play.py -ai0 maxime_agent -ai1 random_agent -f 1 -g false"
chemin2_programme="python pontu_play.py -ai0 random_agent -ai1 maxime_agent -f 1 -g false"
rm resultat.txt
touch resultat.txt
echo "combat random agent vs Maxime en cours"
# Boucle pour exécuter le programme plusieurs fois
start=$(date +%s.%N)
for ((i=1;i<=2;i++)); do
  echo "Exécution numéro $i"
  $chemin_programme | grep win >> resultat.txt
  $chemin2_programme | grep win >> resultat.txt
done
end=$(date +%s.%N)
runtime=$(echo "$end - $start" | bc)
echo "  Maxime vs random agent" >> statistique.txt
echo "" >> statistique.txt
grep -o 'maxime' resultat.txt | sort | uniq -c >> statistique.txt
grep -o 'basic' resultat.txt | sort | uniq -c >> statistique.txt
echo "Time: $runtime" >> statistique.txt





# Chemin du programme à exécuter
chemin_programme="python pontu_play.py -ai0 basic_agent -ai1 maxime_agent -f 1 -g false"
chemin2_programme="python pontu_play.py -ai0 maxime_agent -ai1 basic_agent -f 1 -g false"
rm resultat.txt
touch resultat.txt
echo "combat basic agent vs Maxime en cours"
# Boucle pour exécuter le programme plusieurs fois
start=$(date +%s.%N)
for ((i=1;i<=num_executions;i++)); do
  echo "Exécution numéro $i"
  $chemin_programme | grep win >> resultat.txt
  $chemin2_programme | grep win >> resultat.txt
done
end=$(date +%s.%N)
runtime=$(echo "$end - $start" | bc)
echo -e "\n" >> statistique.txt
echo "  Maxime vs basic agent" >> statistique.txt
echo "" >> statistique.txt
grep -o 'maxime' resultat.txt | sort | uniq -c >> statistique.txt
grep -o 'basic' resultat.txt | sort | uniq -c >> statistique.txt
echo "Time: $runtime" >> statistique.txt




# Chemin du programme à exécuter
chemin_programme="python pontu_play.py -ai0 romain_agent -ai1 maxime_agent -f 1 -g false"
chemin2_programme="python pontu_play.py -ai0 maxime_agent -ai1 romain_agent -f 1 -g false"
rm resultat.txt
touch resultat.txt
echo "combat Romain vs Maxime en cours"
# Boucle pour exécuter le programme plusieurs fois
start=$(date +%s.%N)
for ((i=1;i<=num_executions;i++)); do
  echo "Exécution numéro $i"
  $chemin_programme | grep win >> resultat.txt
  $chemin2_programme | grep win >> resultat.txt
done
end=$(date +%s.%N)
runtime=$(echo "$end - $start" | bc)
echo -e "\n" >> statistique.txt
echo "  Maxime vs Romain" >> statistique.txt
echo "" >> statistique.txt
grep -o 'maxime' resultat.txt | sort | uniq -c >> statistique.txt
grep -o 'romain' resultat.txt | sort | uniq -c >> statistique.txt
echo "Time: $runtime" >> statistique.txt






rm resultat.txt
touch resultat.txt
# Chemin du programme à exécuter
chemin_programme="python pontu_play.py -ai0 old_maxime_agent -ai1 maxime_agent -f 1 -g false"
chemin2_programme="python pontu_play.py -ai0 maxime_agent -ai1 old_maxime_agent -f 1 -g false"

# Boucle pour exécuter le programme plusieurs fois
start=$(date +%s.%N)
echo "combat old Maxime vs Maxime en cours"
for ((i=1;i<=num_executions;i++)); do
  echo "Exécution numéro $i"
  $chemin_programme | grep win >> resultat.txt
  $chemin2_programme | grep win >> resultat.txt
done
end=$(date +%s.%N)
runtime=$(echo "$end - $start" | bc)
echo -e "\n" >> statistique.txt
echo "  old Maxime vs Maxime" >> statistique.txt
echo "" >> statistique.txt
grep -o '\bmaxime\b' resultat.txt | sort | uniq -c >> statistique.txt
grep -o '\bold_maxime\b' resultat.txt | sort | uniq -c >> statistique.txt
echo "Time: $runtime" >> statistique.txt