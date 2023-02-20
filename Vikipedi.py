import wikipedia
import docx

# Wikipedia dil ayarını Türkçe olarak ayarla
wikipedia.set_lang("tr")

while True:
    # Arama terimini kullanıcıdan al
    check = input("Ne hakkında bilgi almak istersiniz (Çıkmak için q): ")
    
    if check.lower() == "q":
        break
    
    result = wikipedia.search(check)

    # Yeni bir Word belgesi oluştur
    doc = docx.Document()

    # core_properties özelliğine ait author alanını ayarla
    doc.core_properties.author = "omer-x-kiyak"

    # Her bir arama sonucu için özetleri belgeye ekle
    for item in result:
        try:
            # Sayfayı getir ve özetini ekle
            page = wikipedia.page(item)
            if page.title:
                doc.add_heading(page.title, level=1)
                doc.add_paragraph(page.summary)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
            continue
        except wikipedia.exceptions.PageError as e:
            print(f"Sayfa bulunamadı: {e}")
            continue

    if result:
        # Dosyayı kaydet
        doc.save(check + ' arama_sonucu.docx' )

        print("Dosya kaydedildi.")
    else:
        print("Arama sonucu bulunamadı.")
