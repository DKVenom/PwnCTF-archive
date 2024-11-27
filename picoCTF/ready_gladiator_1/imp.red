;redcode
;name Hybrid-Warrior
;assert 1
spl 1              ; Multi-process bombing
spl 1
mov 0, 2           ; Basic self-replication (Imp-like)
loop:
    mov bomb, >5   ; Bomb 5 steps ahead
    add #5, loop   ; Move loop forward
    jmp loop       ; Repeat bombing
bomb:
    dat #0         ; Bomb definition
end loop            ; Start at the loop
end
