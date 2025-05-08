use std::collections::HashMap;

fn main() {
    let texto = "Olá mundo! Olá, programação em Rust.";

 
    let texto_limpo = texto
        .to_lowercase()
        .replace(&[',', '.', '!', '?'][..], "");

    let mut frequencia = HashMap::new();

    for palavra in texto_limpo.split_whitespace() {
        *frequencia.entry(palavra).or_insert(0) += 1;
    }

    for (palavra, contagem) in &frequencia {
        println!("{}: {}", palavra, contagem);
    }
}
