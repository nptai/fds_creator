in="$PWD"/"$1";
out="$PWD"/"$2";
cd "$in";
echo "$out";
rm -rf "$out"
mkdir "$out";
cnt=1;
for i in $(ls -d */); do
    dout="$out"/"$cnt";
    mkdir "$dout";
    cp -rf "${i}"/* "$dout";
    echo "$cnt" "${i%%/}";
    let cnt=$cnt+1
done >> "$out"/label.txt;