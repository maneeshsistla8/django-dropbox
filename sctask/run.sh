nohup python manage.py runserver &
a=$(python postreq.py)

if (( $a == 201 )) ; then
	echo "Successfully posted"
	python export.py
	python upload.py
	echo "Successfully exported and uploaded"
fi	