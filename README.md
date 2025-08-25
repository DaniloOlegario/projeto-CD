****
Para Windows (Usando o Agendador de Tarefas)
O Windows tem um programa chamado "Agendador de Tarefas" que pode ser usado para agendar scripts.

Abra o Agendador de Tarefas: Pressione a tecla Windows, digite Agendador de Tarefas e abra o aplicativo.

Crie uma Tarefa Básica: No painel da direita, clique em "Criar Tarefa Básica...".

Nome e Descrição:

Nome: Dê um nome, como Importar Dados Planilha.

Descrição: Adicione uma descrição, como Executa o script de importação de dados a cada 5 minutos.

Clique em Avançar.

Gatilho (Quando a tarefa será iniciada):

Selecione "Diariamente" e clique em Avançar.

Escolha a data e a hora de início (pode ser a hora atual).

Clique em Avançar.

Ação (O que a tarefa fará):

Selecione "Iniciar um programa" e clique em Avançar.

Configurar o Programa:

Programa/script: Digite o caminho completo para o seu interpretador Python, por exemplo: C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python310\python.exe

Adicionar argumentos (opcional): Digite o caminho completo para o seu script, por exemplo: C:\caminho\para\sua\pasta\import_data.py

Clique em Avançar e, depois, em Concluir.

A sua tarefa de importação agora será executada automaticamente a cada 5 minutos. Se os dados da sua planilha mudarem, o seu painel irá refletir as alterações assim que você clicar no botão "Atualizar".
***