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

        weight = jobs[i][2]
        value = jobs[i][3]

        # Recorremos la capacidad de mayor a menor
        # para no usar el mismo job más de una vez
        for c in range(capacity_W, weight - 1, -1):

            new_value = dp[c - weight] + value

            if new_value > dp[c]:

                dp[c] = new_value
                take[i][c] = True

    # Reconstrucción de los jobs seleccionados
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

print(solve_dynamic_programming(C2, 0))
print(solve_dynamic_programming(C2, 5))