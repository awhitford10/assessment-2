from classes.inventory import Inventory

class Interface():
    def __init__(self):
        self.customers, self.high_cust_id = Inventory.objects('customers')
        self.videos, self.high_vid_id = Inventory.objects('inventory')
    
    def run(self):

        print(f'\nWelcome to to DrewBuster Videos!!!\n')

        while True:
            response = input(f"\nWhat would you like to do?\n1. View video inventory\n2. View customer's rented videos\n3. Rent video\n4. Return video\n5. Add new customer\n6. Exit\n\n")

            if response == '1':
                Inventory.view_current_inventory(self)
                

            elif response == '2':
                Inventory.view_customers_rented_videos(self)

            elif response == '3':
                Inventory.rent_video_to_customer(self)
                
            elif response == '4':
                Inventory.return_video_from_customer(self)

            elif response == '5':
                Inventory.add_customer(self, self.high_cust_id)
                self.high_cust_id += 1

            elif response == '6':
                break

            else:
                print(f'\nInvaild input\n\n')


