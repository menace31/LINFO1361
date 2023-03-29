#!/bin/bash

# Nombre de fois que l'on veut exécuter le programme
num_executions=10

rm statistique.txt
touch statistique.txt

# Chemin du programme à exécuter
chemin_programme="python pontu_play.py -ai0 romain_agent -ai1 maxime_agent -f 1 -g false"
chemin2_programme="python pontu_play.py -ai0 maxime_agent -ai1 romain_agent -f 1 -g false"
rm resultat.txt
touch resultat.txt
# Boucle pour exécuter le programme plusieurs fois
for ((i=1;i<=num_executions;i++)); do
  echo "Exécution numéro $i"
  $chemin_programme | grep win >> resultat.txt
  $chemin2_programme | grep win >> resultat.txt
done

echo "  Maxime vs Romain" >> statistique.txt
echo "" >> statistique.txt
grep -o 'maxime' resultat.txt | sort | uniq -c >> statistique.txt
grep -o 'romain' resultat.txt | sort | uniq -c >> statistique.txt