import os
import csv
from classes.customer import Customer
from classes.video import Video

class Inventory():

    def view_current_inventory(self):
        for video in self.videos:
            print(video)
        
    def view_customers_rented_videos(self):
        customer_id = input(f'\nEnter your customer id:\t')
        for customer in self.customers:
            if customer['id'] == customer_id and customer['current_video_rentals'] != '':
                return(print(f"\n{customer['first_name']} {customer['last_name']} currently has the following movies checked out:\n\t\t {customer['current_video_rentals']}\n"))
            elif customer['id'] == customer_id and customer['current_video_rentals'] == '':
                return(print(f"\n{customer['first_name']} {customer['last_name']} currently has no movies checked out\n"))
        print(f'\nCustomer id not found\n')
                
    def rent_video_to_customer(self):
        customer_id = input(f'\nEnter customer id:\t')
        video_title = input(f'Enter video title:\t')
        customer_flag = False
        video = Video.check_video_in_inventory(self,video_title)
        customer = Customer.rent_match_customer(self,customer_id)
        if video == None or customer == None: 
            return
        if customer['current_video_rentals']=='':
            customer['current_video_rentals'] = video['title']
        else:
            customer['current_video_rentals'] += f"/{video['title']}"
        video['copies_available'] = str(int(video['copies_available']) - 1)
        Inventory.save('inventory',['id','title','rating','copies_available'],self.videos)
        Inventory.save('customers',['id','first_name','last_name','current_video_rentals'],self.customers)

    def return_video_from_customer(self):
        customer_id = input(f'\nEnter customer id:\t')
        video_title = input(f'Enter video title:\t')
        customer = Customer.return_match_customer(self,customer_id)
        video = Video.check_return_video_in_inventory(self,video_title)
        new_movie_list = Customer.extract_new_rented_list(self,customer,video_title)
        if customer == None or new_movie_list == None:
            return
        video['copies_available'] = str(int(video['copies_available']) + 1)
        customer['current_video_rentals'] = ('' if new_movie_list==[] else '/'.join(new_movie_list))
        Inventory.save('inventory',['id','title','rating','copies_available'],self.videos)
        Inventory.save('customers',['id','first_name','last_name','current_video_rentals'],self.customers)      

    def add_customer(self, high_cust_id):
        first_name = input(f'\nEnter first name:\t')
        last_name = input(f'\nEnter last name:\t')
        self.customers.append({
            'id': high_cust_id + 1,
            'first_name' : first_name,
            'last_name' : last_name,
            'current_video_rentals' : ''
        })
        Inventory.save('customers',['id','first_name','last_name','current_video_rentals'],self.customers)

    @classmethod
    def objects(cls,save_type):
        data = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../data/{save_type}.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        return data, int(row['id'])

    @classmethod
    def save(cls,save_type,headers_list,data):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../data/{save_type}.csv")
        final = []
        for x in data:
            final.append(list(x.values()))
        with open(path, 'w') as csvfile:
            data_csv = csv.writer(csvfile, delimiter=',')
            data_csv.writerow(headers_list)
            data_csv.writerows(final)
