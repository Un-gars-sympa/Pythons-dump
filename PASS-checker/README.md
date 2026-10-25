# PASS-checker

Un petit script Python qui classe un mot de passe en **faible**, **moyen** ou **fort**.

Mon tout premier programme ever.

## Fonctionnement

1. Il vérifie si le mot de passe est une ligne exacte dans deux wordlists (`rockyou.txt` qui n'est pas dans le repo contrairement à `francais.txt`). Si c'est le cas, le script indique que le mot de passe est crackable et s'arrête.
2. Sinon, il calcule un score à partir de :
   - la longueur
   - le nombre de caractères spéciaux
   - le nombre de majuscules
   - le nombre de chiffres
   - une pénalité pour les caractères répétés à la suite (`aa`, `111`...)
3. Le score donne la note finale.

## Utilisation

```
python PASS-checker.py Password123
```

Si le mot de passe contient des caractères spéciaux comme `!`, `&` ou `|`, mets-le entre guillemets :

```
python PASS-checker.py "P@ss!word"
```

## Fichiers nécessaires

Les deux wordlists doivent être dans le même dossier que le script.

- `francais.txt` : inclus dans ce dépôt. Source : [ajouter la source]
- `rockyou.txt` : non inclus (environ 130 Mo). À télécharger ici : [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)

## Limites

Le score est une simple heuristique, pas une vraie mesure de sécurité.

- Seules les répétitions à la suite sont détectées, pas les motifs comme `abab`, `abc` ou `123`
- Les minuscules ne sont pas comptées
- Le mot de passe est passé en argument, donc il reste dans l'historique du terminal, son utilisation est donc plus à titre pédagogique

---

# PASS-checker

A small Python script that rates a password as **weak**, **medium** or **strong**.

My very first program ever.

## How it works

1. It checks if the password is an exact line in two wordlists (`rockyou.txt`, which is not in the repo, unlike `francais.txt`). If it is, the script says the password is crackable and stops.
2. Otherwise, it computes a score from:
   - the length
   - the number of special characters
   - the number of uppercase letters
   - the number of digits
   - a penalty for consecutive repeated characters (`aa`, `111`...)
3. The score gives the final rating.

## Usage

```
python PASS-checker.py Password123
```

If the password contains special characters like `!`, `&` or `|`, put it in quotes:

```
python PASS-checker.py "P@ss!word"
```

## Files needed

Both wordlists must be in the same folder as the script.

- `francais.txt`: included in this repo. Source: [add the source]
- `rockyou.txt`: not included (about 130 MB). Download it here: [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)

## Limits

The score is a simple heuristic, not a real measure of security.

- Only consecutive repeats are detected, not patterns like `abab`, `abc` or `123`
- Lowercase letters are not counted
- The password is passed as an argument, so it stays in your shell history, which is why it is meant for educational use only
