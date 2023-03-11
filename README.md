# Nomad_Flight_Club_Web

My first project made with Django. It is a tool for finding cheapest flights between two locations.
User submits two cities plus various additional parameters and gets best results for the query. 

The app consumes Tequila.com API for finding flights. It also uses basic Celery Beats configuration for every hour/day checks of new available connections.
If new connection is found, the user is notified by email about new cheapest connection. 
