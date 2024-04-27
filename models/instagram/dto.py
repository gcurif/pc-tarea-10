#primera clase de mierda con nombre de usuario, contraseña, edad, gmail y genero
class NewUser:
    def __init__(self, username, password, age, email, gender):
        self.username = username
        self.password = password
        self.age = age
        self.email = email
        self.gender = gender

    def showNewUser(self):
        print("Username: ", self.username)
        print("Password: ", self.password)
        print("Age: ", self.age)
        print("Email: ", self.email)
        print("Gender: ", self.gender)


NewUserSaniel = NewUser("Sanielgay123", "sanielVSpene123", "56", "sanielwenopalpene@gmail.com", "transexual")
NewUserSaniel.showNewUser()
print("_______________________________________________________________________________")

#segunda clase de mierda con nombre de usuario, fecha, contenido url, laiks, y visualisasiones
class Stories:
    def __init__(self, username, date, contentURL, likes, views):
        self.username = username
        self.date = date
        self.contentURL = contentURL
        self.likes = likes
        self.views = views

    def showStories(self):
        print("Username: ", self.username)
        print("Date: ", self.date)
        print("Content URL: ", self.contentURL)
        print("Likes: ", self.likes)
        print("Views: ", self.views)
      

storieSaniel = Stories("Sanielgay123", "15/01/2015","fotogay.png", "2", "0")
storieSaniel.showStories()
print("_______________________________________________________________________________")

#tercera clase de mierda con nombre de usuario, contenido url, laik y komentarios
class Publications:
    def __init__(self, username, date, contentURL, likes, comments):
        self.username = username
        self.date = date
        self.contentURL = contentURL
        self.likes = likes
        self.comments = comments

    def showPublications(self):
        print("Username: ", self.username)
        print("Date: ", self.date)
        print("Content URL: ", self.contentURL)
        print("Likes: ", self.likes)
        print("Comments: ", self.comments)


publicationSaniel = Publications("Sanielgay123", "03/12/1878","fotoano.png", "0", "0")
publicationSaniel.showPublications()
print("_______________________________________________________________________________")

#cuarta clase de mierda con nombre de usuario, laiks, fecha, id de comentario y texto
class Comments: 
    def __init__(self, username, date, likes, comentID, text):
        self.username = username
        self.date = date
        self.likes = likes
        self.comentID = comentID
        self.text = text

    def showComments(self):
        print("Username: ", self.username)
        print("Date: ", self.date)
        print("Likes: ", self.likes)
        print("Coment ID: ", self.comentID)
        print("Text: ", self.text)


commentSaniel = Comments("Sanielgay123", "03/10/2367 A.C","0", "2343250342", "yo opino que los nazis debieron haber matado a todos los judios")
commentSaniel.showComments()
print("_______________________________________________________________________________")

#quinta clase de mierda con nombre de usuario, fecha de creacion, publicaciones, seguidores y seguidos
class Profile:
    def __init__(self, username, creationDate, publications, followers, followed ):
        self.username = username
        self.creationDate = creationDate
        self.publications = publications
        self.followers = followers
        self.followed = followed

    def showProfile(self):
        print("Username: ", self.username)
        print("Creation Date: ", self.creationDate)
        print("Publications: ", self.publications)
        print("Followers: ", self.followers)
        print("Followed: ", self.followed)


profileSaniel = Profile("Sanielgay123", "03/10/4214214234243 A.C","0", "1", "123430")
profileSaniel.showProfile()
print("_______________________________________________________________________________")

#sexta clase de mierda con nombre de usuario, fecha, url de video, laiks y comentarios
class Reels:
    def __init__(self, username, date, contentURL, likes, comments):
        self.username = username
        self.date = date
        self.contentURL = contentURL
        self.likes = likes
        self.comments = comments

    def showReels(self):
        print("Username: ", self.username)
        print("Date: ", self.date)
        print("Content URL: ", self.contentURL)
        print("Likes: ", self.likes)
        print("Comments: ", self.comments)


reelSaniel = Reels("Sanielgay123", "03/11/2024 A.C","videoano.png", "4357632", "2")
reelSaniel.showReels()