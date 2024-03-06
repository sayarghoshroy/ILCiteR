mkdir temp
cd temp

metadata_path="/shared/data3/anon/S2ORC/20200705v1/full/metadata/"

file_id=0

for file_id in {0..99}
do
        echo "Processing File "$file_id
        file_name="metadata_"$file_id".jsonl.gz"
        file_path="$metadata_path$file_name"
        cp $file_path .
        gzip -d -f $file_name

        work_file="/home/anon3/cite_reco_gather/temp/metadata_"$file_id".jsonl"

        python3 ../gather_meta.py $file_id
        rm $work_file
done

echo "Task Completed"