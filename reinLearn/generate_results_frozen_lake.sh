#!/bin/bash
for f in grid_results/results_FrozenLake-v0_*; do (cat "${f}"; echo "") >> grid_results/finalResults_FrozenLake.csv; done
rm grid_results/results_FrozenLake-v0_*

sed -E -e "s/[[:blank:]]+/;/g" grid_results/finalResults_FrozenLake.csv > grid_results/finalResults_FrozenLake_final.csv
