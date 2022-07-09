from sqlalchemy.orm import Query

from lesson_13.homework.models import Purchase


def rendering(purchases: Query, dictionary: dict[str: Purchase]) -> None:
    some_func = dictionary["User name"]
    print(some_func(purchases[1]))
    table_header = dictionary.keys()

    """
    for length in max_lengths:
        template.append("{:^" + f"{length}" + "}")
    template = "|".join(template)
    """


