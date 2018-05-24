class Message:
    def __init__(self, message):
        self.message = message
    
    def __contains__(self, str):
        return str in self.message
    
class FormattedMessage(Message):
    def __contains__(self, str):
        return str.lower() in self.message.lower()

m1 = Message("Hey mademoiselle !")
m2 = FormattedMessage("Hey mademoiselle !")

print("hey" in m1)
print("maDEMoiselle" in m2)