class Options:
    def __init__(self):
        self.connection_string = 'DRIVER={SQL Server};SERVER=.;DATABASE=BFproject;Trusted_Connection=yes;'
        self.add_jenre = 'exec AddValuesInGenre'
        self.get_genre_by_user = 'exec GetGenreByUser'
        self.get_users_and_genre = 'GetUsersAndGenre'
