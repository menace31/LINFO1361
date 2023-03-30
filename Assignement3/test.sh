#!/bin/bash

# Nombre de fois que l'on veut exécuter le programme
random_executions=1
num_executions=1
old_executions=1

rm statistique.txt
touch statistique.txt



test(){
  # Chemin du programme à exécuter
  chemin_programme="python pontu_play.py -ai0 maxime_agent -ai1 $1 -f 1 -g false"
  chemin2_programme="python pontu_play.py -ai0 $1 -ai1 maxime_agent -f 1 -g false"
  rm resultat.txt
  touch resultat.txt
  echo "combat $1 vs Maxime en cours"
  # Boucle pour exécuter le programme plusieurs fois
  start=$(date +%s.%N)
  echo "">> statistique.txt
  echo "">> statistique.txt
  for ((i=1;i<=$2;i++)); do
    echo "Exécution numéro $i"
    $chemin_programme | grep win >> resultat.txt
    $chemin2_programme | grep win >> resultat.txt
  done
  end=$(date +%s.%N)
  runtime=$(echo "$end - $start" | bc)
  runtime=$(printf "%1.0f" $runtime)
  echo "  Maxime vs $1" >> statistique.txt
  grep -o 'maxime' resultat.txt | sort | uniq -c >> statistique.txt
  grep -o $1 resultat.txt | sort | uniq -c >> statistique.txt
  echo "    Time: $runtime secondes" >> statistique.txt
  }

if [ $random_executions -gt 0 ]
then
    test "random_agent" random_executions
fi

if [ $num_executions -gt 0 ]
then
    test "basic_agent" num_executions
    test "romain_agent" num_executions
fi

if [ $old_executions -gt 0 ]
then
    test "old_maxime_agent" old_executions
fi


