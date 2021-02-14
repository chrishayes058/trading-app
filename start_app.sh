#! /bin/sh
trap "exit" INT TERM ERR
trap "kill 0" EXIT

chalice local &
python stream.py &

wait

#chalice local & 
#pid_chalice=$!
#echo "Started Chalice"

#python stream.py &
#pid_websocket=$!
#echo "Started websocket"

#trap "kill -2 $pid_chalice $pid_websocket" SIGINT
#wait $pid_chalice $pid_websocket
#echo "Running..."
