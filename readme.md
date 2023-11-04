<h1 align="center">Upload PDF Flashcard Creator</h1>

## O que é?
Site que permite fazer o upload de um documento de texto e gera flashcards automaticamente a partir desse arquivo.

## Propósito
Automatizar o processo de criação de flashcards para estudo com base em anotações sobre um determinado tema.

## Requisitos funcionais

### Essenciais
- Fazer upload de um txt;
- Gerar um grupo de flashcards para estudo com base no documento de texto submetido.

### Importantes
- Salvar flashcards para visualização posterior;
- Editar pergunta e resposta do flashcard;
- Excluir flashcard.

### Desejáveis
- Salvar documento submetido, de modo que seja possível ver qual conteúdo originou os flashcards;
- Excluir grupo de flashcards;
- Editar nome e descrição do grupo de flashcards;
- Dar feedback com relação a facilidade do flashcard, caso tenha sido difícil, o flashcard deve reaparecer depois de um intervalo de tempo;
- Baixar documento de origem do grupo de flashcards;
- Filtrar grupo de flashcards;
- Pesquisar grupo de flashcards;
- Associar categorias a um grupo de flashcards;
- Exportar flashcards como pdf e pptx.
- Compartilhar flashcards;
- Criar grupo de flashcards.
- Adicionar novos flashcards;

## Requisitos não funcionais
- Ausência de limitação com relação ao número de páginas do documento;
- Possibilidade de upar documentos nos seguintes formatos: pdf, md, doc, docx e txt.
- Interface amigável onde seja possível ver todos os grupos de flashcards já criados;
- Animações e transições ao virar ou mudar para um novo flashcard;
- Ícones e textos de feedback que indiquem se as operações estão ocorrendo, foram bem sucedidas ou falharam;
- Social sign-on;
- Validações nos formulários;
- Possibilidade de gerar flashcards sem conta no site.

## Tecnologias
### Full stack
- Nextjs
- Typescript

### Front-end
- Tailwind
- Formik
- yup
- Framer motion
- Axios

### Back-end
- Langchain
- Prisma
- NodeJS
- SQLite
- Express Async Errors
- JSON web token
- bcryptjs
- dotenv
- ts-node-dev
- zod