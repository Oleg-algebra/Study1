for i in {1..5}
do
	echo $i
	touch file$i.txt
	echo file$i.txt
	rm file$i.txt
done
