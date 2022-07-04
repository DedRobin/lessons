from sqlalchemy import inspect

from create_session import create_current_session
from models import *


def _max_lenght_charachters_in_each_column(fields: list, column_names: list) -> list:
    highs = []
    for index in range(len(column_names)):
        high = max([len(str(value[index])) for value in fields] + [len(column_names[index])])
        highs.append(high)
    return highs


def show_table(model_object: list) -> None:
    session = create_current_session()
    LENGHT_COLUMN = 60
    fields = []

    if isinstance(model_object[0], User):
        all_columns = [column.name for column in inspect(User).c]
        print(("|" + "-" * LENGHT_COLUMN) * len(all_columns) + "|")
        string = "|" + ("{:^" + str(LENGHT_COLUMN) + "}|") * len(all_columns)
        print(string.format(*all_columns))
        print(("|" + "-" * LENGHT_COLUMN) * len(all_columns) + "|")
        for current_user in model_object:
            fields.append([current_user.id,
                           current_user.email,
                           current_user.password])

    elif isinstance(model_object[0], Profile):
        all_columns = [column.name for column in inspect(Profile).c]
        print(("|" + "-" * LENGHT_COLUMN) * len(all_columns) + "|")
        string = "|" + ("{:^" + str(LENGHT_COLUMN) + "}|") * len(all_columns)
        print(string.format(*all_columns))
        print(("|" + "-" * LENGHT_COLUMN) * len(all_columns) + "|")
        for current_profile in model_object:
            fields.append([current_profile.id,
                           current_profile.name,
                           current_profile.phone,
                           current_profile.age,
                           current_profile.user.id])

    elif isinstance(model_object[0], Address):
        all_columns = [column.name for column in inspect(Address).c]
        print(("|" + "-" * LENGHT_COLUMN) * len(all_columns) + "|")
        string = "|" + ("{:^" + str(LENGHT_COLUMN) + "}|") * len(all_columns)
        print(string.format(*all_columns))
        print(("|" + "-" * LENGHT_COLUMN) * len(all_columns) + "|")
        for current_address in model_object:
            fields.append([current_address.id,
                           current_address.city,
                           current_address.address.replace("\n", " "),
                           current_address.user.id])

    elif isinstance(model_object[0], Product):
        all_columns = [column.name for column in inspect(Product).c]
        print(("|" + "-" * LENGHT_COLUMN) * len(all_columns) + "|")
        string = "|" + ("{:^" + str(LENGHT_COLUMN) + "}|") * len(all_columns)
        print(string.format(*all_columns))
        print(("|" + "-" * LENGHT_COLUMN) * len(all_columns) + "|")
        for current_product in model_object:
            fields.append([current_product.id,
                           current_product.product_name,
                           current_product.price,
                           current_product.product_quantity,
                           current_product.comment])

    elif isinstance(model_object[0], Purchase):
        all_columns = [column.name for column in inspect(Purchase).c]
        for current_purchase in model_object:
            fields.append([current_purchase.id,
                           current_purchase.purchase_quantity,
                           current_purchase.user.id,
                           current_purchase.product.id])

        hihgs = _max_lenght_charachters_in_each_column(fields, all_columns)

        # TOP LINE
        header = ["|"]
        for index_of_column in range(len(all_columns)):
            header.append(("-" * hihgs[index_of_column]) + "|")
        header = "".join(header)
        print(header)

        # NAME OF COLUMNS
        name_of_columns = ["|"]
        for index_of_column in range(len(all_columns)):
            name_of_columns.append(("{:^" + str(hihgs[index_of_column]) + "}|"))
        name_of_columns = "".join(name_of_columns)
        print(name_of_columns.format(*all_columns))

        # MIDDLE LINE
        print(header)

        # DATA
        for field in fields:
            content = ["|"]
            for index_of_column in range(len(all_columns)):
                content.append(("{:^" + str(hihgs[index_of_column]) + "}|"))
            content = "".join(content)
            print(content.format(*field))

    # BOT LINE

    bot = ["|"]
    for index_of_column in range(len(all_columns)):
        bot.append(("-" * hihgs[index_of_column]) + "|")
    print("".join(bot))


if __name__ == '__main__':
    test_session = create_current_session()

    # print("User")
    # test_user = test_session.query(User)
    # show_table(test_user)
    #
    # print("Product")
    # test_model = test_session.query(Product)
    # show_table(test_model)
    #
    # print("Profile")
    # test_profile = test_session.query(Profile)
    # show_table(test_profile)

    print("Purchase")
    test_purchase = test_session.query(Purchase)
    show_table(test_purchase)
    #
    # print("Address")
    # test_address = test_session.query(Address)
    # show_table(test_address)
