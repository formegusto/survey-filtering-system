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

calculate = {
    "temperature": temperature,

}
