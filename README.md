Python (assim como C#, Java, Perl, Ruby e Lua) utiliza garbage collection ao invés de gerenciamento de memória manual. O gerenciador de memória procura periodicamente por qualquer objeto que não está mais sendo referenciados pelo programa.

O Python utiliza um heap privado contendo todos os objetos e estruturas de dados. Ele utiliza aspectos variados de gerenciamento de armazenamento dinâmico, como: compartilhamento, segmentação, pré-alocação ou caching.

O programador não possui acesso a este heap privado, ele é gerenciado pelo interpretador. A alocação do objetos no heap é feita sob demanda pelo gerenciador de memória do Python, a API core dá acesso a algumas ferramentas para o programador. Informações mais detalhadas podem ser encontradas na documentação do Python.