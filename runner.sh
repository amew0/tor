mkdir -p new
mkdir -p results/logs
mkdir -p results/output
dat="$(date +"%F-%H-%M")"
touch results/logs/${dat}.err
touch results/logs/${dat}.std
# export CUDA_VISIBLE_DEVICES=1 
# set PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:128
python mymain.py --output out_${dat} 2>results/logs/${dat}.err >results/logs/${dat}.std
