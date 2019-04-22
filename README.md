# Guerra Civil Brasileira Bot

[![Guerra Civil Brasileira Bot](img/banner.jpg)](https://ggvaldez.github.io/GuerraCivilBRBot/)

[![Share on Facebook](img/facebook.svg)](https://www.facebook.com/sharer/sharer.php?u=#https://ggvaldez.github.io/GuerraCivilBRBot/)
[![Share on WhatsApp](img/whatsapp.svg)](https://wa.me/?text=https%3A%2F%2Fggvaldez.github.io%2FGuerraCivilBRBot%2F)
[![Share on Twitter](img/twitter.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Fggvaldez.github.io%2FGuerraCivilBRBot%2F)
[![GitHub stars](https://img.shields.io/github/stars/ggvaldez/GuerraCivilBRBot.svg?style=social)](https://github.com/ggvaldez/GuerraCivilBRBot/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ggvaldez/GuerraCivilBRBot.svg?style=social)](https://github.com/ggvaldez/GuerraCivilBRBot/network/members)
[![Download](img/download.svg)](https://github.com/ggvaldez/GuerraCivilBRBot/archive/master.zip)

**Algorítimo feito por fans da página [Guerra Civil Brasileira Bot](https://www.facebook.com/GCBrasileiraBot).**

## Como executar

Por padrão calcula-se 10.000 simulações e a saída é por ordem alfabétida dos
estados brasileiros. Execute os comandos abaixo no seu terminal:

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

### Todos os sistemas operacionais

- **Python 2.7**
- git _(Apenas necessário caso não faça download direto do repositório)_

### Windows
No Windows, você também precisara de um terminal de comando. Caso já não tenha
um, pode usar a recomendação a seguir:

- [Comder, **versão full**](https://cmder.net/)

<!--
- https://en.wikipedia.org/wiki/Military_simulation

-->

# Autor
Gustavo Valdez <work(at)ggvaldez.com>
