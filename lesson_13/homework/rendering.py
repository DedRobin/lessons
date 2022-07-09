from sqlalchemy.orm import Query


def rendering(query: Query, dictionary: dict) -> None:

    table_header = dictionary.keys()
    table_data = dictionary.values()

    max_lengths = [max(len(str(key)), len(str(value))) + 2 for key, value in dictionary.items()]
    template = []
    for length in max_lengths:
        template.append("{:^" + f"{length}" + "}")
    template = "|".join(template)
    print(template.format(*table_header))
    for purchase in query:
        print(template.format(*table_data))


