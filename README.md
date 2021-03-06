# O Planilhão 

* Grupo:
   * Filipe Rodrigues Batista de Oliveira (2018055091) - Front-end
   * Gabriel Tonioni Duarte (2018054842) - Front-end
   * Jackson Nunes Silva (2018054532) - Banco de dados
   * Raphael Heringer Rangel (2015055937) - Back-end
* Escopo: Site para ["planilhão DCC"](https://docs.google.com/spreadsheets/d/1b3ZAhH9FYQv4KxN5b-7h_hkhnZd1tILS3Ue60rOGJ-o/edit?usp=drive_web&ouid=107912368015206779024)
* Requisitos Funcionais: 
   * Avaliar professor;
   * Consultar avaliação do professor;
   * Consultar informações do professor (website);
   * Postar comentários sobre o professor;
* Tecnologias:
   * Front-end: HTML + CSS + Python;
   * Back-end: Django;
   * Banco de dados: SQLite;
   * Controle de versão: Git;

## Backlog do produto:
  * História: Como usuário, eu gostaria de avaliar o professor (P)
  * História: Como usuário, eu gostaria de consultar as avaliações do professor (P)
  * História: Como usuário, eu gostaria de verificar as informações do professor ✔️
  * História: Como usuário, eu gostaria de pesquisar um professor específico ✔️
  * História: Como usuário, eu gostaria de ler sobre o site e sua política de moderação ✔️
  * História: Como admin, eu gostaria de remover avaliações ✔️
  * História: Como admin, eu gostaria de editar as informações de um professor ✔️
  * História: Como admin, eu gostaria de adicionar ou remover um professor ✔️

## Backlog do sprint:
  * História: Como usuário, eu gostaria de avaliar o professor 
    * Tarefas:
      * Implementar a interface web; [Filipe] ✔️
      * Instalar banco de dados, projetar e criar tabelas; [Jackson] ✔️
      * Implementar interface da avaliação da didática ("com estrela"); [Filipe, Gabriel] ✔️
      * Implementar interface da avaliação da relação com alunos ("com coração"); [Filipe, Gabriel] ✔️
      * Implementar sistema de avaliação da didática ("com estrela"); [Raphael, Gabriel] ❌
      * Implementar sistema de avaliação da relação com alunos ("com coração"); [Raphael, Gabriel] ❌
      * Implementar sistema de envio de comentários sobre o professor; [Raphael] (P)
      * Implementar a interface web e conectar com backend; [Gabriel] ✔️
  * História: Como usuário, eu gostaria de consultar as avaliações do professor
    * Tarefas:
      * Popular banco de dados com as avaliações feitas no planilhão; [Jackson] ✔️
      * Implementar interface da avaliação da didática ("com estrela"); [Filipe] ❌
      * Implementar sistema de verificar a avaliação da didática ("com estrela"); [Raphael, Gabriel] ❌
      * Implementar sistema de verificar avaliação da relação com alunos ("com coração"); [Raphael, Gabriel] ❌
      * Implementar menu pull down ao clicar sobre a foto do professor (mostrando os comentários já existentes); [Raphael] ✔️
      * Implementar a interface web e conectar com backend; [Raphael, Gabriel] ✔️
  * História: Como usuário, eu gostaria de verificar as informações do professor 
    * Tarefas:
      * Implementar a interface web; [Filipe] ✔️
      * Adicionar nome e foto do professor (tirado do site do DCC); [Jackson] ✔️
      * Adicionar link para página pessoal do professor; [Jackson] ❌
      * Adicionar área de estudo do professor; [Jackson] ✔️
      * Implementar a interface web e conectar com backend; [Raphael, Gabriel] ✔️
  * História: Como usuário, eu gostaria de pesquisar um professor específico
    * Tarefas: 
      * Implementar sistema de busca; [Gabriel] ✔️
      * Projetar e testar a interface do sistema de busca; [Gabriel] ✔️
  * História: Como usuário, eu gostaria de ler sobre o site e sua política de moderação
    * Tarefas:
      * Implementar a interface web; [Filipe, Gabriel] ✔️
  * História: Como admin, eu gostaria de remover avaliações
    * Tarefas:
      * Implementar a interface de admin; [Raphael] ✔️  
  * História: Como admin, eu gostaria de editar as informações de um professor
    * Tarefas:
      * Implementar a interface de admin; [Raphael] ✔️
  * História: Como admin, eu gostaria de adicionar ou remover um professor
    * Tarefas:
      * Implementar a interface de admin; [Raphael] ✔️
      
## Diagrama da Arquitetura do Sistema:
![image](https://user-images.githubusercontent.com/42478443/124494113-d2feb580-dd8c-11eb-92eb-5d0aa6bb9e23.png)
![image](https://user-images.githubusercontent.com/42478443/124494320-135e3380-dd8d-11eb-8614-7cea8772961b.png)
![image](https://user-images.githubusercontent.com/42478443/124494546-5b7d5600-dd8d-11eb-8a89-d91280c8b775.png)

