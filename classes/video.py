class Video():

    def check_video_in_inventory(self,video_title):
        available_flag = False
        for video in self.videos:
            if video['title'] == video_title and int(video['copies_available']) >= 0:
                available_flag = True
                return(video)
            elif video['title'] == video_title and int(video['copies_available']) == 0:
                print(f"\nAll copies of {video['title']} are currently rented out\n")
                return
        if available_flag == False:
            print(f'\n{video_title} does not appear to be in our inventory.\n')
            return

    def check_return_video_in_inventory(self,video_title):
        video_flag = False
        for video in self.videos:
            if video['title'] == video_title:
                video_flag = True
                return(video)
        if video_flag == False:
            print(f'\n{video_title} was not found in the system\n')
            return


    