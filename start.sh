echo "Cloning Repo...."

git clone https://github.com/ScriptBuddy/extract /extract

cd /extract

pip3 install -r requirements.txt

echo "Starting Bot...."

python3 main.py

