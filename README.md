# ListImprovement
Este é um projeto que eu desenvolvi para me auxiliar em uma tarefa do trabalho que demandava muito tempo, filtrar e organizar planilhas de Instagram scraping (Raspagem de dados de usúariso do Instragram, como e-mail, número de telefone, localidade, biografia do perfil etc.)

O programa é bem simples, eu usei o RE para conseguir encontrar as palavras-chaves que identificavam se os perfis eram ou não clínicas, utilizei o Pandas para manipular as planilhas e formatar elas pra otimizar ainda mais meu trabalho e agora recentemente utilizei o Tkinter para criar uma interface muito muito simples apenas para uso pessoal.

Como o programa funciona? Quando iniciado, ele abre uma janela feita com Tkinter que tem apenas um botão, quando pressionado, ele executa a função manipular_planilha, que abre o explorador de arquivos, para o usúario selecionar a planilha que ele quer manipular, essa planilha deve conter OBRIGATÓRIAMENTE essas seguintes colunas: 

"Username", "Phone number", "Phone country code", "Public email", "City", "External url" e "Biography".

**Se quiser utilizar o programa, sugiro que utilize esta extensão para fazer o scraping:** 
https://chromewebstore.google.com/detail/growman-extrator-de-e-mai/hndnabgpcmhdmaejoapophbidipmgnpb

Após selecionar a planilha, ele executará o código, que filtrará a coluna "Biography" para manter somente os perfis que contenham as palavras-chaves contidas no arquivo "keywords.json", que fazem referencia a clínicas de estética ou medicina estética em geral, após essa filtragem, ele vai separar a planilha em dois arquivos, um arquivo "bruto", sem nenhum tipo de formatação, e outro arquivo formatado conforme as necessidades, que são separar os leads por região, Contatos do Brasil, Portugal, Espanha, Sem Número e do resto do Mundo, oque facilita o disparo de mensagens posteriormente. 

Se tudo der certo (Esperamos que dê) aparecerá um pop-up confirmando que deu tudo certo, se nada acontecer, provavelmente há algo de errado com seu arquivo, revise ele e refaça o processo!

Discord: felipepietro

