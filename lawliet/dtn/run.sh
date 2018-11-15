!#/bin/bash

## usage
## ./run.sh $DISTANCIA

## @params
ipServer="192.168.12.4"
distancia=$1
contador=10

## testo o outro rasp
while [[ $contador -ne 0 ]]; do
	ping -c 1 $ipServer
	ans=$?
	if [[ $ans -eq 0 ]]; then
		((contador=1))
	fi
	((contador = contador - 1))	
done

if [[ $ans -eq 0 ]]; then
	echo "rasp ativo!"

	echo ""
	echo "inicializando..."
	echo ""
else
	exit 1
fi

mkdir -p experimento
cd experimento
#rm -rf $distancia
mkdir -p $distancia
cd $distancia

## pega potencia do sinal
for i in `seq 1 5`;
do
	signal=$(iwlist wlan0 scan | grep "icomp-ctic" -B 5 | grep Signal | cut -d '=' -f 3)
	echo $signal >> signalpower.out
done

# gambi pra enviar 10M quando dá erro de falta de espaco/permissao no /var/dtn/dtnperf/dtnbuffer.snd
touch ~/dtn/teste

for i in `seq 1 5`;
do
	echo "execucao $i"
	for payload in 50K 100K 250K 500K 1M 2.5M 10M;
	do
		echo "execucao $payload"
		# dtnperf-client
		# -e 300 segundos de expiracao
		# -D full level log
		# -f gambi de file
		goodput=$(sudo dtnperf-client -d dtn://kira.dtn -n $payload -p $payload -e 300000 -D 2 -f ~/dtn/teste | grep goodput | cut -d '=' -f 3 | tr -s ' ' | cut -d ')' -f 1)
		echo $goodput >> goodput$payload-$i.out
	done
done

echo "[FINISHED]";
