TOOL_ENV=/home/wdmlink/chunwei/tools/myenv/bin

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/wdmlink/chunwei/tools/sqlite_build/lib
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/wdmlink/chunwei/tools/mysql/lib/mysql

$TOOL_ENV/python manage.py runserver 10.48.56.63:8090
