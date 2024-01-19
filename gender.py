from genderize import Genderize

def get_gender(sale_df, order_id):

    first_occurrence_index = sale_df.loc[sale_df['ORDERNUMBER'] == order_id].index[0]
    name = sale_df.loc[first_occurrence_index, ['CONTACTFIRSTNAME', 'CONTACTLASTNAME']]

    gender = Genderize().get(name)[0]['gender']

    return gender