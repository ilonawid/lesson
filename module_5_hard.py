from idlelib.editor import keynames
from locale import currency
from re import search
from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, adult_mode=False, ):
        self.title = title
        self.duration = int(duration)
        self.adult_mode = adult_mode
        self.time_now = 0

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.current_user = None
        self.videos = []

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return None
        user = User(nickname, password, age)
        self.users.append(user)
        self.current_user = user
        print(f'Пользователь {nickname} успешно зарегистрирован')
        return user

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = nickname
                print(f'Пользователь {nickname} успешно авторизован')
                return user
        return None


    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, title):
        result = []
        for video in self.videos:
            if title.lower() in video.title.lower():
                result.append(video)
        return result


    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return None
        for video in self.videos:
            if title == video.title:
                if self.current_user.age < 18 and video.adult_mode is True:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    return None
                while video.time_now < video.duration:
                    print(video.time_now, end=' ')
                    sleep(1)
                    video.time_now += 1
                print('Конец видео')
                video.time_now = 0


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео

ur.add(v1, v2)

    # Проверка поиска

print(ur.get_videos('лучший'))

print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')

#     # Проверка входа в другой аккаунт
#
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)

#     # Попытка воспроизведения несуществующего видео
#
ur.watch_video('Лучший язык программирования 2024 года!')
