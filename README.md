# Guerra Civil Brasileira Bot
Algorítimo feito por fans da página [Guerra Civil Brasileira Bot](https://www.facebook.com/GCBrasileiraBot)

## Como executar

Exibe-se os estados em ordem alfabética. O padrão é 10.000 simulações.

```sh
git clone https://github.com/ggvaldez/GuerraCivilBRBot.git
cd GuerraCivilBRBot
python2.7 bot.py
```

Para ter o resultado ordenado de forma descrecente:

```sh
python2.7 bot.py | sort -k2 -r -n -t':'
```

## Do algorítimo
> Aviso: esta implementação pode ser considera como um exemplo de
  _jogos de guerra_, mas não é, nem pretende ser, uma [simulação militar](https://en.wikipedia.org/wiki/Military_simulation) <sup>(destino em inglês)</sup>.

- Escolhe aleatóriamente um dos estados atacantes
- Escolhe aleatóriamente se a fronteira será via terra ou via água
    - Se via água, o estado atacante atacará um outro estado banhado pelo oceano
      atlântico.

## Requisitos

- Python 2.7
- git

<!--
- https://en.wikipedia.org/wiki/Military_simulation

-->

# Autor
Gustavo Valdez <work(at)ggvaldez.com>