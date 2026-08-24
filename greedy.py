

c1 = [
    ("P01", "Health Check Service",        1,  6),
    ("P02", "Cache Refresh",               2, 11),
    ("P03", "Log Processing",              3, 16),
    ("P04", "Thumbnail Generation",        4, 21),
    ("P05", "Search Index Update",         5, 26),
    ("P06", "Analytics Batch",             6, 31),
    ("P07", "Recommendation Refresh",      7, 36),
    ("P08", "Video Processing",            8, 40),
    ("P09", "Database Maintenance",        9, 45),
    ("P10", "Machine Learning Inference", 10, 50)
]

c2 = [
    ("Q10", "Realtime Analytics",       10,  60),
    ("Q20", "Search Reindexing",        20, 100),
    ("Q30", "Video Transcoding",        30, 120),
    ("Q35", "Database Replication",     35, 130),
    ("Q40", "Model Inference Batch",    40, 135),
    ("Q45", "Large ETL Pipeline",       45, 140),
    ("Q50", "Database Migration",       50, 150)
]

jobs_in_order_c1 = sorted(c1,key=lambda job: (-job[3] / job[2], job[2], job[0])
)

jobs_in_order_c2 = sorted(c2, key=lambda job: (-job[3] / job[2], job[2], job[0])
)

W = [20, 35, 50, 65, 80, 95, 110, 140]

def greedy(jobs, w):
    total_cost = 0
    total_relief = 0
    chosen_ids = []

    for job in jobs:
        job_id = job[0]
        job_cost = job[2]
        job_relief = job[3]

        if total_cost + job_cost > w:
            continue
        else:
            total_cost += job_cost
            total_relief += job_relief
            chosen_ids.append(job_id)

    return total_relief, chosen_ids

def validate_solution(jobs, capacity_W, best_load_relief, chosen_ids):

    jobs_by_id = {job[0]: job for job in jobs}


    for job_id in chosen_ids:
        if job_id not in jobs_by_id:
            return False, f"El job {job_id} no existe"

    if len(chosen_ids) != len(set(chosen_ids)):
        return False, "Hay jobs repetidos"

   
    total_cost = 0
    total_relief = 0

    for job_id in chosen_ids:
        job = jobs_by_id[job_id]

        total_cost += job[2]
        total_relief += job[3]


    if total_cost > capacity_W:
        return False, "El costo total supera la capacidad W"

    if total_relief != best_load_relief:
        return False, "El load relief no coincide con los jobs seleccionados"

    return True, "Solución válida"

for w in W:

    best_relief, chosen_ids = greedy(jobs_in_order_c1, w )

    valid, message = validate_solution(c1, w, best_relief, chosen_ids )

    print("C1 - W:", w)
    print("Relief:", best_relief)
    print("Jobs:", chosen_ids)
    print("Validación:", message)
    print()

for w in W:

    best_relief, chosen_ids = greedy(jobs_in_order_c2, w)
 
    valid, message = validate_solution(c2, w,  best_relief, chosen_ids)

    print("C2 - W:", w)
    print("Relief:", best_relief)
    print("Jobs:", chosen_ids)
    print("Validación:", message)
    print()

