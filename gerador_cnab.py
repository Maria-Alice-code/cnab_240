class Header_arquivo:  # identificador 0
    def __init__(self, df):
        self.output = []
        for i in range(0, 24):
            a = df['_c1'].iloc[i]  # Valor a ser formatado
            x = int(df['_c2'].iloc[i])  # Valor de comprimento para formatação
            
            # Se o valor de 'a' for brancos, substituímos por 'x' espaços
            if a == "BRANCOS" or a == "Brancos":
                formatted = ' ' * x
            else:
                formatted = f"{a:0{x}}"  # Em casos de valores normais, continuar com padrão AUTABANCK

            self.output.append(formatted)  # adicionar na lista final

    def __str__(self):
        return ''.join(self.output)


class Header_Lote:  # identificador 0
    def __init__(self, df):
        self.output = []
        for i in range(0, 23):
            a = df['_c6'].iloc[i]  # Valor a ser formatado
            x = int(df['_c7'].iloc[i])  # Valor de comprimento para formatação
            
            # Se o valor de 'a' for brancos, substituímos por 'x' espaços
            if a == "BRANCOS" or a == "Brancos":
                formatted = ' ' * x
            else:
                formatted = f"{a:0{x}}"  # Em casos de valores normais, continuar com padrão AUTABANCK

            self.output.append(formatted)  # adicionar na lista final

    def __str__(self):
        return ''.join(self.output)


class Segmentos_TP:  # identificador P
    def __init__(self, df):
        self.output = []
        for i in range(len(df)):
            a = df['_c11'].iloc[i]  # Valor a ser formatado
            x = int(df['_c12'].iloc[i])  # Valor de comprimento para formatação
            
            # Se o valor de 'a' for brancos, substituímos por 'x' espaços
            if a == "BRANCOS" or a == "Brancos":
                formatted = ' ' * x
            else:
                formatted = f"{a:0{x}}"  # Em casos de valores normais, continuar com padrão AUTABANCK

            self.output.append(formatted)  # adicionar na lista final

    def __str__(self):
        return ''.join(self.output)


class Segmentos_TQ:  # identificador P
    def __init__(self, df):
        self.output = []
        for i in range(0, 22):
            a = df['_c16'].iloc[i]  # Valor a ser formatado
            x = int(df['_c17'].iloc[i])  # Valor de comprimento para formatação
            
            # Se o valor de 'a' for brancos, substituímos por 'x' espaços
            if a == "BRANCOS" or a == "Brancos":
                formatted = ' ' * x
            else:
                formatted = f"{a:0{x}}"  # Em casos de valores normais, continuar com padrão AUTABANCK

            self.output.append(formatted)  # adicionar na lista final

    def __str__(self):
        return ''.join(self.output)


class Trailer_5:  # identificador P
    def __init__(self, df):
        self.output = []
        for i in range(0, 15):
            a = df['_c21'].iloc[i]  # Valor a ser formatado
            x = int(df['_c22'].iloc[i])  # Valor de comprimento para formatação
            
            # Se o valor de 'a' for brancos, substituímos por 'x' espaços
            if a == "BRANCOS" or a == "Brancos":
                formatted = ' ' * x
            else:
                formatted = f"{a:0{x}}"  # Em casos de valores normais, continuar com padrão AUTABANCK

            self.output.append(formatted)  # adicionar na lista final

    def __str__(self):
        return ''.join(self.output)


class Trailer_9:  # identificador P
    def __init__(self, df):
        self.output = []
        for i in range(0, 8):
            a = df['_c26'].iloc[i]  # Valor a ser formatado
            x = int(df['_c27'].iloc[i])  # Valor de comprimento para formatação
            
            # Se o valor de 'a' for brancos, substituímos por 'x' espaços
            if a == "BRANCOS" or a == "Brancos":
                formatted = ' ' * x
            else:
                formatted = f"{a:0{x}}"  # Em casos de valores normais, continuar com padrão AUTABANCK

            self.output.append(formatted)  # adicionar na lista final

    def __str__(self):
        return ''.join(self.output)


def gerar_cnab(df):
    linhas = []

    # Usando as classes para gerar o conteúdo CNAB
    linhas.append(str(Header_arquivo(df)))  # Criando a instância da classe Header_arquivo
    linhas.append(str(Header_Lote(df)))     # Criando a instância da classe Header_Lote
    linhas.append(str(Segmentos_TP(df)))  # Criando a instância da classe Segmentos_TP
    linhas.append(str(Segmentos_TQ(df)))  # Criando a instância da classe Segmentos_TQ
    linhas.append(str(Trailer_5(df)))  # Criando a instância da classe Trailer_5
    linhas.append(str(Trailer_9(df)))  # Criando a instância da classe Trailer_9

    return '\n'.join(linhas)
