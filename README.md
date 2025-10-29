Projeto Python: Operações de Lista com Testes Unitários

Este projeto demonstra a refatoração de um script Python procedural (que apenas imprime na tela) para um módulo de lógica de negócios ("operacoes_lista.py") e um conjunto de testes unitários ("test_operacoes.py") que validam essa lógica.

O objetivo é mostrar as melhores práticas de desenvolvimento de software, incluindo a criação de funções puras e reutilizáveis e a garantia de qualidade através de testes (TDD - Test Driven Development).

📦 Estrutura do Projeto

operacoes_lista.py

  Este arquivo contém o "módulo de lógica". Todas as funções de processamento de dados estão aqui.
  
capitalizar_nomes()
filtrar_inteiros()
filtrar_warnings_por_prefixo()
calcular_soma()
calcular_media()

test_operacoes.py
  Este arquivo contém os testes unitários (usando a biblioteca "unittest") que verificam se cada função no módulo de lógica está funcionando como esperado.

⚙️ Instalação

Este projeto usa apenas bibliotecas padrão do Python ("unittest", "typing"). Nenhuma instalação de pacotes externos (via pip) é necessária.

🧪 Como Rodar os Testes

Para verificar se todas as funções lógicas estão corretas, execute os testes unitários.

1.  Certifique-se de que os dois arquivos (operacoes_lista.py e test_operacoes.py) estão na mesma pasta.
2.  Navegue até essa pasta em seu terminal.
3.  Execute o unittest (modo padrão):

    ```bash
    python -m unittest test_operacoes.py
    ```

4.  Para uma saída mais detalhada (verbose), que lista cada teste individualmente, use a flag -v:

    ```bash
    python -m unittest -v test_operacoes.py
    ```
