
massa_muscular <- c(82, 91, 100, 68, 87, 78, 78, 80, 65, 84, 116, 76, 97, 105, 100, 73, 73, 68)
idade <- c(71, 64, 43, 67, 56, 75, 62, 65, 57, 56, 48, 55, 48, 53, 49, 73, 78, 66)


plot(idade, massa_muscular,
     main = "Dispersão: Idade vs Massa Muscular",
     xlab = "Idade (anos)",
     ylab = "Massa Muscular",
     pch = 19,
     col = "blue")


correlacao <- cor(idade, massa_muscular)
cat("Coeficiente de correlação:", correlacao, "\n")


modelo <- lm(massa_muscular ~ idade)
summary(modelo)


abline(modelo, col = "red", lwd = 2)


idade_50 <- data.frame(idade = 50)
predicao_50 <- predict(modelo, idade_50)
cat("Estimativa da massa muscular para 50 anos:", predicao_50, "\n")
