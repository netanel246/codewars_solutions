
def switch_dict(dic):
    res = {}
    for k, v in dic.items():
        if v in res.keys():
            res[v].append(k)
        else:
            res[v] = [k]
    return res


if __name__ == "__main__":
    before = {
        'Ice': 'Cream',
        'Age': '21',
        'Light': 'Cream',
        'Double': 'Cream'
    }

    expected_ans = {
        'Cream': ['Ice', 'Double', 'Light'],
        '21': ['Age']
    }

    print(switch_dict(before))
    print(expected_ans)