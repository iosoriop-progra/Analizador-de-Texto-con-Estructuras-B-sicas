from main import TextAnalyzer


def test_normalization():
    text = "Hola, Mundo!!"
    result = TextAnalyzer("dummy").normalize_text(text)
    assert result == "hola mundo"


def test_tokenization():
    text = "hola mundo python"
    analyzer = TextAnalyzer(text)
    analyzer.analyze()
    assert analyzer.tokens == ["hola", "mundo", "python"]


def test_word_count():
    text = "hola hola mundo"
    analyzer = TextAnalyzer(text)
    analyzer.analyze()
    assert analyzer.word_counts["hola"] == 2
    assert analyzer.word_counts["mundo"] == 1


def test_empty_text():
    try:
        TextAnalyzer("").analyze()
    except ValueError:
        assert True
    else:
        assert False


if __name__ == "__main__":
    test_normalization()
    test_tokenization()
    test_word_count()
    test_empty_text()
    print("Pruebas básicas ejecutadas correctamente.")