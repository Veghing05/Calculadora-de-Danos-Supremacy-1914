def calcular_dano(hp, dano_base, fortificacao=0, influencia_combate=0, ataque=True):
    """
    Calcula o dano (ataque ou defesa) com base nos parâmetros fornecidos.
    
    Args:
        hp (float): Pontos de vida da unidade.
        dano_base (float): Dano base da unidade.
        fortificacao (float, optional): Porcentagem de aumento de defesa devido à fortificação (padrão é 0).
        influencia_combate (float, optional): Influência de combate (expressa como porcentagem negativa ou positiva, padrão é 0).
        ataque (bool): Se True, calcula o dano de ataque; se False, calcula o dano de defesa.
    
    Returns:
        tuple: HP restante, dano final, dano mínimo, dano máximo, cor
    """
    if ataque:
        dano = dano_base
        dano -= dano * influencia_combate / 100
        dano_min = dano - 0.1 * dano_base
        dano_max = dano + 0.1 * dano_base
        cor = "\033[91m"  # Vermelho para ataque
    else:
        dano = dano_base
        dano += dano * fortificacao / 100
        dano -= dano * influencia_combate / 100
        dano_min = dano - 0.1 * dano_base
        dano_max = dano + 0.1 * dano_base
        cor = "\033[94m"  # Azul para defesa
    
    dano_final = max(0, min(hp, dano))
    hp_restante = hp - dano_final

    return hp_restante, dano_final, dano_min, dano_max, cor

# Exemplo de uso:
print("Calculadora de Danos")
print("-" * 20)

# Entrada para o atacante
hp_unidade_ataque = float(input("\033[91mHP do atacante: \033[0m"))
dano_base_unidade_ataque = float(input("\033[91mDano base do atacante: \033[0m"))
influencia_combate_unidade_ataque = float(input("\033[91mInfluência de combate do atacante (%): \033[0m"))

# Entrada para o defensor
hp_unidade_defesa = float(input("\033[94mHP do defensor: \033[0m"))
dano_base_unidade_defesa = float(input("\033[94mDano base do defensor: \033[0m"))
fortificacao_unidade_defesa = float(input("\033[94mPorcentagem de fortificação do defensor (%): \033[0m"))
influencia_combate_unidade_defesa = float(input("\033[94mInfluência de combate do defensor (%): \033[0m"))

# Cálculo dos danos
hp_restante_ataque, dano_ataque, dano_ataque_min, dano_ataque_max, cor_ataque = calcular_dano(
    hp_unidade_ataque, dano_base_unidade_ataque, 0, influencia_combate_unidade_ataque, ataque=True)
hp_restante_defesa, dano_defesa, dano_defesa_min, dano_defesa_max, cor_defesa = calcular_dano(
    hp_unidade_defesa, dano_base_unidade_defesa, fortificacao_unidade_defesa, influencia_combate_unidade_defesa, ataque=False)

# Exibição dos resultados
print("*" * 6 + " Resultado do combate " + "*" * 6)
print(f"{cor_ataque}Dano de ataque entre: {dano_ataque_min:.2f} e {dano_ataque_max:.2f}\033[0m")
print(f"{cor_ataque}HP restante do atacante: {hp_restante_ataque:.2f}\033[0m")
print()
print(f"{cor_defesa}Dano de defesa entre: {dano_defesa_min:.2f} e {dano_defesa_max:.2f}\033[0m")
print(f"{cor_defesa}HP restante do defensor: {hp_restante_defesa:.2f}\033[0m")
