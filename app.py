from src.CalculateWinner import CalculateWinner
from test.TestCalculateWinner import TestCalculateWinner
import unittest

if __name__ == '__main__':
    # Se instancia el objeto CalculateWinner
    calculator = CalculateWinner()

    # Datos
    datatest = [
        ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
        ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
    ]

    # Se ejecuta las pruebas unitarias con detalle
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(TestCalculateWinner))

    # Se llama a la función para calcular el ganador
    print(calculator.determine_winner(datatest))
