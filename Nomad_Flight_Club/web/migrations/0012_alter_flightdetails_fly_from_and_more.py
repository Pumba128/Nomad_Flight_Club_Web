# Generated by Django 4.1.4 on 2023-01-01 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_alter_flightdetails_fly_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightdetails',
            name='fly_from',
            field=models.CharField(choices=[('Abu Dhabi', 'Abu Dhabi'), ('Abuja', 'Abuja'), ('Accra', 'Accra'), ('Addis Ababa', 'Addis Ababa'), ('Adelaide', 'Adelaide'), ('Ahmedabad', 'Ahmedabad'), ('Albuquerque', 'Albuquerque'), ('Algiers', 'Algiers'), ('Amman', 'Amman'), ('Amsterdam', 'Amsterdam'), ('Ankara', 'Ankara'), ('Antananarivo', 'Antananarivo'), ('Ashgabat', 'Ashgabat'), ('Asmara', 'Asmara'), ('Astana', 'Astana'), ('Asunción', 'Asunción'), ('Austin', 'Austin'), ('Baghdad', 'Baghdad'), ('Baku', 'Baku'), ('Baltimore', 'Baltimore'), ('Bamako', 'Bamako'), ('Bangalore', 'Bangalore'), ('Bangkok', 'Bangkok'), ('Bangui', 'Bangui'), ('Banjul', 'Banjul'), ('Beijing', 'Beijing'), ('Beirut', 'Beirut'), ('Belgrade', 'Belgrade'), ('Belmopan', 'Belmopan'), ('Berlin', 'Berlin'), ('Bishkek', 'Bishkek'), ('Bissau', 'Bissau'), ('Bloemfontein', 'Bloemfontein'), ('Bogotá', 'Bogotá'), ('Boston', 'Boston'), ('Brasília', 'Brasília'), ('Bratislava', 'Bratislava'), ('Brazzaville', 'Brazzaville'), ('Bridgetown', 'Bridgetown'), ('Brisbane', 'Brisbane'), ('Brussels', 'Brussels'), ('Bucharest', 'Bucharest'), ('Budapest', 'Budapest'), ('Buenos Aires', 'Buenos Aires'), ('Bujumbura', 'Bujumbura'), ('Cairo', 'Cairo'), ('Canberra', 'Canberra'), ('Cape Town', 'Cape Town'), ('Caracas', 'Caracas'), ('Chandigarh', 'Chandigarh'), ('Charlotte', 'Charlotte'), ('Chennai', 'Chennai'), ('Chicago', 'Chicago'), ('Chisinau', 'Chisinau'), ('Colombo', 'Colombo'), ('Columbus', 'Columbus'), ('Conakry', 'Conakry'), ('Copenhagen', 'Copenhagen'), ('Dakar', 'Dakar'), ('Dallas', 'Dallas'), ('Damascus', 'Damascus'), ('Darwin', 'Darwin'), ('Delhi', 'Delhi'), ('Denver', 'Denver'), ('Detroit', 'Detroit'), ('Dhaka', 'Dhaka'), ('Djibouti', 'Djibouti'), ('Doha', 'Doha'), ('Dubai', 'Dubai'), ('Dublin', 'Dublin'), ('Dushanbe', 'Dushanbe'), ('El Paso', 'El Paso'), ('Fort Worth', 'Fort Worth'), ('Freetown', 'Freetown'), ('Gaborone', 'Gaborone'), ('Georgetown', 'Georgetown'), ('Guangzhou', 'Guangzhou'), ('Guatemala City', 'Guatemala City'), ('Havana', 'Havana'), ('Ho Chi Minh City', 'Ho Chi Minh City'), ('Hobart', 'Hobart'), ('Houston', 'Houston'), ('Hyderabad', 'Hyderabad'), ('Indianapolis', 'Indianapolis'), ('Islamabad', 'Islamabad'), ('Istanbul', 'Istanbul'), ('Jacksonville', 'Jacksonville'), ('Jaipur', 'Jaipur'), ('Jakarta', 'Jakarta'), ('Jerusalem', 'Jerusalem'), ('Kabul', 'Kabul'), ('Kanpur', 'Kanpur'), ('Karachi', 'Karachi'), ('Kiev', 'Kiev'), ('Kigali', 'Kigali'), ('Kingston', 'Kingston'), ('Kinshasa', 'Kinshasa'), ('Kolkata', 'Kolkata'), ('Kuala Lumpur', 'Kuala Lumpur'), ('Kuwait', 'Kuwait'), ('Lahore', 'Lahore'), ('Las Vegas', 'Las Vegas'), ('Libreville', 'Libreville'), ('Lilongwe', 'Lilongwe'), ('Lima', 'Lima'), ('Lisbon', 'Lisbon'), ('Ljubljana', 'Ljubljana'), ('London', 'London'), ('Los Angeles', 'Los Angeles'), ('Louisville', 'Louisville'), ('Luanda', 'Luanda'), ('Lucknow', 'Lucknow'), ('Madrid', 'Madrid'), ('Maldives', 'Maldives'), ('Managua', 'Managua'), ('Manama', 'Manama'), ('Manila', 'Manila'), ('Maputo', 'Maputo'), ('Maseru', 'Maseru'), ('Melbourne', 'Melbourne'), ('Memphis', 'Memphis'), ('Mexico City', 'Mexico City'), ('Milwaukee', 'Milwaukee'), ('Minsk', 'Minsk'), ('Mogadishu', 'Mogadishu'), ('Monrovia', 'Monrovia'), ('Montevideo', 'Montevideo'), ('Moroni', 'Moroni'), ('Mumbai', 'Mumbai'), ('Muscat', 'Muscat'), ("N'Djamena", "N'Djamena"), ('Nagpur', 'Nagpur'), ('Nairobi', 'Nairobi'), ('Nashville', 'Nashville'), ('Nassau', 'Nassau'), ('New Delhi', 'New Delhi'), ('New York', 'New York'), ('Niamey', 'Niamey'), ('Nouakchott', 'Nouakchott'), ('Oklahoma City', 'Oklahoma City'), ('Ottawa', 'Ottawa'), ('Ouagadougou', 'Ouagadougou'), ('Panama City', 'Panama City'), ('Paramaribo', 'Paramaribo'), ('Paris', 'Paris'), ('Perth', 'Perth'), ('Philadelphia', 'Philadelphia'), ('Phoenix', 'Phoenix'), ('Port Louis', 'Port Louis'), ('Port-au-Prince', 'Port-au-Prince'), ('Portland', 'Portland'), ('Porto-Novo', 'Porto-Novo'), ('Prague', 'Prague'), ('Pretoria', 'Pretoria'), ('Pune', 'Pune'), ('Quito', 'Quito'), ('Rabat', 'Rabat'), ('Riga', 'Riga'), ('Riyadh', 'Riyadh'), ('Rome', 'Rome'), ('San Antonio', 'San Antonio'), ('San Diego', 'San Diego'), ('San Francisco', 'San Francisco'), ('San Jose', 'San Jose'), ('San José', 'San José'), ('San Salvador', 'San Salvador'), ("Sana'a", "Sana'a"), ('Santiago', 'Santiago'), ('Sarajevo', 'Sarajevo'), ('Seattle', 'Seattle'), ('Seoul', 'Seoul'), ('Shanghai', 'Shanghai'), ('Shenzhen', 'Shenzhen'), ('Singapore', 'Singapore'), ('Skopje', 'Skopje'), ('Sofia', 'Sofia'), ('Surat', 'Surat'), ('Sydney', 'Sydney'), ('Tallinn', 'Tallinn'), ('Tashkent', 'Tashkent'), ('Tbilisi', 'Tbilisi'), ('Tegucigalpa', 'Tegucigalpa'), ('Tehran', 'Tehran'), ('Tel Aviv', 'Tel Aviv'), ('Tirana', 'Tirana'), ('Tokyo', 'Tokyo'), ('Tripoli', 'Tripoli'), ('Vienna', 'Vienna'), ('Vilnius', 'Vilnius'), ('Warsaw', 'Warsaw'), ('Washington D.C.', 'Washington D.C.'), ('Windhoek', 'Windhoek'), ('Yaoundé', 'Yaoundé'), ('Yerevan', 'Yerevan'), ('Zagreb', 'Zagreb')], max_length=30),
        ),
        migrations.AlterField(
            model_name='flightdetails',
            name='fly_to',
            field=models.CharField(choices=[('Abu Dhabi', 'Abu Dhabi'), ('Abuja', 'Abuja'), ('Accra', 'Accra'), ('Addis Ababa', 'Addis Ababa'), ('Adelaide', 'Adelaide'), ('Ahmedabad', 'Ahmedabad'), ('Albuquerque', 'Albuquerque'), ('Algiers', 'Algiers'), ('Amman', 'Amman'), ('Amsterdam', 'Amsterdam'), ('Ankara', 'Ankara'), ('Antananarivo', 'Antananarivo'), ('Ashgabat', 'Ashgabat'), ('Asmara', 'Asmara'), ('Astana', 'Astana'), ('Asunción', 'Asunción'), ('Austin', 'Austin'), ('Baghdad', 'Baghdad'), ('Baku', 'Baku'), ('Baltimore', 'Baltimore'), ('Bamako', 'Bamako'), ('Bangalore', 'Bangalore'), ('Bangkok', 'Bangkok'), ('Bangui', 'Bangui'), ('Banjul', 'Banjul'), ('Beijing', 'Beijing'), ('Beirut', 'Beirut'), ('Belgrade', 'Belgrade'), ('Belmopan', 'Belmopan'), ('Berlin', 'Berlin'), ('Bishkek', 'Bishkek'), ('Bissau', 'Bissau'), ('Bloemfontein', 'Bloemfontein'), ('Bogotá', 'Bogotá'), ('Boston', 'Boston'), ('Brasília', 'Brasília'), ('Bratislava', 'Bratislava'), ('Brazzaville', 'Brazzaville'), ('Bridgetown', 'Bridgetown'), ('Brisbane', 'Brisbane'), ('Brussels', 'Brussels'), ('Bucharest', 'Bucharest'), ('Budapest', 'Budapest'), ('Buenos Aires', 'Buenos Aires'), ('Bujumbura', 'Bujumbura'), ('Cairo', 'Cairo'), ('Canberra', 'Canberra'), ('Cape Town', 'Cape Town'), ('Caracas', 'Caracas'), ('Chandigarh', 'Chandigarh'), ('Charlotte', 'Charlotte'), ('Chennai', 'Chennai'), ('Chicago', 'Chicago'), ('Chisinau', 'Chisinau'), ('Colombo', 'Colombo'), ('Columbus', 'Columbus'), ('Conakry', 'Conakry'), ('Copenhagen', 'Copenhagen'), ('Dakar', 'Dakar'), ('Dallas', 'Dallas'), ('Damascus', 'Damascus'), ('Darwin', 'Darwin'), ('Delhi', 'Delhi'), ('Denver', 'Denver'), ('Detroit', 'Detroit'), ('Dhaka', 'Dhaka'), ('Djibouti', 'Djibouti'), ('Doha', 'Doha'), ('Dubai', 'Dubai'), ('Dublin', 'Dublin'), ('Dushanbe', 'Dushanbe'), ('El Paso', 'El Paso'), ('Fort Worth', 'Fort Worth'), ('Freetown', 'Freetown'), ('Gaborone', 'Gaborone'), ('Georgetown', 'Georgetown'), ('Guangzhou', 'Guangzhou'), ('Guatemala City', 'Guatemala City'), ('Havana', 'Havana'), ('Ho Chi Minh City', 'Ho Chi Minh City'), ('Hobart', 'Hobart'), ('Houston', 'Houston'), ('Hyderabad', 'Hyderabad'), ('Indianapolis', 'Indianapolis'), ('Islamabad', 'Islamabad'), ('Istanbul', 'Istanbul'), ('Jacksonville', 'Jacksonville'), ('Jaipur', 'Jaipur'), ('Jakarta', 'Jakarta'), ('Jerusalem', 'Jerusalem'), ('Kabul', 'Kabul'), ('Kanpur', 'Kanpur'), ('Karachi', 'Karachi'), ('Kiev', 'Kiev'), ('Kigali', 'Kigali'), ('Kingston', 'Kingston'), ('Kinshasa', 'Kinshasa'), ('Kolkata', 'Kolkata'), ('Kuala Lumpur', 'Kuala Lumpur'), ('Kuwait', 'Kuwait'), ('Lahore', 'Lahore'), ('Las Vegas', 'Las Vegas'), ('Libreville', 'Libreville'), ('Lilongwe', 'Lilongwe'), ('Lima', 'Lima'), ('Lisbon', 'Lisbon'), ('Ljubljana', 'Ljubljana'), ('London', 'London'), ('Los Angeles', 'Los Angeles'), ('Louisville', 'Louisville'), ('Luanda', 'Luanda'), ('Lucknow', 'Lucknow'), ('Madrid', 'Madrid'), ('Maldives', 'Maldives'), ('Managua', 'Managua'), ('Manama', 'Manama'), ('Manila', 'Manila'), ('Maputo', 'Maputo'), ('Maseru', 'Maseru'), ('Melbourne', 'Melbourne'), ('Memphis', 'Memphis'), ('Mexico City', 'Mexico City'), ('Milwaukee', 'Milwaukee'), ('Minsk', 'Minsk'), ('Mogadishu', 'Mogadishu'), ('Monrovia', 'Monrovia'), ('Montevideo', 'Montevideo'), ('Moroni', 'Moroni'), ('Mumbai', 'Mumbai'), ('Muscat', 'Muscat'), ("N'Djamena", "N'Djamena"), ('Nagpur', 'Nagpur'), ('Nairobi', 'Nairobi'), ('Nashville', 'Nashville'), ('Nassau', 'Nassau'), ('New Delhi', 'New Delhi'), ('New York', 'New York'), ('Niamey', 'Niamey'), ('Nouakchott', 'Nouakchott'), ('Oklahoma City', 'Oklahoma City'), ('Ottawa', 'Ottawa'), ('Ouagadougou', 'Ouagadougou'), ('Panama City', 'Panama City'), ('Paramaribo', 'Paramaribo'), ('Paris', 'Paris'), ('Perth', 'Perth'), ('Philadelphia', 'Philadelphia'), ('Phoenix', 'Phoenix'), ('Port Louis', 'Port Louis'), ('Port-au-Prince', 'Port-au-Prince'), ('Portland', 'Portland'), ('Porto-Novo', 'Porto-Novo'), ('Prague', 'Prague'), ('Pretoria', 'Pretoria'), ('Pune', 'Pune'), ('Quito', 'Quito'), ('Rabat', 'Rabat'), ('Riga', 'Riga'), ('Riyadh', 'Riyadh'), ('Rome', 'Rome'), ('San Antonio', 'San Antonio'), ('San Diego', 'San Diego'), ('San Francisco', 'San Francisco'), ('San Jose', 'San Jose'), ('San José', 'San José'), ('San Salvador', 'San Salvador'), ("Sana'a", "Sana'a"), ('Santiago', 'Santiago'), ('Sarajevo', 'Sarajevo'), ('Seattle', 'Seattle'), ('Seoul', 'Seoul'), ('Shanghai', 'Shanghai'), ('Shenzhen', 'Shenzhen'), ('Singapore', 'Singapore'), ('Skopje', 'Skopje'), ('Sofia', 'Sofia'), ('Surat', 'Surat'), ('Sydney', 'Sydney'), ('Tallinn', 'Tallinn'), ('Tashkent', 'Tashkent'), ('Tbilisi', 'Tbilisi'), ('Tegucigalpa', 'Tegucigalpa'), ('Tehran', 'Tehran'), ('Tel Aviv', 'Tel Aviv'), ('Tirana', 'Tirana'), ('Tokyo', 'Tokyo'), ('Tripoli', 'Tripoli'), ('Vienna', 'Vienna'), ('Vilnius', 'Vilnius'), ('Warsaw', 'Warsaw'), ('Washington D.C.', 'Washington D.C.'), ('Windhoek', 'Windhoek'), ('Yaoundé', 'Yaoundé'), ('Yerevan', 'Yerevan'), ('Zagreb', 'Zagreb')], max_length=30),
        ),
    ]