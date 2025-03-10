def get_q_table_value(gamma : float, n: int) -> float:
    q_table = {
        "0.95": {
            "5": 1.37,
            "6": 1.09,
            "7": 0.92,
            "8": 0.80,
            "9": 0.71,
            "10": 0.65,
            "11": 0.59,
            "12": 0.55,
            "13": 0.52,
            "14": 0.48,
            "15": 0.46,
            "16": 0.44,
            "17": 0.42,
            "18": 0.40,
            "19": 0.39,
            "20": 0.37,
            "25": 0.32,
            "30": 0.28,
            "35": 0.26,
            "40": 0.24,
            "45": 0.22,
            "50": 0.21,
            "60": 0.188,
            "70": 0.174,
            "80": 0.161,
            "90": 0.151,
            "100": 0.143,
            "150": 0.115,
            "200": 0.099,
            "250": 0.089
        },
        "0.99":  {
            "5": 2.67,
            "6": 2.01,
            "7": 1.62,
            "8": 1.38,
            "9": 1.20,
            "10": 1.08,
            "11": 0.98,
            "12": 0.90,
            "13": 0.83,
            "14": 0.78,
            "15": 0.73,
            "16": 0.70,
            "17": 0.66,
            "18": 0.63,
            "19": 0.60,
            "20":0.58,
            "25":0.49,
            "30":0.43,
            "35":0.38,
            "40":0.35,
            "45":0.32,
            "50":0.30,
            "60": 0.269,
            "70": 0.245,
            "80": 0.226,
            "90": 0.211,
            "100": 0.198,
            "150": 0.160,
            "200": 0.136,
            "250": 0.120
            },
        "0.999": {
            "5": 5.64,
            "6": 3.88,
            "7": 2.98,
            "8": 2.42,
            "9": 2.06,
            "10": 1.80,
            "11": 1.60,
            "12": 1.45,
            "13": 1.33,
            "14": 1.23,
            "15": 1.15,
            "16": 1.07,
            "17": 1.01,
            "18": 0.96,
            "19": 0.92,
            "20": 0.88,
            "25": 0.73,
            "30": 0.63,
            "35": 0.56,
            "40": 0.50,
            "45": 0.46,
            "50": 0.43,
            "60":  0.38,
            "70":  0.34,
            "80":  0.31,
            "90":  0.29,
            "100":  0.27,
            "150":  0.211,
            "200":  0.185,
            "250":  0.162
        }
    }

    return q_table[str(gamma)][str(n)]
