# O problema
O presente problema se refere aos dados de vinhos portugueses "Vinho Verde", que possuem
variantes de vinho branco e tinto. Devido a questões de privacidade, apenas variáveis
físico-químicas (input) e sensoriais (output) estão disponíveis (por exemplo, não há dados
sobre tipo de uva, marca do vinho, preço de venda, etc).

# Questões

a. Como foi a definição da sua estratégia de modelagem?
Escolhi utilizar as variáveis que tinham maior relação com a variável resposta: `quality`.

Eu escolhi testar 2 abordagens:
    - Regressão Linear,
    - Random Forests.

    Para a regressão linear os atributos foram normalizados utilizando-se z-score (com a lib StandardScale). A Random Forest não necessita desse pré processamento, mas foram feitas duas estratégias, com e sem otimização de hiperparâmetros.

b. Como foi definida a função de custo utilizada?

A função de custo, foi o mse (mean squared error). O RandomForestRegressor suporta essa função e o mae (mean absolute error). Já que o MSE penaliza mais erros maiores, ele é mais benefico que o MAE para esse problema (já que é preferível errar um pouco a nota do que errar por um valor muito alto).

c. Qual foi o critério utilizado na seleção do modelo final?

Média do mean squared error e r2. Assim temos uma métrica que é mais robusta aos erros e que obtém boas futuras medidas.

d. Qual foi o critério utilizado para validação do modelo? Por que escolheu utilizar este método?

O modelo foi validado utilizando-se as métricas de avaliação acima e o conjunto de teste, que foi composto por 30% dos dados do conjunto original. Com essa estratégia eu garanto que o modelo final possui resultados bons em dados que não foram utilizados para treinamento do modelo.


e. Quais evidências você possui de que seu modelo é suficientemente bom?

O modelo da Random Forest que foi treinado sem a otimização de hiperparâmetros possui a melhor média de erro e um bom desempenho para os valores intermédiarios de qualidade de vinho. O desempenho baixo para os valores 3 e 8 e 9 deve-se a quantidade de dados desses valores. Uma possível solução para esse problema seria transformar o problema em um classificador multiclasse (com valores de 3 à 9) e utilizar alguma técnica de balanceameneto de datasets (como over ou under sampling) para garantir que existirão valores para as qualidades que possuem poucos dados.


