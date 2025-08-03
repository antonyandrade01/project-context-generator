import os

def encontrar_e_copiar_arquivos(arquivo_nomes, diretorio_busca, arquivo_saida):
    """
    Lista todos os arquivos em um diretório e, em seguida, encontra arquivos específicos,
    copiando o caminho e o conteúdo para um arquivo de saída, tentando múltiplas
    codificações de caracteres.

    Argumentos:
        arquivo_nomes (str): O caminho para o arquivo .txt contendo os nomes dos arquivos a serem buscados.
        diretorio_busca (str): O diretório onde a busca pelos arquivos será realizada.
        arquivo_saida (str): O caminho para o arquivo de texto onde o resultado será salvo.
    """
    try:
        with open(arquivo_nomes, 'r', encoding='utf-8') as f:
            nomes_procurados = [linha.strip() for linha in f]
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_nomes}' não foi encontrado.")
        return

    # Lista de codificações para tentar ler os arquivos
    encodings_para_tentar = ['utf-8', 'latin-1', 'cp1252']

    with open(arquivo_saida, 'w', encoding='utf-8') as saida:
        # Primeiro, lista todos os arquivos e diretórios sem filtro.
        saida.write("--- LISTA COMPLETA DE ARQUIVOS NO DIRETÓRIO ---\n\n")
        for pasta_raiz, _, arquivos in os.walk(diretorio_busca):
            for nome_arquivo in arquivos:
                caminho_completo = os.path.join(pasta_raiz, nome_arquivo)
                # Garante barras normais no caminho para consistência
                saida.write(f"{caminho_completo.replace(os.sep, '/')}\n")
        
        # Adiciona um separador para maior clareza no arquivo de saída
        saida.write("\n\n--- CONTEÚDO DOS ARQUIVOS FILTRADOS ---\n\n")
        
        # Agora, busca os arquivos específicos e tenta ler seus conteúdos
        for pasta_raiz, _, arquivos in os.walk(diretorio_busca):
            for nome_arquivo in arquivos:
                # O filtro permanece o mesmo: nomes na lista ou arquivos .html
                if nome_arquivo in nomes_procurados or nome_arquivo.lower().endswith('.html'):
                    caminho_completo = os.path.join(pasta_raiz, nome_arquivo)
                    saida.write(f"{caminho_completo.replace(os.sep, '/')}\n")
                    
                    conteudo = None
                    for encoding in encodings_para_tentar:
                        try:
                            with open(caminho_completo, 'r', encoding=encoding) as conteudo_arquivo:
                                conteudo = conteudo_arquivo.read()
                                # Se a leitura funcionou, saímos do loop de tentativas
                                break
                        except UnicodeDecodeError:
                            # Se deu erro com a codificação atual, tenta a próxima
                            continue
                    
                    if conteudo:
                        saida.write(f"{conteudo}\n\n")
                    else:
                        saida.write(f"NÃO FOI POSSÍVEL LER O CONTEÚDO DO ARQUIVO COM AS CODIFICAÇÕES TESTADAS.\n\n")

    print(f"Busca concluída. Os resultados foram salvos em '{arquivo_saida}'.")

if __name__ == '__main__':
    # Substitua pelos caminhos corretos no seu sistema
    arquivo_com_nomes = 'nomes_dos_arquivos.txt'
    diretorio_para_buscar = '.'  # representa o diretório atual
    arquivo_de_saida = 'resultado.txt'

    encontrar_e_copiar_arquivos(arquivo_com_nomes, diretorio_para_buscar, arquivo_de_saida)