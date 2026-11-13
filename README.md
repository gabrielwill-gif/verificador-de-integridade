# 🔎 Verificador de Integridade de Arquivos

Script em Python que calcula o hash SHA-256 de um arquivo e, se você quiser, compara com um hash esperado para detectar alterações.

## Para que serve
- Conferir se um download não foi corrompido ou adulterado
- Verificar se um arquivo mudou ao longo do tempo
- Praticar conceitos de integridade, um dos pilares da segurança da informação

## Como executar
Calcular o hash:
```bash
python verificador_integridade.py arquivo.zip
```

Comparar com um hash esperado:
```bash
python verificador_integridade.py arquivo.zip HASH_ESPERADO
```

## Como funciona
- Lê o arquivo em blocos, então funciona com arquivos grandes
- Usa a biblioteca padrão `hashlib`, sem dependências externas
- Retorna código de saída diferente de zero quando o hash não confere

## Tecnologias
Python 3.9+

## Próximos passos
- Suporte a outros algoritmos (SHA-512, SHA-3)
- Verificar uma pasta inteira e gerar um relatório
- Testes automatizados com pytest
