import wikipedia


def gets_summary(wiki_result: str) -> str:

    paragraph = wiki_result.split('. ')
    summary = paragraph[0] + '. '

    if len(summary) < 90:
        summary += paragraph[1] + '. '
        if len(summary) < 90:
            summary += paragraph[2] + '. '

    return summary


def search(query: str) -> str:
    wikipedia.set_lang('pt')

    if query == '' or query == ' ' * len(query):
        return 'A busca não pode ser vazia.'

    try:
        result = wikipedia.summary(query)

        summary = gets_summary(result)

        return summary

    except wikipedia.exceptions.DisambiguationError:
        return 'Encontrei muitos resultados para tal busca, por favor, seja mais específico.'

    except wikipedia.exceptions.PageError:
        return 'Não encontrei nenhuma página relacionada a essa busca.'

    except wikipedia.exceptions.WikipediaException:
        return 'Não encontrei nenhum parâmentro para buscar sobre.'
