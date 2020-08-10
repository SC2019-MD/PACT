#$ -N Mono3D_transient_64_4
#$ -j y
#$ -pe mpi_4_tasks_per_node 4
python M3D.py
echo $NSLOTS

