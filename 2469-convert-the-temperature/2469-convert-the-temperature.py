class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        arr=[]
        kelvin=0
        faherenheit=0
        kelvin=celsius+273.15
        faherenheit=celsius*1.80+32.00
        arr.append(kelvin)
        arr.append(faherenheit)
        return arr
