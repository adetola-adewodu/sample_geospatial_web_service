
# Create new virtual environment
virtualenv [your environment]

# Use the virtual environment
source [your environment]/bin/activate

# Generate a requirements file
pip freeze > requirements.txt

# Install required packages from requirements file
pip install -r requirements.txt

# Migrate models to the database
python manage.py makemigrations

# Mark migrations to run without actually running them for the application
python manage.py migrate --fake locations

# Sync the database to Create and make changes for tables
python manage.py migrate

# Sync the database without making changes to the tables in the database
python manage.py migrate --fake locations

# Copy csv to the database
COPY locations_location(name,longitude,latitude) FROM 
'/your directory path /campus_building_points.csv' DELIMITER ',' CSV HEADER;

# Find the near points to the center of Howard
select * from locations_location 
ORDER BY ST_MakePoint(longitude,latitude) <-> ST_MakePoint(38.921216999999999,-77.020461999999995) 
limit 5;


# select name, longitude and latitude with name = 'howard_center'
SELECT name, longitude, latitude
  FROM locations_location where name = 'howard_center';

# Import state geojson to create a states table
ogr2ogr -f PostgreSQL PG:"dbname=database  user=user password=password" stategeo.json -nln states

# Import Alabama State data to create NHDArea table
ogr2ogr -f PostgreSQL PG:"dbname=database  user=user password=password" NHDArea-Alabama.shp -nln locations_nhdarea

# Add Georgia Area data to NHDArea table
ogr2ogr -append -f PostgreSQL PG:"dbname=database user=user password=password" NHDArea-Georgia.shp -nln locations_nhdarea