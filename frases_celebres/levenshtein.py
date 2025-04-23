import Levenshtein

input1 = "vida"
input2 = "diva"

dist = Levenshtein.distance(input1, input2)
print(f"Distancia de Levenshtein entre '{input1}' y '{input2}': es {dist}")

ratio = Levenshtein.ratio(input1, input2)
print(f"El radio de Levenshtein entre '{input1}' y '{input2}': es {ratio}")
#El levenshtein setradio() devuelve un valor entre 0 y 1, donde 1 significa que las cadenas son idénticas.

set_ratio = Levenshtein.setratio(input1, input2)
print(f"El set ratio de Levenshtein entre '{input1}' y '{input2}': es {set_ratio}")
# Levenshtein.ratio() devuelve un valor entre 0 y 1, donde 1 significa que las cadenas son idénticas.

hamming = Levenshtein.hamming(input1, input2)
print(f"Distancia de Hamming entre '{input1}' y '{input2}': es {hamming}")
# La distancia de Hamming solo se puede calcular entre cadenas de la misma longitud. Si las cadenas son de diferente longitud, se lanzará una excepción.