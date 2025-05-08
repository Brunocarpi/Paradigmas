praias <- data.frame(
  praia = c("Joaquina", "Campeche", "Armação", "Praia Mole"),
  caranguejos = c(42, 34, 59, 18)
)

print("Data frame inicial:")
print(praias)


menos_30 <- subset(praias, caranguejos < 30)
print("Praias com menos de 30 caranguejos:")
print(menos_30)


praias$regiao <- c("leste", "sul", "sul", "leste")
print("Data frame com coluna 'regiao':")
print(praias)


leste_menos_20 <- subset(praias, regiao == "leste" & caranguejos < 20)
print("Praias da região leste com menos de 20 caranguejos:")
print(leste_menos_20)


sul_mais_40 <- subset(praias, regiao == "sul" & caranguejos > 40)
print("Praias do sul com mais de 40 caranguejos:")
print(sul_mais_40)


mais_50 <- subset(praias, caranguejos > 50)
regioes_mais_50 <- unique(mais_50$regiao)
print("Regiões com praias com mais de 50 caranguejos:")
print(regioes_mais_50)
