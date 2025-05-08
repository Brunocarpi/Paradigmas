library(dplyr)

data(Titanic)

Titanic_df <- as.data.frame(Titanic)

str(Titanic_df)


feminino <- Titanic_df %>% filter(Sex == "Female")
print("Passageiros do sexo feminino:")
print(feminino)


terceira_sobreviventes <- Titanic_df %>%
  filter(Class == "3rd", Survived == "Yes")
print("Passageiros da 3ª classe que sobreviveram:")
print(terceira_sobreviventes)


adultos_sobreviventes_por_classe <- Titanic_df %>%
  filter(Age == "Adult", Survived == "Yes") %>%
  group_by(Class) %>%
  summarise(Total = sum(Freq))
print("Número de passageiros adultos sobreviventes por classe:")
print(adultos_sobreviventes_por_classe)


homens_adultos_por_classe <- Titanic_df %>%
  filter(Sex == "Male", Age == "Adult") %>%
  group_by(Class) %>%
  summarise(Total = sum(Freq))
print("Número de passageiros masculinos adultos em cada classe:")
print(homens_adultos_por_classe)


mulheres_adultas_sobreviventes <- Titanic_df %>%
  filter(Sex == "Female", Age == "Adult", Survived == "Yes") %>%
  group_by(Class) %>%
  summarise(Total = sum(Freq))
print("Número de mulheres adultas sobreviventes por classe:")
print(mulheres_adultas_sobreviventes)
