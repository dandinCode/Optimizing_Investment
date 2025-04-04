from mip import Model, xsum, maximize, CONTINUOUS

m = Model("TCC")

lista_acoes = ['ITUB4', 'PETR4', 'PETR3', 'BBAS3', 'ELET3', 'SBSP3', 'WEGE3', 'BBDC4', 'B3SA3', 'ABEV3', 'ITSA4', 'EMBR3', 'BPAC11', 'EQTL3', 'SUZB3', 'JBSS3', 'RDOR3', 'PRIO3', 'RENT3', 'BBSE3', 'ENEV3', 'RADL3', 'GGBR4', 'CMIG4', 'RAIL3', 'TOTS3', 'VIVT3', 'UGPA3', 'VBBR3', 'CPLE6', 'BBDC3', 'KLBN11', 'BRFS3', 'TIMS3', 'ENGI11', 'LREN3', 'CCRO3', 'STBP3', 'ELET6', 'NTCO3', 'HAPV3', 'EGIE3', 'ISAE4', 'ASAI3', 'SANB11', 'ALOS3', 'CMIN3', 'BRAV3', 'CSAN3', 'CXSE3', 'TAEE11', 'HYPE3', 'PSSA3', 'CPFE3', 'MULT3', 'CSNA3', 'GOAU4', 'CYRE3', 'FLRY3', 'POMO4', 'RECV3', 'BRAP4', 'MRFG3', 'CRFB3', 'IRBR3', 'IGTI11', 'AZZA3', 'SLCE3', 'USIM5', 'BRKM5', 'YDUQ3', 'COGN3', 'SMTO3', 'AURE3', 'MGLU3', 'VIVA3', 'RAIZ4', 'VAMO3', 'MRVE3', 'AZUL4', 'PCAR3', 'PETZ3', 'BEEF3', 'LWSA3', 'CVCB3', 'AMOB3']

lista_dy = [0.66, 19.69, 18.0, 6.27, 3.06, 1.36, 0.94, 1.79, 1.97, 5.74, 8.31, 0.11, 2.89, 0.27, 3.95, 7.3, 2.51, 0.18, 4.9, 11.27, 0, 1.58, 5.03, 11.91, 0.52, 0.81, 4.0, 3.94, 12.83, 5.6, 1.82, 0.96, 3.59, 7.62, 6.88, 5.66, 2.55, 4.4, 8.14, 7.85, 0, 2.96, 10.52, 1.27, 5.85, 4.41, 14.18, 1.83, 5.8, 7.56, 7.58, 5.69, 4.28, 10.33, 3.82, 14.38, 5.11, 4.24, 9.75, 9.49, 21.0, 13.83, 15.24, 1.29, 0, 3.46, 8.6, 7.39, 4.91, 0, 4.19, 12.02, 4.5, 0.72, 2.59, 3.2, 9.75, 12.14, 0, 0, 0, 14.13, 0, 2.62, 0, 0]

lista_desvio_padrao = [1.2444385167690184, 1.422345684634686, 1.6678740160087573, 1.1566194124221096, 1.4702734763790055, 1.571111364620631, 1.7472212804341802, 1.5094460650893804, 2.0740021828862645, 1.4000382691425954, 1.234147428455306, 2.775911681795358, 1.7895619407335452, 1.8511319495375884, 1.7412884404334996, 2.332566316368116, 1.9044052691596516, 1.9389286742349878, 2.771020689589306, 1.0276717778104583, 1.761988180228355, 1.8554275921813745, 1.8391620400015634, 1.5969430384330137, 1.7650304875926324, 2.014842282783173, 1.5799498953527589, 2.172778465770335, 1.8569820090892777, 1.3635055148873099, 1.4484043237266149, 1.202455131369075, 2.4774021574820884, 1.6807374461543352, 1.6403907185339517, 2.881921700368353, 1.6499384185098105, 2.007385786452922, 1.3062073548076614, 3.1208063053333093, 3.079922162088372, 1.1553745569600866, 1.316796234241099, 2.925931840962945, 1.5391806662330618, 1.5532485076185467, 2.7801264032421114, 3.245117229351721, 2.3352753717547285, 1.4756413407559688, 0.9348052565367735, 2.072817375345221, 1.365248050575697, 1.2642022419257917, 1.65103385968022, 2.771367234062126, 1.8193102908349124, 2.186839140247599, 1.6535983116290762, 2.6637664451993186, 2.1346704917000796, 1.444846550288514, 2.986491646562732, 3.0019362951284467, 3.659475215822703, 1.7709162405712333, 2.555165522250449, 1.5359126305141866, 2.934367761910703, 2.802186230889361, 3.4412030503990936, 3.5974788022394093, 2.1473549624245836, 1.5482895254220854, 4.165281143232933, 2.3221826581741176, 2.3387746588500513, 3.8310152336089045, 3.0276289322492485, 4.804959187378106, 3.9673031356521067, 4.334634262308399, 2.7586766694467206, 3.0803923415434182, 4.373250192024218, 7.441988927958001]

lista_setor = ['Financial Services', 'Energy', 'Energy', 'Financial Services', 'Utilities', 'Utilities', 'Industrials', 'Financial Services', 'Financial Services', 'Consumer Defensive', 'Industrials', 'Industrials', 'Financial Services', 'Utilities', 'Basic Materials', 'Consumer Defensive', 'Healthcare', 'Energy', 'Industrials', 'Financial Services', 'Utilities', 'Healthcare', 'Basic Materials', 'Utilities', 'Industrials', 'Technology', 'Communication Services', 'Energy', 'Consumer Cyclical', 'Utilities', 'Financial Services', 'Basic Materials', 'Consumer Defensive', 'Communication Services', 'Utilities', 'Consumer Cyclical', 'Industrials', 'Industrials', 'Utilities', 'Consumer Defensive', 'Financial Services', 'Utilities', 'Utilities', 'Consumer Defensive', 'Financial Services', 'Real Estate', 'Basic Materials', 'Energy', 'Energy', 'Financial Services', 'Utilities', 'Healthcare', 'Financial Services', 'Utilities', 'Real Estate', 'Basic Materials', 'Basic Materials', 'Consumer Cyclical', 'Healthcare', 'Industrials', 'Energy', 'Financial Services', 'Consumer Defensive', 'Consumer Cyclical', 'Financial Services', 'Real Estate', 'Consumer Cyclical', 'Consumer Defensive', 'Basic Materials', 'Basic Materials', 'Consumer Defensive', 'Consumer Defensive', 'Basic Materials', 'Utilities', 'Consumer Cyclical', 'Consumer Cyclical', 'Utilities', 'Industrials', 'Real Estate', 'Industrials', 'Consumer Cyclical', 'Consumer Cyclical', 'Consumer Defensive', 'Technology', 'Consumer Cyclical', 'Consumer Cyclical']

soma_desvio_padrao = sum(lista_desvio_padrao)

risco_aceitavel =  soma_desvio_padrao/len(lista_desvio_padrao)     # conservador: 1.934039869376412855, moderado: 2.223034332616566, agressivo: 2.512028795856720145

percentual_maximo = 0.2 



n = len(lista_acoes)

# variaveis: x_i = qtd do capital investido no ativo i
x = [m.add_var(var_type=CONTINUOUS, lb=0) for _ in range(n)]

# função objetivo
m.objective = maximize(xsum(x[i] * lista_dy[i] for i in range(n)))

# restrições
for i in range(n):
    if lista_desvio_padrao[i] > risco_aceitavel:
        m += x[i] == 0 # desvio padrão do ativo i deve ser menor que risco aceito pelo perfil do investidor


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
    print("\n\n")
    for i in range(n):
        if x[i].x > 0.001: 
            print(f"Investir {x[i].x*100:.2f}% em {lista_acoes[i]}")
    print(f"DY total máximo: {m.objective_value:.2f}%")
