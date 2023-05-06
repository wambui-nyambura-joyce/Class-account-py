class Fruit:
    nutrient ="Vit C"
    def __init__(self,name,color,taste):
        self.name = name
        self.color = color
        self.taste = taste
    def fruit_price(self):
        return (f"{self.name} is 30 Kenyan shillings")
    def describe_fruit(self):
        return (f"{self.color} {self.name} are always {self.taste}")
    def fruit_expiry_rate(self):
        return (f"{self.name} have a high expiring rate.")
        