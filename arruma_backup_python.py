from os import listdir, remove, rename

for arquivo in listdir("./python"):
    nome_arquivo = ""
    try:
        nome_arquivo = arquivo[: arquivo.index("(2020") - 1]
    except ValueError:
        continue

    arquivos_repetidos = []
    for arquivo_repetido in listdir("./python"):
        try:
            if nome_arquivo == arquivo_repetido[: arquivo_repetido.index("(2020") - 1]:
                arquivos_repetidos.append(arquivo_repetido)
        except ValueError:
            continue

    while len(arquivos_repetidos) > 1:
        remove(f"./python/{arquivos_repetidos.pop(0)}")
    
    arquivo_definitivo = arquivos_repetidos[0]
    extensao_arquivo = arquivo[arquivo.index("UTC)") + 4 :]
    rename(f"./python/{arquivo_definitivo}", f"./python/{nome_arquivo}{extensao_arquivo}")
