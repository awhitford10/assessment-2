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
        available_flag, customer_flag = False, False
        for video in self.videos:
            if video['title'] == video_title and int(video['copies_available']) >= 0:
                available_flag = True
                break
            elif video['title'] == video_title and int(video['copies_available']) == 0:
                print(f"\nAll copies of {video['title']} are currently rented out\n")
                return
        if available_flag == False:
            print(f'\n{video_title} does not appear to be in our inventory.\n')
            return
        for customer in self.customers:
            if customer['id'] == customer_id and len(customer['current_video_rentals'].split('/')) < 3:
                customer_flag = True
                break
            elif customer['id'] == customer_id and len(customer['current_video_rentals'].split('/')) == 3:
                print(f'\n{customer["first_name"]} {customer["last_name"]} already has 3 items checked out. Please return one before checking out any more.')
                return
        if customer_flag == False:
            print(f'\nWe cannot find your customer id in the system\n')
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
        video_flag, customer_flag, final_flag = False, False,False
        for customer in self.customers:
            if customer['id'] == customer_id:
                customer_flag = True
                break
        if customer_flag == False:
            print(f'\nThe customer id was not found in the system\n')
            return
        for video in self.videos:
            if video['title'] == video_title:
                video_flag = True
                break
        if video_flag == False:
            print(f'\n{video_title} was not found in the system\n')
            return
        customer_movie_list = customer['current_video_rentals'].split('/')
        new_movie_list = []
        for x in customer_movie_list:
            if x == video_title:
                final_flag = True
                continue
            else:
                new_movie_list.append(x)
        if final_flag == False:
            print(f'\n{video_title} does not seem to be checked out to you\n')

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
