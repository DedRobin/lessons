import numpy as np
from sqlalchemy.orm import Query


def rendering(purchases: Query, dictionary: dict) -> None:
    column_names = np.array(list(dictionary.keys()))
    data = []
    for purchase in purchases:
        row = [upload(purchase) for upload in dictionary.values()]
        data.append(row)

    data_as_np_array = np.array(data)

    max_lengths = []
    for index in range(len(column_names)):
        column = data_as_np_array[:, index]
        max_length_of_data = max(len(x) for x in column)
        length_of_column_name = len(column_names[index])
        max_length_of_column = max(max_length_of_data, length_of_column_name) + 2
        max_lengths.append(max_length_of_column)

    template = []  #
    for length in max_lengths:
        template.append("{:^" + f"{length}" + "}")
    template = "|" + "|".join(template) + "|"

    template_for_line = []
    for length in max_lengths:
        template_for_line.append("-" * length)
    template_for_line = "|" + "|".join(template_for_line) + "|"

    # RENDERING TABLE

    # SPLITTING LINE
    print(template_for_line)

    # HEADER
    print(template.format(*column_names))

    # SPLITTING LINE
    print(template_for_line)

    # DATA
    for x in data:
        print(template.format(*x))

    # SPLITTING LINE
    print(template_for_line)
