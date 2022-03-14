''' Vamos mostrar como utilizar o modo append (a) para adicionar conteúdo a um arquivo já existente.

Para isso, vamos abrir o arquivo dados_write.txt, criado pelo script9, utilizando o modo a.
Utilizamos esse modo para acrescentar conteúdo a um arquivo. Confira, a seguir, o script11.'''

arquivo_escrita = open('dados_write2.txt', 'a')
arquivo_escrita.write('\n conteudo adiiconal. ')
arquivo_escrita.close()

