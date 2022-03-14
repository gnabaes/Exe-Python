'''Escrevendo conteúdo em um arquivo'''
'''Nesta seção, vamos mostrar como, a partir da função open, escrever conteúdo em um arquivo.
A primeira modificação é alterar o modo de acesso ao arquivo. Para escrita de texto, podemos utilizar o modo w (write) ou o modo a (append):'''

''' No exemplo a seguir, vamos criar dois scripts para mostrar o uso do modo w. No primeiro, script9, 
vamos utilizar o método write. No segundo, script10, vamos utilizar o método writelines.
'''

arquivo_escrita = open('dados_write2.txt','w')
arquivo_escrita.write('conteudo  da primeira  linha.')
arquivo_escrita.write('\n conteudo da segunda linha')
arquivo_escrita.close()

linhas = ['conteudo  da primeira  linha ', '\n conteudo da segunda  linha.']
arquivo_escrita = open('dados_write.txt2', 'w')
arquivo_escrita.writelines(linhas)
arquivo_escrita.close()


