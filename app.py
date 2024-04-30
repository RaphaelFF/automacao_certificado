import openpyxl
from PIL import Image, ImageDraw, ImageFont

#abrindo planilha
planilha = openpyxl.load_workbook('planilha_curso.xlsx')

#acessando a pagina da planilha
pagina_planilha = planilha['pagina1']

#acessando as celulas da planilha
for linha in pagina_planilha.iter_rows(min_row=2) :
    curso = linha[0].value
    nome_aluno = linha[1].value
    carga_horaria = linha[2].value
    data_conclusao = linha[3].value

    #abrindo a imagem do certificado padrao com a bilblioteca pillow - image
    imagem = Image.open('certificado-padrao.jpg')
    
    #criando um objeto draw para desenhar na imagem
    imagem_objeto = ImageDraw.Draw(imagem)

    #definindo a fonte do texto
    fonte_nome = ImageFont.truetype('./fontes/OpenSans-Bold.ttf',40)
    fonte_curso = ImageFont.truetype('./fontes/OpenSans-Bold.ttf',50)
    fonte_geral = ImageFont.truetype('./fontes/OpenSans-Regular.ttf',28)

    #adicionando o texto na imagem
    imagem_objeto.text((355,430), nome_aluno, 'black', font=fonte_nome)
    imagem_objeto.text((405,499), data_conclusao, 'black', font=fonte_geral)
    imagem_objeto.text((355,540), curso, 'black', font=fonte_curso)
    imagem_objeto.text((650,670), carga_horaria, 'black', font=fonte_geral)

    #salvando as imagem modificadas
    imagem.save(f'./certificados_salvos/{nome_aluno}.png')
    
