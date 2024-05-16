#definindo os sets em sala de aula:
A1 = {2, 3, 4, 5, 6}
A2 = {1, 2, 4, 5}
A3 = {0, 1, 5, 7, 2, 4}

#definindo o que tem em comum entre as regiões:
regiao1 = A1 - A2 - A3
regiao3 = A2 - A1 - A3
regiao4 = A3 - A1 - A2
regiao2 = A1.intersection(A2) - A3
regiao6 = A1.intersection(A3) - A2
regiao5 = A3.intersection(A2) - A1
regiao7 = ((A1|A2|A3) - regiao1 - regiao3 - regiao4 - regiao2 - regiao6 - regiao5)

print('oi, temos os seguintes resultados')
print('regiao1:', regiao1, 'regiao2:', regiao2, 'regiao3:', regiao3, 'regiao4:', regiao4, 'regiao5:', regiao5, 'regiao6:', regiao6, 'regiao7:', regiao7)

