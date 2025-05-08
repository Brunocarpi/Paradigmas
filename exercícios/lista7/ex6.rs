use std::io;
use regex::Regex;

fn main() {

    println!("Digite uma frase:");
    let mut frase = String::new();
    io::stdin().read_line(&mut frase).expect("Falha ao ler");


    let re = Regex::new(r"[^\w\s]").unwrap(); 
    let frase_limpa = re.replace_all(&frase.to_lowercase(), "");

    let palavras: Vec<&str> = frase_limpa.split_whitespace().collect();

    let mut palindromos = Vec::new();
    for palavra in palavras {
        if palavra.chars().eq(palavra.chars().rev()) && palavra.len() > 1 {
            palindromos.push(palavra.to_string());
        }
    }

    if palindromos.is_empty() {
        println!("Nenhuma palavra palíndroma foi encontrada.");
    } else {
        println!(
            "Foram encontradas {} palavras palíndromos:",
            palindromos.len()
        );
        for p in palindromos {
            println!("{}", p);
        }
    }
}
