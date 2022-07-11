from sqlalchemy.orm import Query


def print_result_to_console(purchases: Query, dictionary: dict) -> None:
    column_names = list(dictionary.keys())
    data = []
    for purchase in purchases:
        row = [upload(purchase) for upload in dictionary.values()]
        data.append(row)
    list_of_column = "\n".join("\t" + str(i) + ") " + str(x) for i, x in enumerate(column_names, 1))
    while True:
        try:
            index = int(input(f"Sorted by:\n{list_of_column}\n\n\tSelect -> "))
        except ValueError:
            print(f"Incorrect input! Enter integer 1 or {len(column_names)}.")
        else:
            if index not in range(1, len(column_names) + 1):
                print(f"Incorrect input! Enter integer 1 or {len(column_names)}.")
                continue
            else:
                try:
                    sort_kind = int(input("""Choose kind of sorting:
\t1) Ascending;
\t2) Descending.
    
\tSelection -> """))
                except ValueError:
                    print("Incorrect input! Enter integer 1 or 2.")
                else:
                    reverse = False
                    if sort_kind == 1:
                        reverse = True
                    elif sort_kind == 2:
                        pass
                    else:
                        print("Incorrect unput! Enter integer 1 or 2.")
                        continue

                    data = sorted(data, key=lambda x: x[index - 1], reverse=reverse)
                    print()

                    max_lengths = []
                    for index in range(len(column_names)):
                        column = [str(x[index]) for x in data]

                        max_length_of_data = max(len(x) for x in column)
                        length_of_column_name = len(column_names[index])
                        max_length_of_column = max(max_length_of_data, length_of_column_name) + 2
                        max_lengths.append(max_length_of_column)

                    template_for_data = []  #
                    for length in max_lengths:
                        template_for_data.append("{:^" + f"{length}" + "}")
                    template_for_data = "|" + "|".join(template_for_data) + "|"

                    template_for_line = []
                    for length in max_lengths:
                        template_for_line.append("-" * length)
                    template_for_line = "|" + "|".join(template_for_line) + "|"

                    """RENDERING TABLE"""

                    # SPLITTING LINE
                    print(template_for_line)

                    # HEADER
                    print(template_for_data.format(*column_names))

                    # SPLITTING LINE
                    print(template_for_line)

                    # DATA
                    for row in data:
                        print(template_for_data.format(*row))

                    # SPLITTING LINE
                    print(template_for_line)

                    # return
