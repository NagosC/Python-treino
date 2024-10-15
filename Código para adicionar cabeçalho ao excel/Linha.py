import os
import win32com.client as win32

pasta_excel = r"C:\Users\leand\OneDrive\Documents\Python Scripts\Excel" 
imagem_cabecalho = r"C:\Users\leand\OneDrive\Documents\Python Scripts\logo.png"  

# Verifica se a imagem existe
if not os.path.exists(imagem_cabecalho):
    raise FileNotFoundError(f"Imagem do cabeçalho não encontrada: {imagem_cabecalho}")


arquivos_excel = [f for f in os.listdir(pasta_excel) if f.endswith((".xlsx", ".xlsm"))]


excel = win32.gencache.EnsureDispatch("Excel.Application")
excel.Visible = False  

for arquivo in arquivos_excel:
    caminho_arquivo = os.path.join(pasta_excel, arquivo)  

    try:
     
        wb = excel.Workbooks.Open(caminho_arquivo)

       
        for sheet in wb.Sheets:
           
            sheet.Rows(1).Insert()

         
            last_column = sheet.UsedRange.Columns.Count  
            sheet.Range(sheet.Cells(1, 1), sheet.Cells(1, last_column)).Merge()

            sheet.Rows(1).RowHeight = 90  

            imagem = sheet.Shapes.AddPicture(
                Filename=imagem_cabecalho,
                LinkToFile=False,
                SaveWithDocument=True,
                Left=sheet.Cells(1, 1).Left, 
                Top=sheet.Cells(1, 1).Top,  
                Width=1301,  
                Height=90   
            )

       
            imagem.LockAspectRatio = True  
            imagem.Width = sheet.Columns(last_column).Width * 7 

    

        wb.Save()
        print(f"Imagem adicionada com sucesso em: {arquivo}")

    except Exception as e:
        print(f"Erro ao processar {arquivo}: {e}")

    finally:
        wb.Close()  # Fecha o arquivo


excel.Quit()
print("Processo concluído!")
