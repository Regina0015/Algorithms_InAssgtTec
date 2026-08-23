def solve_dynamic_programming(jobs, capacity_W):

    n = len(jobs)

    # Guarda el mejor valor para cada capacidad
    dp = [0] * (capacity_W + 1)

    # Guarda las decisiones para reconstruir
    # los jobs seleccionados
    take = []

    for i in range(n):
        row = [False] * (capacity_W + 1)
        take.append(row)

    # Revisamos cada job
    for i in range(n):

        job_id = jobs[i][0]
        weight = jobs[i][2]
        value = jobs[i][3]

        # Recorremos la capacidad de mayor a menor
        for c in range(capacity_W, weight - 1, -1):

            new_value = dp[c - weight] + value

            if new_value > dp[c]:
                dp[c] = new_value
                take[i][c] = True

    # Reconstrucción
    chosen_ids = []

    c = capacity_W

    for i in range(n - 1, -1, -1):

        if take[i][c]:

            job_id = jobs[i][0]
            weight = jobs[i][2]

            chosen_ids.append(job_id)

            c = c - weight

    chosen_ids.reverse()

    return dp[capacity_W], chosen_ids

C2 = [
    ("Q10", "Realtime Analytics",       10,  60),
    ("Q20", "Search Reindexing",        20, 100),
    ("Q30", "Video Transcoding",        30, 120),
    ("Q35", "Database Replication",     35, 130),
    ("Q40", "Model Inference Batch",    40, 135),
    ("Q45", "Large ETL Pipeline",       45, 140),
    ("Q50", "Database Migration",       50, 150)
]


value, selected = solve_dynamic_programming(C2, 50)

print("Best load relief:", value)
print("Selected jobs:", selected)
