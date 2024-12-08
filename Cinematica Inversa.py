import math
import os
import sys

# Função para limpar a tela
def clear_screen():
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:                # Para Unix/Linux/Mac
        os.system('clear')

# Função para imprimir linhas de separação
def print_separator(char='=', length=50):
    print(char * length)

# Função para imprimir títulos
def print_title(title):
    print_separator('=')
    print(f"{title.center(length:=50)}")
    print_separator('=')

# Função para imprimir subtítulos
def print_subtitle(subtitle):
    print_separator('-')
    print(f"{subtitle.center(length:=50)}")
    print_separator('-')

# Função para validar se um valor é positivo
def is_positive(value, name):
    if value <= 0:
        raise ValueError(f"O valor de {name} deve ser positivo. Recebido: {value}")
    return value

# Função para validar Phi
def validate_phi(phi_degrees):
    if not (0 <= phi_degrees <= 360):
        raise ValueError(f"O ângulo Phi deve estar entre 0° e 360°. Recebido: {phi_degrees}°")
    return math.radians(phi_degrees)

# Métodos Algébricos
def calculate_theta2_algebrico(x, y, l1, l2):
    print_subtitle('Θ2 (Algébrico)')
    print('Fórmula utilizada: cos(Θ2) = (x² + y² - l1² - l2²) / (2 * l1 * l2)\n')

    try:
        numerator = x**2 + y**2 - l1**2 - l2**2
        denominator = 2 * l1 * l2

        if denominator == 0:
            raise ZeroDivisionError("Denominador é zero na fórmula de Θ2 (Algébrico).")

        cos_theta2 = numerator / denominator
        # Limitar cos_theta2 para evitar erros de arredondamento
        cos_theta2 = max(min(cos_theta2, 1), -1)
        print(f'cos(Θ2) = ({x:.2f}² + {y:.2f}² - {l1:.2f}² - {l2:.2f}²) / (2 * {l1:.2f} * {l2:.2f}) = {cos_theta2:.4f}')

        sin_theta2 = math.sqrt(1 - cos_theta2**2)
        print(f'sin(Θ2) = √(1 - {cos_theta2:.4f}²) = {sin_theta2:.4f}')

        theta2 = math.atan2(sin_theta2, cos_theta2)
        theta2_deg = math.degrees(theta2)
        print(f'\nΘ2 = -atan2({sin_theta2:.4f}, {cos_theta2:.4f}) = {-theta2_deg:.2f}°\n')
        return -theta2  # Θ2 = -theta2

    except ZeroDivisionError as zde:
        print(f"Erro de Matemática: {zde}")
        raise
    except ValueError as ve:
        print(f"Erro de Matemática: {ve}")
        raise
    except Exception as e:
        print(f"Erro durante o cálculo de Θ2 (Algébrico): {e}")
        raise

def calculate_theta2_linha_algebrico(x, y, l1, l2):
    print_subtitle("Θ2' (Algébrico)")
    print("Fórmula utilizada: Θ2' = atan((l2*sin(Θ2'))/(l1 + l2*cos(Θ2')))\n")

    try:
        numerator = x**2 + y**2 - l1**2 - l2**2
        denominator = 2 * l1 * l2

        if denominator == 0:
            raise ZeroDivisionError("Denominador é zero na fórmula de Θ2' (Algébrico).")

        cos_theta2 = numerator / denominator
        # Limitar cos_theta2 para evitar erros de arredondamento
        cos_theta2 = max(min(cos_theta2, 1), -1)
        print(f'cos(Θ2\') = ({x:.2f}² + {y:.2f}² - {l1:.2f}² - {l2:.2f}²) / (2 * {l1:.2f} * {l2:.2f}) = {cos_theta2:.4f}')

        sin_theta2 = math.sqrt(1 - cos_theta2**2)
        print(f'sin(Θ2\') = √(1 - {cos_theta2:.4f}²) = {sin_theta2:.4f}')

        theta2 = math.atan2(sin_theta2, cos_theta2)
        theta2_deg = math.degrees(theta2)
        print(f'\nΘ2\' = atan2({sin_theta2:.4f}, {cos_theta2:.4f}) = {theta2_deg:.2f}°\n')
        return theta2  # Θ2' = theta2

    except ZeroDivisionError as zde:
        print(f"Erro de Matemática: {zde}")
        raise
    except ValueError as ve:
        print(f"Erro de Matemática: {ve}")
        raise
    except Exception as e:
        print(f"Erro durante o cálculo de Θ2' (Algébrico): {e}")
        raise

def calculate_theta1_algebrico(x, y, l1, l2, theta2): 
    print_subtitle('Θ1 (Algébrico)')
    print('Fórmula utilizada: Θ1 = atan(y/x) - atan((l2*sin(Θ2))/(l1 + l2*cos(Θ2)))\n')

    try:
        term1 = math.atan2(y, x)
        print(f'term1 = atan2({y:.2f}, {x:.2f}) = {term1:.4f} radians')

        term2_cos = l1 + l2 * math.cos(theta2)
        term2_sin = l2 * math.sin(theta2)
        term2 = math.atan2(term2_sin, term2_cos)
        print(f'term2 = atan2(l2*sin(Θ2) = {term2_sin:.4f}, l1 + l2*cos(Θ2) = {term2_cos:.4f}) = {term2:.4f} radians')

        theta1 = term1 - term2
        theta1_deg = math.degrees(theta1)
        print(f'\nΘ1 = {math.degrees(term1):.2f}° - {math.degrees(term2):.2f}° = {theta1_deg:.2f}°\n')
        return theta1

    except Exception as e:
        print(f"Erro durante o cálculo de Θ1 (Algébrico): {e}")
        raise

def calculate_theta1_linha_algebrico(x, y, l1, l2, theta2_linha):
    print_subtitle("Θ1' (Algébrico)")
    print("Fórmula utilizada: Θ1' = atan(y/x) - atan((l2*sin(Θ2'))/(l1 + l2*cos(Θ2')))\n")

    try:
        term1 = math.atan2(y, x)
        print(f'term1 = atan2({y:.2f}, {x:.2f}) = {term1:.4f} radians')

        term2_cos = l1 + l2 * math.cos(theta2_linha)
        term2_sin = l2 * math.sin(theta2_linha)
        term2 = math.atan2(term2_sin, term2_cos)
        print(f'term2 = atan2(l2*sin(Θ2\') = {term2_sin:.4f}, l1 + l2*cos(Θ2\') = {term2_cos:.4f}) = {term2:.4f} radians')

        theta1_linha = term1 - term2
        theta1_linha_deg = math.degrees(theta1_linha)
        print(f'\nΘ1\' = {math.degrees(term1):.2f}° - {math.degrees(term2):.2f}° = {theta1_linha_deg:.2f}°\n')
        return theta1_linha

    except Exception as e:
        print(f"Erro durante o cálculo de Θ1' (Algébrico): {e}")
        raise

def calculate_theta3(phi, theta1, theta2):
    print_subtitle('Θ3')
    theta3 = math.degrees(phi) - (math.degrees(theta1) + math.degrees(theta2))

    print(f'Θ3 = {math.degrees(phi):.2f}° - ({math.degrees(theta1):.2f}° + {math.degrees(theta2):.2f}°) = {theta3:.2f}°')
    return theta3

def calculate_theta3_linha(phi, theta1_linha, theta2_linha):
    print_subtitle("Θ3' (Algébrico)")
    theta3 = math.degrees(phi) - (math.degrees(theta1_linha) + math.degrees(theta2_linha))

    print(f'Θ3\' = {math.degrees(phi):.2f}° - ({math.degrees(theta1_linha):.2f}° + {math.degrees(theta2_linha):.2f}°) = {theta3:.2f}°')
    return theta3

# Função Principal
def main():
    while True:
        # Coletar entradas do usuário
        try:
            print_title("Cálculo de Cinemática Inversa")
            print()
            L1 = float(input('L1 = '))
            L1 = is_positive(L1, 'L1')
            L2 = float(input('L2 = '))
            L2 = is_positive(L2, 'L2')
            L3 = float(input('L3 = '))
            L3 = is_positive(L3, 'L3')
            Phi_degrees = float(input('Phi (em graus) = '))
            Phi = validate_phi(Phi_degrees)

            GARRA = input('A questão é com garra? (s/n) ').strip().lower()

            if GARRA in ['s', 'sim']:
                print('\nQuestão com Garra')
                xGARRA = float(input('Informe o xGARRA: '))
                yGARRA = float(input('Informe o yGARRA: '))
                x3 = xGARRA - L3 * math.cos(Phi)
                y3 = yGARRA - L3 * math.sin(Phi)
                print(f'\nx3 = {x3:.2f}, y3 = {y3:.2f}\n')
            else:
                x3 = float(input('Informe o x3: '))
                y3 = float(input('Informe o y3: '))
                print()

            # Verificação de Alcançabilidade
            distancia = math.sqrt(x3**2 + y3**2)
            if distancia > (L1 + L2):
                print("Erro: O ponto (x3, y3) está fora do alcance do manipulador.")
                sys.exit(1)

            print_separator('=')
            print('Escolha o Método de Cálculo'.center(50))
            print_separator('=')
            print('1. Método Algébrico'.center(50))
            print('2. Método Geométrico'.center(50))
            print_separator('=')
            metodo = input('Digite o número do método que deseja usar (1 ou 2): ').strip()

            if metodo == '1':
                print('\n' + '-'*50 + '\n')
                print_title("Método Algébrico Selecionado")
                print()

                # Cálculos Algébricos
                theta2 = calculate_theta2_algebrico(x3, y3, L1, L2)
                theta2_linha = calculate_theta2_linha_algebrico(x3, y3, L1, L2)

                theta1 = calculate_theta1_algebrico(x3, y3, L1, L2, theta2)
                theta1_linha = calculate_theta1_linha_algebrico(x3, y3, L1, L2, theta2_linha)

                theta3 = calculate_theta3(Phi, theta1, theta2)
                theta3_linha = calculate_theta3_linha(Phi, theta1_linha, theta2_linha)

                print_separator('=')
                print('Resultado Final (Algébrico)'.center(50))
                print_separator('=')
                print(f'Θ1  = {math.degrees(theta1):.2f}°')
                print(f'Θ1\' = {math.degrees(theta1_linha):.2f}°\n')

                print(f'Θ2  = {math.degrees(theta2):.2f}°')
                print(f'Θ2\' = {math.degrees(theta2_linha):.2f}°\n')

                print(f'Θ3  = {theta3:.2f}°')
                print(f'Θ3\' = {theta3_linha:.2f}°\n')

            elif metodo == '2':
                print('\n' + '-'*50 + '\n')
                print_title("Método Geométrico Selecionado")
                print()

                # Cálculos Geométricos
                theta2 = calculate_theta2_geometrico(x3, y3, L1, L2)
                theta2_linha = calculate_theta2_linha_geometrico(x3, y3, L1, L2)

                theta1 = calculate_theta1_geometrico(x3, y3, L1, L2, theta2)
                theta1_linha = calculate_theta1_linha_geometrico(x3, y3, L1, L2, theta2_linha)

                theta3 = calculate_theta3_geometrico(Phi, theta1, theta2)
                theta3_linha = calculate_theta3_linha_geometrico(Phi, theta1_linha, theta2_linha)

                print_separator('=')
                print('Resultado Final (Geométrico)'.center(50))
                print_separator('=')
                theta1_deg = math.degrees(theta1)
                theta1_linha_deg = math.degrees(theta1_linha)
                theta2_deg = math.degrees(theta2)
                theta2_linha_deg = math.degrees(theta2_linha)

                print(f'Θ1  = {theta1_deg:.2f}°')
                print(f'Θ1\' = {theta1_linha_deg:.2f}°\n')

                print(f'Θ2  = {theta2_deg:.2f}°')
                print(f'Θ2\' = {theta2_linha_deg:.2f}°\n')

                print(f'Θ3  = {theta3:.2f}°')
                print(f'Θ3\' = {theta3_linha:.2f}°\n')

            else:
                print("\nOpção inválida. Por favor, selecione 1 ou 2.\n")
                continue  # Retorna ao início do loop

        except ValueError as ve:
            print(f"\nErro de Entrada: {ve}\n")
            continue  # Retorna ao início do loop para tentar novamente
        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}\n")
            continue  # Retorna ao início do loop para tentar novamente

        # Perguntar se o usuário deseja resolver outra questão
        while True:
            novamente = input("Deseja resolver outra questão? (s/n): ").strip().lower()
            if novamente in ['s', 'sim']:
                clear_screen()
                break  # Sai do loop interno e recomeça o loop principal
            elif novamente in ['n', 'não', 'nao']:
                print("\nEncerrando o programa. Até mais!\n")
                sys.exit()
            else:
                print("Entrada inválida. Por favor, responda com 's' ou 'n'.")

# Métodos Geométricos
def calculate_theta2_geometrico(x, y, l1, l2):
    print_subtitle('Θ2 (Geométrico)')
    print('Fórmula utilizada: cos(Θ2) = (x² + y² - l1² - l2²) / (2 * l1 * l2)\n')

    try:
        numerator = x**2 + y**2 - l1**2 - l2**2
        denominator = 2 * l1 * l2

        if denominator == 0:
            raise ZeroDivisionError("Denominador é zero na fórmula de Θ2 (Geométrico).")

        cos_theta2 = numerator / denominator
        # Limitar cos_theta2 para evitar erros de arredondamento
        cos_theta2 = max(min(cos_theta2, 1), -1)
        print(f'cos(Θ2) = ({x:.2f}² + {y:.2f}² - {l1:.2f}² - {l2:.2f}²) / (2 * {l1:.2f} * {l2:.2f}) = {cos_theta2:.4f}')

        theta2 = -math.acos(cos_theta2)
        theta2_deg = math.degrees(theta2)
        print(f'\nΘ2 = -arccos({cos_theta2:.4f}) = {theta2_deg:.2f}°\n')
        return theta2

    except ZeroDivisionError as zde:
        print(f"Erro de Matemática: {zde}")
        raise
    except ValueError as ve:
        print(f"Erro de Matemática: {ve}")
        raise
    except Exception as e:
        print(f"Erro durante o cálculo de Θ2 (Geométrico): {e}")
        raise

def calculate_theta2_linha_geometrico(x, y, l1, l2):
    print_subtitle("Θ2' (Geométrico)")
    print("Fórmula utilizada: Θ2' = arccos((x² + y² - l1² - l2²) / (2 * l1 * l2))\n")

    try:
        numerator = x**2 + y**2 - l1**2 - l2**2
        denominator = 2 * l1 * l2

        if denominator == 0:
            raise ZeroDivisionError("Denominador é zero na fórmula de Θ2' (Geométrico).")

        cos_theta2 = numerator / denominator
        # Limitar cos_theta2 para evitar erros de arredondamento
        cos_theta2 = max(min(cos_theta2, 1), -1)
        print(f'cos(Θ2\') = ({x:.2f}² + {y:.2f}² - {l1:.2f}² - {l2:.2f}²) / (2 * {l1:.2f} * {l2:.2f}) = {cos_theta2:.4f}')

        theta2 = math.acos(cos_theta2)
        theta2_deg = math.degrees(theta2)
        print(f'\nΘ2\' = arccos({cos_theta2:.4f}) = {theta2_deg:.2f}°\n')
        return theta2

    except ZeroDivisionError as zde:
        print(f"Erro de Matemática: {zde}")
        raise
    except ValueError as ve:
        print(f"Erro de Matemática: {ve}")
        raise
    except Exception as e:
        print(f"Erro durante o cálculo de Θ2' (Geométrico): {e}")
        raise

def calculate_theta1_geometrico(x, y, l1, l2, theta2): 
    print_subtitle('Θ1 (Geométrico)')
    print('Fórmula utilizada: Θ1 = atan(y/x) - atan((l2*sin(Θ2))/(l1 + l2*cos(Θ2)))\n')

    try:
        term1 = math.atan2(y, x)
        print(f'term1 = atan2({y:.2f}, {x:.2f}) = {term1:.4f} radians')

        term2_cos = l1 + l2 * math.cos(theta2)
        term2_sin = l2 * math.sin(theta2)
        term2 = math.atan2(term2_sin, term2_cos)
        print(f'term2 = atan2(l2*sin(Θ2) = {term2_sin:.4f}, l1 + l2*cos(Θ2) = {term2_cos:.4f}) = {term2:.4f} radians')

        theta1 = term1 - term2
        theta1_deg = math.degrees(theta1)
        print(f'\nΘ1 = {math.degrees(term1):.2f}° - {math.degrees(term2):.2f}° = {theta1_deg:.2f}°\n')
        return theta1

    except Exception as e:
        print(f"Erro durante o cálculo de Θ1 (Geométrico): {e}")
        raise

def calculate_theta1_linha_geometrico(x, y, l1, l2, theta2_linha):
    print_subtitle("Θ1' (Geométrico)")
    print("Fórmula utilizada: Θ1' = atan(y/x) - atan((l2*sin(Θ2'))/(l1 + l2*cos(Θ2')))\n")

    try:
        term1 = math.atan2(y, x)
        print(f'term1 = atan2({y:.2f}, {x:.2f}) = {term1:.4f} radians')

        term2_cos = l1 + l2 * math.cos(theta2_linha)
        term2_sin = l2 * math.sin(theta2_linha)
        term2 = math.atan2(term2_sin, term2_cos)
        print(f'term2 = atan2(l2*sin(Θ2\') = {term2_sin:.4f}, l1 + l2*cos(Θ2\') = {term2_cos:.4f}) = {term2:.4f} radians')

        theta1_linha = term1 - term2
        theta1_linha_deg = math.degrees(theta1_linha)
        print(f'\nΘ1\' = {math.degrees(term1):.2f}° - {math.degrees(term2):.2f}° = {theta1_linha_deg:.2f}°\n')
        return theta1_linha

    except Exception as e:
        print(f"Erro durante o cálculo de Θ1' (Geométrico): {e}")
        raise

def calculate_theta3_geometrico(phi, theta1, theta2):
    print_subtitle('Θ3 (Geométrico)')
    print('Fórmula utilizada: Θ3 = Phi (em graus) - (Θ1 + Θ2)\n')

    try:
        phi_deg = math.degrees(phi)
        theta1_deg = math.degrees(theta1)
        theta2_deg = math.degrees(theta2)
        theta3 = phi_deg - (theta1_deg + theta2_deg)
        print(f'Θ3 = {phi_deg:.2f}° - ({theta1_deg:.2f}° + {theta2_deg:.2f}°) = {theta3:.2f}°\n')
        return theta3

    except Exception as e:
        print(f"Erro durante o cálculo de Θ3 (Geométrico): {e}")
        raise

def calculate_theta3_linha_geometrico(phi, theta1_linha, theta2_linha):
    print_subtitle("Θ3' (Geométrico)")
    print("Fórmula utilizada: Θ3' = Phi (em graus) - (Θ1' + Θ2')\n")

    try:
        phi_deg = math.degrees(phi)
        theta1_linha_deg = math.degrees(theta1_linha)
        theta2_linha_deg = math.degrees(theta2_linha)
        theta3_linha = phi_deg - (theta1_linha_deg + theta2_linha_deg)
        print(f'Θ3\' = {phi_deg:.2f}° - ({theta1_linha_deg:.2f}° + {theta2_linha_deg:.2f}°) = {theta3_linha:.2f}°\n')
        return theta3_linha

    except Exception as e:
        print(f"Erro durante o cálculo de Θ3' (Geométrico): {e}")
        raise

if __name__ == "__main__":
    main()

