from mip import Model, xsum, maximize, CONTINUOUS

m = Model("TCC")

lista_acoes = ['PETR4', 'ITUB4', 'PETR3', 'BBAS3', 'ELET3', 'SBSP3', 'WEGE3', 'BBDC4', 'B3SA3', 'ABEV3', 'ITSA4', 'EMBR3', 'BPAC11', 'EQTL3', 'SUZB3', 'JBSS3', 'RDOR3', 'PRIO3', 'RENT3', 'BBSE3', 'ENEV3', 'RADL3', 'GGBR4', 'CMIG4', 'RAIL3', 'TOTS3', 'VIVT3', 'UGPA3', 'VBBR3', 'CPLE6', 'BBDC3', 'KLBN11', 'BRFS3', 'TIMS3', 'ENGI11', 'LREN3', 'CCRO3', 'STBP3', 'ELET6', 'NTCO3', 'HAPV3', 'EGIE3', 'ISAE4', 'ASAI3', 'SANB11', 'ALOS3', 'CMIN3', 'BRAV3', 'CSAN3', 'CXSE3', 'TAEE11', 'HYPE3', 'PSSA3', 'CPFE3', 'MULT3', 'CSNA3', 'GOAU4', 'CYRE3', 'FLRY3', 'POMO4', 'RECV3', 'BRAP4', 'MRFG3', 'CRFB3', 'IRBR3', 'IGTI11', 'AZZA3', 'SLCE3', 'USIM5', 'BRKM5', 'YDUQ3', 'COGN3', 'SMTO3', 'AURE3', 'MGLU3', 'VIVA3', 'RAIZ4', 'VAMO3', 'MRVE3', 'AZUL4', 'PCAR3', 'PETZ3', 'BEEF3', 'LWSA3', 'CVCB3', 'AMOB3']

lista_dy = [19.69, 0.66, 18.0, 6.27, 3.06, 1.36, 0.94, 1.79, 1.97, 5.74, 8.31, 0.11, 2.89, 0.27, 3.95, 7.3, 2.51, 0.18, 4.9, 11.27, 0, 1.58, 5.03, 11.91, 0.52, 0.81, 4.0, 3.94, 12.83, 5.6, 1.82, 0.96, 3.59, 7.62, 6.88, 5.66, 2.55, 4.4, 8.14, 7.85, 0, 2.96, 10.52, 1.27, 5.85, 4.41, 14.18, 1.83, 5.8, 7.56, 7.58, 5.69, 4.28, 10.33, 3.82, 14.38, 5.11, 4.24, 9.75, 9.49, 21.0, 13.83, 15.24, 1.29, 0, 3.46, 8.6, 7.39, 4.91, 0, 4.19, 12.02, 4.5, 0.72, 2.59, 3.2, 9.75, 12.14, 0, 0, 0, 14.13, 0, 2.62, 0, 0]

lista_desvio_padrao = [1.4135819913913021, 1.2379333590167476, 1.650553037349403, 1.1561227383880333, 1.4717304944417022, 1.5706139515315465, 1.748762336723007, 1.5059369350990588, 2.0822208424729425, 1.394377967464723, 1.2303053815219938, 2.781297482291021, 1.7982246508689779, 1.851136353219384, 1.7411630811190637, 2.3329498338931716, 1.9012579818981907, 1.939352150439419, 2.772594463119261, 1.0277238877698827, 1.7608574375282817, 1.8566527898669978, 1.842229302666241, 1.6502511791167438, 1.7705800963720173, 2.0141806669802422, 1.5828443239177143, 2.1811767191863214, 1.86782684966065, 1.3665224499171478, 1.4440998630262616, 1.1999048240538386, 2.4810288103800846, 1.6856913214961262, 1.646000006860668, 2.8809021141317954, 1.655611097588636, 2.007459465718765, 1.3076762097288153, 3.123082094897785, 3.079922162088372, 1.1559289058510862, 1.3177794955102415, 2.928468283780866, 1.5317519340746628, 1.5580500035516314, 2.701584113376879, 3.2580443381085185, 2.339376995436275, 1.4757142896978952, 0.9352154618971203, 2.0742430036925916, 1.3648624958070195, 1.2646257520121145, 1.6547526162999455, 2.77961963348671, 1.8218812172698586, 2.18906700593547, 1.6569016599341, 2.6645960073246258, 2.142876764728616, 1.4740486203799916, 2.9880467571861216, 3.0019362951284467, 3.6729488014971508, 1.7808457365338493, 2.5418612164701644, 1.5311275030178766, 2.940095494120367, 2.8106647869801287, 3.436230037747559, 3.6001835535970037, 2.1541794261898537, 1.5482895254220854, 4.165937736866387, 2.315571584310796, 2.339008746733859, 3.83739464727529, 3.0288575526185046, 4.803658907016885, 3.9724134527061015, 4.334742818518355, 2.757923419422573, 3.0803923415434182, 4.377617675561232, 7.404905263049118]

lista_setor = ['Energy', 'Financial Services', 'Energy', 'Financial Services', 'Utilities', 'Utilities', 'Industrials', 'Financial Services', 'Financial Services', 'Consumer Defensive', 'Industrials', 'Industrials', 'Financial Services', 'Utilities', 'Basic Materials', 'Consumer Defensive', 'Healthcare', 'Energy', 'Industrials', 'Financial Services', 'Utilities', 'Healthcare', 'Basic Materials', 'Utilities', 'Industrials', 'Technology', 'Communication Services', 'Energy', 'Consumer Cyclical', 'Utilities', 'Financial Services', 'Basic Materials', 'Consumer Defensive', 'Communication Services', 'Utilities', 'Consumer Cyclical', 'Industrials', 'Industrials', 'Utilities', 'Consumer Defensive', 'Financial Services', 'Utilities', 'Utilities', 'Consumer Defensive', 'Financial Services', 'Real Estate', 'Basic Materials', 'Energy', 'Energy', 'Financial Services', 'Utilities', 'Healthcare', 'Financial Services', 'Utilities', 'Real Estate', 'Basic Materials', 'Basic Materials', 'Consumer Cyclical', 'Healthcare', 'Industrials', 'Energy', 'Financial Services', 'Consumer Defensive', 'Consumer Cyclical', 'Financial Services', 'Real Estate', 'Consumer Cyclical', 'Consumer Defensive', 'Basic Materials', 'Basic Materials', 'Consumer Defensive', 'Consumer Defensive', 'Basic Materials', 'Utilities', 'Consumer Cyclical', 'Consumer Cyclical', 'Utilities', 'Industrials', 'Real Estate', 'Industrials', 'Consumer Cyclical', 'Consumer Cyclical', 'Consumer Defensive', 'Technology', 'Consumer Cyclical', 'Consumer Cyclical']

soma_desvio_padrao = sum(lista_desvio_padrao)

risco_aceitavel = 2.2526344253822277     #soma_desvio_padrao/len(lista_desvio_padrao)     # conservador: 1.959791950082538099, moderado: 2.2526344253822277, agressivo: 2.545476900681917301

percentual_maximo = 0.2 


n = len(lista_acoes)

# variaveis: x_i = qtd do capital investido no ativo i
x = [m.add_var(var_type=CONTINUOUS, lb=0) for _ in range(n)]

# função objetivo
m.objective = maximize(xsum(x[i] * lista_dy[i] for i in range(n)))

# restrições
for i in range(n):
    if lista_desvio_padrao[i] > risco_aceitavel:
        m += x[i] == 0# desvio padrão do ativo i deve ser menor que risco aceito pelo perfil do investidor


# Restrições por setor
setor_indices = {}
for i in range(n):
    setor = lista_setor[i]
    if setor not in setor_indices:
        setor_indices[setor] = []
    setor_indices[setor].append(i)

for indices in setor_indices.values():
    m += xsum(x[i] for i in indices) <= percentual_maximo   # não deve investir mais que o permitido em um unico ativo

m += xsum(x[i] for i in range(n)) == 1   # deve investir todo capital

m.write('model.lp')

m.optimize()

if m.num_solutions > 0:
    risco_carteira = 0.0
    dy_carteira = 0.0
    alocacoes = []
    
    for i in range(n):
        if x[i].x > 0.001:
            percentual = x[i].x * 100
            risco_carteira += x[i].x * lista_desvio_padrao[i]
            dy_carteira += x[i].x * lista_dy[i]
            alocacoes.append((lista_acoes[i], percentual, lista_setor[i]))
    
    print("\nRESULTADO DA OTIMIZAÇÃO:")
    print(f"Dividend Yield da carteira: {dy_carteira:.2f}%")
    print(f"Risco (Desvio Padrão) da carteira: {risco_carteira:.2f}%")
    print(f"Risco aceitável definido: {risco_aceitavel:.2f}%")
    
    print("\nALOCAÇÃO POR ATIVO:")
    print("{:<10} {:<15} {:<10}".format("Ativo", "Alocação (%)", "Setor"))
    for ativo, perc, setor in alocacoes:
        print("{:<10} {:<15.2f} {:<10}".format(ativo, perc, setor))
    
    print("\nALOCAÇÃO POR SETOR:")
    setor_alocacao = {}
    for ativo, perc, setor in alocacoes:
        if setor not in setor_alocacao:
            setor_alocacao[setor] = 0.0
        setor_alocacao[setor] += perc
    
    for setor, perc in setor_alocacao.items():
        print(f"{setor}: {perc:.2f}%")