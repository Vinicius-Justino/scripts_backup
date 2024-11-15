from os import listdir

arquivos_organizados = [arquivo[: arquivo.index(".")] for arquivo in listdir("./python")]
arquivos_backup = []

for arquivo in arquivos_backup:
    try:
        nome_arquivo = arquivo[: arquivo.index("(2020") - 1]
        if nome_arquivo not in arquivos_backup:
            arquivos_backup.append(nome_arquivo)
    except ValueError:
        arquivos_backup.append(nome_arquivo)

for arquivo in arquivos_backup:
    if arquivo not in arquivos_organizados:
        print(arquivo)