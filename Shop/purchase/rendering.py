from sqlalchemy.orm import Query


def rendering(purchases: Query, dictionary: dict) -> None:
    column_names = list(dictionary.keys())
    data = []
    for purchase in purchases:
        row = [upload(purchase) for upload in dictionary.values()]
        data.append(row)
    r_column_names = "\n".join("\t" + str(i) + ") " + str(x) for i, x in enumerate(column_names[1:], 1))
    index = int(input(f"Sorted by:\n{r_column_names} \n\tSelect -> "))
    data = sorted(data, key=lambda x: x[index])
    # if selection == 1:
    #     data = sorted(data, key=lambda x: x[1])  # BY USER NAME
    # elif selection == 2:
    #     data = sorted(data, key=lambda x: x[2])  # BY USER EMAIL
    # elif selection == 3:
    #     data = sorted(data, key=lambda x: x[3])  # BY USER PHONE
    # elif selection == 4:
    #     data = sorted(data, key=lambda x: x[4])  # BY USER AGE
    # elif selection == 5:
    #     data = sorted(data, key=lambda x: x[5])  # BY USER CITY
    # elif selection == 6:
    #     data = sorted(data, key=lambda x: x[6])  # BY USER ADDRESS
    # elif selection == 7:
    #     data = sorted(data, key=lambda x: x[7])  # BY PRODUCT NAME
    # elif selection == 8:
    #     data = sorted(data, key=lambda x: x[8])  # BY PRODUCT PRICE
    # elif selection == 9:
    #     data = sorted(data, key=lambda x: x[9])  # BY PRODUCT COMMENT
    # elif selection == 10:
    #     data = sorted(data, key=lambda x: x[10])  # BY PRODUCT QUANTITY
    # elif selection == 11:
    #     data = sorted(data, key=lambda x: x[11])  # BY PURCHASE QUANTITY

    max_lengths = []
    for index in range(len(column_names)):
        # column = data_as_np_array[:, index]
        column = [str(x[index]) for x in data]

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
    for row in data:
        print(template.format(*row))

    # SPLITTING LINE
    print(template_for_line)
