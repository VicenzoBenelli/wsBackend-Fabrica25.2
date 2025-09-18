# Desafio Backend-Fabrica 2025


# 🎬 API de Filmes - Django Rest Framework  

Essa é uma API de filmes feita em **Django Rest Framework**, integrada com a **OMDb API** (The Open Movie Database).  
A ideia é simples: você manda o **título do filme**, e a mágica acontece — o sistema puxa os dados direto da OMDb e salva no nosso banco.  

O projeto já está **deployado no Render**, tanto o **backend** quanto o **PostgreSQL**.  
👉 [Link do backend no Render](https://wsbackend-fabrica25-2.onrender.com)  

---

## 🚀 Funcionalidades

- **Cadastro automático de filmes** via OMDb (manda só o título e o resto vem automático).  
- **Gerenciamento de resenhas** (nota + descrição + vínculo ao filme e usuário).  
- **Autenticação JWT** (login, refresh e verificação de tokens).  
- **Gerenciamento de usuários customizados** (com possibilidade de associar resenhas).  

## 🔑 Autenticação  

A API usa **JWT**:  

- `POST /api/token/` → gera o token de acesso e refresh  
- `POST /api/token/refresh/` → renova o token  
- `POST /api/token/verify/` → verifica se o token ainda é válido  

---

## 📡 Endpoints principais

### Filmes
- `GET /app/Filme/` → lista todos os filmes  
- `POST /app/Filme/` → cria um filme.  
  > **Detalhe**: aqui você só precisa mandar o campo `title`. O sistema vai consultar a OMDb API e preencher os outros dados automaticamente.  

Exemplo de payload:  
```json
{
  "title": "Inception"
}
```

### Resenhas
- `GET /app/Resenha/` → lista resenhas  
- `POST /app/Resenha/` → cria resenha (precisa estar autenticado)  

Exemplo de payload:  
```json
{
  "nome": "Opinião sincera",
  "nota": 9.5,
  "filme_id": 1,
  "descricao": "Um dos melhores filmes de ficção científica!"
}
```

### Usuários
- `GET /app/CustomUser/` → lista usuários  
- `POST /app/CustomUser/` → cria usuário  

---

## 🌍 Deploy

Tudo está rodando no **Render**:  

- Backend: 👉 [https://wsbackend-fabrica25-2.onrender.com](https://wsbackend-fabrica25-2.onrender.com/app/)  
- Banco: PostgreSQL gerenciado pelo Render  
