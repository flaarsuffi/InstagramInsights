#!/usr/bin/env python3
"""
Meta Business API - Authorization Script
Gera token de acesso para Instagram insights
"""

import os
import sys
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

# Carregar variáveis de .env
load_dotenv()

APP_ID = os.getenv('META_APP_ID')
APP_SECRET = os.getenv('META_APP_SECRET')
REDIRECT_URI = os.getenv('META_REDIRECT_URI')

# URLs da Meta API
AUTHORIZE_URL = "https://www.instagram.com/oauth/authorize"
TOKEN_URL = "https://graph.instagram.com/v18.0/access_token"
GRAPH_URL = "https://graph.instagram.com/v18.0"

def step1_generate_auth_url():
    """Gera URL para autorização (seu ou da amiga)"""
    print("\n" + "="*70)
    print("PASSO 1: Gerar Link de Autorização")
    print("="*70)

    scopes = "instagram_basic,instagram_graph_user_profile,pages_read_engagement,pages_read_user_content"

    params = {
        "client_id": APP_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": scopes,
        "response_type": "code"
    }

    auth_url = f"{AUTHORIZE_URL}?{urlencode(params)}"

    print(f"\n🔗 Envie este link para sua amiga autorizar:\n")
    print(auth_url)
    print(f"\nEla vai:")
    print("  1. Fazer login no Instagram")
    print("  2. Clicar em 'Autorizar'")
    print("  3. Ser redirecionada para: http://localhost:3000/callback?code=XXXXX")

    return auth_url

def step2_exchange_code_for_token(code):
    """Troca o código por um token de acesso permanente"""
    print("\n" + "="*70)
    print("PASSO 2: Trocar Código por Token")
    print("="*70)

    params = {
        "client_id": APP_ID,
        "client_secret": APP_SECRET,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI,
        "code": code
    }

    print(f"\n📤 Enviando requisição para Meta...")

    try:
        response = requests.post(TOKEN_URL, params=params)
        response.raise_for_status()

        data = response.json()

        if "error" in data:
            print(f"\n❌ Erro: {data['error']['message']}")
            return None

        access_token = data.get("access_token")
        user_id = data.get("user_id")

        print(f"\n✅ Token gerado com sucesso!")
        print(f"   User ID: {user_id}")
        print(f"   Token: {access_token[:20]}...")

        return {
            "access_token": access_token,
            "user_id": user_id
        }

    except requests.exceptions.RequestException as e:
        print(f"\n❌ Erro na requisição: {e}")
        return None

def step3_get_instagram_account(access_token):
    """Busca os dados da conta Instagram"""
    print("\n" + "="*70)
    print("PASSO 3: Buscar Dados da Conta Instagram")
    print("="*70)

    url = f"{GRAPH_URL}/me"
    params = {
        "fields": "id,username,name,biography,website,profile_picture_url",
        "access_token": access_token
    }

    print(f"\n📤 Buscando dados da conta...")

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        if "error" in data:
            print(f"\n❌ Erro: {data['error']['message']}")
            return None

        print(f"\n✅ Dados da conta:")
        print(f"   Username: {data.get('username')}")
        print(f"   Name: {data.get('name')}")
        print(f"   Bio: {data.get('biography')}")
        print(f"   ID: {data.get('id')}")

        return data

    except requests.exceptions.RequestException as e:
        print(f"\n❌ Erro: {e}")
        return None

def step4_get_instagram_pages(access_token):
    """Busca as páginas Instagram conectadas"""
    print("\n" + "="*70)
    print("PASSO 4: Buscar Páginas Instagram")
    print("="*70)

    url = f"{GRAPH_URL}/me/instagram_accounts"
    params = {
        "access_token": access_token
    }

    print(f"\n📤 Buscando páginas...")

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        if "error" in data:
            print(f"\n❌ Erro: {data['error']['message']}")
            return None

        accounts = data.get("data", [])

        if not accounts:
            print(f"\n⚠️  Nenhuma página Instagram Business encontrada!")
            print(f"   Certifique-se que a página é do tipo BUSINESS")
            return None

        print(f"\n✅ Páginas encontradas:")
        for i, account in enumerate(accounts, 1):
            print(f"   {i}. {account.get('name')} (ID: {account.get('id')})")

        return accounts

    except requests.exceptions.RequestException as e:
        print(f"\n❌ Erro: {e}")
        return None

def save_to_env(token_data, account_data):
    """Salva os dados no .env"""
    print("\n" + "="*70)
    print("PASSO 5: Salvar Dados")
    print("="*70)

    env_file = ".env"

    # Ler .env atual
    with open(env_file, 'r') as f:
        lines = f.readlines()

    # Atualizar valores
    updates = {
        "META_USER_TOKEN": token_data["access_token"],
        "META_USER_ID": str(token_data["user_id"]),
        "META_PAGE_ID": str(account_data[0]["id"]) if account_data else "pending"
    }

    new_lines = []
    for line in lines:
        updated = False
        for key, value in updates.items():
            if line.startswith(f"{key}="):
                new_lines.append(f"{key}={value}\n")
                updated = True
                break
        if not updated:
            new_lines.append(line)

    # Escrever .env atualizado
    with open(env_file, 'w') as f:
        f.writelines(new_lines)

    print(f"\n✅ Dados salvos em .env:")
    print(f"   META_USER_TOKEN: {updates['META_USER_TOKEN'][:20]}...")
    print(f"   META_USER_ID: {updates['META_USER_ID']}")
    print(f"   META_PAGE_ID: {updates['META_PAGE_ID']}")

def main():
    """Fluxo completo de autorização"""

    print("\n" + "🔐 META BUSINESS API - Authorization Flow".center(70))
    print("="*70)

    # Validar credenciais
    if not APP_ID or not APP_SECRET:
        print("\n❌ Erro: META_APP_ID ou META_APP_SECRET não configurados em .env")
        sys.exit(1)

    print(f"\n✅ Credenciais carregadas:")
    print(f"   App ID: {APP_ID}")
    print(f"   App Secret: {APP_SECRET[:20]}...")

    # Passo 1: Gerar URL
    auth_url = step1_generate_auth_url()

    # Passo 2: Obter código
    print("\n" + "="*70)
    print("Próxima Ação:")
    print("="*70)
    print("\n1. Copie o link acima")
    print("2. Cole em um navegador")
    print("3. Autorize o acesso")
    print("4. Será redirecionado para: http://localhost:3000/callback?code=XXXXX")
    print("5. Cole o código abaixo\n")

    code = input("Cole o código aqui (código após 'code='): ").strip()

    if not code:
        print("\n❌ Código não fornecido!")
        sys.exit(1)

    # Trocar código por token
    token_data = step2_exchange_code_for_token(code)
    if not token_data:
        sys.exit(1)

    # Passo 3: Buscar dados da conta
    account_data = step3_get_instagram_account(token_data["access_token"])
    if not account_data:
        sys.exit(1)

    # Passo 4: Buscar páginas
    pages = step4_get_instagram_pages(token_data["access_token"])
    if not pages:
        sys.exit(1)

    # Passo 5: Salvar
    save_to_env(token_data, pages)

    print("\n" + "="*70)
    print("✅ AUTORIZAÇÃO CONCLUÍDA COM SUCESSO!")
    print("="*70)
    print("\nVocê pode agora rodar:")
    print("  python fetch_instagram_posts.py")
    print("\n")

if __name__ == "__main__":
    main()
