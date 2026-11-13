import hashlib
import sys
from pathlib import Path


def calcular_hash(caminho: Path, algoritmo: str = "sha256") -> str:
    """Calcula o hash de um arquivo lendo em blocos (funciona com arquivos grandes)."""
    h = hashlib.new(algoritmo)
    with caminho.open("rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(8192), b""):
            h.update(bloco)
    return h.hexdigest()


def main():
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python verificador_integridade.py <arquivo>")
        print("  python verificador_integridade.py <arquivo> <hash_esperado>")
        sys.exit(1)

    caminho = Path(sys.argv[1])
    if not caminho.is_file():
        print(f"Erro: arquivo não encontrado: {caminho}")
        sys.exit(1)

    hash_calculado = calcular_hash(caminho)
    print(f"Arquivo: {caminho.name}")
    print(f"SHA-256: {hash_calculado}")

    if len(sys.argv) >= 3:
        esperado = sys.argv[2].strip().lower()
        if hash_calculado == esperado:
            print("Resultado: OK, o arquivo está íntegro.")
        else:
            print("Resultado: ALERTA, o hash não confere. O arquivo pode ter sido alterado.")
            sys.exit(2)


if __name__ == "__main__":
    main()
