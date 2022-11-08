import math as mt

# 설문 점수 계산 모듈


def temperature(value):
    if (value >= 18) & (value <= 20):
        return 20
    else:
        err = 0
        if value <= 18:
            err = 18 - value
        else:
            err = value - 20
        return 20 - round(err / 2)


def humidity(value):
    if (value >= 40) & (value <= 60):
        return 20
    else:
        err = 0
        if value <= 40:
            err = 40 - value
        else:
            err = value - 60
        return 20 - round(err / 5)


def light(value):
    if (value >= 700) & (value <= 1500):
        return 20
    else:
        err = 0
        if value < 700:
            err = 700 - value
        else:
            err = value - 1500
        return 20 - round(err / 100)


def pm2_5(value):
    if (value <= 100):
        return 20
    else:
        err = 0
        err = value - 100
        return 20 - mt.ceil(err / 10)


def noise(value):
    if (value <= 10):
        return 20
    else:
        err = 0
        err = value - 10
        return 20 - mt.ceil(err / 2)


def odor(value):
    return 20 - (2 * value)


def congestion(value):
    if ((value >= 3) & (value <= 5)):
        return 20
    else:
        err = 0
        if value < 3:
            err = 3 - value
        else:
            err = value - 5
        return 20 - (err * 2)


def skin_temperature(value):
    if ((value >= 30) & (value <= 34)):
        return 20
    else:
        err = 0
        if value < 30:
            err = 30 - value
        else:
            err = value - 34
        return 20 - (err * 2)


calculate = {
    'temperature': temperature, 'humidity': humidity, 'light': light,
    'pm2.5': pm2_5, 'noise': noise, 'odor': odor,
    'congestion': congestion, 'skin temparature': skin_temperature
}


# calculate = {
#     'temp':temperature, 'hum': humidity,
#     'lux': light, 'dust': pm2_5, 'db': noise, 'smell':odor,
#     'congestion': congestion, 'skin':skin_temperature
# }
