def SCP(U, S, i=0, cubiertos=None, seleccionados=None, K=3):
    if cubiertos is None:
        cubiertos = set()
    if seleccionados is None:
        seleccionados = []

    if cubiertos == U:
        return seleccionados
    if i >= len(S):
        return None
    if len(seleccionados) >= K:
        return None

    nuevos_cubiertos = cubiertos.union(S[i])
    solucion1 = set_covering(U, S, i + 1, nuevos_cubiertos, seleccionados + [S[i]], K)
    solucion2 = set_covering(U, S, i + 1, cubiertos, seleccionados, K)

    if solucion1 is None and solucion2 is None:
        return None
    if solucion1 is None:
        return solucion2
    if solucion2 is None:
        return solucion1

    if len(solucion1) <= len(solucion2):
        return solucion1
    else:
        return solucion2
