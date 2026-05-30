[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=28&duration=4000&pause=1500&color=1E90FF&center=true&vCenter=true&width=800&lines=Olá%2C+sou+Roberto+Átila!;Desenvolvedor+Full-Stack;Java+%7C+PHP+%7C+JavaScript+%7C+React+Native;Construindo+soluções+reais+desde+o+técnico.)](https://git.io/typing-svg)

---

### Desenvolvedor Full-Stack | Java · PHP · JavaScript | Segurança Web & Cloud

Desenvolvo aplicações web e mobile completas — de APIs REST em Spring Boot até interfaces em React e React Native — com foco em segurança (RBAC, JWT, auditoria de logins) e arquitetura real. Atualmente no 3º ano do Técnico em **Informática para Internet** e **Desenvolvimento de Sistemas** na ETEC Jacinto Ferreira de Sá e buscando minha primeira oportunidade de **Estágio em Desenvolvimento Full-Stack ou Backend**.

---

### 🚀 Projeto CORE

#### MarkitosSystem — SaaS de Faturamento Multi-Tenant

> Sistema web de gestão de faturamento arquitetado como SaaS. Cada empresa opera em espaço 100% isolado — clientes, produtos e faturas completamente separados entre tenants. Desenvolvido como TCC com autenticação JWT/BCrypt, RBAC, auditoria de acessos e orquestração via Docker Compose.

**Arquitetura:** Java 17 + Spring Boot 3.2 · MariaDB 10.4 · Vanilla JS · Spring Security (Stateless) · Docker Compose

**O que demonstra:**

- **Multi-tenancy por coluna discriminadora** — `empresa_id` injetado via JWT claim, filtrado em cada query no Service/Repository sem bibliotecas externas
- **Autenticação JWT + BCrypt** — token com claims `role` e `empresaId`; senhas com BCrypt rounds=10; fluxo stateless via `SecurityFilter`
- **RBAC** — rotas `/api/admin/**` restritas a `ROLE_admin`; demais endpoints filtrados automaticamente por `empresaId`
- **Auditoria de logins** — tabela `login_logs` registra toda tentativa (sucesso/falha, IP, user-agent, motivo); detecção automática de ataques com bloqueio de IP após 2+ falhas em 15 min
- **Estoque com movimentação** — entradas/saídas com `MovimentacaoEstoque`, alertas de estoque baixo via `AlertaEstoqueDTO`
- **Dashboard admin global** — visão consolidada de todas as empresas, faturamento e estatísticas do sistema
- **Containerizado** — Docker Compose sobe backend + MariaDB com uma linha

`Java 17` `Spring Boot 3.2` `Spring Security` `JWT` `BCrypt` `MariaDB 10.4` `Docker` `HTML` `CSS` `JavaScript` *(🔒 Repositório privado)*

---

### 📂 Projetos Públicos

| Projeto | Descrição Técnica | Stack | Link |
|---|---|---|---|
| **EduGestor v3** | Gestão escolar Full-Stack com CRUD de alunos/professores, controle de notas, chamada digital, relatórios automatizados e notificações via SendGrid. Arquitetura híbrida SQLite + Supabase Cloud, foco em performance, segurança e UX. | PHP 8, React 18, TypeScript 5, Tailwind 4, SQLite, Supabase, SendGrid | [Repositório](https://github.com/robertoatila/EduGestor-v3) |
| **Sushi & Sashimi Bar** | App mobile de pedidos de restaurante japonês desenvolvido para apresentação final da ETEC. Cardápio visual com `FlatList`, `ProductCard` reutilizável, navegação inferior por abas, acordeão de horários com destaque dinâmico para o dia atual e status ABERTO/FECHADO em tempo real. Compatível com Expo Go, Android, iOS e Web. | React Native, JavaScript, Expo, @expo/vector-icons | [Repositório](https://github.com/robertoatila/Atividade-ProjetoFinal-ExpoGo) |
| **Portfólio Arduino** | Portfólio web imersivo estilo Maker/Cyberpunk com zero frameworks. Inclui simulador interativo de circuitos, syntax highlighter com numeração de linha (CSS Counters), boot screen de compilação autêntico e PWA instalável. Performance extrema via `IntersectionObserver` e `requestAnimationFrame`. | HTML5, CSS3, JavaScript ES6+, PWA | [Repositório](https://github.com/robertoatila/Portf-lios-de-Projetos-Arduino) |
| **Cartão de Visitas Digital** | App mobile de portfólio profissional em React Native com 3 telas (cartão, contatos, skills), navegação por estado global, renderização condicional e design responsivo com paleta corporativa. | React Native, JavaScript, Expo | [Repositório](https://github.com/robertoatila/Cartao-de-visitas) |
| **Sonic e as Escadas v2.0** | Jogo de plataformas side-scrolling com 2 fases de dificuldade crescente. Robotnik com IA vetorial que rastreia o Sonic a cada frame (cálculo de ângulo por `atan2`), sistema de tiros de blaster, espinhos com ciclo de ativação, 4 vidas, timer por fase e física de pulo customizada. Construído em HTML5 Canvas puro, sem bibliotecas. | HTML5 Canvas, CSS3, JavaScript | [Repositório](https://github.com/robertoatila/Sonic-Game) |
| **Invincible – Invasão de Marte** | Jogo de luta side-scrolling baseado na HQ Invincible, com 3 fases de dificuldade progressiva e boss final. Construído em HTML5 Canvas puro, sem bibliotecas externas. | HTML5 Canvas, JavaScript | [Repositório](https://github.com/robertoatila/invincible-game) |

---

## 📊 Estatísticas

<div align="center">

[![GitHub Streak](https://streak-stats.demolab.com?user=robertoatila&theme=radical&locale=pt_BR)](https://git.io/streak-stats)

<img height="160em" src="https://github-readme-stats-sigma-five.vercel.app/api?username=robertoatila&show_icons=true&theme=radical&hide_border=true"/>
<img height="160em" src="https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=robertoatila&layout=compact&langs_count=7&theme=radical&hide_border=true"/>

</div>

---

## 🛠 Stack

**Backend & APIs**
[![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)](https://github.com/robertoatila)
[![Spring Boot](https://img.shields.io/badge/Spring_Boot_3-6DB33F?style=flat-square&logo=springboot&logoColor=white)](https://github.com/robertoatila)
[![PHP](https://img.shields.io/badge/PHP_8-777BB4?style=flat-square&logo=php&logoColor=white)](https://github.com/robertoatila)
[![MySQL](https://img.shields.io/badge/MySQL_8-4479A1?style=flat-square&logo=mysql&logoColor=white)](https://github.com/robertoatila)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)](https://github.com/robertoatila)

**Frontend & Mobile**
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://github.com/robertoatila)
[![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=flat-square&logo=typescript&logoColor=white)](https://github.com/robertoatila)
[![React](https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB)](https://github.com/robertoatila)
[![React Native](https://img.shields.io/badge/React_Native-20232A?style=flat-square&logo=react&logoColor=61DAFB)](https://github.com/robertoatila)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white)](https://github.com/robertoatila)
[![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white)](https://github.com/robertoatila)
[![Expo](https://img.shields.io/badge/Expo-000020?style=flat-square&logo=expo&logoColor=white)](https://github.com/robertoatila)

**Infra & Cloud**
[![AWS EC2](https://img.shields.io/badge/AWS_EC2-FF9900?style=flat-square&logo=amazonaws&logoColor=white)](https://github.com/robertoatila)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://github.com/robertoatila)
[![nginx](https://img.shields.io/badge/nginx-009639?style=flat-square&logo=nginx&logoColor=white)](https://github.com/robertoatila)
[![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white)](https://github.com/robertoatila)
[![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)](https://github.com/robertoatila)

---

## Contato

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/roberto-%C3%A1tila-almeida-azevedo-0a64412b4/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/robertoatila)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:roberto.atila10@gmail.com)
