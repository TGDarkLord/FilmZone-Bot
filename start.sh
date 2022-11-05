if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TGDarkLord/MovieTime-Bot.git /MovieTime-Bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /MovieTime-Bot
fi
cd /MovieTime-Bot
pip3 install -U -r requirements.txt
echo "Starting Bot..."
python3 bot.py
