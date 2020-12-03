##############
Gabriela R Campos
CEN0336 - Introdução a programação de computadores aplicadas a ciências biológicas
Prof. Dr. Diego M. Riãno-Pachón
Trabalho Final: 'CONTANDO SEMENTES COM PYTHON'
Piracicaba/2020
##############

O projeto 'Contando sementes com Python' foi desenvolvido como trabalho final exigido pela disciplina CEN0336.

Para que você consiga rodar o código com sucesso é necessário seguir as diretrizes:

	1. No seu diretório de trabalho devem ter os seguintes arquivos:
		1.1 Counting_seeds.py
		1.2 feijao_001.jpg (Imagem utilizada para gerar a função seeds_num().
		1.3 Um diretório com todas as imagens a serem analisadas.

	2. Na linha de comando é necessário informar o nome do diretório onde se encontram as imagens (argumento para o comando sys.argv[1]).

	3. O script está programado para ler imagens tipo JPG, caso seja outra extensão é preciso mudar a informação na linha 47.

	4. As imagens devem ser nomeadas da seguinte maneira: NOME DO TRATAMENTO/GRUPO_REPETIÇÃO/PARCELA.jpg (ou outra extensão)
		EXEMPLO: milho_001.jpg
		O id da parcela DEVE ser composto por TRÊS digítos, caso não seja suficiente mudar o código na linha 52 e 86, adicionando \d para cada dígito a mais.
		

	5. O default da função seeds_num() para o threshold é 110. Verificar se esse mesmo valor se aplica aos seus arquivos, caso não encontrar o novo valor limite para a binarização.

