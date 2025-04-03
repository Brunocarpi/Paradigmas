# #include <iostream>
# #include <vector>
# #include <algorithm>
# #include <map>
# #include <iomanip>
# #include <limits>

# using namespace std;


# double calcularMedia(const vector<double>& vetor) {
#     if (vetor.empty()) return 0.0;
#     double soma = 0.0;
#     for (double num : vetor) {
#         soma += num;
#     }
#     return soma / vetor.size();
# }


# double calcularMediana(vector<double> vetor) {
#     if (vetor.empty()) return 0.0;
#     sort(vetor.begin(), vetor.end());
#     int tamanho = vetor.size();
#     if (tamanho % 2 == 0) {
#         return (vetor[tamanho / 2 - 1] + vetor[tamanho / 2]) / 2.0;
#     } else {
#         return vetor[tamanho / 2];
#     }
# }


# vector<double> calcularModa(const vector<double>& vetor) {
#     map<double, int> frequencia;
#     for (double num : vetor) {
#         frequencia[num]++;
#     }

#     int maxFrequencia = 0;
#     for (const auto& par : frequencia) {
#         if (par.second > maxFrequencia) {
#             maxFrequencia = par.second;
#         }
#     }

#     vector<double> modas;
#     for (const auto& par : frequencia) {
#         if (par.second == maxFrequencia) {
#             modas.push_back(par.first);
#         }
#     }

#     return modas;
# }


# vector<double> lerVetor(int id) {
#     int tamanho;
#     cout << "Digite o tamanho do vetor " << id << " (max 10): ";
#     cin >> tamanho;
#     while (tamanho < 1 || tamanho > 10) {
#         cout << "Tamanho inválido! Digite um valor entre 1 e 10: ";
#         cin >> tamanho;
#     }

#     vector<double> vetor(tamanho);
#     cout << "Digite os " << tamanho << " elementos do vetor " << id << ":\n";
#     for (int i = 0; i < tamanho; ++i) {
#         cin >> vetor[i];
#     }
#     return vetor;
# }

# int main() {
#     vector<vector<double>> vetores(3);

  
#     for (int i = 0; i < 3; ++i) {
#         vetores[i] = lerVetor(i + 1);
#     }


#     for (int i = 0; i < 3; ++i) {
#         cout << "\n--- Vetor " << i + 1 << " ---\n";
#         cout << "Elementos: ";
#         for (double num : vetores[i]) {
#             cout << num << " ";
#         }
#         cout << "\n";

#         double media = calcularMedia(vetores[i]);
#         double mediana = calcularMediana(vetores[i]);
#         vector<double> modas = calcularModa(vetores[i]);

#         cout << fixed << setprecision(2);
#         cout << "Média: " << media << "\n";
#         cout << "Mediana: " << mediana << "\n";

#         if (modas.size() == vetores[i].size()) {
#             cout << "Moda: Nenhuma (todos os elementos são únicos)\n";
#         } else {
#             cout << "Moda(s): ";
#             for (double moda : modas) {
#                 cout << moda << " ";
#             }
#             cout << "\n";
#         }
#     }

#     return 0;
# }