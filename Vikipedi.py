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

    # Her bir arama sonucu için özetleri belgeye ekle
    for item in result:
        try:
            # Başlık ekle
            doc.add_heading(item, level=1)
            # Özet ekle
            doc.add_paragraph(wikipedia.page(item).summary)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
            continue

    if result:
        # Dosyayı kaydet
        doc.save(check + ' arama_sonucu.docx' )

        print("Dosya kaydedildi.")
    else:
        print("Arama sonucu bulunamadı.")
