import requests
from bs4 import BeautifulSoup

session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.9",
}


url_login = "https://ici.rectaskimob.com.br/Login"
response = session.get(url_login, headers=headers)

# Extrai o token CSRF do HTML
soup        = BeautifulSoup(response.text, "html.parser")
token_input = soup.find("input", {"name": "__RequestVerificationToken"})

if not token_input:
    print("❌ Token CSRF não encontrado.")
    exit()

token = token_input["value"]
print("✅ Token CSRF encontrado:", token)

# 2️⃣ POST com os dados de login
url_post = "https://ici.rectaskimob.com.br/Login/Login"
payload = {
    "__RequestVerificationToken": token,
    "Email": "vitor.silva@transbpo.com.br", 
    "Senha": "NB063858@vhs"  
}


headers_post = headers.copy()
headers_post["Referer"] = url_login

response_post = session.post(url_post, headers=headers_post, data=payload)

# 3️⃣ Verifica se logou com sucesso
if "Logout" in response_post.text or "sair" in response_post.text.lower():
    print("✅ Login realizado com sucesso!")
else:
    print("⚠️ Algo deu errado. Verifique e-mail/senha ou redirecionamento.")
    with open("resposta_login.html", "w", encoding="utf-8") as f:
        f.write(response_post.text)
    print("🔍 HTML da resposta salvo como resposta_login.html")
