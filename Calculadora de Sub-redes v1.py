# Coleta de Dados:
eRede = str(input("Qual o endereço da rede a ser calculada? ")).strip().replace(".", " ").split()
cRede = str(input("Qual a classe da rede? ")).strip().upper()
sRede = int(input("Quantas sub-redes deseja, sendo 1 nenhuma sub-rede? "))
resp = ''
if sRede != 1:
    resp = str(input("Deseja obter o endereço de cada sub-rede?(s/n): ")).strip()

ips = []
rede = []
x = sRede
e_ip = 256 / sRede

for i in range(4):
    eRede[i] = int(eRede[i])

def Binary(n):
    s = bin(n)
    s1 = s[2:]
    while len(s1) < 8:
        s1 = '0' + str(s1)
    return s1

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
    q_ip = (65536 / sRede)

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
print('\nExistem {} IPs disponíveis em cada sub-rede, sendo {} o número de hosts.\n'.format(int(q_ip), int(h_ip)))
print('MÁSCARA:\nDecimal: {}\nBinário: {}\nCIDR: /{}\n'.format(dec_mask, bin_mask, CIDR))
print('Ip inserido em binário: {}\n'.format(bin_eRede))
if resp == 's':
    print('Os endereços de rede obtidos são: {}'.format(rede))
