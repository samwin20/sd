bash'''
    @task
    def classify_and_extract(self):
        for file_path in all_files:
            spawn(self.classify_document, file_path)

'''
@task: This is a decorator provided by Locust that marks the method as a task. When a simulated user (in this case, an instance of ParallelServiceUser) is running, it will randomly pick and execute tasks. The classify_and_extract method is one such task.

classify_and_extract(self): This is the task method itself. When this task is executed by a simulated user, the code inside this method will run.

for file_path in all_files:: This loop iterates over each file path in the all_files list. The all_files list contains paths to documents, as you mentioned.

spawn(self.classify_document, file_path): For each file path in the all_files list, this line spawns (or starts) a new greenlet (a lightweight, cooperative multitasking task provided by the gevent library) to execute the classify_document method with the current file_path as its argument.

In essence, what this task does is:

For each document path in the all_files list, it starts a new asynchronous task (greenlet) to classify that document.
These asynchronous tasks run concurrently, allowing multiple documents to be processed in parallel, up to the limits set by the semaphores and other concurrency controls in your script.
The purpose of this design is to simulate multiple users classifying multiple documents simultaneously, which helps in load testing the classifier service to see how it performs under concurrent load.




un script Locust qui simule un scénario d'orchestration pour le traitement de documents par plusieurs services en parallèle. Voici une explication des principales fonctionnalités du code :

Définition des services et de leurs caractéristiques :

Un ensemble de services est défini, chaque service ayant des caractéristiques telles que le nom, le chemin des fichiers associés, la capacité maximale de traitement en parallèle, une liste d'UUID en attente, et un compteur de traitements en cours.
Les services sont stockés dans la liste services.
Initialisation des sémaphores :

Des sémaphores sont créées pour chaque service, limitant le nombre de traitements en parallèle.
Initialisation des ports de service :

Un dictionnaire service_ports associe chaque service à un port.
Mode d'exécution (MODE) :

Le mode d'exécution est défini avec la variable MODE.
En mode "orchestrate", le script orchestre le traitement de documents par plusieurs services simultanément.
En mode "load testing", un fichier aléatoire est sélectionné pour traitement.
Partage d'état entre les utilisateurs Locust :

Une variable partagée documents_processed est utilisée pour suivre le nombre de documents traités.
Définition de la classe ParallelServiceUser :

Un utilisateur Locust est défini avec une méthode classify_and_extract représentant une tâche.
La méthode classify_and_extract sélectionne des documents et les soumet à des services en fonction du mode d'exécution.
Le script est conçu pour fonctionner avec plusieurs utilisateurs (user_count=10) et un taux d'apparition d'utilisateur d'une personne par seconde (spawn_rate=1).
Méthode classify_document :

La méthode classify_document traite un document en utilisant le service de classification, puis délègue le traitement à un service approprié en fonction du type de document détecté.
Méthode process_service :

La méthode process_service est appelée pour effectuer le traitement réel par un service spécifié.
Exécution du script :

La fonction __main__ configure la journalisation et crée un environnement Locust.
L'environnement est configuré pour utiliser la classe ParallelServiceUser.
La simulation démarre avec 10 utilisateurs et un taux d'apparition de 1 utilisateur par seconde.
Le script bloque l'exécution jusqu'à ce que tous les utilisateurs aient terminé (env.runner.greenlet.join()).
En résumé, ce script Locust simule un scénario d'orchestration où des documents sont classifiés par un service de classification, puis traités par différents services en parallèle. Le script est conçu pour être utilisé dans un environnement de test de charge pour évaluer les performances du système.



env = Environment(user_classes=[ParallelServiceUser]): Ici, vous créez une instance de l'environnement Locust. Vous spécifiez une classe d'utilisateur (ParallelServiceUser) qui représentera le comportement des utilisateurs lors de la simulation.

env.create_local_runner(): Vous créez un exécuteur local pour exécuter la simulation localement.

env.runner.start(user_count=10, spawn_rate=1): Vous démarrez l'exécution de la simulation avec un total de 10 utilisateurs (user_count=10). Le taux d'apparition (spawn rate) est de 1 utilisateur par seconde (spawn_rate=1). Cela signifie qu'un nouvel utilisateur est ajouté à la simulation chaque seconde jusqu'à ce que le nombre total d'utilisateurs atteigne 10.

env.runner.greenlet.join(): Cette ligne attend que toutes les tâches (greenlets) soient terminées. En d'autres termes, elle bloque l'exécution jusqu'à ce que la simulation soit terminée.

En résumé, ce code utilise Locust pour simuler 10 utilisateurs (user_count=10) qui exécutent le comportement défini dans la classe ParallelServiceUser. Ces utilisateurs sont ajoutés à la simulation à un taux d'un utilisateur par seconde. L'exécution de la simulation est bloquée jusqu'à ce que tous les utilisateurs aient terminé leur exécution.
