def create_features(data):
    # Age groups
    data['age_group_Senior'] = int(data['age'] > 50)
    data['age_group_Young'] = int(data['age'] < 30)

    # Balance group
    data['balance_group_Low'] = int(data['balance'] < 50000)

    # Credit score groups
    data['credit_score_group_Low'] = int(data['credit_score'] < 500)
    data['credit_score_group_Medium'] = int(500 <= data['credit_score'] <= 700)

    # One-hot encoding manually
    data['country_Germany'] = 1 if data['country'] == "Germany" else 0
    data['country_Spain'] = 1 if data['country'] == "Spain" else 0

    data['gender_Male'] = 1 if data['gender'] == "Male" else 0

    # Remove raw categorical
    data.pop('country')
    data.pop('gender')

    return data