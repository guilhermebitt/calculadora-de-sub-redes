#Função de Binário
def Binary(n):
    s = bin(n)
    s1 = s[2:]
    while len(s1) < 8:
        s1 = '0' + str(s1)
    return s1

while True:
    #''Banco de Dados'':
    eRede = str(input("Qual o endereço da rede a ser calculada? ")).strip().replace(".", " ").split()
    sRede = int(input("Quantas sub-redes deseja, sendo 1 nenhuma sub-rede? "))
    ips = []
    rede = []
    x = sRede
    for i in range(4):
        eRede[i] = int(eRede[i])

    #Calculador de Classe de Rede:
    if (eRede[0] == 192 and eRede[1] > 167) or (eRede[0] > 192):
        cRede = 'C'
        e_ip = int(256 / sRede)
    elif (eRede[0] == 172 and eRede[1] > 15) or (eRede[0] > 172 and eRede[0] < 192):
        cRede = 'B'
        e_ip = int(256 / sRede)
        if sRede > 256:
            cRede = 'C'
            e_ip = int(65538 / sRede)
    elif (eRede[0] == 172 and eRede[1] < 16) or (eRede[0] < 172):
        cRede = 'A'
        e_ip = int(256 / sRede)
        if sRede > 256:
            cRede = 'B'
            e_ip = int(65538 / sRede)
        if sRede > 65538:
            cRede = 'C'
            e_ip = int(16777216 / sRede)

    bin_eRede = ('{}.{}.{}.{}'.format(Binary(eRede[0]), Binary(eRede[1]), Binary(eRede[2]), Binary(eRede[3])))

    # Verificação de Classe:
    if cRede == 'C':
        while x != 0:
            ips.append(256 - (x * e_ip))
            eRede[3] = int(ips[sRede - x])
            rede.insert(sRede - x, (str(eRede)))
            x = x - 1
        dec_mask = ('255.255.255.{}'.format(eRede[3]))
        bin_mask = ('11111111.11111111.11111111.{}'.format(Binary(eRede[3])))
        CIDR = bin_mask.count('1')
        q_ip = (256 / sRede)

    if cRede == 'B':
        while x != 0:
            ips.append(256 - (x * e_ip))
            eRede[2] = int(ips[sRede - x])
            eRede[3] = 0
            rede.insert(sRede - x, (str(eRede)))
            x = x - 1
        dec_mask = ('255.255.{}.0'.format(eRede[2]))
        bin_mask = ('11111111.11111111.{}.00000000'.format(Binary(eRede[2])))
        CIDR = bin_mask.count('1')
        q_ip = (65538 / sRede)

    if cRede == 'A':
        while x != 0:
            ips.append(256 - (x * e_ip))
            eRede[1] = int(ips[sRede - x])
            eRede[2] = 0
            eRede[3] = 0
            rede.insert(sRede - x, (str(eRede)))
            x = x - 1
        dec_mask = ('255.{}.0.0'.format(eRede[1]))
        bin_mask = ('11111111.{}.00000000.00000000'.format(Binary(eRede[1])))
        CIDR = bin_mask.count('1')
        q_ip = (16777216 / sRede)

    h_ip = q_ip - 2

    # Resposta:
    print('\nIp inserido em binário: {}'.format(bin_eRede))
    print('Existem {} IPs disponíveis em cada sub-rede, sendo {} o número de hosts.\n'.format(int(q_ip), int(h_ip)))
    print('MÁSCARA:\nDecimal: {}\nBinário: {}\nCIDR: /{}'.format(dec_mask, bin_mask, CIDR))
    print('=-'*20)
