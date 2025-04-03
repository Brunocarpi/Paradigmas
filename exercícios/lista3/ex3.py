# #include <iostream>
# #include <vector>
# #include <sstream>
# using namespace std;

# class Nome {
# private:
#     vector<string> partes;

# public:
    
#     Nome(const string& nomeCompleto) {
#         istringstream iss(nomeCompleto);
#         string parte;
#         while (iss >> parte) {
#             partes.push_back(parte);
#         }
#     }

    
#     string getSobrenome() const {
#         if (partes.empty()) return "";
#         return partes.back(); 
#     }

    
#     string getIniciais() const {
#         string iniciais;
#         for (size_t i = 0; i < partes.size() - 1; ++i) { 
#             if (!partes[i].empty()) {
#                 iniciais += partes[i][0]; 
#                 iniciais += ". ";         
#             }
#         }
#         return iniciais;
#     }

   
#     string formatar() const {
#         if (partes.empty()) return "";
#         return getSobrenome() + ", " + getIniciais();
#     }
# };

# int main() {
#     string nomeCompleto;
#     cout << "Digite o nome completo: ";
#     getline(cin, nomeCompleto);

#     Nome nome(nomeCompleto);
#     cout << nome.formatar() << endl;

#     return 0;
# }