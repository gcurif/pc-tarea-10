#primera clase de mierda con nombre de usuario, contraseña, edad, gmail y genero
class NewUser:
    def __init__(self, username, password, age, email, gender):
        self.username = username
        self.password = password
        self.age = age
        self.email = email
        self.gender = gender

    def print_info(self):
        print(f"Username: {self.username}, Password: {self.password}, Age: {self.age}, Email: {self.email}, Gender: {self.gender}")

#segunda clase de mierda con nombre de usuario, fecha, contenido url, laiks, y visualisasiones
class Stories:
    def __init__(self, username, date, contentURL, likes, views):
        self.username = username
        self.date = date
        self.contentURL = contentURL
        self.likes = likes
        self.views = views
    
    def print_info(self):
        print(f"Username: {self.username}, Date: {self.date}, Content URL: {self.contentURL}, Likes: {self.likes}, Views: {self.views}")

#tercera clase de mierda con nombre de usuario, contenido url, laik y komentarios
class Publications:
    def __init__(self, username, date, contentURL, likes, comments):
        self.username = username
        self.date = date
        self.contentURL = contentURL
        self.likes = likes
        self.comments = comments

    def print_info(self):
        print(f"Username: {self.username}, Date: {self.date}, Content URL: {self.contentURL}, Likes: {self.likes}, Comments: {self.comments}")

#cuarta clase de mierda con nombre de usuario, laiks, fecha, id de comentario y texto
class Comments: 
    def __init__(self, username, date, likes, comentID, text):
        self.username = username
        self.date = date
        self.likes = likes
        self.comentID = comentID
        self.text = text

    def print_info(self):
        print(f"Username: {self.username}, Date: {self.date}, Likes: {self.likes}, Comment ID: {self.comentID}, Text: {self.text}")

#quinta clase de mierda con nombre de usuario, fecha de creacion, publicaciones, seguidores y seguidos
class Profile:
    def __init__(self, username, creationDate, publications, followers, followed ):
        self.username = username
        self.creationDate = creationDate
        self.publications = publications
        self.followers = followers
        self.followed = followed

    def print_info(self):
        print(f"Username: {self.username}, Creation Date: {self.creationDate}, Publications: {self.publications}, Followers: {self.followers}, Followed: {self.followed}")

#sexta clase de mierda con nombre de usuario, fecha, url de video, laiks y comentarios
class Reels:
    def __init__(self, username, date, contentURL, likes, comments):
        self.username = username
        self.date = date
        self.contentURL = contentURL
        self.likes = likes
        self.comments = comments

    def print_info(self):
        print(f"Username: {self.username}, Date: {self.date}, Content URL: {self.contentURL}, Likes: {self.likes}, Comments: {self.comments}")