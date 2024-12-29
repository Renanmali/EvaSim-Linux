# EvaSim-Linux

Simulador EvaSIM com as novas funcionalidades


Instruções para a organização do ambiente:

    1- Em template-code-xml está armazenado um template base para que possa ser utilizado na criação do código;

    2- Em codes-xml, é o espaço para a alocação dos scripts gerados e também para realizar a compilação do código/

    3- Para compilar o código execute o seguinte comando em seu terminal:

        python3 eva_parser.py codes-xml/"Nome do seu script" -c

    4- Após isso, será gerado seu arquivo "name"_EvaML.xml no diretório principal. Mova-o para a pasta codes-EvaML;

    Pasta "codes-EvaML" foi criada com o intuito de armazenar os scripts a serem executados no no simulador.
