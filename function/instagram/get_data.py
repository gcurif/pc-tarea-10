from models.instagram.dto import *

def showInstagramData():


    #nuevos usuarios
    print("Mostrando Usuarios:")

    NewUserSaniel = NewUser("Sanielgay123", "sanielVSpene123", "56", "sanielwenopalpene@gmail.com", "transexual")
    NewUserHarold = NewUser("haroldweko", "haroldchamorromaricon123", "53", "haroldweko@gmail.com", "lesbiana")
    NewUserTata = NewUser("tatatraidor", "tatapagamemasporfa", "31, 33 o 75", "tatatraidor@gmail.com", "gay")


    NewUserSaniel.print_info()
    NewUserHarold.print_info()
    NewUserTata.print_info()

    # comentarios

    print("_______________________________________________________________________________")
    print("Mostrando comentarios:")

    storieSaniel = Stories("Sanielgay123", "15/01/2015","fotogay.png", "2", "0")
    storieHarold = Stories("Haroldweko", "15/01/2015","fotoweko.png", "23", "03332")
    storieTata = Stories("tatatraidor", "15/01/1970", "fotosexo.png", "1", "2323")


    storieSaniel.print_info()
    storieHarold.print_info()
    storieTata.print_info()

    #publicaciones

    print("_______________________________________________________________________________")
    print("Mostrando Publicaciones:")

    publicationSaniel = Publications("Sanielgay123", "03/12/1878","fotoano.png", "0", "0")
    publicationHarold = Publications("haroldweko", "03/03/2000", "fotopene.png", "8", "90")
    publicationTata = Publications("tatatraidor", "03/03/2000", "fotopene.png", "43", "98")


    publicationSaniel.print_info()
    publicationHarold.print_info()
    publicationTata.print_info()

    #Comentarios

    print("_______________________________________________________________________________")
    print("Mostrando Comentarios:")

    commentSaniel = Comments("Sanielgay123", "03/10/2367 A.C","0", "2343250342", "yo opino que los nazis debieron haber matado a todos los judios")
    commentHarold = Comments("haroldweko", "03/03/2000", "098", "423324324", "soy un esclavo y me gusta el pene")
    commentTata = Comments("tatatraidor", "03/03/2000", "63726", "434563", "ooh, que buen dia, le pagare mas a el pastita")

    commentSaniel.print_info()
    commentHarold.print_info()
    commentTata.print_info()

    #perfil

    print("_______________________________________________________________________________")
    print("Mostrando Perfiles:")

    profileSaniel = Profile("Sanielgay123", "03/10/4214214234243 A.C","0", "1", "123430")
    profileHarold = Profile("haroldweko", "03/03/2000", "098", "423324324", "2")
    profileTata = Profile("tatatraidor", "03/03/2000", "63726", "434563", "1")

    profileSaniel.print_info()
    profileHarold.print_info()
    profileTata.print_info()

    #reels

    print("_______________________________________________________________________________")
    print("Mostrando Reels:")



    reelSaniel = Reels("Sanielgay123", "03/11/2024 A.C","videoano.png", "4357632", "2")
    reelHarold = Reels("haroldweko", "03/03/2000", "fotopene.png", "8", "90")
    reelTata = Reels("tatatraidor", "03/03/2000", "fotopene.png", "43", "98")

    reelSaniel.print_info()
    reelHarold.print_info()
    reelTata.print_info()