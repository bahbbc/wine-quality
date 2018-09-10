# O problema
O presente problema se refere aos dados de vinhos portugueses "Vinho Verde", que possuem
variantes de vinho branco e tinto. Devido a questões de privacidade, apenas variáveis
físico-químicas (input) e sensoriais (output) estão disponíveis (por exemplo, não há dados
sobre tipo de uva, marca do vinho, preço de venda, etc).

# Questões

a. Como foi a definição da sua estratégia de modelagem?
Eu escolhi testar 2 abordagens:
    - Regressão Linear,
    - Random Forests.

    Para a regressão linear os atributos foram normalizados utilizando-se z-score (com a lib StandardScale). A Random Forest não necessita desse pré processamento, mas foram feitas duas estratégias, com e sem otimização de hiperparâmetros.

b. Como foi definida a função de custo utilizada?

mean_squared_error
c. Qual foi o critério utilizado na seleção do modelo final?

Menor mean_squared_error
d. Qual foi o critério utilizado para validação do modelo? Por que escolheu utilizar este método?
e. Quais evidências você possui de que seu modelo é suficientemente bom?
