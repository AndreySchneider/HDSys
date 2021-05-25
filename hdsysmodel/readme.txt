As linhas são as cardinalidades. O círculo na linha representa 0. O traço na linha representa 1. A terminação com vários traços representa N.

Logo um usuário pode ter zero ou um endereço correspondente, mas o endereço deve obrigatoriamente corresponder a um usuário.

Um usuário pode corresponder a zero ou um adm/gestor/profissional/paciente (qualquer combinação dos quatro tipos de usuário), mas um adm/gestor/profissional/paciente deve obrigatoriamente corresponder a um usuário.

Um usuário pode corresponder a zero ou N eventos, mas um evento sempre tem um usuário.

Um usuário pode corresponder a zero ou um autor de um evento, mas um autor de um evento sempre tem um usuário.

Cada evento corresponde a um autor (no software não dava pra colocar obrigatoriedade de 1 para 1 então ficou o símbolo de zero ou um). Cada autor de evento corresponder a um evento.

Um evento corresponde a zero ou um login (o evento pode ser ou não um login). Todo login é um evento.

Um evento corresponde a zero ou uma medida. A medida é sempre um evento. 

A medida pode ter um alarme. O alarme é correspondente a uma medida.

Agora a edição e a remoção. Elas também são tabelas porque é para armazenar todas as mudanças (um log) para evitar manipulações indevidas no sistema.

Então, entrando nos casos de uso.

Um profissional ou paciente vai modificar um medida de um paciente. 

Não gera um novo evento relacionado a tabela medida (apenas a atualização de uma linha da tabela medida). Gera um novo evento relacionado a edição. Cria uma novo linha na tabela evento, na tabela autor e na tabela edição (com os dados antigos da linha correspondente na tabela medida).

Um profissional ou paciente vai remover um medida de um paciente.

O evento relacionado a medida é removido das tabela evento. A medida é removida da tabela medida.Gera um novo evento relacionado a remoção. Cria uma novo linha na tabela evento, na tabela autor e na tabela remoção (com os dados da linha apagada na tabela medida).

