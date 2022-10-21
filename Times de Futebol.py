brasileirão = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print(f"Os cinco ´primeiros times são: {brasileirão[:5]} ")
print(f"Os cinco ultimos times são {brasileirão[-5:]}")
print(f"Times em ordem alfábetica {sorted(brasileirão)}: ")
print(f"O flamengo está na {brasileirão.index('Flamengo')} posição")

