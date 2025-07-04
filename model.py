from mip import Model, xsum, maximize, CONTINUOUS

m = Model("TCC")

# dados 2023-2024
lista_acoes = ['PETR4', 'ITUB4', 'PETR3', 'BBAS3', 'ELET3', 'SBSP3', 'WEGE3', 'BBDC4', 'B3SA3', 'ABEV3', 'ITSA4', 'EMBR3', 'BPAC11', 'EQTL3', 'SUZB3', 'JBSS3', 'RDOR3', 'PRIO3', 'RENT3', 'BBSE3', 'ENEV3', 'RADL3', 'GGBR4', 'CMIG4', 'RAIL3', 'TOTS3', 'VIVT3', 'UGPA3', 'VBBR3', 'CPLE6', 'BBDC3', 'KLBN11', 'BRFS3', 'TIMS3', 'ENGI11', 'LREN3', 'CCRO3', 'STBP3', 'ELET6', 'NTCO3', 'HAPV3', 'EGIE3', 'ISAE4', 'ASAI3', 'SANB11', 'ALOS3', 'CMIN3', 'BRAV3', 'CSAN3', 'CXSE3', 'TAEE11', 'HYPE3', 'PSSA3', 'CPFE3', 'MULT3', 'CSNA3', 'GOAU4', 'CYRE3', 'FLRY3', 'POMO4', 'RECV3', 'BRAP4', 'MRFG3', 'CRFB3', 'IRBR3', 'IGTI11', 'AZZA3', 'SLCE3', 'USIM5', 'BRKM5', 'YDUQ3', 'COGN3', 'SMTO3', 'AURE3', 'MGLU3', 'VIVA3', 'RAIZ4', 'VAMO3', 'MRVE3', 'AZUL4', 'PCAR3', 'PETZ3', 'BEEF3', 'LWSA3', 'CVCB3']

lista_dy = [23.82257404600782, 1.2556591133547437, 22.51027609166715, 6.882707473433716, 0.5508643519066314, 1.7808479478301276, 1.708996344290917, 9.809919192751767, 3.4620595094332662, 5.368502743638161, 2.362251235766911, 0.0, 2.1435865369078337, 1.005953735481859, 2.159480849580151, 4.557331948340943, 1.304550026686313, 0.157750274057631, 2.490100954115421, 11.860355456542985, 0.0, 1.056757229905694, 7.058264196575556, 13.500623601802097, 0.28898029178626833, 1.9699829909164652, 9.84207594707993, 1.3921312381811606, 4.07540679303222, 3.373126233840387, 9.989172123438522, 6.394881858780967, 0.0, 9.443366168788659, 3.039685765557618, 2.159249271025769, 1.3875133568373266, 5.711129313350416, 3.4902399878200976, 0.0, 0.0, 6.806985809263743, 9.061764703515056, 0.37640461146706355, 5.554801940836877, 2.0760118099903115, 9.398133422144376, 0.0, 2.2916481070850376, 8.760863517691392, 8.58808414555777, 3.6492823839090667, 7.102536538715727, 7.814970847541399, 4.2998052093723125, 7.739548407027015, 15.341956127292066, 3.7684027001867593, 2.6339122850307377, 4.801990988304397, 5.283359376935386, 13.74337298334662, 0.0, 1.2070891787703566, 0.0, 1.60378481239633, 3.0771827703880024, 6.85825192211071, 3.6609922182518844, 0.0, 1.2989850522883333, 0.0, 4.438615205563389, 23.41927620734537, 0.0, 1.1176340438942154, 6.644008317187823, 3.5024021624769337, 0.0, 0.0, 0.0, 0.45885187721876175, 7.374859644887167, 0.887366990502852, 0.0]

lista_desvio_padrao = [2.005304886747068, 1.4718107819871364, 2.048793257880982, 1.5225567086252192, 1.8900153997573093, 1.7243376265297004, 1.594417993677956, 1.8629025031371622, 2.200563421617291, 1.3122515212601886, 1.351584598433549, 1.9911511809620086, 2.179288367959151, 1.401436637318514, 1.5969366320756926, 2.0421753912509755, 2.657838771413574, 2.332929818588418, 1.9789101097685846, 1.2630098084776438, 1.9726488514153793, 1.4285630349755871, 1.7846285173087908, 1.5955985007359756, 1.6244638248357726, 2.0066329078217375, 1.359886194412736, 1.8964898967215653, 2.2139302564425387, 1.4747961776429146, 1.5457394504739415, 1.4026554791045096, 3.8449627234024635, 1.3950071561452915, 1.8010388221321918, 2.9769949267613387, 1.5703088477512224, 2.1166750850044953, 1.7677815410962001, 3.100826810798511, 5.152940085964918, 1.0721371794524734, 1.3172296622216855, 2.7922227741666155, 1.512379386038474, 1.8169542973277406, 2.2995728591529896, 3.1194968004572434, 1.9471661491423442, 1.1844213930693046, 0.9505851803926084, 1.838496015292917, 1.4490712535339103, 1.4128520600546999, 1.6748970969931911, 2.533027123705629, 1.730485996194831, 2.400402839966178, 1.8069773027030227, 2.264659263734668, 2.8765995400896065, 1.7075154009602955, 2.685895371090444, 2.941709206968878, 4.133688180464139, 1.811884819198466, 2.6435361255410683, 1.5456842153887786, 1.9153430807103622, 3.217880247390554, 3.997046246472238, 2.89829212744934, 2.211303248416598, 1.061245097677842, 4.873122779607485, 2.2328061386251146, 2.715956280799848, 3.0151229547015523, 3.403398796982213, 4.963955784760873, 5.394507129718882, 3.521670412093314, 2.726172359974032, 3.8021751150834673, 5.090440451364796]

lista_setor = ['Energy', 'Financial Services', 'Energy', 'Financial Services', 'Utilities', 'Utilities', 'Industrials', 'Financial Services', 'Financial Services', 'Consumer Defensive', 'Industrials', 'Industrials', 'Financial Services', 'Utilities', 'Basic Materials', 'Consumer Defensive', 'Healthcare', 'Energy', 'Industrials', 'Financial Services', 'Utilities', 'Healthcare', 'Basic Materials', 'Utilities', 'Industrials', 'Technology', 'Communication Services', 'Energy', 'Consumer Cyclical', 'Utilities', 'Financial Services', 'Basic Materials', 'Consumer Defensive', 'Communication Services', 'Utilities', 'Consumer Cyclical', 'Industrials', 'Industrials', 'Utilities', 'Consumer Defensive', 'Financial Services', 'Utilities', 'Utilities', 'Consumer Defensive', 'Financial Services', 'Real Estate', 'Basic Materials', 'Energy', 'Energy', 'Financial Services', 'Utilities', 'Healthcare', 'Financial Services', 'Utilities', 'Real Estate', 'Basic Materials', 'Basic Materials', 'Consumer Cyclical', 'Healthcare', 'Industrials', 'Energy', 'Financial Services', 'Consumer Defensive', 'Consumer Cyclical', 'Financial Services', 'Real Estate', 'Consumer Cyclical', 'Consumer Defensive', 'Basic Materials', 'Basic Materials', 'Consumer Defensive', 'Consumer Defensive', 'Basic Materials', 'Utilities', 'Consumer Cyclical', 'Consumer Cyclical', 'Utilities', 'Industrials', 'Real Estate', 'Industrials', 'Consumer Cyclical', 'Consumer Cyclical', 'Consumer Defensive', 'Technology', 'Consumer Cyclical']

soma_desvio_padrao = sum(lista_desvio_padrao)

risco_aceitavel = soma_desvio_padrao/len(lista_acoes)   
print(risco_aceitavel)  
# conservador: 1.975112589653949948   -   moderado: 2.2702443559240804   -   agressivo: 2.565376122194210852


percentual_maximo = 0.2


n = len(lista_acoes)

# variaveis: x_i = qtd do capital investido no ativo i
x = [m.add_var(var_type=CONTINUOUS, lb=0) for _ in range(n)]

# função objetivo
m.objective = maximize(xsum(x[i] * lista_dy[i] for i in range(n)))

# restrições

# restrição para remover as primeiras 3 carteiras geradas
# ativos_usados = ['PETR4', 'VIVT3', 'GOAU4', 'BRAP4', 'AURE3', 'PETR3', 'BBSE3', 'CMIG4', 'TIMS3', 'CMIN3', 'BBDC3', 'STBP3', 'ISAE4', 'CSNA3', 'BEEF3']
# for ativo in ativos_usados:
#     idx = lista_acoes.index(ativo)
#     m += x[idx] == 0

m += xsum(x[i] * lista_desvio_padrao[i] for i in range(n)) <= risco_aceitavel   # desvio padrão do ativo i deve ser menor que risco aceito pelo perfil do investidor 


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
        if x[i].x > 0.0001:
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
