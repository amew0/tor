dat="coco128-$(date +"%F-%H-%M")"
mkdir -p results/logs
mkdir -p results/output
touch results/logs/${dat}.err
touch results/logs/${dat}.std
export CUDA_VISIBLE_DEVICES=1 
python mymain.py  --output results/output/out_${dat} --save_dir results/data --cache_dir results/cache 2>results/logs/${dat}.err >results/logs/${dat}.std
