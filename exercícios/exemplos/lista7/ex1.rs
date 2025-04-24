use std::collections::HashSet;  
// Importa HashSet, que armazena valores únicos. Vamos usá-lo para detectar ciclos nos números. 
 
use std::io;  
// Importa o módulo para entrada de dados via teclado. 
// Função que calcula a soma dos quadrados dos dígitos de um número. 
// Exemplo: 82 -> 8² + 2² = 64 + 4 = 68 
fn soma_dos_quadrados(mut n: i32) -> i32 { 
    let mut soma = 0; // Inicializa a soma em 0 
    while n > 0 { 
        let digito = n % 10;       // Pega o último dígito 
        soma += digito * digito;   // Soma o quadrado do dígito 
        n /= 10;                   // Remove o último dígito 
    } 
    soma // Retorna o resultado final da soma dos quadrados 
} 

 
// Função que verifica se um número é feliz ou não 
fn numero_feliz(mut n: i32) -> bool { 
    let mut visitados = HashSet::new(); // Armazena os números já vistos para evitar ciclos 
 
    // Continua enquanto n não for 1 e ainda não tenha sido visitado 
    while n != 1 && !visitados.contains(&n) { 
        visitados.insert(n);           // Adiciona o número ao conjunto 
        n = soma_dos_quadrados(n);     // Calcula a próxima soma 
    } 
 
    n == 1 // Retorna true se chegou a 1, ou false se entrou em ciclo 
} 
 
fn main() { 
    println!("Digite um número inteiro positivo:"); 
    let mut entrada = String::new(); // Armazena a entrada do usuário 
    io::stdin() 
        .read_line(&mut entrada)              // Lê a linha digitada 
        .expect("Erro ao ler entrada");       // Mostra erro se a leitura falhar 
 
    // Tenta converter a entrada para inteiro 
    let numero: i32 = match entrada.trim().parse() { 
        Ok(n) if n > 0 => n, // Se for um número positivo válido, usamos ele 
        _ => { 
            println!("Por favor, digite um número inteiro positivo válido."); 
            return; // Encerra se a entrada for inválida 
        } 
    }; 
 
    // Verifica se o número é feliz e imprime o resultado 
 

 
    if numero_feliz(numero) { 
        println!("{} é um número feliz! 🎉", numero); 
    } else { 
        println!("{} não é um número feliz. 😢", numero); 
    } 
}