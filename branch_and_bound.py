from typing import List, Tuple, Any

def solve_branch_and_bound(jobs: List[Tuple[Any, str, int, int]], capacity_W: int) -> Tuple[int, List[Any]]:

  # si la 'integer offloading capacity' es cero o menor, o ya no hay trabajos, devolvemos cero y la lista vacia
  if capacity_W <= 0 or len(jobs) == 0:
    return 0, []

  # hacemos una copia de los trabajos
  order = jobs[:]

  # ordenamos los trabajos de mayor a menor relacion valor/costo
  for i in range(len(order)):
    for j in range(i + 1, len(order)):

      vwi = order[i][3] / order[i][2] # calculamos la relacion valor/costo: vi / wi
      vwj = order[j][3] / order[j][2]

      if vwi < vwj:
        temp = order[i]
        order[i] = order[j]
        order[j] = temp

  n = len(order)

  # guardamos el mejor valor y los identificadores de los trabajos elegidos
  mejorValue = 0
  mejorSet = []

  # función para calcular el 'upper bound'
  def ubound(i, remaining, value):
    upper = value
    capacityLeft = remaining

    while i < n and order[i][2] <= capacityLeft: # restamos el costo a la capacidad restante y agregamos el valor del trabajo
      capacityLeft -= order[i][2]
      upper += order[i][3]
      i += 1

    if i < n and capacityLeft > 0: # si quedara capacidad y trabajos pero no para un trabajo completo tomamos una parte de el
      rm = capacityLeft / order[i][2] # se calcula parte del trabajo que se puede tomar en cuenta
      upper += rm * order[i][3]

    return upper

  def dfs(i, remaining, value, chosen):
    nonlocal mejorValue, mejorSet

    if value > mejorValue: # revisar si lo actual es mejor que la solución anterior
      mejorValue = value
      mejorSet = chosen[:]

    if i == n or remaining == 0: # si ya no quedan trabajos ni capacidad
      return

    UB = ubound(i, remaining, value)

    if UB <= mejorValue:
      return

    weight = order[i][2] # obtenemos costo y valor del trabajo
    jobV = order[i][3]

    if weight <= remaining: # si el trabajo cabe en la capacidad disponible agregamos el ID del trabajo a la lista de elegidos
      chosen.append(order[i][0])
      dfs(i + 1, remaining - weight, value + jobV, chosen) # exploramos la rama y seguimos con el siguiente trabajo

      chosen.pop() # lo quitamos para explorar otra rama

    dfs(i + 1, remaining, value, chosen) # no seleccionar el trabajo

  # explorar desde el primer trabajo sin seleccionar nada
  dfs(0, capacity_W, 0, [])

  # ordenamos los ID
  mejorSet.sort()

  return mejorValue, mejorSet