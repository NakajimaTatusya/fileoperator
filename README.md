# How To

## Source Repository

1. git レポジトリ作成

```cmd
mkdir myrepo
cd myrepo

git init .
```

2. 仮想環境用のgitignoreを作る

```
.Python
[Bb]in
[Ii]nclude
[Ll]ib
[Ll]ib64
[Ll]ocal
[Ss]cripts
pyvenv.cfg
.venv
pip-selfcheck.json
```

3. 仮想環境構築

```cmd
python -m venv .
```

4. 必要なパッケージをpipで入れる

```cmd
pip install hogehoge
```

5. requirements.txt 作成

```cmd
pip list
pip freeze > requirements.txt
```

6. リモートリポジトリへプッシュ

```cmd
git remote name url
git add .
git commit -m "comment here."
git push -u origin
```

## clone repogitory

1. git clone
2. python venv
3. pip install -r requirements.txt

