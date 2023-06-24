class Validators_characters:
    @staticmethod
    def verify_correct_classe_armadura(data):
        """ Check armor class for characters  """

        return data['armor_class'] > 0

    @staticmethod
    def verify_correct_max_point_life(data):
        """ Check max life points is correct """

        return data['max_life_point'] > 0

    @staticmethod
    def verify_correct_current_life_points(data):
        """ Check if current life points is correct  """

        return data['current_life_points'] > 0

    @staticmethod
    def verify_correct_temp_life_points(data):
        """ Check if temporary life points is correct """

        return data['points_life_temp'] > 0

    validators_data_characters = {
        'armor_class': lambda data: data if Validators_characters.verify_correct_classe_armadura(data) else {'armor_class': 'The number of points to armor class is not correct! This number of points  must be greater than 0'},
        'max_life_point ': lambda data: data if Validators_characters.verify_correct_max_point_life(data) else {'max_life_point': 'The number of max life points  is not correct! This number of points  must be greater than 0'},
        'current_life_points': lambda data: data if Validators_characters.verify_correct_current_life_points(data) else {'current_life_points': 'The number of currect life points  is not correct! This number of points  must be greater than 0'},
        'points_life_temp': lambda data: data if Validators_characters.verify_correct_temp_life_points(data) else {'points_life_temp': 'The number of temporary life points  is not correct! This number of points  must be greater than 0'}
    }
