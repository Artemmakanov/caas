Кот предпочитает "Milk" и "Meat"



Сначала следует поставить виртуальное окружение -  .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

запустить DNS server - sudo python3 dns.py
Затем запустить tcp и udp сервер и flask - sh start.sh


Для того чтобы проверить, что размер сообщения может быть произвольным - можно изменить CHUNK_SIZE в start.sh на любое число, и затем, обязательно поменять значение этой переменной в Jupyter Notebook-е для тестирования.