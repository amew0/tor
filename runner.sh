rm -r new
rm -r results
mkdir -p new
mkdir -p results/logs
mkdir -p results/output
dat="$(date +"%F-%H-%M")"
touch results/logs/${dat}.err
touch results/logs/${dat}.std
export CUDA_VISIBLE_DEVICES=2
nohup python mymain.py --population 100 --generations 20 --offsprings 100 --mutation_rate 0.25 --batch_size 4 --epochs 100 2>results/logs/${dat}.err >results/logs/${dat}.std &
