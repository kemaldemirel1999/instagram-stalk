from user_data import scrape
from user_diff import find_diff
import os

if __name__ == '__main__':
    usr = input('[Required] - Whose followers do you want to scrape: ')
    usr_file_path = os.getcwd() + "/" + usr + "/"
    again = input('Do you want to scrape again but it may take long time. If you want, type [Y]')

    if not os.path.exists(os.getcwd() + "/" + usr):
        os.mkdir(os.getcwd() + "/" + usr)

    if again == "Y":
        scrape(usr, usr_file_path)
        find_diff(usr)
    else:
        if os.path.exists(usr_file_path+'followings.txt') and os.path.exists(usr_file_path+'followers.txt'):
            find_diff(usr)
        else:
            scrape(usr, usr_file_path)
            find_diff(usr)


