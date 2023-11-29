# Entrega projeto PBC

## Introdução

<p align="justify"> O Exame Nacional do Ensino Médio (ENEM) é um dos passos mais importantes da
trajetória de qualquer estudante no nosso país, porém é de conhecimento comum que nem
todos têm as mesmas oportunidades, assim gerando uma desigualdade entre eles. </p>

<p align="justify"> Para combater esse problema foram criadas diversas cotas para todas as categorias de estudantes, sendo elas baseadas em raça, em renda ou em deficiências. Assim, pessoas que possam possivelmente ter tido seu aprendizado prejudicado por fatores diversos ganham o direito de competir somente com pessoas com situações semelhantes pelas vagas separadas para o seu grupo de cotas. </p>

<p align="justify"> Ademais, é importante ressaltar a presença dos dados referentes às escolas em que cada aluno se formou, assim abrindo margem para uma comparação entre os formandos de escolas públicas e particulares, dentro e fora das cotas. </p>

<p align="justify"> Portanto, dadas informações citadas acima, o assunto em questão possui como objetivo apresentar dados, a fim de fornecer uma análise abrangente e detalhada sobre os resultados do ENEM 2022, examinando minuciosamente as informações coletadas, esperando com que tais contribuam para a compreensão das possíveis correlações entre variáveis socioeconômicas presentes na realização do exame e em sua obtenção de resultados. </p>

<p align="justify"> Logo, diante da nossa hipótese, pode-se ser esperado que ao decorrer das análises, se obtenha um resultado que mostre como as diferenças avaliadas beneficiem o grupo social cujas condições estivessem mais favoráveis ao sucesso das notas do que a obtenção de um resultado negativo, visto que atualmente, dentre as diversas esferas da sociedade, os grupos que apresentam dificuldades estruturais e/ou econômicas, são mais suscetíveis à falha por não apresentarem as mesmas oportunidades que os demais. </p>

## Descrição da base de dados

<p align="justify"> A base de dados a ser utilizada no trabalho será os Microdados do Enem 2022, que podem ser encontrados em: <a href="https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem" target="_blank">Enem-Inep</a>. </p>

<p align="justify"> Os dados presentes na base, englobam o número de inscrição do participante, o qual é apenas uma máscara, logo não representa o número original, informações básicas sobre os inscritos, como a faixa etária, que varia de menor de 17 anos até maior de 70 anos, o sexo, estado civil, cor/raça, nacionalidade, o ano de conclusão do ensino médio, o tipo de escola que estudou no ensino médio (pública ou privada) e se o inscrito é considerado treineiro, no caso de não concluir o ensino médio em 2022. </p>

<p align="justify"> Também estão presentes dados sobre a escola do participante, como a sigla do estado e o nome do município em que a escola está localizada, a dependência administrativa (federal, estadual, municipal ou privada) e localização (urbana ou rural). E  a sigla do estado e o nome do município de aplicação da prova. </p>

<p align="justify"> Além disso, pode-se encontrar os dados da prova objetiva e da redação, o primeiro inclui a presença nas provas dos dois dias (ciências da natureza, ciências humanas, linguagens e códigos e matemática), a língua estrangeira escolhida pelo participante, o código das provas aplicadas (cor, libras, digital, reaplicação), a nota que o inscrito obteve em cada prova, vetor com as respostas dos participantes e vetor com o gabarito de cada prova. O segundo, a nota total obtida na redação, a nota de cada competência (da 1ª a 5ª) e a situação da redação (anulada, em branco, fuga do tema, texto insuficiente, sem problemas). </p>

<p align="justify"> O último item da base de dados, apresenta as questões e as respostas do questionário socioeconômico, o qual é composto por 25 perguntas, que contêm o nível de escolaridade e a ocupação dos pais do participante, a quantidade de de pessoas que moram com o inscrito, a renda mensal da família, características da residência e se tem acesso à internet. </p>

<p align="justify"> Por fim, a base de dados a ser utilizada apresenta 76 colunas e 1048576 linhas. </p>



|  Nome da coluna        | Descrição                     | Tipo      | Valores esperados       | 
| ---------------------- | ----------------------------- | --------- | ----------------------- |
| TP_FAIXA_ETARIA        | Faixa etária                  | Inteiro   | 1 a 20 |
| TP_SEXO                | Sexo                          | Caractere | "F" e "M" |
| TP_COR_RACA            | Cor/raça                      | Inteiro   | 0 a 6 |
| TP_ST_CONCLUSAO        | Situação de conclusão do <br />Ensino Médio | Inteiro | 1 a 4 |
| TP_ANO_CONCLUIU        | Ano de Conclusão do Ensino <br />Médio | Inteiro | 0 a 16 |                       
| TP_ESCOLA              | Tipo de escola do Ensino <br />Médio | Inteiro | 1 a 3 |
| TP_ENSINO              | Tipo de instituição que <br />concluiu ou concluirá o <br />Ensino Médio | Inteiro | 1 ou 2 | 
| IN_TREINEIRO           | Indica se o inscrito fez a <br />prova com intuito de apenas <br />treinar seus conhecimentos | Inteiro | 0 ou 1 | 
| NO_MUNICIPIO_ESC       | Nome do município da escola | String | “Vitória”, “São Paulo”, <br />“Rio de Janeiro” etc |
| SG_UF_ESC              | Sigla da Unidade da <br />Federação da escola | String | “ES”, “SP”, “RJ”, “AM" <br />etc |
| TP_DEPENDENCIA_ADM_ESC | Dependência administrativa <br />(Escola) | Inteiro | 1 a 4 |   
| TP_PRESENCA_CN         | Presença na prova objetiva de <br />Ciências da Natureza | Inteiro | 0 a 2 |
| TP_PRESENCA_CH         | Presença na prova objetiva de <br />Ciências Humanas | Inteiro | 0 a 2 |   
| TP_PRESENCA_LC         | Presença na prova objetiva de <br />Linguagens e Códigos | Inteiro | 0 a 2 | 
| TP_PRESENCA_MT         | Presença na prova objetiva de <br />Matemática | Inteiro | 0 a 2 |      
| NU_NOTA_CN             | Nota da prova de Ciências da <br />Natureza | Float | 0 a 1000 |            
| NU_NOTA_CH             | Nota da prova de Ciências <br />Humanas | Float | 0 a 1000 |           
| NU_NOTA_LC             | Nota da prova de Linguagens <br />e Códigos | Float | 0 a 1000 |    
| NU_NOTA_MT             | Nota da prova de Matemática | Float| 0 a 1000 |                              
| TP_LINGUA              | Língua Estrangeira | Inteiro | 0 ou 1 |                                
| TP_STATUS_REDACAO      | Situação da redação do <br />participante | Inteiro | 1 a 9 |
| NU_NOTA_COMP1          | Nota da competência 1 - <br />Demonstrar domínio da <br />modalidade escrita formal da <br />Língua Portuguesa. | Inteiro | 0 a 200 |
| NU_NOTA_COMP2          | Nota da competência 2 - <br />Compreender a proposta de <br />redação e aplicar conceitos <br />das várias áreas de <br />conhecimento para desenvolver <br />o tema, dentro dos limites <br />estruturais do texto <br />dissertativo-argumentativo <br />em prosa. | Inteiro |  0 a 200 |
| NU_NOTA_COMP3          | Nota da competência 3 - <br />Selecionar, relacionar, <br />organizar e interpretar <br />informações, fatos, opiniões e <br />argumentos em defesa de um <br />ponto de vista. | Inteiro | 0 a 200 |
| NU_NOTA_COMP4          | Nota da competência 4 - <br />Demonstrar conhecimento <br />dos mecanismos linguísticos <br />necessários para a construção <br />da argumentação. | Inteiro | 0 a 200 |
| NU_NOTA_COMP5          | Nota da competência 5 - <br />Elaborar proposta de <br />intervenção para o problema <br />abordado, respeitando os <br />direitos humanos. | Inteiro | 0 a 200 |
| NU_NOTA_REDACAO        | Nota da prova de redação | Inteiro | 0 a 1000 |                               
| Q006                   | Corresponde à questão 6 do <br />questionário socioeconômico, <br />o aluno deve informar a renda <br />mensal de sua família. | Caractere | “A” a “Q” |                

