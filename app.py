import openpyxl
from PIL import Image, ImageDraw, ImageFont

#abrindo planilha
planilha = openpyxl.load_workbook('planilha_curso.xlsx')

#acessando a pagina da planilha
pagina_planilha = planilha['pagina1']

#acessando as celulas da planilha
for linha in pagina_planilha.iter_rows(min_row=2) :
    curso = linha[0].value
    print(curso)
    break
