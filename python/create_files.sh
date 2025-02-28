if [ -z "$1" ]; then
    echo "Usage: $0 <directory_name>"
    exit 1
fi

directory_name=$1

cd /workspaces/atcoder/code/python
mkdir "$directory_name"
cd "$directory_name"

touch A.py
touch B.py
touch C.py
touch D.py
touch E.py
touch F.py
