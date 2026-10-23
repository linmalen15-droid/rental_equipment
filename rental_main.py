from rental_tracker import collect_equipments, show_equipments
from rental_storage import load_equipments, save_equipments

#load previously stored products
all_equipments = load_equipments()

#collect new products from the user
new_equipments = collect_equipments()

#add new products to the existing list of products
all_equipments.extend(new_equipments)

#save the complete updated list
save_equipments(all_equipments)

#display the product summary
for equipment in new_equipments: 
    show_equipments(equipment)