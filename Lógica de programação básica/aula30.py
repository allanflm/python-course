"""
Constantes: "Variaveis" que nao vao mudar!
muitas condicoes no mesmo if(ruim)
    <- contagem de complexidade (ruim)
"""

velocidade = 61
local_carro = 100

RADAR_1 = 60  # Velocidade maxima do radar!
LOCAL_1 = 100  # local onde o radar 1 esta!
RADAR_RANGE = 1  # A distancia onde o radar pega

vel_carro_pass_rad_1 = velocidade > RADAR_1

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
    vel_carro_pass_rad_1

carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_rad_1

if vel_carro_pass_rad_1:
    print("Velocidade carro passou do radar 1.")

if carro_passou_radar_1:
    print("Carro passou radar 1")

if carro_multado_radar_1:
    print("Carro multado em radar 1")
