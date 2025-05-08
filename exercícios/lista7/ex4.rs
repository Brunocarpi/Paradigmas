use std::io;

fn main() {
    let mut numeros = Vec::new();

    for i in 1..=3 {
        println!("Digite o {}º número inteiro:", i);
        let mut entrada = String::new();
        io::stdin().read_line(&mut entrada).expect("Falha ao ler");
        let numero: i32 = entrada.trim().parse().expect("Digite um número válido");
        numeros.push(numero);
    }

    numeros.sort();

    println!("Números em ordem crescente: {:?}", numeros);
}
