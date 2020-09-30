<h1 align="center">Masonite Forurm</h1>

<div align="center">
  <strong>Community Forum for Masonite Framework</strong>
</div>

<div align="center">
  <h3>
    <a href="https://www.hellomasonite.com/">
      Read our Blog
    </a>
    <span> | </span>
    <a href="https://twitter.com/HelloMasonite">
      Follow us on Twitter
    </a>
  </h3>
</div>

# Installation

1. Clone this repository with git clone git@github.com:hellomasonite/masonite-forum.git
2. `virtualenv -p python3.6 venv`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. `cp .env-example .env`
6. Setup a local database called `masoniteforum`
7. Setup a working e-mail driver like Mailtrap
8. `craft migrate`
9. `craft serve`
10. Run `craft queue:work`