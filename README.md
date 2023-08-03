#  Projet de conception d'un systeme de recommandation de contenus basé sur l'intelligence artifcielle
<img src="docs/imgs/background.jfif" alt="images de couverture" width = "100%" height="250px" style="opacity: 0.8;">
<p>Notre projet consiste en la production d'un algoritheme de recommandation de contenus basé sur l'utilisation d'algorithe de'intelligence artificielle et deployé sur le web à travers un site web <br>
    
<h2>Table de matière</h2>
<ul>
<li><a href="#">Description</a></li>
<li><a href="#">Approche utiliséé</a></li>
<li><a href="#">Processus Backend</a></li>
<li><a href="#">Presentaion de l'interface</a></li>
<li><a href="#">Installation et utilisation du site</a></li>
<li><a href="#">Crédits</a></li>
</ul>
<br>

<ol>
    <li style="color: red;"><h3>Description du projet</h3></li><br>
    <strong style="color: blue;">Comment fonctionne t-il?</strong><br>
        Grace aux diverses informations de l'utilisateurs de l'application ainsi que des donnnées que nous disposons , nous entrainons un modele d'intelligence artificielle que tient en compte les preferences de l'utilisateur qinsi que 
        ceux des personnes(autres utilisateurs) ayant des similarités de gout avec celui-ci. <br>
        Les données recoltées de l'utilisateurs sont enregistré dans notre base de données pour etres utilisées à leur tour pour servir premierement à la personnalisation des recommandation et 
        deuxiemement à la recommandation d'autres utilisateurs ayant des similarités avec lui.
    <li style="color: red;"><h3>Description de l'approche utilisée</h3></li><br>
    <strong style="color: blue;">Architecture de notre projet</strong><br>
    <img src="docs/imgs/architecture.png" alt="architecture du projet" width="100%" height="450px"><br>
    <strong style="color: blue;">Description de l'architecture</strong><br>
    <p>Le projet se focalise sur 3 principaux point:
        <ul>
            <li style="font-weight: 800;  list-style: square;color: rgb(5, 98, 126);">La recolte continu de données</li>: Nous avons créer des algorithmes chargés de collecter des données utilisateurs lors de leur connection à l'application.
            <li style="font-weight: 800;  list-style: square;color: rgb(5, 98, 126);">Le traitement des données</li>: Ici nous construisons des algorithmes permettant de traiter les données du datasets et des données des utilisateurcollecter sur l'interface afin de les mettre sous un format adequate pour le l'entrainement du modèle d'IA ainsi que la construction des differentes bases de données.
            <li style="font-weight: 800;  list-style: square;color: rgb(5, 98, 126);">La construction du modeles d'IA</li>/ ici il s'agit de construire le modeles d'IA capable de faire les recommandations de produit eux differents utilisateurs en tenant compte de leur preference. Le modeles se base sur deux principes: Le filtrag collaboratif, qui donnes des recommandations en tenant compte des smilarités de gout entre utilisateurs et 
            le filtrage de contenus qui tient compte de la popularite d'un produits par rapport aux prefernce de l'utilisateur pour ces recommandations.
        </ul>
    </p>
    <li style="color: red;"><h3>Description du processus backend </h3></li><br>
    <P> Le processus de recommandation est basé sur 2 points clés : Le pretraitement de données et la recommandation par le modeles d'IA, tous les deux codés en python.</P>
    <UL>
        <li style="color: rgb(0, 156, 255);"><h3>Les algorithmes de pretraitement des donneés :</h3></li><br>
        Les alogorithemes de pretraitement de données premettent de metre en forme les données recoltée pour l'entrainement du modeles d'IA.
        En python, dans un pipeline de pretraitement prealablement  cré, nous construisons successivement des algorithe permettant de mettre à jour, nettoyer, analyser et encoder les données suivant des normes etablies dans le cahier de charge pour pouvoir affiner les recommanadation. <br>
        <strong>Comment cela se passe?</strong><br>
        Une fois les données recoltées et constituant notre dataset, nous trions les données obsolètes, nous effacons les donneés non-necessaires à la conception de notre modele, nous standardisons les données puis nous creons les porgramme permettant de faire un analyse sentiment pour les données de types textes.
        Apres cela nous nettoyons et analysons les données de notre datasets nettoyé pour l'encodage de ceux-ci. <br>
        Une fois cela terminer, nous enregistrons les données utiles à notre algorithme dans des bases de données pour une meilleur utilisation lors de la recolte des données utilisateur. <br>
        <li style="color: rgb(0, 156, 255);">Le modèle d'IA:</li><br>
        Le modele d'IA se focalise pincipalement sur les preference de l'utilisateur concerné par la recommandation. C'est à dire que le systeme ne recommnade que les rpoduits susceptibles de plaire à l'utilisateur en fonction des données recoltées. <br>
        <strong>Comment ça marche?</strong><br>
        Une fois l'utilisateur connecté , il lui est demandé d'entrrer ses preferences ou de les choisir parmis un collection d'articles proposés. <br>
        premierement, les données collectées de l'utislisateur sont analysées et traiter par les algorithmes de pretraitement des données et stocker dans des bases de données pour l'entrainement du modèle d'IA.Ensuite, nous utilisons le principe
    </UL>
</ol>
<h2>Interface utilisateur du site web</h2>
<img src="docs/imgs/capture2.png"><br>
<img src="./docs/imgs/capture3.png">
<div style = "border-top = 2px solid red" id = "h5">
  <h2 font-color = "red">Installation et utilisation du projet</h2>
  <h3><li>Avec Docker</li></h3>
  <h3><li>Avec l'invite de commande </li></h3>

<div style = "border-top = 2px solid red" id ="h6">
  <h2 font-color = "red">Crédits</h2>
	<h3>Langages utilisés</h3>
	<p>
		<img alt="Static Badge" src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
  		<img alt="Static Badge" src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white">
		<img alt="Static Badge" src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E">
		<img alt="Static Badge" src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
		<img alt="Static Badge" src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
	</p>
 <h3>Me contacter</h3>
 <p>
	 <img alt="Static Badge" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
	 <img alt="Static Badge" src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white">
	 <img alt="Static Badge" src="https://img.shields.io/badge/Quora-%23B92B27.svg?&style=for-the-badge&logo=Quora&logoColor=white">
	 <img alt="Static Badge" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white">
 </p>
	
</div>

