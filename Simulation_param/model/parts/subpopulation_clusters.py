# Computed clusters data

clusters = ['0','1','2','3','4','5','6','7','8','9']

mixingAgents = ['0','1','2','3','4','5','6','7','8','9','external']

clustersMedianSourceBalance = [310.0,174.5,206.38,64767.51,229.17,251652.0,18304.36,211.7,250.5,310.0]

clusters1stQSourceBalance = [112.53,119.22,100.46,64767.51,100.0,251652.0,14050.3,109.42,102.46,150.72]

clusters3rdQSourceBalance = [800.24,540.43,582.48,64767.51,924.5,251652.0,24857.5,670.44,968.88,1458.79]

clustersMu = [291.21,606.38,514.12,1589.17,527.76,3909.86,1291.45,601.12,457.42,1783.02]

clustersSigma = [731.89,1529.2,1882.62,5646.55,1337.06,8736.56,3381.92,1548.68,1496.74,7596.17]

UtilityTypesOrdered = {'0': {'Food/Water': 1,
  'Farming/Labour': 2,
  'Shop': 3,
  'Fuel/Energy': 4,
  'None': 5,
  'Transport': 6,
  'Savings Group': 7,
  'Education': 8,
  'Health': 9,
  'Environment': 10,
  'Staff': 11,
  'System': 12,
  'Chama': 13,
  'Game': 14},
 '1': {'Food/Water': 1},
 '2': {'Savings Group': 1, 'Farming/Labour': 2, 'Food/Water': 3},
 '3': {'Farming/Labour': 1,
  'Food/Water': 2,
  'Shop': 3,
  'Savings Group': 4,
  'Fuel/Energy': 5,
  'None': 6,
  'Transport': 7,
  'Education': 8},
 '4': {'Food/Water': 1,
  'Savings Group': 2,
  'Farming/Labour': 3,
  'Shop': 4,
  'Fuel/Energy': 5,
  'Health': 6,
  'None': 7,
  'Transport': 8,
  'Education': 9},
 '5': {'Farming/Labour': 1,
  'Food/Water': 2,
  'Savings Group': 3,
  'Shop': 4,
  'Fuel/Energy': 5,
  'Transport': 6},
 '6': {'Food/Water': 1,
  'Farming/Labour': 2,
  'Shop': 3,
  'Fuel/Energy': 4,
  'Savings Group': 5,
  'Education': 6,
  'Transport': 7,
  'None': 8,
  'Health': 9,
  'Staff': 10},
 '7': {'Savings Group': 1, 'Food/Water': 2, 'Farming/Labour': 3, 'Shop': 4},
 '8': {'Savings Group': 1,
  'Food/Water': 2,
  'Health': 3,
  'Education': 4,
  'Farming/Labour': 5,
  'Shop': 6},
 '9': {'Savings Group': 1},
 'external': {'Food/Water':1,
                    'Fuel/Energy':2,
                    'Health':3,
                    'Education':4,
                    'Savings Group':5,
                    'Shop':6}}


utilityTypesProbability = {'0': {'Food/Water': 0.3376267211378423,
  'Farming/Labour': 0.3294560447874111,
  'Shop': 0.19210546224844907,
  'Fuel/Energy': 0.041685580269329704,
  'None': 0.03374186715085489,
  'Transport': 0.028086699954607355,
  'Savings Group': 0.01813814495385081,
  'Education': 0.012445150552277198,
  'Health': 0.00450143743380239,
  'Environment': 0.0012672113784233622,
  'Staff': 0.0006808896958692692,
  'System': 0.0002080496292933878,
  'Chama': 3.782720532607051e-05,
  'Game': 1.8913602663035257e-05},
 '1': {'Food/Water': 1.0},
 '2': {'Savings Group': 0.6427282569469506,
  'Farming/Labour': 0.25045110068567306,
  'Food/Water': 0.1068206423673764},
 '3': {'Farming/Labour': 0.25480153649167736,
  'Food/Water': 0.1882202304737516,
  'Shop': 0.18437900128040974,
  'Savings Group': 0.16645326504481434,
  'Fuel/Energy': 0.12419974391805377,
  'None': 0.07554417413572344,
  'Transport': 0.0038412291933418692,
  'Education': 0.002560819462227913},
 '4': {'Food/Water': 0.3145801420414984,
  'Savings Group': 0.2651441303439632,
  'Farming/Labour': 0.16724690154574573,
  'Shop': 0.1522072134800167,
  'Fuel/Energy': 0.06057652137585295,
  'Health': 0.03328227266397438,
  'None': 0.0036206656454532793,
  'Transport': 0.0020888455646845844,
  'Education': 0.0012533073388107507},
 '5': {'Farming/Labour': 0.35526315789473684,
  'Food/Water': 0.35526315789473684,
  'Savings Group': 0.18421052631578946,
  'Shop': 0.05263157894736842,
  'Fuel/Energy': 0.02631578947368421,
  'Transport': 0.02631578947368421},
 '6': {'Food/Water': 0.3230154767848228,
  'Farming/Labour': 0.2860708936595107,
  'Shop': 0.18871692461308037,
  'Fuel/Energy': 0.0983524712930604,
  'Savings Group': 0.040439340988517224,
  'Education': 0.032950574138791815,
  'Transport': 0.013979031452820768,
  'None': 0.012980529206190713,
  'Health': 0.0024962556165751375,
  'Staff': 0.000998502246630055},
 '7': {'Savings Group': 0.7747841105354059,
  'Food/Water': 0.15751295336787566,
  'Farming/Labour': 0.04870466321243523,
  'Shop': 0.018998272884283247},
 '8': {'Savings Group': 0.6999073215940685,
  'Food/Water': 0.19258572752548656,
  'Health': 0.03670064874884152,
  'Education': 0.03132530120481928,
  'Farming/Labour': 0.02057460611677479,
  'Shop': 0.018906394810009268},
 '9': {'Savings Group': 1.0},
'external': {'Food/Water':0.6,
                    'Fuel/Energy':0.10,
                    'Health':0.03,
                    'Education':0.015,
                    'Savings Group':0.065,
                    'Shop':0.19}}