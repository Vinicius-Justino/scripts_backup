from os import listdir, remove, rename

for exercicio in listdir("./C"):
    for extensao in [".o", ".c", ".exe"]:
        arquivos_repetidos = sorted([arquivo for arquivo in listdir(f"./C/{exercicio}") if extensao in arquivo])
        if len(arquivos_repetidos) == 0:
            continue
        
        while len(arquivos_repetidos) > 1:
            remove(f"./C/{exercicio}/{arquivos_repetidos.pop(0)}")
        
        arquivo_definitivo = arquivos_repetidos[0]
        nome_arquivo_definitivo = arquivo_definitivo[: arquivo_definitivo.index("(") - 1]
        rename(f"./C/{exercicio}/{arquivo_definitivo}", f"./C/{exercicio}/{nome_arquivo_definitivo}{extensao}")
