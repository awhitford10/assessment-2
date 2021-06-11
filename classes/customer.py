class Customer():

    def rent_match_customer(self,customer_id):
        customer_flag = False
        for customer in self.customers:
            if customer['id'] == customer_id and len(customer['current_video_rentals'].split('/')) < 3:
                customer_flag = True
                return(customer)
            elif customer['id'] == customer_id and len(customer['current_video_rentals'].split('/')) == 3:
                print(f'\n{customer["first_name"]} {customer["last_name"]} already has 3 items checked out. Please return one before checking out any more.')
                return
        if customer_flag == False:
            print(f'\nWe cannot find your customer id in the system\n')
            return

    def return_match_customer(self,customer_id):
        customer_flag = False
        for customer in self.customers:
            if customer['id'] == customer_id:
                customer_flag = True
                return(customer)
        if customer_flag == False:
            print(f'\nThe customer id was not found in the system\n')
            return

    def extract_new_rented_list(self,customer,video_title):
        final_flag = False
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
            return
        return(new_movie_list)

        

    