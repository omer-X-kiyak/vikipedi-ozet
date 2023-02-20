# vikipedi-özet
Bu kod, kullanıcının belirlediği bir arama terimini Wikipedia'da arar ve her bir arama sonucu için özetlerini bir Word belgesinde toplar. Daha sonra belgeyi kullanıcının istediği bir isimle kaydeder.

Kodun ilk satırlarında, Wikipedia'nın Türkçe sürümüne erişmek için dil ayarı Türkçe olarak ayarlanır. Ardından, bir while döngüsü kullanarak kullanıcıdan arama terimini alırız. Kullanıcı "q" harfine basarsa döngüden çıkılır.

Arama terimi kullanıcıdan alındıktan sonra, Wikipedia'da bu terime göre arama yapılır ve sonuçlar "result" adlı bir değişkende saklanır. Daha sonra "docx" modülü kullanılarak yeni bir Word belgesi oluşturulur. Sonrasında, her bir arama sonucu için özetleri belgeye ekleriz.

Eğer sonuç varsa, kullanıcının belirlediği isimle bir Word belgesi oluşturulur ve içeriği kaydedilir. Sonuç yoksa, "Arama sonucu bulunamadı." mesajı verilir.
