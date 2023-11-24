# Escalonador de Processos


<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/mauricio-sj/process_scheduler_memor_virtual?color=%2304D361">
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/mauricio-sj/process_scheduler_memor_virtual">
  <a href="https://github.com/mauricio-sj/process_scheduler_memor_virtual/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/mauricio-sj/process_scheduler_memor_virtual">
  </a>
  <a href="https://github.com/seu-usuario/seu-repositorio/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/seu-usuario/seu-repositorio?style=social">
  </a>
</p>


Simulador de execução de processos em Python, desenvolvido como parte da avaliação da disciplina MATA58 - Sistemas Operacionais, do Departamento de Ciência da Computação da Universidade Federal da Bahia, sob a orientação do professor Maycon Leone Maciel Peixoto. Este simulador representa uma ferramenta educacional para entender os conceitos de escalonamento de processos, gerenciamento de memória e operações de entrada/saída em sistemas operacionais. O código foi criado para explorar e visualizar o comportamento de diferentes algoritmos de escalonamento e estratégias de gerenciamento de recursos em um ambiente simulado.

***
## Sumário

1. [Situação](#Situação)  
2. [Funcionamento](#Funcionamento)  
3. [Requisitos do trabalho](#Requisitos)
4. [Entrada](#Entrada)
5. [Saída](#Saida)
6. [Convenções adotadas](#Convenções)
7. [Adicionais](#Adicionais)
8. [Uso do programa](#Uso)  
. [Requisitos para execução do programa](#Requisitos)  
. [Instalação dos requisitos](#Start)  
. [Execução do programa](#Execução)
9. [Desenvolvimento](#Autores)

***

<div id='Situação'/>  

## :clipboard: Situação  

Imagine um sistema operacional com funcionalidades avançadas de escalonamento de processos. Esse ambiente é projetado para acomodar até ```N``` processos, onde o usuário define previamente o número desejado. Cada processo é caracterizado por três parâmetros cruciais:

- **Tempo de chegada:** Momento em que o processo está pronto para execução.
- **Tempo de execução:** Período que o processo necessita para ser concluído.
- **Deadline:** O prazo final para a conclusão do processo.

Além disso, para configurar o sistema de forma global, são necessárias duas informações fundamentais:

- **Tempo do quantum do sistema:** A quantidade de tempo atribuída a cada processo durante sua execução.
- **Tempo de sobrecarga:** O intervalo de tempo consumido na troca de processos do sistema.

Essas configurações permitem que o sistema opere de maneira eficiente, garantindo que cada processo seja tratado de acordo com suas especificações temporais. Isso proporciona uma experiência de escalonamento avançada, otimizando a utilização dos recursos disponíveis e atendendo aos prazos estabelecidos pelos usuários.

<div id='Funcionamento'/>

## :computer: Funcionamento


Este sistema operacional inclui:

> A implementação obrigatória de todos os algoritmos mencionados a seguir, tanto no contexto de escalonamento quanto de paginação. O cumprimento dessa exigência é essencial para a avaliação do trabalho.



#### [Algoritmos de escalonamento](https://pt.wikipedia.org/wiki/Escalonamento_de_processos)

- **FCFS (First Come First Served):**
    - Implementa um algoritmo de escalonamento baseado em fila, onde o primeiro processo a chegar é o primeiro a ser executado.

- **SJF (Shortest Job First):**
    - Utiliza um critério de ordenação crescente dos processos com base no tempo de execução, escolhendo o processo com o menor tempo primeiro.

- **Round Robin:**
    - Adota um princípio de compartilhamento igualitário, atribuindo a cada processo um quantum de tempo, e o escalonamento ocorre em um ciclo circular.

- **EDF (Earliest Deadline First):**
    - Prioriza o processo com o prazo de vencimento mais curto na fila de prontos, ideal para sistemas de tempo real.

#### **Algoritmos de Substituição de Páginas:**

- **FIFO (First In First Out):**
    - Remove a página mais antiga da memória, seguindo uma abordagem baseada na ordem de chegada.

- **LRU (Least Recently Used):**
    - Remove preferencialmente páginas mais antigas e menos utilizadas, utilizando informações de uso para decisões de substituição.

Esses algoritmos foram implementados em Python, aproveitando as funcionalidades _built-in_ da linguagem para ordenação e manipulação de dados. A escolha dessas implementações visa praticidade e clareza no entendimento do código.

- **Gráfico de Gantt:**
    - Implementamos um [Gráfico de Gantt](https://pt.wikipedia.org/wiki/Diagrama_de_Gantt) para visualizar as execuções dos processos ao longo do tempo. Essa representação gráfica oferece uma visão clara do tempo de execução de cada processo.

- **Visualização da CPU e da RAM:**
    - Adicionamos elementos visuais para representar a CPU e a RAM no ambiente gráfico. A visualização da CPU mostra o estado atual da execução, indicando se está ociosa, em execução, ou em estados específicos como sobrecarga. A RAM é apresentada de forma clara, destacando as páginas presentes em tempo real.

- **Gráfico de Uso da RAM e do Disco:**
    - Criamos gráficos que exibem o uso da RAM e do Disco, proporcionando uma visualização dinâmica das páginas presentes. Isso auxilia na análise do comportamento do sistema operacional em relação à utilização desses recursos.

- **Delay para Verificação da Execução:**
    - Introduzimos _delay_ para possibilitar uma verificação mais detalhada da execução do sistema. Isso permite observar a evolução dos processos e a interação com os diferentes componentes ao longo do tempo.

Para implementar esses recursos, utilizamos a biblioteca [PyQt5](https://pypi.org/project/PyQt5/), que oferece elementos gráficos e de interface para criar uma experiência visual completa e interativa. Essas adições visuais melhoram significativamente a compreensão do funcionamento do sistema operacional e facilitam a análise de seu desempenho.

<div id='Requisitos'/>

## :ballot_box_with_check: Requisitos do Trabalho

- **Tamanho das Páginas:**
    - Cada página possui um tamanho de **4 KB**, conforme especificação.

- **Capacidade da RAM:**
    - A memória RAM é definida com uma capacidade de **200 KB**, proporcionando um ambiente restrito para simulação.

- **Abstração de Disco:**
    - Implementamos uma abstração de disco para gerenciar a memória virtual. Isso permite uma gestão eficiente de páginas, possibilitando a utilização de espaço adicional quando necessário.

- **Tratamento de Falta de Página (_Page Fault_):**
    - Em caso de falta de página, ou seja, quando uma página necessária não está presente na RAM, é utilizado um tempo específico para o acesso ao disco. Esse intervalo de tempo, representado por _N_ unidades, permite a busca e recuperação da página necessária.

- **Execução Condicional dos Processos:**
    - Os processos só são executados se todas as suas páginas estiverem presentes na RAM. Essa condição garante que o sistema operacional tenha acesso completo às instruções e dados necessários para a execução do processo.

- **Abstração Adicional:**
    - O grupo tem a liberdade para criar abstrações adicionais conforme necessário. Essa flexibilidade permite adaptar o sistema operacional de acordo com os requisitos específicos do trabalho.



Deve ser escolhido um dos algoritmos de escalonamento de processo ofertados

- ``` FCFS (First Come First Served) ```;  
- ``` SJF (Shortest Job First) ```;
- ``` RR (Round-Robin)```;
- ``` EDF (Earliest Deadline First) ```;
- ``` SPN (Shortest Process Next) ```;
- ``` LOT (Loteria) ```;
- ``` PRIO (Prioridade) ```;

 > Os três últimos algoritmos foram adicionalmente implementados. Mais informações [aqui](#Adicionais)

Deve ser escolhido um dos algoritmos de paginação:

- ``` FIFO (First-In First-Out) ```;  
- ``` LRU (Least Recently Used) ```

<div id='Saída'/>

## :outbox_tray: Saída

A resposta deve ser dada em função do **turn-around médio** (tempo de espera + tempo de execução), o **gráfico de Gantt correspondente** às execuções dos processos, e o **estado da RAM**, durante a execução dos processos, de acordo o algoritmo de escalonamento e o algoritmo de paginação escolhidos

<div id='Convenções'/>

## :pushpin: Convenções adotadas

-   Utilizamos a notação ``` FCFS (First Come, First Served)```, no código, para nomear o algoritmo de escalonamento de processos e desambiguar da notação ``` FIFO  (First In, First Out) ```, utilizada para nomear o algoritmo de paginação, pois embora os dois algoritmos tenham teoricamente o mesmo funcionamento o escopo deles é diferente.  

-   Utilizamos uma **memória virtual** com o dobro de capacidade da memória RAM, ou seja,  **400 K**  

- A **capacidade do disco** é o somatório de `B`<sub>i</sub> para i variando de 1 a ``N``, ou seja, assumimos que o disco comporta todas as páginas de todos os processos criados.

-   Em caso de _page fault_ utilizamos ``` teto ((B - A) / W) ``` **_tiques_ de clock** para uso do disco, onde:

    -   `A` é o **número de páginas, desse processo, já alocadas na RAM** e;  

    -   `W ` é a **quantidade de páginas, escritas na RAM, por segundo**, em nossa implementação, escolhemos o valor de ```2 páginas por segundo```  


<div id='Uso'/>

## :gear: Uso do programa

O programa pode ser utilizado em qualquer plataforma que tenha Python 3.x
> É aconselhado a utilizar a [release](mauricio-sj/process_scheduler) mais recente 


<div id='Start'/>

### Instalação dos requisitos

- Abra um Terminal ou Prompt de Comando dentro da pasta ``` process-escalonator/ ```:  

> :warning: É recomendado que se instale as bibliotecas em um ambiente virtual, evitando conflitos de versões das bibliotecas instaladas localmente no seu computador. Para tal siga as instruções a seguir, de acordo sua plataforma.

- Linux:  

```sh
  python3 -m venv env
  source env/bin/activate  
```

- Windows:  

```sh
  python -m venv env
  env\Scripts\activate
```

<div id='Execução'/>

### Execução do programa

Para executar basta dar o comando:

```sh
  python InterFace.py
```

Em plataformas Linux é bom especificar a versão do Python, já que em algumas o Python 3.x ainda vem como padrão, com o comando:

```sh
  python3 InterFace.py
```

<div id='Autores'/>
