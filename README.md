# Entrega projeto PBC

## 1. Introdução

<p align="justify"> O Exame Nacional do Ensino Médio (ENEM) é um dos passos mais importantes da
trajetória de qualquer estudante no nosso país, porém é de conhecimento comum que nem
todos têm as mesmas oportunidades, assim gerando uma desigualdade entre eles. </p>

<p align="justify"> Para combater esse problema foram criadas diversas cotas para todas as categorias de estudantes, sendo elas baseadas em raça, em renda ou em deficiências. Assim, pessoas que possam possivelmente ter tido seu aprendizado prejudicado por fatores diversos ganham o direito de competir somente com pessoas com situações semelhantes pelas vagas separadas para o seu grupo de cotas. </p>

<p align="justify"> Ademais, é importante ressaltar a presença dos dados referentes às escolas em que cada aluno se formou, assim abrindo margem para uma comparação entre os formandos de escolas públicas e particulares, dentro e fora das cotas. </p>

<p align="justify"> Portanto, dadas informações citadas acima, o assunto em questão possui como objetivo apresentar dados, a fim de fornecer uma análise abrangente e detalhada sobre os resultados do ENEM 2022, examinando minuciosamente as informações coletadas, esperando com que tais contribuam para a compreensão das possíveis correlações entre variáveis socioeconômicas presentes na realização do exame e em sua obtenção de resultados. </p>

<p align="justify"> Logo, diante da nossa hipótese, pode-se ser esperado que ao decorrer das análises, se obtenha um resultado que mostre como as diferenças avaliadas beneficiem o grupo social cujas condições estivessem mais favoráveis ao sucesso das notas do que a obtenção de um resultado negativo, visto que atualmente, dentre as diversas esferas da sociedade, os grupos que apresentam dificuldades estruturais e/ou econômicas, são mais suscetíveis à falha por não apresentarem as mesmas oportunidades que os demais. </p>

## 2.1. Descrição da base de dados

<p align="justify"> A base de dados a ser utilizada no trabalho será os Microdados do Enem 2022, que podem ser encontrados em: <a href="https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem" target="_blank">Enem-Inep</a>. </p>

<p align="justify"> Os dados presentes na base, englobam o número de inscrição do participante, o qual é apenas uma máscara, logo não representa o número original, informações básicas sobre os inscritos, como a faixa etária, que varia de menor de 17 anos até maior de 70 anos, o sexo, estado civil, cor/raça, nacionalidade, o ano de conclusão do ensino médio, o tipo de escola que estudou no ensino médio (pública ou privada) e se o inscrito é considerado treineiro, no caso de não concluir o ensino médio em 2022. </p>

<p align="justify"> Também estão presentes dados sobre a escola do participante, como a sigla do estado e o nome do município em que a escola está localizada, a dependência administrativa (federal, estadual, municipal ou privada) e localização (urbana ou rural). E  a sigla do estado e o nome do município de aplicação da prova. </p>

<p align="justify"> Além disso, pode-se encontrar os dados da prova objetiva e da redação, o primeiro inclui a presença nas provas dos dois dias (ciências da natureza, ciências humanas, linguagens e códigos e matemática), a língua estrangeira escolhida pelo participante, o código das provas aplicadas (cor, libras, digital, reaplicação), a nota que o inscrito obteve em cada prova, vetor com as respostas dos participantes e vetor com o gabarito de cada prova. O segundo, a nota total obtida na redação, a nota de cada competência (da 1ª a 5ª) e a situação da redação (anulada, em branco, fuga do tema, texto insuficiente, sem problemas). </p>

<p align="justify"> O último item da base de dados, apresenta as questões e as respostas do questionário socioeconômico, o qual é composto por 25 perguntas, que contêm o nível de escolaridade e a ocupação dos pais do participante, a quantidade de de pessoas que moram com o inscrito, a renda mensal da família, características da residência e se tem acesso à internet. </p>

<p align="justify"> Por fim, a base de dados a ser utilizada apresenta 76 colunas e 1048576 linhas. </p>

## 2.2 Características da base de dados que o grupo irá focar na análise

### Tabela 1

|  Nome da coluna        | Descrição                     | Tipo      | Valores esperados       | 
| ---------------------- | ----------------------------- | --------- | ----------------------- |
| TP_FAIXA_ETARIA        | <p align="center"> Faixa etária </p>                 | Inteiro   | 1 a 20 |
| TP_SEXO                | <p align="center"> Sexo </p>                         | Caractere | "F" e "M" |
| TP_COR_RACA            | <p align="center"> Cor/raça </p>                     | Inteiro   | 0 a 6 |
| TP_ST_CONCLUSAO        | <p align="center"> Situação de conclusão do Ensino Médio </p> | Inteiro | 1 a 4 |
| TP_ANO_CONCLUIU        | <p align="center"> Ano de Conclusão do Ensino Médio </p>| Inteiro | 0 a 16 |                       
| TP_ESCOLA              | <p align="center"> Tipo de escola do Ensino Médio </p> | Inteiro | 1 a 3 |
| TP_ENSINO              | <p align="center"> Tipo de instituição que concluiu ou concluirá o <br />Ensino Médio  </p> | Inteiro | 1 ou 2 | 
| IN_TREINEIRO           | <p align="center"> Indica se o inscrito fez a prova com intuito de apenas <br />treinar seus conhecimentos </p> | Inteiro | 0 ou 1 | 
| NO_MUNICIPIO_ESC       | <p align="center"> Nome do município da escola </p> | String | “Vitória”, “São Paulo”, <br />“Rio de Janeiro” etc |
| SG_UF_ESC              | <p align="center"> Sigla da Unidade da Federação da escola </p> | String | “ES”, “SP”, “RJ”, <br />“AM" etc |
| TP_DEPENDENCIA_ADM_ESC | <p align="center"> Dependência administrativa (Escola) </p> | Inteiro | 1 a 4 |   
| TP_PRESENCA_CN         | <p align="center"> Presença na prova objetiva de Ciências da Natureza </p> | Inteiro | 0 a 2 |
| TP_PRESENCA_CH         | <p align="center"> Presença na prova objetiva de Ciências Humanas </p> | Inteiro | 0 a 2 |   
| TP_PRESENCA_LC         | <p align="center"> Presença na prova objetiva de Linguagens e Códigos </p> | Inteiro | 0 a 2 | 
| TP_PRESENCA_MT         | <p align="center"> Presença na prova objetiva de Matemática </p> | Inteiro | 0 a 2 |      
| NU_NOTA_CN             | <p align="center"> Nota da prova de Ciências da Natureza </p> | Float | 0 a 1000 |            
| NU_NOTA_CH             | <p align="center"> Nota da prova de Ciências Humanas </p> | Float | 0 a 1000 |           
| NU_NOTA_LC             | <p align="center"> Nota da prova de Linguagens e Códigos </p> | Float | 0 a 1000 |    
| NU_NOTA_MT             | <p align="center"> Nota da prova de Matemática </p> | Float| 0 a 1000 |                              
| TP_LINGUA              | <p align="center"> Língua Estrangeira | Inteiro </p> | 0 ou 1 |                                
| TP_STATUS_REDACAO      | <p align="center"> Situação da redação do participante </p> | Inteiro | 1 a 9 |
| NU_NOTA_COMP1          | <p align="center"> Nota da competência 1 - Demonstrar domínio da <br />modalidade escrita formal da Língua Portuguesa. </p> | Inteiro | 0 a 200 |
| NU_NOTA_COMP2          | <p align="center"> Nota da competência 2 - Compreender a proposta de <br />redação e aplicar conceitos das várias áreas de <br />conhecimento para desenvolver o tema, dentro dos limites <br />estruturais do texto dissertativo-argumentativo em prosa. </p> | Inteiro |  0 a 200 |
| NU_NOTA_COMP3          | <p align="center"> Nota da competência 3 - Selecionar, relacionar, <br />organizar e interpretar <br />informações, fatos, opiniões e <br />argumentos em defesa de um <br />ponto de vista. </p> | Inteiro | 0 a 200 |
| NU_NOTA_COMP4          | <p align="center"> Nota da competência 4 - Demonstrar conhecimento <br />dos mecanismos linguísticos <br />necessários para a construção <br />da argumentação. </p> | Inteiro | 0 a 200 |
| NU_NOTA_COMP5          | <p align="center"> Nota da competência 5 - Elaborar proposta de <br />intervenção para o problema <br />abordado, respeitando os <br />direitos humanos. </p> | Inteiro | 0 a 200 |
| NU_NOTA_REDACAO        | <p align="center"> Nota da prova de redação | Inteiro | 0 a 1000 |                               
| Q006                   | <p align="center"> Corresponde à questão 6 do questionário socioeconômico, <br />o aluno deve informar a renda mensal de sua família. </p> | Caractere | “A” a “Q” |                

## 3. Análise dos resultados

<p align="justify"> Pode ser encontrada no arquivo pdf: <a href="https://github.com/pedroblq/P_enem/blob/main/Analise-dos-resultados.pdf" target="_blank">Análise dos resultados-pdf</a>. </p> 

Caso haja erro no arquivo de código upado acima, o mesmo pode ser acessado via: <a href="https://github.com/pedroblq/P_enem/blob/85c7c43b8fcc66c38163c5624c589cacf7c17426/PBC" target="_blank">Arquivo do código via Google Colab</a>

## 4. Metodologia

<p align="justify"> Neste trabalho utilizamos um estudo de caso, com dados providos de uma base de dados fornecida pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP). As análises foram feitas de forma quantitativa. A base de dados fornecida pelo INEP abrange todos os alunos que tomaram parte no Exame Nacional do Ensino Médio (ENEM). Para este trabalho consideramos a média do aluno em cada uma das 4 seções da prova (matemática, língua portuguesa, ciências da natureza e ciências humanas) e a redação, a classificação do aluno perante as cotas (raciais, de escola pública e sociais), faixa etária e o estado de realização da prova. </p>

<p align="justify"> A programação foi toda feita na linguagem Python, utilizando de bibliotecas como pandas, numpy e matplotlib. Toda a programação foi feita no software Google Colab e o upload foi feito para o repositório do github: <a href="https://github.com/pedroblq/P_enem.git" target="_blank">Trabalho PBC - Github</a>. </p>

<p align="justify"> Para a análise dos dados de 2022 direcionamos nossa atenção para as notas dos alunos e os possíveis limitantes presentes no contexto de cada um (tipo de educação, renda e sua cor de pele), para assim tentar localizar se existe alguma relação entre essas características com a média dos alunos, tanto nas questões objetivas quanto na redação. </p>

## 5. Conclusão

<p align="justify"> Esse trabalho analisou os dados dos estudantes que prestaram o ENEM 2022, tendo como principal objetivo evidenciar as diferenças das notas dos alunos de diferentes etnias e classes sociais. Além disso, também foi avaliado o tipo de escola que o candidato estudou e sua idade ao fazer a prova. </p>

<p align="justify"> Em primeiro momento já se torna evidente a necessidade das cotas raciais e sociais, uma vez que as maiores notas pertencem aos alunos que têm a maior renda, e quando analisamos por etnias vemos que os de pele branca tem destaque nas notas também. </p>

<p align="justify"> Quando tratamos sobre os tipos de escola que os estudantes frequentaram, as particulares e federais tomam a liderança, o que em parte evidencia ainda mais a análise que liga a renda com o desempenho (no caso das particulares), e ressalta o grande valor da educação de qualidade das federais brasileiras. Outro fator a ser ressaltado é como a maior diferença das notas vem na prova de matemática, mostrando que é uma área onde o ensino público brasileiro deixa a desejar. </p>

<p align="justify"> Ainda mais podemos perceber que a maioria dos candidatos estão na faixa de 17-19 anos, o que é esperado sendo essa a idade comum para os alunos terminarem o ensino médio. </p>

<p align="justify"> Assim nossa hipótese que os grupos mais privilegiados teriam as maiores notas se concretiza, uma vez que os alunos brancos, com mais dinheiro e muitas vezes de escolas particulares ocupam as maiores notas. </p>

