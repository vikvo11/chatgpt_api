#FROM python:3-onbuild
#COPY . /usr/src/app
#RUN pip install --upgrade pip
#COPY ./google_trans_new_fix.py /usr/local/lib/python3.6/site-packages/google_trans_new/google_trans_new.py
#CMD ["python", "app.py"]

# Используем образ Python 3
FROM python:3.11

# Устанавливаем рабочую директорию в контейнере
WORKDIR /usr/src/app

# Копируем содержимое текущей директории в рабочую директорию в контейнере
COPY . .

# Обновляем pip
RUN pip install --upgrade pip

# Копируем исправленный файл google_trans_new.py в пакет google_trans_new
#COPY ./google_trans_new_fix.py /usr/local/lib/python3.6/site-packages/google_trans_new/google_trans_new.py

#RUN ls /usr/src/app
#RUN echo $(ls /usr/src/app)
#RUN ls /usr/src/app > directory_contents.txt
RUN pip install -r requirements.txt
# Запускаем приложение Python
CMD ["python", "app.py"]
