#!/usr/bin/bash 

rm -r logs 
mkdir logs 

f="rnaProfile"

g++ -pg -O3 "$f".cpp -o "$f".out
echo -n > "$f".txt

for i in $(seq 100 100 2500) ; do
    echo -n "$i " >> "$f".txt
    for j in $(seq 1 1 10) ; do
        python3 genSequence.py "$i"
        ./"$f".out in.txt
        x=$(gprof "$f".out gmon.out -bq | awk ' NR == 4 ' | awk '{print $(NF-1)}')
        if echo "$x" | grep -Eq '[0-9]+[.][0-9]+'; then
                echo -n "$x " >> "$f".txt
        fi
        gprof "$f".out gmon.out -bp > logs/"$f"_"$i"_"$j".txt
    done
echo "" >> "$f".txt
done
python3 averagetimes.py > results.txt
