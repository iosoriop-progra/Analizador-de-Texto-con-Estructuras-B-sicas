class TextAnalyzer:
    
    def __init__(self, text: str):
        self.original_text = text
        self.normalized_text = ""
        self.tokens = []
        self.word_counts = {}

    
    def normalize_text(self, text: str) -> str:
        """
        Normaliza el texto:
        - Convierte a minúsculas
        - Elimina puntuación común
        - Elimina espacios extra
        """
        text = text.lower()

        punctuation = ".,;:!?()[]{}\"'"

        for char in punctuation:
            text = text.replace(char, "")

        text = " ".join(text.split())

        return text

    def tokenize(self):
        """Esto nos sirve para dividir el texto normal en tokens."""
        self.tokens = self.normalized_text.split()

    def count_words(self):
        """Usando un diccionario, cuenta la recuencia de cada palabra."""
        for token in self.tokens:
            if token in self.word_counts:
                self.word_counts[token] += 1
            else:
                self.word_counts[token] = 1

    def analyze(self):
        """Sirve para ejecutar el analísis completo."""
        if not self.original_text.strip():
            raise ValueError("El texto está vacío.")

        self.normalized_text = self.normalize_text(self.original_text)
        self.tokenize()
        self.count_words()

    def report(self):
        """Imprime el reporte ."""
        total_tokens = len(self.tokens)
        unique_tokens = len(set(self.tokens))

        print("\n----- REPORTE -----")
        print(f"Total de palabras: {total_tokens}")
        print(f"Palabras únicas: {unique_tokens}")

        # Top de las 10 palabras
        sorted_words = sorted(
            self.word_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )

        print("\nTop 10 palabras más frecuentes:")
        for word, count in sorted_words[:10]:
            print(f"{word}: {count}")

        # Aquí medimos la longitud promedio
        lengths = [len(word) for word in self.tokens]
        avg_length = sum(lengths) / len(lengths)
        print(f"\nLongitud promedio de palabra: {avg_length:.2f}")

        # Para las palabras más largas y cortas
        max_length = max(lengths)
        min_length = min(lengths)

        longest = {w for w in self.tokens if len(w) == max_length}
        shortest = {w for w in self.tokens if len(w) == min_length}

        print(f"Palabras más largas: {longest}")
        print(f"Palabras más cortas: {shortest}")

    def query(self, word: str):
        """Permite consultar una palabra específica."""
        word = word.lower()

        if word in self.word_counts:
            freq = self.word_counts[word]
            total = len(self.tokens)
            percentage = (freq / total) * 100

            print(f"\nFrecuencia: {freq}")
            print(f"Porcentaje: {percentage:.2f}%")

            if freq == 1:
                print("Es una palabra rara.")
            elif freq >= 5:
                print("Es una palabra común.")
            else:
                print("Es una palabra  frecuente.")
        else:
            print("La palabra no está en el texto.")


def read_from_file():
    """Lee texto desde un archivo."""
    try:
        path = input("Ingrese la ruta del archivo: ")
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print("Error al leer archivo:", e)

    return ""


def read_from_console():
    """Lee texto pegado en consola."""
    print("Pegue el texto (escriba * salir * en una línea para terminar):")
    print("Omita los **")
    lines = []

    while True:
        line = input()
        if line == "salir":
            break
        lines.append(line)

    return "\n".join(lines)


if __name__ == "__main__":
    print("1. Leer desde archivo")
    print("2. Ingresar texto manualmente")

    option = input("Seleccione opción: ")

    if option == "1":
        text = read_from_file()
    elif option == "2":
        text = read_from_console()
    else:
        print("Opción inválida.")
        exit()

    analyzer = TextAnalyzer(text)

    try:
        analyzer.analyze()
        analyzer.report()

        while True:
            word = input("\nIngrese palabra para consultar (salir para cerrar el programa): ")
            if word == "salir":
                break
            analyzer.query(word)

    except ValueError as e:
        print("Error:", e)