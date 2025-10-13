from datetime import datetime

formato = "[%d/%m/%Y] %H:%M:%S - "
data = datetime.now()
print(data.strftime(formato))
