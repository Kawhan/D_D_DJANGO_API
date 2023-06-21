class Validators_characters:
    @staticmethod
    def verify_correct_classe_armadura(data):
        """ Check armor class for characters  """

        return data['classe_armadura'] > 0

    @staticmethod
    def verify_correct_max_point_life(data):
        """ Check max life points is correct """

        return data['ponto_vida_max'] > 0

    @staticmethod
    def verify_correct_current_life_points(data):
        """ Check if current life points is correct  """

        return data['pontos_vida_atual'] > 0

    @staticmethod
    def verify_correct_temp_life_points(data):
        """ Check if temporary life points is correct """

        return data['pontos_vida_temp'] > 0

    validators_data_characters = {
        'classe_armadura': lambda data: data if Validators_characters.verify_correct_classe_armadura(data) else {'classe_armadura': 'The number of points to armor class is not correct! This number of points  must be greater than 0'},
        'pontos_vida_max ': lambda data: data if Validators_characters.verify_correct_max_point_life(data) else {'ponto_vida_max': 'The number of max life points  is not correct! This number of points  must be greater than 0'},
        'pontos_vida_atual': lambda data: data if Validators_characters.verify_correct_current_life_points(data) else {'pontos_vida_atual': 'The number of currect life points  is not correct! This number of points  must be greater than 0'},
        'pontos_vida_temp': lambda data: data if Validators_characters.verify_correct_temp_life_points(data) else {'pontos_vida_temp': 'The number of temporary life points  is not correct! This number of points  must be greater than 0'}
    }
