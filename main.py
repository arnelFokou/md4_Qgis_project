import pandas as pd

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
    return data_cleaned


print(clean_data(network_df,infra_df,building_df))