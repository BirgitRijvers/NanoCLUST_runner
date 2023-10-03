from itertools import permutations
from subprocess import run



reads_path = ""
db = ""
taxdb = ""
nf_path = ""

params = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 400, 600, 800, 1000]
perms = permutations(params, 2)

for perm in list(perms):
    u, c = perm
    command = f"nextflow run {nf_path} -profile docker --reads {reads_path} -db {db} --taxdb {taxdb} --outdir results/U_{u}k_C_{c} --umap_set_size {u*1000} --min_cluster_size {c} --polishing_reads {c}"
    run(command)
