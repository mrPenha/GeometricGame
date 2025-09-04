"""
Jogo de plataforma simples usando Pygame.
Plataforma:
    Plataformas em desníveis
    Portal de saída = forma geométrica do player
Player:
    player = forma geométrica (exceto retangulo pois é a plataforma(chão))
    movimentação do player:
        conforme movimenta para os lados = rotaciona
        se pular:
            pula e rotaciona para o lado indicado ao mesmo tempo
            
Niveis:
    3 niveis para iniciar
    cada nivel com dificuldade crescente
    dependendo do nivel, o player pode ganhar habilidades:
    recompensa:
        cada recompensa = 1 habilidade
        1 recompensa por nivel
        so aparece nos niveis mais difíceis
        habilidade:
            se o player usar a habilidade ela desaparece, senao pode usar no próximo nivel
            pulo duplo:
                pode usar quantas vezes quiser, se passar de nivel, desaparece
            grapple hook:
                ao usar, puxa o player para o local onde foi usado
                ao ser puxado, se colidir com a parte inferior de uma plataforma, para o movimento e perde o grapple hook
            teletransporte:
                não pode ser usado para sair do nivel (longe do portal de saída)
                se não usado no nivel atual, perde a habilidade.
        
Mapa do jogo:
    Plataforma mapeada em matriz
    Cada nivel = matriz diferente

Por enquanto é isso.     
"""