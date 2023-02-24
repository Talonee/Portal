a=1
for i in *.jpg; do
	new=$(printf "%0d.jpg" "$a")
	#mv -f -- "$i" "$new"
	echo "$i --> $new"
	let a=a+1
done
