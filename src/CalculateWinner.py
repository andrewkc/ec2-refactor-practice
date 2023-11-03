import csv
import re

class CalculateWinner:

    # Técnica: Cambio de nombre. Se cambió el nombre del método para que sea más descriptivo.
    def read_data(self, filename):
        data = []
        with open(filename, 'r') as csvfile:
            next(csvfile)  # Skip header
            datareader = csv.reader(csvfile)
            for row in datareader:
                data.append(row)
        return data

    # Técnica: Cambio de nombre. Se cambió el nombre del método para que sea más descriptivo.
    def is_valid_dni(self, dni):
        return re.match(r'^\d{8}$', dni) is not None

    # Técnica: Método de extracción. Creó un nuevo método para contar votos válidos.
    def count_valid_votes(self, data):
        valid_votes = {}
        total_votes = 0

        for row in data:
            if self.is_valid_dni(row[3]) and row[5] == '1':
                total_votes += 1
                valid_votes[row[4]] = valid_votes.get(row[4], 0) + 1

        return valid_votes, total_votes

    # Técnica: Método de extracción. Creó un nuevo método para determinar los ganadores.
    def determine_winners(self, valid_votes):
        if not valid_votes:
            return []

        max_votes = max(valid_votes.values())
        winning_candidates = [candidate for candidate, votes in valid_votes.items() if votes == max_votes]

        return winning_candidates

    # Técnica: Método de extracción. Creó un nuevo método para calcular el ganador.
    def determine_winner(self, data):
        valid_votes, total_votes = self.count_valid_votes(data)
        winning_candidates = self.determine_winners(valid_votes)

        if max(valid_votes.values()) / total_votes > 0.5:
            return [winning_candidates[0]]
        else:
            return winning_candidates[:2]