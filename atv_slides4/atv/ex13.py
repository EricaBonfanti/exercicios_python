#Criar um programa em Python que ajuda a verificar se um parafuso está apertado
#corretamente de acordo com o torque especificado. O torque é uma medida de força
#rotacional aplicada a um objeto, e é especialmente importante na engenharia mecânica
#para garantir a segurança das montagens.

#Peça ao usuário para inserir o valor do torque aplicado (em Nm).
#Peça ao usuário para inserir o valor do torque de aperto recomendado (em Nm)
#para o parafuso em questão.
#Compare o torque aplicado com o torque de aperto recomendado.
#Se o torque aplicado estiver dentro de 10% acima ou abaixo do torque recomendado,
#exiba: "O parafuso está apertado corretamente." Caso contrário, exiba:
#"O parafuso não está apertado corretamente."

torque = int(input("Digite o valor do torque aplicado em (nM): \n"))
torque_recomendado = int(input("Digite o valor do torque recomendado em (nM): \n"))

if torque >= 0.9 * torque_recomendado and torque <= 1.1 * torque_recomendado:
    print("O parafuso está apertado corretamente.")
else:
    print("O parafuso não está apertado corretamente.")