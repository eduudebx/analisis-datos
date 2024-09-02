library(readxl)
library(dplyr)
library(openxlsx)


main <- function(){
    datos <- read_excel('datos-encuesta.xlsx')

    datos <- datos %>%
        mutate(Redes_Sociales = Redes_Sociales %>%
                trimws() %>% 
                toupper() %>%
                sub("\\.$", "", .))
    
    datos <- datos %>% select(-Marca_Temporal)


    write.xlsx(datos, 'datos-limpios.xlsx')  
}


main()