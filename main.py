import pandas as pd
from config import *

#Import data
network_df = pd.read_excel("./data/reseau_en_arbre.xlsx")
infra_df = pd.read_csv("./data/infra.csv")
building_df = pd.read_excel("./data/batiments.xlsx")

#Processing data
def clean_data(network_df,infra_df,building_df):
    network_df = network_df[network_df['infra_type']=='a_remplacer']
    infra_df = pd.merge(network_df,infra_df, how='left', left_on='infra_id', right_on='id_infra')
    infra_df.drop(columns=['infra_id','nb_maisons','infra_type'],inplace=True)
    data_cleaned = pd.merge(infra_df,building_df,how='left',on='id_batiment')
    data_cleaned.drop_duplicates(inplace=True)
    return data_cleaned

def rebuilding_cost(dataframe):
    total_amount=0    
    for _,line in dataframe.iterrows():
        longueur = line['longueur']
        if line['type_infra'] == 'aerien':
            total_amount += longueur*aerian_cost_per_meter
        elif line['type_infra'] == 'semi-aerien':
            total_amount += longueur*semi_aerian_cost_per_meter
        elif line['type_infra'] == 'fourreau':
            total_amount += longueur*duct_cost_per_meter
        else:
            print(f"valeur non prise en charge{_,line['type_infra']}")
    return total_amount






dataset_cleaned = clean_data(network_df,infra_df,building_df)
print(f"le montant total est de {rebuilding_cost(dataset_cleaned):.2f} euros")