use std::io;

fn main() {
    println!("Digite um número inteiro para ver sua tabuada:");

    let mut numero = String::new();
    io::stdin().read_line(&mut numero).expect("Falha ao ler");

    let numero: i32 = numero.trim().parse().expect("Por favor, digite um número válido");

    println!("Tabuada de {}:", numero);

    for i in 1..=10 {
        println!("{} x {} = {}", numero, i, numero * i);
    }
}
