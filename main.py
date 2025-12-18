import pandas as pd
from config import *
from infras import Infra
from buildings import Buildings

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
    dataframe_selected = dataframe[['id_infra','longueur','type_infra']].drop_duplicates('id_infra')
    for _,line in dataframe_selected.iterrows():
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

def time_to_rebuild_hospital(dataframe):
    list_times =[]
    hospital = dataframe[dataframe['type_batiment']=='hôpital']
    for _,line in hospital.iterrows():
        longueur = line['longueur']
        if line['type_infra'] == 'aerien':
            list_times.append(aerian_duration_per_meter* longueur/ max_workers_per_infra)
        elif line['type_infra'] == 'semi-aerien':
            list_times.append(semi_aerian_duration_per_meter* longueur/ max_workers_per_infra)
        elif line['type_infra'] == 'fourreau':
            list_times.append(duct_duration_per_meter* longueur/ max_workers_per_infra)
        else:
            print(f"valeur non prise en charge{_,line['type_infra']}")
    return max(list_times)

def create_objects(dataframe):   
    for infra in set(dataframe.id_infra):
        longueur = dataframe[dataframe['id_infra']==infra].longueur.values[0]
        nb_maisons = dataframe[dataframe['id_infra']==infra].nb_maisons.sum()
  
        infras[infra] = Infra(infra_id=infra,
                              longueur=longueur,
                              nb_maisons=nb_maisons,
                              infra_state='a_remplacer')
    
    for building in set(dataframe.id_batiment):
        infras_buildings = list(dataframe[dataframe['id_batiment']==building].id_infra.values)
        liste_infras = [infras[infra] for infra in infras_buildings]
        buildings[building] = Buildings(id_building = building, liste_infras = liste_infras )

    

dataset_cleaned = clean_data(network_df,infra_df,building_df)
# print(dataset_cleaned.head(20))
# dataset_cleaned.to_csv('dataset.csv')
# infras={}
# buildings = {}
# create_objects(dataset_cleaned)
# print(infras['P000462'].get_infra_difficulty())
print(f"le montant total est de {rebuilding_cost(dataset_cleaned):.2f} euros")
print(f"le temps de reparation des infrastructures pour atteindre l'hopital est de: {time_to_rebuild_hospital(dataset_cleaned)}")
