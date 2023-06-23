from notifypy import Notify

notification = Notify()
notification.title = "Price Watch Alert - Laptop #2" 
notification.message = "The price of Laptop #2 has dropped below $ 500 on webshop X."
notification.icon = 'images/pricewatch_icon.png'
notification.application_name = 'Price Watch'

notification.send()
