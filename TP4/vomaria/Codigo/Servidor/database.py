lista_respostas = []


lista_usuarios = {'mario': 1,
          'BatmanCozineiro':1,
          'padeiro32': 1,
          'marcos': 1,
          'CangacoCozineiro': 1,
          'MestreDiarreia': 1,
          'animalDaCozinha': 1}

senhas = {'mario': 123,
          'BatmanCozineiro':123,
          'padeiro32': 123,
          'marcos': 123,
          'CangacoCozineiro': 132,
          'MestreDiarreia': 123,
          'animalDaCozinha': 123}

amigos = {'mario': "|BatmanCozineiro|padeiro32|CangacoCozineiro|MestreDiarreia|animalDaCozinha|marcos",
          'BatmanCozineiro': "|mario|padeiro32|CangacoCozineiro|MestreDiarreia|animalDaCozinha|marcos",
          'padeiro32': "|BatmanCozineiro|mario|CangacoCozineiro|MestreDiarreia|animalDaCozinha|marcos",
          'marcos':"|BatmanCozineiro|padeiro32|CangacoCozineiro|MestreDiarreia|animalDaCozinha|mario",
          'animalDaCozinha': "|BatmanCozineiro|padeiro32|CangacoCozineiro|MestreDiarreia|mario",
          'MestreDiarreia': "|BatmanCozineiro|padeiro32|CangacoCozineiro|animalDaCozinha|mario"}

receitas = {'mario': "|Bacalhau com limao|Bolo de sardinha|Carangueijo com quiabo|Feijoada de frando|Angu com laranja",
            'BatmanCozineiro': "|Bacalhau com limao|Bolo de sardinha|Carangueijo com quiabo|Feijoada de frando|Angu com laranja",
            'padeiro32': "|Bacalhau com limao|Bolo de sardinha|Carangueijo com quiabo|Feijoada de frando|Angu com laranja",
            'marcos': "|Bacalhau com limao|Bolo de sardinha|Carangueijo com quiabo|Feijoada de frando|Angu com laranja",
            'CangacoCozineiro': "|Bacalhau com limao|Bolo de sardinha|Carangueijo com quiabo|Feijoada de frando|Angu com laranja",
            'MestreDiarreia': "|Bacalhau com limao|Bolo de sardinha|Carangueijo com quiabo|Feijoada de frando|Angu com laranja",
            'animalDaCozinha': "|Bacalhau com limao|Bolo de sardinha|Carangueijo com quiabo|Feijoada de frando|Angu com laranja"}

descricoes = {'mario': "Meu nome e mario, tenho 150 anos e estudo computacao desde quando inventaram o computador e ate hoje nao sei nada. Meu shonho e formar.",
              'BatmanCozineiro': "Defendo gotan nas horas vagas e trabalho em uma padaria durante o dia.",
              'padeiro32': "Sou o trigesimo segundo padeiro da minha vila, meu sonho e me tornar o maior padeiro de todos os tempo e dominar todas as outras vilas.",
              'marcos': "Descricao com 65 caracteres, e apos cada 65 caracteres eu faco a quebra de linha pra poder ir pra a proxima linha. Descricao com 65 caracteres, e apos cada 65 caracteres eu faco a quebra de linha pra poder ir pra a proxima linha. Descricao com 65 caracteres.",
              'CangacoCozineiro': "OI",
              'animalDaCozinha': "Falo!!!!!!",
              'MestreDiarreia': "Gororoba do mais alto nivel!"}

receitas_preparo = {'Bacalhau_com_limao': "1kg de bacalhau|10 litros de vinagre]joga tudo na panela e torce pra dar certo.",
                    'Bolo_de_sardinha': "1kg de sardinha|10 litros de vinagre]joga tudo na panela e torce pra dar certo.",
                    'Carangueijo_com_quiabo': "1kg de carangueijo|10 litros de vinagre]joga tudo na panela e torce pra dar certo.",
                    'Feijoada_de_frando': "1kg de Feijao|10 litros de vinagre]joga tudo na panela e torce pra dar certo.",
                    'Angu_com_laranja': "1kg de laranja|10 litros de vinagre]joga tudo na panela e torce pra dar certo."}

garfadas = {'Bacalhau_com_limao': 10,
            'Bolo_de_sardinha': 8,
            'Carangueijo_com_quiabo': 17,
            'Feijoada_de_frando': 8000,
            'Angu_com_laranja': 21}