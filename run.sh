# conda activate py38
pgrep -f GPTServe |xargs kill -9
nohup gunicorn -w 2 -b 0.0.0.0:4600 GPTServe:app --timeout 1000 >> nohup.log 2>&1 &