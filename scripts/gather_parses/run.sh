mkdir temp
cd temp

parse_path="/shared/data3/anon/S2ORC/20200705v1/full/pdf_parses/"

file_id=0

for file_id in {0..99}
do
    echo "Processing File "$file_id
    file_name="pdf_parses_"$file_id".jsonl.gz"
    file_path="$parse_path$file_name"
    cp $file_path .
    gzip -d -f $file_name

    work_file="/home/anon3/cite_reco_gather/temp/pdf_parses_"$file_id".jsonl"

    python3 ../gather_parse.py $file_id
    rm $work_file
done

echo "Task Completed"
