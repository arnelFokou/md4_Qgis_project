aerian_material_cost = 500
semi_aerien_material_cost = 750
duct_material_cost = 900


worker_cost_per_day = 300
worker_cost_per_hour = worker_cost_per_day/8

aerian_duration_per_meter = 2
semi_aerian_duration_per_meter = 4
duct_duration_per_meter = 5

aerian_cost_per_meter = aerian_material_cost + aerian_duration_per_meter*worker_cost_per_hour
semi_aerian_cost_per_meter = semi_aerien_material_cost + semi_aerian_duration_per_meter*worker_cost_per_hour
duct_cost_per_meter = duct_material_cost + duct_duration_per_meter*worker_cost_per_hour
