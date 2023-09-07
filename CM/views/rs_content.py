import mysql.connector
from django.shortcuts import render
from .forms import LienTikTokForm, LienFacebookForm, LienTwitterForm, LienYoutubeForm


def facebook_content(request):
    data_from_db = []  # Initialisez data_from_db en dehors de la condition if

    if request.method == 'POST':
        form = LienFacebookForm(request.POST)  # Instancier le formulaire avec les données soumises

        if form.is_valid():  # Vérifier si le formulaire est valide
            # Les données du formulaire sont maintenant dans form.cleaned_data
            titre = form.cleaned_data['titre']
            lien = form.cleaned_data['lien']
            description = form.cleaned_data['description']
            datesaisie = form.cleaned_data['datesaisie']

            # Établir une connexion à la base de données distante
            db_config = {
                "host": "185.166.188.154",
                "user": "u948053727_capal",
                "password": "Decembre@2023",
                "database": "u948053727_capal"
            }
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # Créer la table si elle n'existe pas
            create_table_query = """
                CREATE TABLE IF NOT EXISTS data_facebook (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    titre VARCHAR(255),
                    lien VARCHAR(255),
                    description TEXT,
                    datesaisie DATE
                )
            """
            cursor.execute(create_table_query)

            # Insérer les données dans la table de la base de données distante
            insert_query = "INSERT INTO data_facebook (titre, lien, description, datesaisie) VALUES (%s, %s, %s, %s)"
            data_to_insert = (titre, lien, description, datesaisie)
            cursor.execute(insert_query, data_to_insert)

            # Valider les changements et fermer la connexion
            connection.commit()
            cursor.close()
            connection.close()

            # Rediriger ou afficher un message de réussite
            form = LienTikTokForm()  # Vous pouvez personnaliser cette redirection

    else:
        form = LienTikTokForm()  # Si la requête n'est pas POST, afficher un formulaire vide

    # Récupérer les données de la base de données (à l'extérieur de la condition if)
    db_config = {
        "host": "185.166.188.154",
        "user": "u948053727_capal",
        "password": "Decembre@2023",
        "database": "u948053727_capal"
    }
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    select_query = "SELECT titre, datesaisie, description, lien FROM data_facebook"
    cursor.execute(select_query)
    data_from_db = cursor.fetchall()

    # Reste de votre code pour afficher le formulaire dans le modèle HTML et la table des données

    context = {'form': form, 'data_from_db': data_from_db}
    return render(request, 'rs/facebook.html', context)


def facebook_tiktok(request):
    data_from_db = []  # Initialisez data_from_db en dehors de la condition if

    if request.method == 'POST':
        form = LienTikTokForm(request.POST)  # Instancier le formulaire avec les données soumises

        if form.is_valid():  # Vérifier si le formulaire est valide
            # Les données du formulaire sont maintenant dans form.cleaned_data
            titre = form.cleaned_data['titre']
            lien = form.cleaned_data['lien']
            description = form.cleaned_data['description']
            datesaisie = form.cleaned_data['datesaisie']

            # Établir une connexion à la base de données distante
            db_config = {
                "host": "185.166.188.154",
                "user": "u948053727_capal",
                "password": "Decembre@2023",
                "database": "u948053727_capal"
            }
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # Créer la table si elle n'existe pas
            create_table_query = """
                    CREATE TABLE IF NOT EXISTS data_tiktok (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        titre VARCHAR(255),
                        lien VARCHAR(255),
                        description TEXT,
                        datesaisie DATE
                    )
                """
            cursor.execute(create_table_query)

            # Insérer les données dans la table de la base de données distante
            insert_query = "INSERT INTO data_tiktok(titre, lien, description, datesaisie) VALUES (%s, %s, %s, %s)"
            data_to_insert = (titre, lien, description, datesaisie)
            cursor.execute(insert_query, data_to_insert)

            # Valider les changements et fermer la connexion
            connection.commit()
            cursor.close()
            connection.close()

            # Rediriger ou afficher un message de réussite
            form = LienTikTokForm()  # Vous pouvez personnaliser cette redirection

    else:
        form = LienTikTokForm()  # Si la requête n'est pas POST, afficher un formulaire vide

    # Récupérer les données de la base de données (à l'extérieur de la condition if)
    db_config = {
        "host": "185.166.188.154",
        "user": "u948053727_capal",
        "password": "Decembre@2023",
        "database": "u948053727_capal"
    }
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    select_query = "SELECT titre, datesaisie, description, lien FROM data_tiktok"
    cursor.execute(select_query)
    data_from_db = cursor.fetchall()

    # Reste de votre code pour afficher le formulaire dans le modèle HTML et la table des données

    context = {'form': form, 'data_from_db': data_from_db}
    return render(request, 'rs/tiktok.html', context)


def facebook_twitter(request):
    data_from_db = []  # Initialisez data_from_db en dehors de la condition if

    if request.method == 'POST':
        form = LienTwitterForm(request.POST)  # Instancier le formulaire avec les données soumises

        if form.is_valid():  # Vérifier si le formulaire est valide
            # Les données du formulaire sont maintenant dans form.cleaned_data
            titre = form.cleaned_data['titre']
            lien = form.cleaned_data['lien']
            description = form.cleaned_data['description']
            datesaisie = form.cleaned_data['datesaisie']

            # Établir une connexion à la base de données distante
            db_config = {
                "host": "185.166.188.154",
                "user": "u948053727_capal",
                "password": "Decembre@2023",
                "database": "u948053727_capal"
            }
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # Créer la table si elle n'existe pas
            create_table_query = """
                        CREATE TABLE IF NOT EXISTS data_twitter (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            titre VARCHAR(255),
                            lien VARCHAR(255),
                            description TEXT,
                            datesaisie DATE
                        )
                    """
            cursor.execute(create_table_query)

            # Insérer les données dans la table de la base de données distante
            insert_query = "INSERT INTO data_twitter(titre, lien, description, datesaisie) VALUES (%s, %s, %s, %s)"
            data_to_insert = (titre, lien, description, datesaisie)
            cursor.execute(insert_query, data_to_insert)

            # Valider les changements et fermer la connexion
            connection.commit()
            cursor.close()
            connection.close()

            # Rediriger ou afficher un message de réussite
            form = LienTwitterForm()  # Vous pouvez personnaliser cette redirection

    else:
        form = LienTwitterForm()  # Si la requête n'est pas POST, afficher un formulaire vide

    # Récupérer les données de la base de données (à l'extérieur de la condition if)
    db_config = {
        "host": "185.166.188.154",
        "user": "u948053727_capal",
        "password": "Decembre@2023",
        "database": "u948053727_capal"
    }
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    select_query = "SELECT titre, datesaisie, description, lien FROM data_twitter"
    cursor.execute(select_query)
    data_from_db = cursor.fetchall()

    # Reste de votre code pour afficher le formulaire dans le modèle HTML et la table des données

    context = {'form': form, 'data_from_db': data_from_db}
    return render(request, 'rs/twitter.html', context)


def facebook_youtube(request):
    data_from_db = []

    if request.method == 'POST':
        form = LienYoutubeForm(request.POST)

        if form.is_valid():
            titre = form.cleaned_data['titre']
            lien = form.cleaned_data['lien']
            description = form.cleaned_data['description']
            datesaisie = form.cleaned_data['datesaisie']

            db_config = {
                "host": "185.166.188.154",
                "user": "u948053727_capal",
                "password": "Decembre@2023",
                "database": "u948053727_capal"
            }
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            create_table_query = """
                            CREATE TABLE IF NOT EXISTS data_youtube (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                titre VARCHAR(255),
                                lien VARCHAR(255),
                                description TEXT,
                                datesaisie DATE
                            )
                        """
            cursor.execute(create_table_query)

            insert_query = "INSERT INTO data_youtube(titre, lien, description, datesaisie) VALUES (%s, %s, %s, %s)"
            data_to_insert = (titre, lien, description, datesaisie)
            cursor.execute(insert_query, data_to_insert)

            connection.commit()
            cursor.close()
            connection.close()

            form = LienYoutubeForm()

    else:
        form = LienYoutubeForm()

    db_config = {
        "host": "185.166.188.154",
        "user": "u948053727_capal",
        "password": "Decembre@2023",
        "database": "u948053727_capal"
    }
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    select_query = "SELECT titre, datesaisie, description, lien FROM data_youtube"
    cursor.execute(select_query)
    data_from_db = cursor.fetchall()

    context = {'form': form, 'data_from_db': data_from_db}
    return render(request, 'rs/youtube.html', context)
