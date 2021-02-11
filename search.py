import wikipedia


def search(query):
    wikipedia.set_lang('pt')

    try:
        search = wikipedia.summary(query).split('. ')
        return search[0]

    except wikipedia.exceptions.DisambiguationError:
        return 'Encontrei muitos resultados para tal busca, por favor, seja mais específico'

    except wikipedia.exceptions.PageError:
        return 'Não encontrei nenhuma página relacionada a essa busca'

    except wikipedia.exceptions.WikipediaException:
        return 'Não encontrei nenhum parâmentro para buscar sobre'


if __name__ == '__main__':
    print(search('abraham lincoln'))
    print(search('dhuashdsadas'))
    print(search(''))
    print(search('   '))
