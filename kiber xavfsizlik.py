from aiogram.types import Message
from aiogram import Bot, Dispatcher, executor
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton
api = '6400569785:AAEkblkrlYyhhuD5KE53AcL7AK1dYUvAFuY'
bot = Bot(api)
dp = Dispatcher(bot)
asosiy_knopka = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="ℹ️ Kiberxavfsizlik - bu ...")],
        [KeyboardButton('▶️ Videokurslar'),KeyboardButton(text='🎞️ Videodarslar')],
        [KeyboardButton(text="📕 Qo'llanmalar (PDF)")],
        [KeyboardButton(text='💾 Kerakli dasturlar'),KeyboardButton(text='📑 Maqolalar')],
        [KeyboardButton(text='💡 Atamalar'),KeyboardButton(text='🌐 Foydali manzillar')],
        [KeyboardButton(text='📲 Aloqa'),KeyboardButton(text='📊 Statistika')]
    ]
)
kiber=ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='Kiberxavfsizlik nima?')],
        [KeyboardButton(text='Kiberxavfsizlik tarixi')],
        [KeyboardButton(text="Kibertahdidlarning tarqalish ko'lami")],
        [KeyboardButton(text='Kiber tahdidlar turlari')],
        [KeyboardButton(text="Kiberxavfsizlikga qayerda o'qiladi?")],
        [KeyboardButton(text='🔙 Orqaga'),KeyboardButton(text='🔝 Asosiy Menyu')]
    ]
)
video=ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='✅ Bepul darslar')],
        [KeyboardButton(text='Tarmoq administratorligi (CISCO)')],
        [KeyboardButton(text='Offensive SQL darslari')],
        [KeyboardButton(text='▶️Orqaga'),KeyboardButton(text='🔝 Asosiy Menyu')]
    ]
)
video2=ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='🗂️ Antivirus - Nod32'),KeyboardButton(text='🗂 Kaspersky')],
        [KeyboardButton(text='Fleshkani himoyalashni eng oson va samarali usuli!')],
        [KeyboardButton(text='Shaxsiy fayllarni yashiramiz!')],
        [KeyboardButton(text="Windows 10'dagi ayg'oqchi funksiyalarini o'chirish")],
        [KeyboardButton(text="O'chirilgan fayllarni qayta tiklash")],
        [KeyboardButton(text='🔙 Orqaga'),KeyboardButton(text='🔝 Asosiy Menyu')]
    ]
)
qollanma=ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='Kiberxavfsizlik asoslari')],
        [KeyboardButton(text='🔙 Orqaga'),KeyboardButton(text='🔝 Asosiy Menyu')]

    ],resize_keyboard=True
)
kerAK=ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='🛡️ Antiviruslar'),KeyboardButton(text='🚫 Reklama bloklovchilar')],
        [KeyboardButton(text='🅿️ Parol menejerlar'),KeyboardButton(text='📛 Firewall dasturlari')],
        [KeyboardButton(text="🔄 Ma'lumotlarni tiklovchilar"),KeyboardButton(text="✅ Ma'lumotlarni himoyalovchilar")],
        [KeyboardButton(text='🔰 VPN dasturlar'),KeyboardButton(text='🈹 Shifrlovchi dasturla')],
        [KeyboardButton(text='❗️Xavfsizlik'),KeyboardButton(text='🌐 Brauzerlar')],
        [KeyboardButton(text='🔙 Orqaga'),KeyboardButton(text='🔝 Asosiy Menyu')]
    ]
)
maqola=ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='Crack dasturlar')],
        [KeyboardButton(text='💣 Zip-bomba')],
        [KeyboardButton(text='Ma’lumotlarni bir zumda o‘chiruvchi fleshka')],
        [KeyboardButton(text="Tizim ustidan nazoratni qo'lga kiritish yo'llari")],
        [KeyboardButton(text="Kiberxavfsizlik bo'yicha foydali maslahatlar")],
        [KeyboardButton(text='🔙 Orqaga'),KeyboardButton(text='🔝 Asosiy Menyu')]
    ]
)
antivirus=ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='Kaspersky Free')],
        [KeyboardButton(text='NOD32')],
        [KeyboardButton(text='Kaspersky')],
        [KeyboardButton(text='⬅️ Orqaga'),KeyboardButton(text='🔝 Asosiy Menyu')]
    ]
)

tarmoq=ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='Tarmoq administratorligi 1-dars'),KeyboardButton(text='Tarmoq administratorligi 2-dars')],
        [KeyboardButton(text='Tarmoq administratorligi 3-dars'),KeyboardButton(text='Tarmoq administratorligi 4-dars')],
        [KeyboardButton(text='Tarmoq administratorligi 5-dars'),KeyboardButton(text='Tarmoq administratorligi 6-dars')],
        [KeyboardButton(text='Tarmoq administratorligi 7-dars'),KeyboardButton(text='Tarmoq administratorligi 8-dars')],
        [KeyboardButton(text='Tarmoq administratorligi 9-dars'),KeyboardButton(text='Tarmoq administratorligi 10-dars')],
        [KeyboardButton(text='Tarmoq administratorligi 9-dars'),KeyboardButton(text='Tarmoq administratorligi 10-dars')],
        [KeyboardButton(text='Tarmoq administratorligi 11-dars'),KeyboardButton(text='Tarmoq administratorligi 12-dars')],
        [KeyboardButton(text='Tarmoq administratorligi 13-dars'),KeyboardButton(text='Tarmoq administratorligi 14-dars')],
        [KeyboardButton(text='Tarmoq administratorligi 15-dars')],
        [KeyboardButton(text='🔙 Orqaga'),KeyboardButton(text='🔝 Asosiy Menyu')]
    ]
)
parol=ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='KeePass'),KeyboardButton(text='LastPass Password')],
        [KeyboardButton(text='🔙 Orqaga'),KeyboardButton(text='🔝 Asosiy Menyu')]
    ],resize_keyboard=True
)
reklama=ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='Adguard')],
        [KeyboardButton(text='🔙 Orqaga'),KeyboardButton(text='🔝 Asosiy Menyu')]
    ],resize_keyboard=True
)
atama=ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='1-qism'),KeyboardButton(text='2-qism')],
        [KeyboardButton(text='🔙 Orqaga'),KeyboardButton(text='🔝 Asosiy Menyu')]
    ],resize_keyboard=True
)
anonim=ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='Anonimlik sari yana bir qadam')],
        [KeyboardButton(text="Raqamli izlarimizni yo'qotamiz")],
        [KeyboardButton(text='🔙 Orqaga'),KeyboardButton(text='🔝 Asosiy Menyu')]

    ],resize_keyboard=True
)
@dp.message_handler(text="📊 Statistika")
async def statistika(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text="""👥 Barcha obunachilar: 19371 kishi.
✅ Faol obunachilar: 11749 kishi.

🔜 Oxirgi 24 soatda 7 obunachi qo'shildi.
🔝 Oxirgi 1 oyda 303 obunachi qo'shildi.

📆 Bot ishga tushganiga 529 kun bo'ldi.

📊 @KiberXavfsizlikBot statistikasi!""")



@dp.message_handler(text="📲 Aloqa")
async def aloqa(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text="""👨🏻‍💻 Loyiha asoschisi —  Jonibek Turapov\n

📩 Murojaatlar uchun — @fullstack_online""")

@dp.message_handler(text="🌐 Foydali manzillar")
async def foyda(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text='🌐 Foydali manzillar',reply_markup=anonim)

@dp.message_handler(text="💡 Atamalar")
async def qanfma(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text='💡 Atamalar',reply_markup=atama)
@dp.message_handler(text="LastPass Password")
async def qanfma233sdfgh(message:Message):
    chatid=message.chat.id
    rasm1=open('rasm2.jpg','rb')
    await bot.send_photo(chat_id=chatid,photo=rasm1,caption="""LastPass Password v4.62.0 (x86/x64)

ℹ️ LastPass Password - LastPass tomonidan ishlab chiqilgan Internet Explorer, Google Chrome, Mozilla Firefox, Opera va Apple Safari uchun yagona plagin o'rnatuvchi sifatida tarqatilgan eng yaxshi parolni saqlash dasturlaridan biri. LastPass-dagi parollar asosiy parol bilan himoyalangan, mahalliy sifatida saqlanadi va boshqa har qanday brauzer bilan sinxronlashtirilishi mumkin. LastPass, shuningdek, parolni kiritish va shakllarni to'ldirishni avtomatlashtirish imkonini beruvchi ariza to'ldiruvchisiga ega.

🛡@KiberXavfsizlikBot""")


@dp.message_handler(text="KeePass")
async def qanfma233(message:Message):
    chatid=message.chat.id
    rasm=open('rasm.jpg','rb')
    await bot.send_photo(chat_id=chatid,photo=rasm,caption="""KeePass v2.45.0 (x86/x64)

ℹ️ KeePass - Rijndael, AES va Twofish shifrlash algoritmlari bilan rivojlangan, shifrlangan ma'lumotlar bazasida parollarni xavfsiz saqlash uchun bepul dastur. Dastur barcha maxfiy ma'lumotlarni samarali va xavfsiz saqlaydi va shaxsiy kompyuterda o'rnatilgan barcha yordamchi dasturlarni himoya qiladi.

🛡@KiberXav""")

@dp.message_handler(text='⬅️ Orqaga')
async def orqa4(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text='⬅️ Orqaga',reply_markup=kerAK)
@dp.message_handler(text="Kaspersky Free")
async def qollanma233(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text="""💻Kaspersky Free  18.0.0.405.2017
#Kaspersky / #antivirus


 📁Bu Kasperskiy antivirusining bepul versiyasi yani litsenziya talab qilmaydigan versiyasi.U foydalanuvchilarni zararli dasturlardan himoya qilish uchun mo'ljallangan va asosan ishlaydigan kompyuterlar uchun mo'ljallangan Microsoft  Windows va macOS,  Linux uchun versiyalari  mavjud. Kasperskiy Anti-Virus xususiyatlari Real vaqt himoya o'z ichiga oladi, aniqlash va viruslar olib tashlash,  reklama, Keylogger, zararli vositalari va avtomatik terish, shuningdek aniqlash va rootkits olib tashlash kabi antivirusdir ©@shk_uz

💻@KiberXavfsizlilBot""",)

@dp.message_handler(text="📑 Maqolalar")
async def maqol(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text='📑 Maqolalar',reply_markup=maqola)

@dp.message_handler(text="🛡️ Antiviruslar")
async def qoll(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text="🛡️ Antiviruslar",reply_markup=antivirus)
@dp.message_handler(text="💾 Kerakli dasturlar")
async def qollanma23(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text="💾 Kerakli dasturlar",reply_markup=kerAK)
@dp.message_handler(text="NOD32")
async def qollanma2sd3hgf(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text="""ESET NOD32 Antivirus 4.2.7 (x64)

ℹ️ ESET NOD32 Antivirusining kalit so'ramaydigan va barcha imkoniyatlarga ega versiyasi. ©️@kompyuter_akademiyasi

🛡@KiberXavfsizlikBot""")

@dp.message_handler(text="Kaspersky")
async def qollma23hgfdcv(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text="""Kaspersky Security Cloud Free

ℹ️ Kaspersky antivirusining bepul versiyasi. Dastur internet yordamida o'rnatiladi (tahminan 250 mb yuklab oladi).

🌐 Dasturni rasmiy sayti (https://www.kaspersky.ru/downloads/thank-you/try-free-cloud-antivirus)dan ham olishingiz mumkin. Windows 10/8.1/8/7 (x32/x64) uchun. ©️@kompyuter_akademiyasi

🛡@KiberXavfsizlikBot""")

















@dp.message_handler(text="Kiberxavfsizlik asoslari")
async def qollanma2(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text="""Kiberxavfsizlik asoslari

✍️ S.K.Ganiev, A.A.Ganiev, Z.T.Xudoyqulov (Toshkent 2020)

ℹ️ O‘quv qo‘llanmada kiberxavfsizlik va uning asosiy tushunchalari, axborotning kriptografik himoyasi, foydalanishni nazoratlash, tarmoq xavfsizligi, foydalanuvchanlikni ta’minlash usullari, dasturiy vositalar xavfsizligi, axborot xavfsizligi siyosati va risklarni boshqarish, kiberjinoyatchilik, kiberhuquq, kiberetika hamda inson faoliyati xavfsizligining nazariy va amaliy asoslari muhokama etilgan.

🛡️@KiberXavfsizlikBot""")

@dp.message_handler(text="📕 Qo'llanmalar (PDF)")
async def qollanm23a(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text="📕 Qo'llanmalar (PDF)",reply_markup=qollanma)
@dp.message_handler(text='🗂️ Antivirus - Nod32')
async def ofis(message:Message):
    chatid=message.chat.id
    nom1=open('virus1.mp4','rb')
    nom2=open('virus2.mp4','rb')
    await bot.send_video(chat_id=chatid,video=nom1,caption="""ESET NOD32 antivirusini o'rnatish

ℹ️ ESET NOD32 antivirusini o'rnatishni va kerakli sozlamalarni amalga oshirishni o'rganamiz. ©️@kompyuter_akademiyasi

🛡️@KiberXavfsizlikBot""")
    await bot.send_video(chat_id=chatid,video=nom2,caption="""ESET NOD32 antivirus bazasini internetsiz (oflayn) yangilash

ℹ️ ESET NOD32 antivirus bazasini internetsiz (oflayn) yangilash bo'yicha videodars. Internetsiz degani kompyuter antivirusi bazasi yangilanishi uchun kompyuter internetga ulanishi shart emasligi tushunilishi kerak. ©️@kompyuter_akademiyasi
Videoda foydalanilgan saytlar:
Nod32.uz
 (https://nod32.uz/offline-base-nod32/23-bazy-obnovlyayutsya-odin-raz-v-dva-dnya-po-vozmozhnosti-ezhednevno.html)Uzsoft.uz

 (https://uzsoft.uz/%D0%B1%D0%B0%D0%B7%D0%B0-%D0%BE%D0%B1%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-esetnod32-tas-ix/)🛡️@KiberXavfsizlikBot""")



@dp.message_handler(text='🎞️ Videodarslar')
async def vilar(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text='🎞️ Videodarslar',reply_markup=video2)
@dp.message_handler(text='▶️Orqaga')
async def orqa2(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text='▶️Orqaga',reply_markup=video)
@dp.message_handler(text='Offensive SQL darslari')
async def ofis(message:Message):
    chatid=message.chat.id
    vid1=open('dars1.mp4','rb')
    await bot.send_video(chat_id=chatid,video=vid1,caption="1- dars | Kirish | Offensive SQL")
@dp.message_handler(text='Tarmoq administratorligi (CISCO)')
async def tarmodlar(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text='Tarmoq administratorligi (CISCO)',reply_markup=tarmoq)
@dp.message_handler(commands='start')
async def start(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text='Assalomu aleykum',reply_markup=asosiy_knopka)
@dp.message_handler(text='Tarmoq administratorligi 1-dars')
async def dars1(message:Message):
    chatid=message.chat.id
    vide1=open('dars1.mp4','rb')
    vide2=open('dars2.mp4','rb')
    await bot.send_video(chat_id=chatid,video=vide1,caption="""📹 Tarmoq Administratorligi  Kirish

YouTube: bit.ly/3DD2pts
Telegram: t.me/TarmoqUstasi

👉 @KiberxavfsizlikBot""")
    await bot.send_video(chat_id=chatid,video=vide2,caption="""📹 Tarmoq Administratorligi  #1DARS

YouTube: bit.ly/3DD2pts
Telegram: t.me/TarmoqUstasi

👉 @KiberxavfsizlikBot""")
@dp.message_handler(text='🗂 Kaspersky')
async def dars2(message:Message):
    chatid=message.chat.id
    nom3=open('virus1.mp4','rb')
    await bot.send_video(chat_id=chatid,video=nom3,caption="""Kaspersky Security Cloud Free antivirusini o'rnatish va foydalanish. Bazasini yangilash, vaqtincha o'chirib turish...

ℹ️ Kompyuter xavfsizligini ta'minlash uchun ham faqatgina ishonchli dasturlardan foydalanish kerak. Bugun juda mashhur bo'lgan Kaspersky antivirusini o'rnatish va foydalanishni ko'rib chiqamiz. Video davomida antivirus bazasini yangilash, vaqtincha o'chirib turish va kompyuterimizga beradigan yuklamasini aniqlashni ham o'rganamiz. ©️@kompyuter_akademiyasi

❗️Dastur internet yordamida o'rnatiladi!

🛡@KiberXavfsizlikBot""")



@dp.message_handler(text='Fleshkani himoyalashni eng oson va samarali usuli!')
async def flesfka(message:Message):
    chatid=message.chat.id
    nom4=open('dars3.mp4','rb')
    await bot.send_video(chat_id=chatid,video=nom4,caption="""Fleshkani viruslardan himoyalashni eng oson va samarali usuli!

ℹ️ Fleshkani viruslardan himoyalashni eng oddiy usulini o'rganamiz. Bu usul ko'pchilik viruslarni to'g'ridan to'g'ri fleshka ichiga kirishini taqiqlaydi. Shu orqali fleshkamizni viruslarda asraymiz. Ushbu usulni amalga oshirish uchun hech qanday dasturni o'rnatish shart emas. ©️@kompyuter_akademiyasi

🛡️@KiberXavfsizlikBot""")

@dp.message_handler(text='Shaxsiy fayllarni yashiramiz!')
async def shaxsiy(message:Message):
    chatid=message.chat.id
    nom5=open('dars3.mp4','rb')
    await bot.send_video(chat_id=chatid,video=nom5,caption="""Shaxsiy fayllarni yashiramiz!

ℹ️ Kompyuterdagi shaxsiy fayllarni yashirishni 2 usuli haqida.
1️⃣ Total Commander (skritiy qilish)
2️⃣ Hide Folders dasturi yordamida. ©️@kompyuter_akademiyasi

🛡️@KiberXavfsizlikBot""")


@dp.message_handler(text="Windows 10'dagi ayg'oqchi funksiyalarini o'chirish")
async def dars2(message:Message):
    chatid=message.chat.id
    nom6=open('dars3.mp4','rb')
    await bot.send_video(chat_id=chatid,video=nom6,caption="""Windows 10 yangilanishi, dasturlarini va ayg'oqchi funksiyalarini o'chirish

ℹ️ Ushbu darsimizda Windows 10 dagi yangilanish, o'zining keraksiz dasturlarini va ayg'oqchi funksiyalarini o'chirishni o'rganamiz!

❗️Bunda OneDrive, obnovleniyaga bo'gliq barcha funsiyalar va boshqa kompyuterni tez ishlashiga qarshilik qiluvchi dasturlardan halos bo'lamiz!
©️@kompyuter_akademiyasi

🛡️@KiberXavfsizlikBot""")

@dp.message_handler(text="O'chirilgan fayllarni qayta tiklash")
async def dam(message:Message):
    chatid=message.chat.id
    vil=open('dars3.mp4','rb')
    await bot.send_video(chat_id=chatid,video=vil,caption="""O'chirilgan fayllarni qayta tiklash (fleshka, doimiy xotira va boshqa qurilmalar)

ℹ️ Kompyuterdan o'chirib yuborilgan fayllarni tiklashni nazariy va amaliy o'rganamiz. Buning uchun Recuva (https://t.me/Kompyuter_akademiyasi/861) dasturidan foydalanamiz. Darsimizni nazariy qismida fayllarni tiklash nimaligi, sifatli tiklashga ta'sir etuvchi omillar haqida gaplashamiz. Amaliy qismida esa fleshkdan o'chirib yuborilgan fayllarni tiklashni o'rganamiz! ©️@kompyuter_akademiyasi

🛡@KiberXavfsizlikBot""")

@dp.message_handler(text='Tarmoq administratorligi 2-dars')
async def dars2(message:Message):
    chatid=message.chat.id
    vide3=open('dars3.mp4','rb')
    await bot.send_video(chat_id=chatid,video=vide3,caption="""📹 Tarmoq Administratorligi  #2DARS

YouTube: bit.ly/3DD2pts
Telegram: t.me/TarmoqUstasi

👉 @KiberxavfsizlikBot""")
@dp.message_handler(text='Tarmoq administratorligi 3-dars')
async def dars3(message:Message):
    chatid=message.chat.id
    vide4=open('dars4.mp4','rb')
    await bot.send_video(chat_id=chatid,video=vide4,caption="""📹 Tarmoq Administratorligi  #3DARS

YouTube: bit.ly/3DD2pts
Telegram: t.me/TarmoqUstasi

👉 @KiberxavfsizlikBot""")
@dp.message_handler(text='Tarmoq administratorligi 4-dars')
async def dars4(message:Message):
    chatid=message.chat.id
    vide5=open('dars5.mp4','rb')
    await bot.send_video(chat_id=chatid,video=vide5,caption="""📹 Tarmoq Administratorligi  #4DARS

YouTube: bit.ly/3DD2pts
Telegram: t.me/TarmoqUstasi

👉 @KiberxavfsizlikBot""")
@dp.message_handler(text='Tarmoq administratorligi 5-dars')
async def dars5(message:Message):
    chatid=message.chat.id
    vide6=open('dars6.mp4','rb')
    await bot.send_video(chat_id=chatid,video=vide6,caption="""📹 Tarmoq Administratorligi  #5DARS

YouTube: bit.ly/3DD2pts
Telegram: t.me/TarmoqUstasi

👉 @KiberxavfsizlikBot""")
@dp.message_handler(text='Tarmoq administratorligi 6-dars')
async def dars6(message:Message):
    chatid=message.chat.id
    vide7=open('dars7.mp4','rb')
    await bot.send_video(chat_id=chatid,video=vide7,caption="""📹 Tarmoq Administratorligi  #6DARS

YouTube: bit.ly/3DD2pts
Telegram: t.me/TarmoqUstasi

👉 @KiberxavfsizlikBot""")

@dp.message_handler(text='Tarmoq administratorligi 7-dars')
async def dars7(message:Message):
    chatid=message.chat.id
    vide8=open('dars8.mp4','rb')
    await bot.send_video(chat_id=chatid,video=vide8,caption="""📹 Tarmoq Administratorligi  #7DARS

YouTube: bit.ly/3DD2pts
Telegram: t.me/TarmoqUstasi

👉 @KiberxavfsizlikBot""")
@dp.message_handler(text='✅ Bepul darslar')
async def bepuldarslar(message:Message):
    chatid=message.chat.id
    videolar2=open('tel1-qism.mp4','rb')
    video3=open('tel.2-qism.mp4','rb')
    video4=open('tel.3-qism.mp4','rb')
    video5=open('tel.4-qism.mp4','rb')
    video6=open('tel.5-qism.mp4','rb')
    video7=open('tel.6-qism.mp4','rb')
    video8=open('tel.7-qism.mp4','rb')
    video9=open('tel.8-qism.mp4','rb')
    video10=open('tel.9-qism.mp4','rb')

    await bot.send_message(chat_id=chatid,text="""IT HOUSE o'quv markazida Kiberxavfsizlik yo'nalishi bo'yicha dars berib kelayotgan Rustam Nusratov ga tegishli darslar.""")
    await bot.send_video(chat_id=chatid,video=videolar2,caption="""1. Kiberxavfsizlik Nima?\n

Internet bilan ishlashda o'zimiz va shaxsiy ma'lumotlarimizni asrashni o'rganamiz! — @Kiberxavfsizlikbot""")
    await bot.send_video(chat_id=chatid,video=video3,caption="""2. OSI Modeli

Internet bilan ishlashda o'zimiz va shaxsiy ma'lumotlarimizni asrashni o'rganamiz! — @Kiberxavfsizlikbot""")
    await bot.send_video(chat_id=chatid,video=video4,caption="""3. Kiberxavfsizlik hodimi vazifalari

Internet bilan ishlashda o'zimiz va shaxsiy ma'lumotlarimizni asrashni o'rganamiz! — @Kiberxavfsizlikbot""")
    await bot.send_video(chat_id=chatid,video=video5,caption="""4. Hackerlar turlari | Ahloqiy hakerlik

Internet bilan ishlashda o'zimiz va shaxsiy ma'lumotlarimizni asrashni o'rganamiz! — @Kiberxavfsizlikbot""")
    await bot.send_video(chat_id=chatid,video=video6,caption="""5. Kiberhujumlar Malumotlar o'g'irlanishi

Internet bilan ishlashda o'zimiz va shaxsiy ma'lumotlarimizni asrashni o'rganamiz! — @Kiberxavfsizlikbot""")
    await bot.send_video(chat_id=chatid,video=video7,caption="""6. Phishing, DDoS Hujum Turlari

Internet bilan ishlashda o'zimiz va shaxsiy ma'lumotlarimizni asrashni o'rganamiz! — @Kiberxavfsizlikbot""")
    await bot.send_video(chat_id=chatid,video=video8,caption="""7. MITM, Brute Force va Zero Day Exploit

Internet bilan ishlashda o'zimiz va shaxsiy ma'lumotlarimizni asrashni o'rganamiz! — @Kiberxavfsizlikbot""")
    await bot.send_video(chat_id=chatid,video=video9,caption="""8. Vulnerable Analysis | Tizimdagi Zaiflik Analizi | Kiberxavfsizlik Bepul Darslari 1-Amaliy Dars

Internet bilan ishlashda o'zimiz va shaxsiy ma'lumotlarimizni asrashni o'rganamiz! — @Kiberxavfsizlikbot""")
    await bot.send_video(chat_id=chatid,video=video10,caption="""9. Manual Vulnerability Analysis | Tizimdagi zaiflikni qo'lda aniqlash | Kiberxavfsizlik Bepul Darslari

Internet bilan ishlashda o'zimiz va shaxsiy ma'lumotlarimizni asrashni o'rganamiz! — @Kiberxavfsizlikbot""")


@dp.message_handler(text="ℹ️ Kiberxavfsizlik - bu ...")
async def turlari(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text="ℹ️ Kiberxavfsizlik - bu ...",reply_markup=kiber)

@dp.message_handler(text="Kiberxavfsizlik nima?")
async def turlari6(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text="""❓Kiberxavfsizlik nima?

ℹ️ Kiberxavfsizlik (ba'zan kompyuter xavfsizligi deb ataladi) - bu kompyuterlar, serverlar, mobil qurilmalar, elektron tizimlar, tarmoqlar va ma'lumotlarni zararli hujumlardan himoya qilish uchun texnik va amaliyotlar to'plami. Kiberxavfsizlik biznesdan tortib mobil texnologiyalargacha bo'lgan turli sohalarda qo'llanilish uchun o’z o’rnini topadi. Ushbu yo'nalishda bir nechta asosiy toifalarni ajratish mumkin:

• Tarmoq xavfsizligi - kompyuter tarmoqlarini turli tahdidlardan, masalan, maqsadli hujumlar yoki zararli dasturlardan himoya qilish bo'yicha harakatlar.

• Ilova xavfsizligi - jinoyatchilar dasturlarda yashirishi mumkin bo'lgan tahdidlardan qurilmalarni himoya qilish. Infektsiyalangan dastur tajovuzkorga himoya qilishi kerak bo'lgan ma'lumotlarga kirish huquqini berishi mumkin. Ilova xavfsizligi ochiq manbalarda paydo bo'lishidan ancha oldin ishlab chiqish bosqichida ta'minlanadi.

• Axborot xavfsizligi - saqlash paytida ham, uzatish paytida ham ma'lumotlarning yaxlitligi va maxfiyligini ta'minlash.

• Operatsion xavfsizlik - axborot aktivlari bilan ishlash va himoya qilish. Ushbu turkumga, masalan, tarmoqqa kirish ruxsatlarini boshqarish yoki ma'lumotlarning qayerda va qanday saqlanishi va uzatilishini belgilaydigan qoidalar kiradi.

• Favqulodda vaziyatlarni tiklash va biznesning uzluksizligi - xavfsizlik hodisasiga (zararli faoliyat) va tizimni buzishi yoki ma'lumotlarning yo'qolishiga olib keladigan boshqa har qanday hodisaga javob berish. Favqulodda vaziyatni tiklash - bu tashkilot hujum oqibatlarini qanday hal qilish va biznes jarayonlarini tiklashni tavsiflovchi qoidalar to'plami. Biznesning uzluksizligi - bu zararli hujum tufayli tashkilot ma'lum resurslardan foydalanish imkoniyatini yo'qotgan taqdirda harakat rejasi.

• Xabardorlikni oshirish - foydalanuvchilarni o'qitish. Ushbu yo'nalish kiberxavfsizlik sohasidagi eng oldindan aytib bo'lmaydigan omil - inson ta'sirini kamaytirishga yordam beradi. Kimningdir xatosi yoki nodonligi tufayli hatto eng xavfsiz tizimga ham hujum qilish mumkin. Shuning uchun har bir tashkilot xodimlarni o'qitishi va ularga asosiy qoidalar haqida aytib berishi kerak: masalan, shubhali elektron pochta qo'shimchalarini ochmaslik yoki shubhali USB qurilmalarini ulamaslik. ©️kaspersky.ru

🛡️@KiberXavfsizlikBot""")
@dp.message_handler(text='▶️ Videokurslar')
async def videolar(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text="▶️ Videokurslar",reply_markup=video)
@dp.message_handler(text='🔝 Asosiy Menyu')
async def asasiy(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text='🔝 Asosiy Menyu',reply_markup=asosiy_knopka)
@dp.message_handler(text='🔙 Orqaga')

async def orqa(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text='🔙 Orqaga',reply_markup=asosiy_knopka)
@dp.message_handler(text="Kiberxavfsizlikga qayerda o'qiladi?")
async def tur(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text="""❓Kiberxavfsizlikga qayerda o'qiladi?

😎 IT va kiberxavfsizlik sohasida ta'lim olish uchun quyidagi OTM'laridan birini tamomlashingiz kerak bo'ladi:

🇺🇿 Davlat ta'lim muassasalari:
• Toshkent axborot texnologiyalari universiteti (https://tuit.uz/)
• Toshkent axborot texnologiyalari universiteti Qarshi filiali (https://www.tuitkf.uz/)
• Toshkent axborot texnologiyalari universiteti Nukus filiali (https://tatunf.uz/)
• Toshkent axborot texnologiyalari universiteti Samarqand filiali (http://samtuit.uz/uz)
• Toshkent axborot texnologiyalari universiteti Farg‘ona filiali (https://tatuff.uz/)
• Toshkent axborot texnologiyalari universiteti Urganch filiali (https://www.ubtuit.uz/)
• Toshkent axborot texnologiyalari universiteti Nurafshon filiali (https://nbtuit.uz/)

🔹 Nodavlat oliy ta'lim muassasalari:
• IT-Park University
• “PDP University”

🔸 Xorijiy oliy ta'lim muassasalari va ularning filiallari:
• Toshkent shahridagi Inxa universiteti (https://inha.uz/)
• O‘zbekistondagi Sharda universiteti (Hindiston) (https://www.shardauniversity.uz/)
• Toshkent shahridagi Adju universiteti (Koreya) (http://www.ajou.uz/uz)
• Toshkent shahridagi Amiti universiteti (Hindiston) (https://amity.uz/uzbek/)

✅ Yuqorida berilgan OTM'larining barchasi davlat ro'yxatidan o'tgan va ularni tamomlaganingizdan so'ng sizda diplom bilan bog'liq muammolar kuzatilmasligi kerak, batafsil ro'yxatni ushbu manzil (https://stat.edu.uz/Univer-list.php)da ko'rishingiz mumkin.

🛡️@KiberXavfsizlikBot""")

@dp.message_handler(text="Kiber tahdidlar turlari")
async def tur2(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text="""Kiber tahdidlar turlari

Kiberxavfsizlik 3 turdagi tahdidlarga qarshi kurashadi:

• Kiberjinoyat - bir yoki bir nechta tajovuzkorlar tomonidan tizim faoliyatini buzish yoki moliyaviy foyda olish maqsadida unga hujum qilish maqsadida uyushtirilgan harakatlar.

• Kiberhujum - asosan siyosiy xarakterga ega bo'lgan ma'lumotlarni to'plashga qaratilgan harakatlar.

• Kiberterrorizm - qo'rquv yoki vahima qo'zg'ash uchun elektron tizimlarni beqarorlashtirishga qaratilgan harakatlar. ©️kaspersky.ru

🛡️@KiberXavfsizlikBot""")

@dp.message_handler(text="Kibertahdidlarning tarqalish ko'lami")
async def tarix(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text="""📈Kibertahdidlarning tarqalish ko'lami

📊 Yildan yilga dunyoda ko'proq tahdidlar va ma'lumotlarning sizib chiqishi ko'paymoqda. Statistik ma'lumotlar hayratlanarli: RiskBased Security hisobotiga ko'ra, faqat 2019 yilning birinchi to'qqiz oyida 7,9 milliard ma'lumotlar buzilishi sodir bo'lgan. Bu ko‘rsatkichlar 2018 yilning shu davriga nisbatan ikki baravardan ko‘proq (112 foiz) ko‘pdir.

📑 Ko'pincha tibbiy va davlat muassasalari yoki chakana savdo tashkilotlari ma'lumotlarning sizib chiqishiga duchor bo'lishadi. Aksariyat hollarda “qahramonlar” turli maqsadli xakerlar bo’ladi. Ma’lumotlarni tarqatishdan asosiy maqsad esa o’sha tashkilotdan qaysidir sabablar uchun qasos olish, xaker o’zining kuchini ko’rsatib qo’yishi yoki tizimdagi kamchiliklarni hammaga namoyish qilish kabi sabablar bo’lishi mumkin.

🔰 Xalqaro Data korporatsiyasi prognozlariga ko‘ra, agar kibertahdidlar soni o‘sishda davom etsa, 2022 yilga borib kiberxavfsizlik yechimlariga sarflanadigan mablag‘ 133,7 milliard dollarga etadi. Butun dunyo hukumatlari kiberxavfsizlikning samarali amaliyotlarini amalga oshirishda tashkilotlarga yordam berish orqali jinoyatchilarga qarshi kurashmoqda.

🇺🇸 Shunday qilib, AQSh Milliy standartlar va texnologiyalar instituti (NIST) xavfsiz IT infratuzilmasi tamoyillarini ishlab chiqdi. NIST zararli kodni zarar keltirmasidan oldin aniqlash va uning tarqalishini oldini olish uchun barcha elektron resurslarni doimiy real vaqt rejimida kuzatishni tavsiya qiladi.

🇬🇧 Buyuk Britaniya hukumatining Milliy kiberxavfsizlik markazi kiberxavfsizlik bo'yicha qo'llanmaning 10 qadamini e'lon qildi. U tizimlarning ishlashini monitoring qilishning ahamiyati haqida gapiradi. Avstraliyada Avstraliya Kiberxavfsizlik Markazi (ACSC) muntazam ravishda so'nggi kibertahdidlar bilan kurashish bo'yicha tavsiyalarni e'lon qiladi.

😑 Turli davr va mamlakatlarda bunday tahdidlarni kamaytirish uchun tuli usullar yaratib, qo’llab borilmoqda. Lekin shu o’rinda xakerlar ham tinch o’tirishayotgani yo’q... ©️kaspersky.ru

🛡️@KiberXavfsizlikBot""")
@dp.message_handler(text="Kiberxavfsizlik tarixi")
async def tarix2(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text="""▫️Kiberxavfsizlik: yaratilish va rivojlanish tarixi

🟢 Aloqa tarmoqlari rivojlanishining dastlabki bosqichlarida foydalanuvchilar sonining kamligi va asosan mahalliy tarmoqlar mavjudligi sababli xavfsizlik masalalari asosiy muammo bo‘lmagan, bu esa barcha foydalanuvchilarning bir-biriga ishonishiga sabab bo'lgan. Texnologiyaning rivojlanishi va aloqa tarmoqlarining o'sishi bilan xavfsizlikning ahamiyati ham oshdi.

🔴 Kiberxavfsizlik tarixi kompyuterlarga birinchi hujumlar paydo bo'lishi bilan boshlanadi. 1989 yilda Robert Morris birinchi kompyuter qurti, o'z-o'zidan tarqaladigan virusni yaratdi. Albatta, bu vaqtgacha hujumlar va viruslar mavjud edi, ammo aynan Morris qurti ARPANET tarmog'idagi birinchi keng ko'lamli va keng tarqalgan DoS hujumi (ingliz. Denial of Service - “denial of service”) edi.

▪️1990-yillarda AQSHda Axborot xavfsizligi boʻyicha tadqiqot konsorsiumi tuzildi, u Kiberjinoyat va terrorizm boʻyicha xalqaro konventsiya uchun taklif ishlab chiqdi. 1997-yil sentyabr oyida RFC 2196 nashr etildi, u Internet hamjamiyatida kompyuter xavfsizligi siyosatini ishlab chiqish bo'yicha ko'rsatmalar berdi. 2014-yilda Yevropa telekommunikatsiya standartlari instituti (ETSI) xalqaro darajada kiberxavfsizlikni standartlashtirish uchun mas’ul bo‘lgan Kiberxavfsizlik texnik qo‘mitasini tuzdi.

😑 Hozirgi vaqtda kompyuter tizimlari va Internetning hayotning barcha sohalariga ta'siri kuchayishi, simsiz tarmoqlarning rivojlanishi (masalan, Bluetooth va Wi-Fi asosida), shuningdek, "aqlli" texnologiyalarning o'sishi tufayli kiberxavfsizlik tobora muhim ahamiyat kasb etmoqda. ©️iot.ru

🛡️@KiberXavfsizlikBot""")
@dp.message_handler(text="📲 Aloqa")
async def aloqa(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text="""👨🏻‍💻 Loyiha asoschisi —  Jonibek Turapov\n

📩 Murojaatlar uchun — @fullstack_online""")





@dp.message_handler(text='📊 Statistika')
async def statistika(message:Message):
    chatid=message.chat.id
    await bot.send_message(chat_id=chatid,text="""👥 Barcha obunachilar: 19361 kishi.\n
✅ Faol obunachilar: 11738 kishi.\n

🔜 Oxirgi 24 soatda 6 obunachi qo'shildi.\n
🔝 Oxirgi 1 oyda 328 obunachi qo'shildi.

📆 Bot ishga tushganiga 527 kun bo'ldi.

📊 @KiberXavfsizlikBot statistikasi!""")

executor.start_polling(dp,skip_updates=True)