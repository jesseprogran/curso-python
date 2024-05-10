#AND ---> TODAS CONDIÇÃO SÃO VERDADEIRA (TRUE)
# idade = 10;
# altura = 1.80;

# resultado = (idade >= 18) and (altura >= 1.80);
# msg = 'pode participar do evento? ' + str(resultado);
# print(msg);

#OR ----> TODAS CONIÇÃO TIVER UMA VERDADEIRA (TRUE) ENTÃO SERÁ (TRUE) OU VICE VERSA

# porta = 'fechou'
# janela = 'fechada'

# alarme = (porta == 'abriu') or (janela == 'abriu')
# msg = 'Alarme disparado? ' + str(alarme)
# print(msg)

#NOT ---> ELE IVERTA A CONDIÇÃO SE FOR VERDADEIRA (TRUE) SERÁ (FALSE) E VICE VERSA

temDinheiro = False
temDinheiro = not temDinheiro
msg = 'Tem dinheiro? ' + str(temDinheiro)
print(msg)
