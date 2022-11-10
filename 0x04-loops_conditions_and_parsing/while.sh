timer=10

while [ $timer -ge '8' ]
	do
		echo 'dont worry'
		timer=$(($timer-1))
	done

echo "out of while"
