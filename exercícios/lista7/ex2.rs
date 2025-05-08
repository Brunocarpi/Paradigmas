use std::io;

fn main() {
    println!("Digite o primeiro número:");

    let mut num1 = String::new();
    io::stdin().read_line(&mut num1).expect("Falha ao ler");

    println!("Digite o segundo número:");

    let mut num2 = String::new();
    io::stdin().read_line(&mut num2).expect("Falha ao ler");

    let num1: i32 = num1.trim().parse().expect("Por favor, digite um número válido");
    let num2: i32 = num2.trim().parse().expect("Por favor, digite um número válido");

    let soma = num1 + num2;

    println!("A soma de {} e {} é: {}", num1, num2, soma);
}
