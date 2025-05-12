import plotly.express as px
import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(page_title="سفر به دنیای مولانا", layout="centered")
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn&display=swap');

    /* همه چیز راست‌چین و فونت وزیر */
    .main, .block-container {
        direction: rtl;
        text-align: right;
        font-family: 'Vazirmatn', sans-serif !important;
    }

    h1, h2, h3, h4, h5, h6 {
        text-align: right !important;
    }

    /* فقط sidebar چپ‌چین بمونه */
    [data-testid="stSidebar"] {
        direction: ltr;
        text-align: left;
    }
    </style>
""", unsafe_allow_html=True)
def present():
    ima=Image.open('god.jpg')
    st.image(ima,caption="",width=500,use_container_width=True)
    st.title("موضوع ارائه : حضرت عشق مولانا")
    st.title("زیر نظر دکتر فائزی")
    st.markdown(" تهیه کنندگان : ارمیا جعفرپور زنوزی و سارو قادری و جمعی از دوستان")


def part_one():
    st.title("✨ سفر به دنیای مولانا")
    st.markdown("به دنیای اندیشه، عشق و عرفان خوش آمدید 🌿")

    image = Image.open("1-سماع مولانا در بازار زرکوبان.jpg")
    st.image(image, caption="سماع مولانا در بازار زرکوبان", use_container_width=True)

    st.header("📜 زندگی‌نامه‌ی مولانا")

    # عنوان صفحه
    st.header("تولد و شروع زندگی")
    st.image("p2.png", caption="لحظه تولد کودک", width=650)
    st.write("""
    مولانا جلال‌الدین محمد بلخی، شاعر و عارف نامی ایرانی، در سال ۱۲۰۷ میلادی در شهر بلخ (افغانستان کنونی) متولد شد. 
    پدر او، بهاءالدین ولد، از علمای برجسته و عارفان زمان خود بود. لقب «مولانا» به معنای «استاد ما» محترم شمرده می‌شود. 
    در کودکی نزد پدر و علما درس خواند و با تعالیم اسلامی و عرفانی آشنا شد.
    """)

    # پاراگراف دوم
    st.header("هجرت به قونیه")
    st.image("p3.png", caption="هجرت خانوادگی", width=650)
    st.write("""
    در حدود سال ۱۲۱۸ میلادی و به دنبال تهدید مغول‌ها و ناآرامی‌های آن دوره، خانواده مولانا بلخ را ترک کرد. 
    پس از گذر از شهرهایی چون نیشابور (که در آنجا با شیخ فریدالدین عطار دیدار کردند) و انجام سفر حج، سرانجام در قونیه (ترکیهٔ کنونی) ساکن شدند. 
    در قونیه، پدر او در یکی از مدارس دینی مشغول به تدریس بود و پس از درگذشت پدر در سال ۱۲۳۱، مولانا جای او نشست و خود فقه و علوم دینی را آموزش داد.
    """)

    # پاراگراف سوم
    st.header("دیدار با شمس تبریزی")
    st.image("p4.jpg", caption="هجرت خانوادگی", width=650)
    st.write("""
    نقطه عطف زندگی مولانا دیدار او با شمس تبریزی، عارف سیّار و پاک‌نهاد تبریزی، در نوامبر ۱۲۴۴ میلادی در قونیه بود. 
    این دوستی معنوی تأثیر ژرفی بر مولانا داشت و او را به شاعری حقیقی و عارف‌گرا بدل کرد. 
    شمس چند ماه در محضر مولانا ماند و پس از جدایی ناخواسته‌اش (که چندی بعد ناپدید شد) مولانا سروده‌های غنایی و عرفانی بسیار به یاد او سرود.
    """)
    st.markdown("<h2 style='text-align: center; color: darkred;'>بیت‌هایی از مولانا در فراق شمس</h2>", unsafe_allow_html=True)
    st.image("p5.jpg", caption="سروده هایی در فراق دوست ", width=650)


    poems = [
        "ای رفته ز دل، رفته ز بر، رفته ز خاطر<br>بر من منگر، تاب نگاه تو ندارم",
        "ز دیده گر سرمه کشم خاک درت را<br>بس روشنی چشم بدان خاک در آید",
        "بیا بیا که شدم بی‌تو، بی‌قرار شبی<br>تو آفتابی و من شب، بیا و روزم کن",
        "بی تو به سر نمی‌شود، بی‌تو به سر نمی‌شود<br>داغ تو دارد این دلم، جای دگر نمی‌شود",
        "چون جان گُذُشتی از برم، بی‌تو چگونه بگذرم؟<br>ای نور چشم و روشنی، بی‌تو به سر نمی‌شود"
    ]

    for verse in poems:
        st.markdown(
            f"<div style='background-color: #f9f3f3; padding: 15px; margin: 10px 0; border-radius: 10px; border-right: 6px solid darkred; text-align: right; direction: rtl;'>{verse}</div>",
            unsafe_allow_html=True
        )
    # col1, col2 = st.columns(2)
    # with col1:
    #     st.image('فیه ما فیه.jpeg',caption="جرعه ای از فیه ما فیه",width=300)
    # with col2:
    #     st.image("perfume.png", caption="مشک و آهوان", width=350)
    #     st.markdown("💬 «مشک را گفتند:تو را یک عیب است: باهرکه بنشینی از بوی خوشت به او نیز دهی. گفت :به آن ننگرم با کی ام به آن بنگرم که من کی ام.»")    

def part_two():
    # پاراگراف پنجم
    st.header("میراث مولانا")
    st.image("p7.jpg",width=600)
    st.write("""
    مولانا جلال‌الدین بلخی به‌خاطر اشعار عارفانه و آموزه‌های معنوی‌اش از بزرگ‌ترین شاعران عرفانی زبان فارسی به شمار می‌آید. 
    آثار او نه تنها در ایران، بلکه در ادبیات ترکی عثمانی، اردو، بنگالی و دیگر زبان‌های مناطق مسلمان نفوذ گسترده‌ای یافته است. 
    پس از مرگ مولانا در سال ۱۲۷۳ میلادی، شاگردان و مریدان او سلسله مولویه (صوفیان مولوی) را بنیان نهادند. 
    تا امروز، آثار مولانا در محافل ادبی و عرفانی مطالعه می‌شوند و خوانندگان بسیاری در ایران و سراسر جهان دارند.
    """)

    st.header("📚 آثار مهم مولانا")
    # image = Image.open("1-سماع مولانا در بازار زرکوبان.jpg")
    # # st.image(image, caption="سماع مولانا در بازار زرکوبان", use_container_width=True)
    # image = Image.open("کلیات-شمس-تبریزی-گالینگور-قابدار-قدرت-قلم-1.jpg")
    # st.image(image, caption="کلیات شمس", use_container_width=True)

    st.markdown("""
    - مثنوی معنوی (۶ دفتر)  
    - دیوان شمس  
    - فیه ما فیه  
    - مجالس سبعه  
    """)
    col1, col2 = st.columns(2)

    with col1:
        st.image("۶دفتر.jpg", caption="مثنوی معنوی", width=250)
        st.markdown("💬 «بشنو این نی چون شکایت می‌کند، از جدایی‌ها حکایت می‌کند...»")
        st.image("مولانا فیه ما فیه.jpg", caption="فیه ما فیه", width=250)
        st.markdown("💬 «هر کسی از ظن خود شد یار من، از درون من نجست اسرار من...»")
        
    with col2:
        st.image("کلیات-شمس-تبریزی-گالینگور-قابدار-قدرت-قلم-1.jpg", caption="دیوان شمس", width=250)
        st.markdown("💬 «تو مرا جان و جهانی، چه کنم جان و جهان را؟»")
        st.image("مجالس سبعه.jpg", caption="مجالس سبعه", width=250)
        st.markdown("💬 «راه عاشق از همه راه‌ها جداست، که در راه او عقل در حیرت بماند.»")
    

def part_three():

    st.title("حکایت‌ها و داستان‌ها")

    st.image("p9.jpg",width=700)
    # استفاده از selectbox برای انتخاب حکایت
    story_option = st.selectbox(
        "انتخاب حکایت",
        ["حکایت مشک", "حکایت آیینه حقیقت", "حکایت شمس و مولانا"]
    )

    if story_option == "حکایت مشک":
        st.subheader("حکایت مشک")
        # ست کردن عنوان اصلی

        # افزودن فاصله
        st.markdown("<br>", unsafe_allow_html=True)

        # نمایش داستان با سبک ادبی
        st.markdown("""
        <div style='background-color: #fef9f4; padding: 20px; border-radius: 15px; border: 1px solid #e0d4c3; font-size: 18px; line-height: 2; color: #4b3621;'>
        مشک را گفتند:  
        «تو را یک عیب است؛ با هر که بنشینی، از بوی خوشَت به او نیز دهی!»  
        گفت:  
        «به آن ننگرم با کی‌ام، به آن بنگرم که من کی‌ام.»  
        </div>
        """, unsafe_allow_html=True)

        # پیام تأمل‌برانگیز در پایان
        col1, col2 = st.columns(2)

        # قرار دادن هر تصویر در یک ستون
        with col1:
            image1 = Image.open("perfume.png")
            st.image(image1, caption="🍂 مشک؛ نمادی از هویت ناب و اثرگذاری بی‌ادعا 🍂", use_container_width=True)

        with col2:
            image2 = Image.open("p6.jpg")
            # st.image(image2, caption="تصویر دوم", use_container_width=True)
            # st.image(image2, caption="تصویر اول", use_container_width=True)
            st.image(image2, caption="🍂 مشک؛ نمادی از هویت ناب و اثرگذاری بی‌ادعا 🍂", use_container_width=True)
        # نمایش تصویر
        st.markdown("""
        <div style='background-color: #fffbe6; padding: 20px; border-radius: 15px; border-left: 5px solid #e3b04b; font-size: 17px; color: #5c4c1c;'>
        🌟 <i>این حکایت به ما می‌آموزد:  
        انسانی که درونش با نور، محبت، و معرفت آکنده است،  
        بدون آنکه بخواهد، بر اطراف خود تأثیر می‌گذارد؛  
        زیرا عطر حقیقت، نیاز به معرفی ندارد.</i> 🌟
        </div>
        """, unsafe_allow_html=True)


    elif story_option == "حکایت آیینه حقیقت":

        st.title("🔮 حکایت آیینه حقیقت")

        # نمایش متن حکایت با طراحی زیبا
        st.markdown("""
        <div style='background-color: #f9f9f9; padding: 20px; border-radius: 15px; font-size: 18px; line-height: 2; color: #333; border-left: 5px solid #888'>
        حقیقت آیینه‌ای بود که از آسمان به زمین افتاد و شکست...  
        هر کس تکه‌ای از آن برداشت، خود را در آن دید،  
        گمان کرد که حقیقت نزد اوست...  
        حال آنکه حقیقت نزد همگان پخش بود...
        </div>
        """, unsafe_allow_html=True)

        # فاصله
        st.markdown("<br>", unsafe_allow_html=True)

        # نمایش تصویر (فرض: نام عکس truth.jpg است)
        image = Image.open("truth.jpg")
        st.image(image, caption="✨ آیینه حقیقت، تکه‌تکه در دستان انسان‌ها ✨", use_container_width=True)

        # پیام تأمل‌برانگیز
        st.markdown("""
        <div style='background-color: #fff8e1; padding: 20px; border-radius: 15px; font-size: 17px; color: #5e4b1d;'>
        🌟 <i>هیچ‌کس مالک تمام حقیقت نیست...  
        هر انسانی تنها بازتابی از بخشی از آن را درک می‌کند.  
        حقیقت در وحدت نگاه‌هاست، نه در انحصار باورها.</i> 🌟
        </div>
        """, unsafe_allow_html=True)

    else:
    
        st.subheader("حکایت شمس و مولانا")
        # اضافه کردن تصویر به حکایت
        # تیتر بخش
        st.markdown("<h2 style='text-align: center; color: #8B0000;'>زخم‌هایی که نور از آن‌ها می‌تابد ✨</h2>", unsafe_allow_html=True)

        # متن عرفانی داستان
        st.markdown("""
        <div style='background-color: #fff8f0; padding: 20px; border-radius: 15px; font-size: 18px; line-height: 2; color: #4b3621; border: 1px solid #e0c9a6;'>
        مولانا:  
        <strong>«پس زخم‌هایم چه؟»</strong>  
        شمس تبریزی :  
        <strong>«نور از محل همین زخم‌ها وارد می‌شود...»</strong>  
        </div>
        """, unsafe_allow_html=True)

        # فاصله قبل از عکس
        st.markdown("<br>", unsafe_allow_html=True)

        # نمایش تصویر
        image = Image.open("p10.jpg")
        st.image(image, caption="💫 صحنه‌ای عرفانی از مولانا و شمس - زخم‌هایی که نور از آن‌ها می‌تابد", use_container_width=True)

        # پیام الهام‌بخش در پایان
        st.markdown("""
        <div style='background-color: #e8f9f1; padding: 20px; border-left: 5px solid #6dc7a4; border-radius: 10px; font-size: 17px; color: #1d4734;'>
        💡 گاه عمیق‌ترین نورها از شکاف‌های روح ما می‌تابند...  
        دردها فقط درد نیستند؛ گذرگاه‌های نورند برای شناخت، رشد، و اتصال به حقیقت.
        </div>
        """, unsafe_allow_html=True)


import streamlit as st

def part_four():
    st.title("📜 اشعار معروف مولانا")
    ima=Image.open("p16.jpg")
    st.image(ima)

    poem = st.selectbox("🧿 یکی از اشعار مشهور را انتخاب کنید :", [
        "بشنو از نی چون حکایت می‌کند",
        "ای عاشقان ای عاشقان امروز ماییم و شما",
        "هر کسی کو دور ماند از اصل خویش",
        "از محبت خارها گل می‌شود"
    ])

    if poem == "بشنو از نی چون حکایت می‌کند":
        ima=Image.open("p13.jpg")
        st.image(ima)
        st.markdown("""
        <div style='background-color:#fffaf3; padding:20px; border-radius:12px; font-size:18px; line-height:2;'>
        🌀 <b>بشنو از نی چون حکایت می‌کند</b><br>
        از جدایی‌ها شکایت می‌کند<br><br>
        کز نیستان تا مرا ببریده‌اند<br>
        از نفیرم مرد و زن نالیده‌اند<br><br>
        سینه خواهم شرحه شرحه از فراق<br>
        تا بگویم شرح درد اشتیاق<br><br>
        هر کسی کو دور ماند از اصل خویش<br>
        باز جوید روزگار وصل خویش<br><br>
        من به هر جمعیتی نالان شدم<br>
        جفت بدحالان و خوش‌حالان شدم<br><br>
        هر کسی از ظن خود شد یار من<br>
        از درون من نجست اسرار من
        </div>
        """, unsafe_allow_html=True)

    elif poem == "ای عاشقان ای عاشقان امروز ماییم و شما":
        ima=Image.open("p14.jpg")
        st.image(ima,width=400)
        st.markdown("""
        <div style='background-color:#fffaf3; padding:20px; border-radius:12px; font-size:18px; line-height:2;'>
        🎶 <b>ای عاشقان ای عاشقان امروز ماییم و شما</b><br>
        افتاده در غرقابه‌ای، دست دعا بر آسمان<br><br>
        امروز وقت رقص و جان، وقت سماع عاشقان<br>
        امروز وقت نغمه‌ای، از بانگ جان جان جان<br><br>
        دل را ز جان پر می‌کنیم، جان را ز دل سرشارتر<br>
        کای جان من، اینجا بمان، کای دل بمان در این مکان
        </div>
        """, unsafe_allow_html=True)

    elif poem == "هر کسی کو دور ماند از اصل خویش":
        ima=Image.open("p15.jpg")
        st.image(ima,width=400)
        st.markdown("""
        <div style='background-color:#fffaf3; padding:20px; border-radius:12px; font-size:18px; line-height:2;'>
        🌿 <b>هر کسی کو دور ماند از اصل خویش</b><br>
        باز جوید روزگار وصل خویش<br><br>
        چون‌که گل رفت و گلستان درگذشت<br>
        نشنوی زان پس ز بلبل سرگذشت<br><br>
        جزو را همچون بود کل کی شود<br>
        آفتابی رفت سوی گل‌سپر<br><br>
        ترک گل کن بلبل بی‌ساز من<br>
        تا ببینی باغ بی‌گل باز من
        </div>
        """, unsafe_allow_html=True)

    elif poem == "از محبت خارها گل می‌شود":
        ima=Image.open("p12.jpg")
        st.image(ima)

        st.markdown("""
        <div style='background-color:#fffaf3; padding:20px; border-radius:12px; font-size:18px; line-height:2;'>
        🌸 <b>از محبت خارها گل می‌شود</b><br>
        از محبت سنگ‌ها مُل می‌شود<br><br>
        با محبت سردی یخ پَر شود<br>
        مهر و لطف حق به دل جاری شود<br><br>
        گر بود در دل محبت خانه‌ای<br>
        هر دو عالم گرددش دیوانه‌ای<br><br>
        از محبت تلخ‌ها شیرین شود<br>
        از محبت مس‌ها زرین شود<br><br>
        از محبت دَردها صافی شود<br>
        از محبت دردها شافی شود
        </div>
        """, unsafe_allow_html=True)

def part_five():
    st.title("🌪️ سماع مولانا")
    col1, col2 = st.columns(2)

    # قرار دادن هر تصویر در یک ستون
    with col1:
        image =Image.open("danse.jpg")
        st.image(image, caption="✨ سماع؛ رقص جان در آغوش حقیقت ✨", use_container_width=True)
        # st.image(image1, caption="تصویر اول", use_container_width=True)

    with col2:
        # st.image(image2, caption="تصویر دوم", use_container_width=True)    image = Image.open("danse.jpg")  # فرض بر اینکه تصویر سماع با این نام ذخیره شده
        image2 = Image.open("danse2.jpg")  # فرض بر اینکه تصویر سماع با این نام ذخیره شده
        st.image(image2, caption="✨ سماع؛ رقص جان در آغوش حقیقت ✨", use_container_width=True)
    # توضیح مفهومی درباره سماع
    st.markdown("""
    <div style='background-color:#fffaf0; padding:20px; border-radius:15px; font-size:18px; line-height:2;'>
    <b>سماع</b> در نگاه مولانا، نه فقط چرخیدن است، بلکه <i>سفری از من به بی‌منی</i>، از خاک به افلاک و از جدایی به وصال است.  
    در این رقص، انسان با چرخیدن به دور خویش، <b>مرکز هستی</b> را می‌جوید؛  
    و با بازوان باز، آغوشی برای <b>معشوق الهی</b> می‌گشاید.  
    <br><br>
    مولانا می‌گوید:<br>
    <i>این سماع از بادِ جان برخاسته‌ست<br>
    مر شما را با چنان جان آشناست</i>
    </div>
    """, unsafe_allow_html=True)

    # نمایش تصویر سماع

    # شعر مکمل سماع
    st.markdown("""
    <div style='background-color:#f9f3f0; padding:20px; border-radius:15px; font-size:17px; line-height:2;'>
    <i>  
    آن کس که بداند و بداند که بداند  
    اسب خرد از گنبد گردون بجهاند  
    آن کس که بداند و نداند که بداند  
    بیدار کنیدش که بسی خواب نماند  
    </i>
    </div>
    """, unsafe_allow_html=True)


def the_end():
    st.title("🔚 پایان سخن")
    ima=Image.open("end.jpg")
    st.image(ima, caption="✨ پایانی از جنس حکمت ✨", use_container_width=True)

    # پیام خداحافظی
    st.markdown("""
    <div style='background-color:#fffbe6; padding: 15px; border-left: 5px solid #e0b754; border-radius: 10px; font-size: 17px; color: #4e3d28; margin-top:20px;'>
    🌸 از همراهی‌تان در این سفر معنوی با مولانا سپاسگزارم.  
    امیدوارم این پرواز کوچک، شعله‌ای از نور در دل شما افروخته باشد...  
    """, unsafe_allow_html=True)


options = st.sidebar.radio('📜 اسلایدهای ارائه', options=[
    "🕊️ بسمه تعالی",
    "✨ سفر به دنیای مولانا",
    "📚 میراث مولانا",
    "📖 حکایت‌ها و داستان‌ها",
    "📝 شعرهای لطیف",
    "🌀 سماع مولانا",
    "🔚 ... والسلام"
])

if options == '✨ سفر به دنیای مولانا':
    part_one()
if options == "📚 میراث مولانا":
    part_two()
elif options == '🕊️ بسمه تعالی':
    present()
elif options == "📖 حکایت‌ها و داستان‌ها":
    part_three()
elif options == "📝 شعرهای لطیف":
    part_four()
elif options == "🌀 سماع مولانا":
    part_five()
elif options == "🔚 ... والسلام":
    the_end()


