# Guerra Civil Brasileira Bot

[![Guerra Civil Brasileira Bot](img/banner.jpg)](https://ggvaldez.github.io/GuerraCivilBRBot/)

[![Share on Facebook](https://img.shields.io/badge/Share-Facebook-blue.svg)](https://www.facebook.com/sharer/sharer.php?u=#https://ggvaldez.github.io/GuerraCivilBRBot/)
[![Share on WhatsApp](https://img.shields.io/badge/Share-WhatsApp-brightgreen.svg)](https://wa.me/?text=https%3A%2F%2Fggvaldez.github.io%2FGuerraCivilBRBot%2F)
[![Share on Twitter](https://img.shields.io/twitter/url/https/ggvaldez.github.io/GuerraCivilBRBot.svg?style=social)](https://twitter.com/intent/tweet?url=https%3A%2F%2Fggvaldez.github.io%2FGuerraCivilBRBot%2F)
![GitHub stars](https://img.shields.io/github/stars/ggvaldez/GuerraCivilBRBot.svg?style=social)
![GitHub forks](https://img.shields.io/github/forks/ggvaldez/GuerraCivilBRBot.svg?style=social)

**Algorítimo feito por fans da página [Guerra Civil Brasileira Bot](https://www.facebook.com/GCBrasileiraBot).**

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
- Escolhe aleatóriamente qual o estado a ser atacado ou se será via água
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
