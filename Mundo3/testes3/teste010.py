try:
    a = 45
    b = 0
    r = a / b
except (ValueError, TypeError):
    print(f'Error:  V_E or T_E')
except ZeroDivisionError:
    print(f'Error: Z_D_E')
except KeyboardInterrupt:
    print(f'Error: K_I')
except Exception as e:
    print(f'O erro encontrado foi: {e.__cause__}')
else:
    print(f' = {r:.1f}')
finally:
    print(f'Volte sempre!')

# Try, Except e finally testado por Kaiky - 2025
