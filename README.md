# GitHub Test Mining

Este projeto busca analisar repositórios do GitHub com foco em contribuições relacionadas a testes de software. Ele utiliza a biblioteca **PyDriller** para mineração de commits e informações adicionais dos repositórios.

## Requisitos

Certifique-se de ter o Python instalado e siga as etapas abaixo:

1. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```

2. Ative o ambiente virtual:
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

3. Instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```

## Funcionalidades

1. **Minerar Repositórios**:
   - Busca repositórios open source em Python usando a API do GitHub.
   - Inclui repositórios com maiores contribuidores (top 15) e repositórios na média.

2. **Classificação**:
   - Divide repositórios em duas classes com base no percentil de contribuidores.

3. **Análise de Testes**:
   - Identifica padrões de testes e commits relacionados a arquivos de teste.

4. **Visualização**:
   - Gera gráficos para análise de contribuidores e commits relacionados a testes.

## Arquitetura do Projeto

- `search_repositories`: Função para buscar repositórios no GitHub.
- `filter_repos_with_contributors`: Filtra e classifica repositórios por número de contribuidores.
- `analyze_testing_patterns`: Analisa padrões de testes em commits.
- `visualize_results`: Gera gráficos para análise.

## Visualização dos Dados

Após executar o notebook, os gráficos gerados mostrarão:

- Número de contribuidores por repositório.
- Quantidade de commits relacionados a testes por repositório.

## Execução

Execute o notebook principal `main.ipynb` para iniciar o processo.

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`. Incluem:

- **pydriller**: Mineração de commits.
- **pandas**: Manipulação de dados.
- **matplotlib**: Visualização de gráficos.
- **requests**: Requisições HTTP para a API do GitHub.