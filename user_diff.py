import numpy as np


def find_diff(usr_file_path):
    followings = []
    followers = []
    with open(usr_file_path + '/followers.txt', 'r') as file:
        lines = file.readlines()
        followers = [line.strip() for line in lines]
    with open(usr_file_path + '/followings.txt', 'r') as file:
        lines = file.readlines()
        followings = [line.strip() for line in lines]

    diff_a_b = np.setdiff1d(followers, followings)
    diff_b_a = np.setdiff1d(followings, followers)

    file = open(usr_file_path + '/only_in_followers', "w")
    for user in diff_a_b:
        file.write(user)
        file.write("\n")
    file.close()

    file = open(usr_file_path + '/only_in_followings', "w")
    for user in diff_b_a:
        file.write(user)
        file.write("\n")
    file.close()