all: str_server
	echo "Server started:";
	echo "pid: "; cat .pid
str_server:
	./sh/str_server.sh

cls_server:
	./sh/cls_server.sh
re: str_server cls_server