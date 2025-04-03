# #include <iostream>
# using namespace std;

# void calcularNotas(int valor) {
#     if (valor < 15 || valor > 500) {
#         cout << "Valor inválido! O saque deve ser entre R$15 e R$500.\n";
#         return;
#     }

#     int notas200 = valor / 200;
#     valor %= 200;

#     int notas50 = valor / 50;
#     valor %= 50;

#     int notas5 = valor / 5;
#     valor %= 5;

#     int notas1 = valor;

    
#     cout << "Notas fornecidas:\n";
#     if (notas200 > 0) cout << notas200 << " nota(s) de R$200\n";
#     if (notas50 > 0) cout << notas50 << " nota(s) de R$50\n";
#     if (notas5 > 0) cout << notas5 << " nota(s) de R$5\n";
#     if (notas1 > 0) cout << notas1 << " nota(s) de R$1\n";
# }

# int main() {
#     int saque;
#     cout << "Digite o valor do saque (entre R$15 e R$500): ";
#     cin >> saque;

#     calcularNotas(saque);

#     return 0;
# }