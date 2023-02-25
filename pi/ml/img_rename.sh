a=1
b=1
for i in *.jpg; do
	new=$(printf "%0d.jpg" "$a")
	#mv -f -- "$i" "$new"
	echo "$i --> $new"
	let a=a+1
done

for i in *.xml; do
	new=$(printf "%0d.xml" "$b")
	#mv -f -- "$i" "$new"
	echo "$i --> $new"
	let b=b+1
done
