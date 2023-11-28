import streamlit as st

Data = {
    "Mual": {
        "Perut Kembung": ["Nyeri Perut", "Nyeri ulu Hati"],
        "Sakit Kepala": ["Gangguan Penglihatan"],
        "Demam": ["Mata Menguning", "Nyeri ulu Hati", "Nyeri Perut", "Urine Berbau Busuk"],
        "Batuk": ["Sakit Tenggorokan"],
        "Lemas": ["Nyeri Punggung"],
    },
    "Sesak Napas": {
        "Batuk": ["Demam", "Nyeri Dada", "Lemas"],
        "Nyeri Dada": ["Kesemutan", "Mudah Lelah"],
        "Sakit Kepala": ["Demam", "Gangguan Penglihatan"],
        "Diare": ["Kesemutan"],
    },
    "Mudah Lelah": {
        "Nyeri Perut" : ["Lemas", "Mata Menguning"],
        "Batuk" : ["Berkeringat di Malam Hari"],
        "Nyeri Sendi" : ["Ruam Pada Kulit"],
        "Sakit Kepala" : ["Kulit Pucat"],
    },
    "Diare": {
        "Sakit Kepala" : ["Nyeri Otot"],
        "Penurunan Berat Badan" : ["Tinja Berminyak"],
        "Nyeri Perut" : ["Mudah Marah"],
        "Bau Mulut" : ["Sulit Buang Gas"],
    },
    "Demam": {
        "Nyeri Sendi" : ["Hilang Nafsu Makan"],
        "Sakit Tenggorokan" : ["Bersin-Bersin"],
        "Benjolan di Punggung" : ["Punggung Bungkuk"],
    },
    "Batuk": {
        "Sakit Tenggorokan" : ["Tenggorokan Kering"],
        "Bersin" : ["Ruam Pada Kulit"],
    },
    "Nyeri Perut": {
        "Penurunan Berat Badan" : ["Nyeri Panggul"],
        "Infeksi Saluran Kemih" : ["Mudah Memar"],
    },
    "Mata Merah": {
        "Pandangan Kabur" : ["Selaput Pterigium Menebal", "Mata Bengkak"],
    },
    "Gangguan Penglihatan" : {
        "Sensitif Cahaya" : ["Penglihatan Ganda"],
    },
    "Nyeri Otot" : {
        "Penurunan Berat Badan" : ["Mudah Kepanasan"],
    },
    "Kesemutan" : {
        "Rentan Sakit" : ["Nyeri Tulang"]
    },
    "Mata Menguning" : {
        "Pendarahan Usus" : ["Pembesaran Limpa"]
    }
}

OutputData = {
    ("Mual", "Perut Kembung", "Nyeri Perut"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Gastritis*",
            "details": "Gastritis adalah peradangan pada dinding lambung yang dapat disebabkan oleh berbagai faktor. Penyakit ini dapat bersifat akut atau kronis. Gejala umum gastritis meliputi nyeri perut, kembung, mual, muntah, dan perut terasa penuh. \n Cara mengatasi gastritis tergantung pada penyebabnya. Beberapa langkah yang dapat diambil untuk meredakan gejala gastritis meliputi: \n Penghindaran pemicu: Hindari konsumsi alkohol, berhenti merokok, dan hindari makanan pedas atau asam yang dapat merangsang produksi asam lambung. Penghindaran obat berisiko: Hindari penggunaan obat-obatan tertentu, seperti NSAID, kecuali di bawah pengawasan dokter. Pengobatan infeksi H. pylori: Jika gastritis disebabkan oleh infeksi bakteri H. pylori, dokter mungkin meresepkan antibiotik untuk mengatasi infeksi. Obat antasam: Dokter dapat meresepkan obat antasam atau penghambat pompa proton (PPI) untuk mengurangi produksi asam lambung. Mengubah pola makan: Makan lebih sering dalam porsi kecil, menghindari makanan pedas atau asam, dan mengonsumsi makanan yang mudah dicerna dapat membantu meredakan gejala. Manajemen stres: Stres dapat memperburuk gejala gastritis. Olahraga, meditasi, dan teknik manajemen stres lainnya dapat membantu. ",
        },
        {
            "message": "*Kemungkinan anda mengalami Kanker Ovarium*",
            "details": "Kanker ovarium adalah jenis kanker yang bermula dari ovarium atau indung telur, organ kecil di panggul yang menghasilkan telur dan hormon wanita. Kanker ovarium biasanya tidak terdeteksi pada tahap awal karena gejalanya seringkali tidak spesifik dan mungkin tidak muncul sampai kanker sudah mencapai tahap yang lebih lanjut. Gejala yang mungkin muncul termasuk perut kembung, nyeri panggul atau perut bawah, perubahan dalam kebiasaan buang air besar atau buang air kecil, penurunan berat badan yang tidak diinginkan, kelelahan, dan perubahan dalam siklus menstruasi. Pengobatan kanker ovarium dapat melibatkan kombinasi pembedahan, kemoterapi, dan terapi radiasi, tergantung pada jenis kanker, tingkat keparahan, dan faktor-faktor lainnya. Keputusan mengenai rencana pengobatan akan bergantung pada sejumlah faktor, dan biasanya tim perawatan kesehatan akan bekerja sama untuk merencanakan pendekatan terbaik. Penting untuk diingat bahwa setiap individu berbeda, dan rencana perawatan akan disesuaikan dengan kondisi kesehatan dan kebutuhan pasien. Konsultasikan dengan dokter untuk mendapatkan informasi lebih lanjut dan mendiskusikan opsi perawatan yang paling sesuai. Jika Anda atau seseorang yang Anda kenal mengalami gejala yang mencurigakan, segera hubungi profesional kesehatan untuk evaluasi lebih lanjut."
        },
    ],
    ("Mual", "Perut Kembung", "Nyeri ulu Hati"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Ulkus Peptikum*",
            "details": "Ulkus peptikum, atau yang sering disebut sebagai tukak lambung atau tukak usus dua belas jari, adalah luka atau kerusakan pada lapisan dalam dinding lambung atau usus dua belas jari. Ulkus peptikum dapat terjadi ketika keseimbangan antara faktor-faktor yang melindungi dinding lambung dan usus dengan faktor-faktor yang dapat menyebabkan kerusakan terganggu. Salah satu penyebab utama ulkus peptikum adalah infeksi bakteri Helicobacter pylori (H. pylori) dan penggunaan obat antiinflamasi nonsteroid (NSAID) seperti ibuprofen atau aspirin. \n \n Pengobatan ulkus peptikum melibatkan mengatasi penyebabnya dan meredakan gejala. Ini dapat melibatkan penggunaan antibiotik untuk mengatasi infeksi H. pylori, obat antasam, dan obat penurun asam untuk mengurangi produksi asam lambung. Penghindaran obat NSAID dan perubahan gaya hidup, seperti menghindari merokok dan minum alkohol, juga dapat direkomendasikan. Penting untuk berkonsultasi dengan profesional kesehatan jika Anda mengalami gejala yang mungkin terkait dengan ulkus peptikum. Pengobatan dini dapat membantu mencegah komplikasi serius seperti perdarahan atau perforasi lambung."
        },
    ],
    ("Mual", "Sakit Kepala", "Gangguan Penglihatan"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Tumor Otak*",
            "details": "Tumor otak adalah pertumbuhan abnormal dari sel-sel di otak atau di sekitarnya. Tumor otak dapat bersifat jinak (non-kanker) atau ganas (kanker). Jenis dan tingkat keparahan tumor otak dapat bervariasi, dan gejalanya tergantung pada lokasi, ukuran, dan jenis tumor. Beberapa tumor otak dapat tumbuh lambat dan tidak menimbulkan gejala untuk waktu yang lama, sementara yang lain dapat menyebabkan gejala yang berkembang pesat. \n \n Diagnosis dan Pengobatan: \n \n Pemeriksaan Neurologis: Melibatkan pemeriksaan fisik dan evaluasi fungsi otak. Pemindaian Otak: CT scan atau MRI dapat membantu mendeteksi keberadaan dan lokasi tumor. Biopsi: Pengambilan sampel jaringan untuk pemeriksaan lebih lanjut. Pengobatan Tumor Otak: Bedah: Mengangkat sebanyak mungkin tumor. Radioterapi: Menggunakan radiasi untuk menghancurkan sel-sel kanker. Kemoterapi: Penggunaan obat-obatan untuk membunuh sel-sel kanker. Terapi Targeted dan Imunoterapi: Pendekatan terapi yang berkembang pesat Manajemen Gejala: Terkadang, pengobatan bertujuan untuk mengurangi gejala dan meningkatkan kualitas hidup. Penting untuk mendiskusikan opsi pengobatan dan prognosis dengan dokter spesialis onkologi atau ahli bedah saraf untuk memahami opsi terbaik berdasarkan jenis, ukuran, dan lokasi tumor otak. Kecepatan diagnosis dan pengobatan dini dapat memainkan peran penting dalam prognosis dan hasil pengobatan."
        },
        {
            "message": "*Kemungkinan anda mengalami gejala Galukoma*",
            "details": "Glaukoma adalah kelompok penyakit mata yang menyebabkan kerusakan saraf optik, yang dapat menyebabkan hilangnya penglihatan. Saraf optik mengirimkan informasi visual dari mata ke otak, dan kerusakan pada saraf optik dapat menyebabkan gangguan atau kehilangan penglihatan. Glaukoma seringkali berkaitan dengan tekanan intraokular yang tinggi (tekanan dalam mata), tetapi ada juga kasus glaukoma yang terjadi dengan tekanan intraokular normal. \n \n Diagnosis dan Pengobatan Glaukoma: \n \n Pemeriksaan Mata Rutin: Pemeriksaan mata rutin sangat penting untuk mendeteksi glaukoma pada tahap awal. Pengukuran Tekanan Intraokular: Mengukur tekanan mata dengan tonometer. Pemeriksaan Saraf Optik: Dokter mata dapat melakukan pemeriksaan untuk mengevaluasi kondisi saraf optik. Pengobatan: Ini dapat melibatkan obat-obatan, terapi laser, atau pembedahan untuk mengurangi tekanan mata. Manajemen Seumur Hidup: Glaukoma seringkali memerlukan manajemen seumur hidup untuk mencegah kerusakan lebih lanjut pada penglihatan. Jika Anda memiliki kekhawatiran tentang kesehatan mata atau merasa memiliki risiko glaukoma, sangat penting untuk menjalani pemeriksaan mata secara teratur oleh dokter mata atau optometris. Glaukoma dapat dikelola dengan baik jika dideteksi pada tahap awal."
        },  
    ],
    ("Mual", "Demam", "Mata Menguning"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Pankreatitis*",
            "details": "Pankreatitis adalah peradangan pada pankreas, sebuah organ yang terletak di belakang perut. Pankreas memiliki peran penting dalam produksi enzim pencernaan dan insulin, yang membantu mengatur kadar gula darah. Pankreatitis dapat bersifat akut atau kronis, tergantung pada lamanya peradangan. \n \n Diagnosis dan Pengobatan Pankreatitis: \n \n Pemeriksaan Darah: Pemeriksaan darah untuk menilai fungsi pankreas dan deteksi enzim yang dilepaskan oleh pankreas. Imaging Medis: CT scan atau MRI dapat membantu melihat kondisi pankreas. Endoskopi: Pemeriksaan dengan endoskop untuk melihat dalam saluran pencernaan. Pengobatan Pankreatitis Akut: Puasa dan Hydration: Penderita mungkin perlu berpuasa untuk memberi istirahat pada pankreas, dan juga mendapatkan cairan intravena. Manajemen Nyeri: Obat penghilang rasa sakit dapat diberikan untuk mengatasi nyeri. Penanganan Penyebab: Tergantung pada penyebabnya, seperti penghentian konsumsi alkohol atau pengangkatan batu empedu. Pengobatan Pankreatitis Kronis: Manajemen Gejala: Diet khusus, suplemen enzim, atau insulin mungkin diperlukan. Pengelolaan Komplikasi: Pankreatitis kronis dapat menyebabkan komplikasi seperti diabetes, yang perlu diatasi. Pembedahan: Dalam beberapa kasus, intervensi bedah mungkin diperlukan. Penting untuk mendapatkan perawatan medis segera jika ada kecurigaan terhadap pankreatitis. Pankreatitis akut bisa menjadi kondisi yang serius dan memerlukan perhatian medis segera. Pankreatitis kronis, meskipun berlangsung lebih lama, juga memerlukan manajemen perawatan yang cermat untuk mengurangi gejala dan komplikasi."
        },
    ],
    ("Mual", "Demam", "Nyeri ulu Hati"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Apendisitis*",
            "details": "Apendisitis adalah peradangan pada usus buntu (apendiks), sebuah organ kecil yang terletak di ujung kanan bawah perut. Apendisitis umumnya disebabkan oleh sumbatan apendiks yang dapat terjadi akibat pembengkakan jaringan limfat, fecalith (endapan tinja keras), tumor, atau infeksi. Jika tidak diobati, apendisitis dapat mengakibatkan pecahnya apendiks, yang dapat menjadi kondisi serius dan mengancam jiwa. \n \n Diagnosis dan Pengobatan Apendisitis: \n \n Pemeriksaan Fisik: Dokter dapat melakukan pemeriksaan fisik untuk menilai gejala dan nyeri di perut. Pemeriksaan Darah: Pemeriksaan darah untuk menilai tanda-tanda infeksi, seperti peningkatan jumlah sel darah putih. Pemeriksaan Pencitraan: CT scan atau USG perut dapat membantu memvisualisasikan apendiks dan menilai kondisinya. Pengobatan Apendisitis: Operasi (Apendektomi): Prosedur pembedahan untuk mengangkat apendiks yang meradang. Ini adalah pengobatan utama untuk apendisitis. Antibiotik: Jika apendisitis belum mencapai tahap pecah, pemberian antibiotik dapat membantu mengurangi infeksi. Apendisitis adalah peradangan pada usus buntu (apendiks), sebuah organ kecil yang terletak di ujung kanan bawah perut. Apendisitis umumnya disebabkan oleh sumbatan apendiks yang dapat terjadi akibat pembengkakan jaringan limfat, fecalith (endapan tinja keras), tumor, atau infeksi. Jika tidak diobati, apendisitis dapat mengakibatkan pecahnya apendiks, yang dapat menjadi kondisi serius dan mengancam jiwa. Gejala Apendisitis: Nyeri Perut: Nyeri umumnya dimulai di sekitar pusar dan kemudian berpindah ke sisi kanan bawah perut. Mual dan Muntah: Mual dan muntah mungkin terjadi sebagai respons terhadap nyeri perut. Hilangnya Nafsu Makan: Banyak orang dengan apendisitis mengalami hilangnya nafsu makan. Demam: Kenaikan suhu tubuh bisa terjadi sebagai tanda infeksi. Perubahan Buang Air Besar: Mungkin terjadi diare atau konstipasi. Perasaan Tidak Nyaman Saat Buang Air Kecil: Nyeri atau ketidaknyamanan saat buang air kecil bisa terjadi. Diagnosis dan Pengobatan Apendisitis: Pemeriksaan Fisik: Dokter dapat melakukan pemeriksaan fisik untuk menilai gejala dan nyeri di perut. Pemeriksaan Darah: Pemeriksaan darah untuk menilai tanda-tanda infeksi, seperti peningkatan jumlah sel darah putih. Pemeriksaan Pencitraan: CT scan atau USG perut dapat membantu memvisualisasikan apendiks dan menilai kondisinya. Pengobatan Apendisitis: Operasi (Apendektomi): Prosedur pembedahan untuk mengangkat apendiks yang meradang. Ini adalah pengobatan utama untuk apendisitis. Antibiotik: Jika apendisitis belum mencapai tahap pecah, pemberian antibiotik dapat membantu mengurangi infeksi. Komplikasi Apendisitis: Perforasi Apendiks: Pecahnya apendiks, yang dapat menyebabkan peritonitis (peradangan pada peritoneum, lapisan yang melapisi organ dalam perut). Abses: Kumpulan nanah yang dapat terbentuk di sekitar apendiks yang meradang. Infeksi Menyebar: Infeksi dari apendiks yang meradang dapat menyebar ke organ-organ sekitarnya. Penting untuk mendapatkan perawatan medis segera jika ada kecurigaan terhadap apendisitis. Apendisitis biasanya memerlukan tindakan bedah untuk menghindari komplikasi yang lebih serius. Jika Anda atau seseorang yang Anda kenal mengalami gejala apendisitis, segera hubungi profesional kesehatan atau pergi ke unit gawat darurat untuk evaluasi lebih lanjut."
        },
    ],
    ("Mual", "Demam", "Nyeri Perut"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Kolesistitis*",
            "details": "Kolesistitis adalah peradangan pada kantong empedu, yang disebut kantong empedu atau kandung empedu. Kandung empedu berperan dalam penyimpanan dan pelepasan empedu, cairan yang diproduksi oleh hati untuk membantu dalam proses pencernaan lemak. Kolesistitis dapat terjadi secara akut atau menjadi kondisi kronis. \n \n Diagnosis dan Pengobatan Kolesistitis: \n \n Pemeriksaan Darah: Pemeriksaan darah dapat menunjukkan tanda-tanda peradangan atau infeksi. Pemeriksaan Citra Medis: Ultrasonografi atau CT scan dapat membantu memvisualisasikan kantong empedu dan mengidentifikasi batu empedu atau peradangan. Hepatobiliar Iminodiacetic Acid (HIDA) Scan: Ini adalah jenis pemeriksaan pencitraan yang dapat membantu memeriksa aliran empedu. Pemeriksaan Endoskopi: Endoskopi dapat digunakan untuk memeriksa saluran empedu secara langsung. Pengobatan Kolesistitis Akut: Puasa: Untuk memberikan istirahat pada kantong empedu. Antibiotik: Jika infeksi hadir. Pain Management: Obat penghilang rasa sakit dapat membantu mengurangi nyeri. Pengobatan Kolesistitis Kronis: Apendektomi: Pengangkatan kantong empedu dapat menjadi solusi untuk kolesistitis kronis yang persisten. Perubahan Gaya Hidup: Perubahan dalam pola makan, khususnya menghindari makanan berlemak, dapat membantu mencegah serangan kolesistitis. Jika Anda mengalami gejala yang mencurigakan, seperti nyeri abdomen yang parah atau gejala yang mencerminkan masalah kandung empedu, segera berkonsultasi dengan profesional kesehatan. Mereka dapat melakukan evaluasi lebih lanjut dan meresepkan perawatan yang sesuai berdasarkan kondisi kesehatan Anda."
        },
    ],
    ("Mual", "Batuk", "Sakit Tenggorokan"): [
        {
            "message": "*Kemungkinan anda mengalami gejala GERD (Gastroesophageal Reflux Disease)*",
            "details": "GERD (Gastroesophageal Reflux Disease) adalah suatu kondisi kronis di mana asam lambung mengalir kembali (refluks) ke dalam kerongkongan (esofagus), menyebabkan iritasi dan merusak lapisan dinding esofagus. Gejala GERD dapat bervariasi dari ringan hingga parah, dan dapat memengaruhi kualitas hidup sehari-hari. \n \n Diagnosis dan Pengobatan GERD: \n \n Pemeriksaan Klinis: Dokter dapat menilai gejala dan riwayat kesehatan pasien. Endoskopi: Pemeriksaan dengan menggunakan tabung fleksibel dengan kamera di ujungnya untuk melihat kondisi esofagus dan lambung. Pemeriksaan pH Metri: Pemeriksaan untuk mengukur tingkat keasaman di dalam esofagus. Manometri Esofagus: Pemeriksaan yang mengukur kontraksi otot esofagus. Pengobatan GERD: Obat Asam: Penggunaan obat antasam atau penghambat pompa proton (PPI) untuk mengurangi produksi asam lambung. Antasida: Untuk mengurangi keasaman. Prokinetik: Untuk meningkatkan gerakan otot lambung.Perubahan Gaya Hidup: Pola Makan Sehat: Hindari makanan yang memicu gejala.Menjaga Berat Badan Ideal: Untuk mengurangi tekanan pada perut.Tidur dengan Kepala Lebih Tinggi: Bisa membantu mencegah refluks.Operasi: Dalam beberapa kasus yang parah, prosedur bedah seperti fundoplikasi dapat direkomendasikan.Jika Anda mengalami gejala GERD yang persisten atau mengganggu, segera berkonsultasi dengan dokter untuk diagnosis dan perawatan yang tepat. Pengobatan dan manajemen yang efektif dapat membantu mengurangi gejala dan mencegah komplikasi lebih lanjut."
        },
    ],
    ("Mual", "Lemas", "Nyeri Punggung"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Gagal Ginjal*",
            "details": "Gagal ginjal adalah kondisi di mana ginjal kehilangan kemampuannya untuk melakukan fungsi penyaringan dan pengeluaran racun dari tubuh. Ini bisa terjadi secara tiba-tiba (gagal ginjal akut) atau berkembang secara perlahan dalam jangka waktu yang lebih lama (gagal ginjal kronis). Gagal ginjal akut bisa menjadi kondisi yang serius dan memerlukan penanganan medis segera. \n \n Diagnosis dan Pengobatan Gagal Ginjal: \n \n Pemeriksaan Darah: Untuk menilai tingkat kreatinin dan urea, yang merupakan indikator fungsi ginjal. Analisis Urin: Untuk memeriksa kandungan zat dan partikel yang dapat mengindikasikan masalah ginjal. Pemeriksaan Pencitraan: Seperti CT scan atau ultrasound untuk melihat kondisi ginjal. Biopsi Ginjal: Pengambilan sampel jaringan ginjal untuk evaluasi lebih lanjut. Pengobatan Gagal Ginjal: Manajemen Tekanan Darah: Kontrol tekanan darah adalah langkah penting. Manajemen Diabetes: Jika diabetes adalah penyebab gagal ginjal. Diet Rendah Garam: Untuk mengurangi retensi cairan. Dialisis: Proses penyaringan darah menggunakan mesin dilakukan jika fungsi ginjal sangat terganggu. Transplantasi Ginjal: Jika gagal ginjal kronis mencapai tingkat yang parah, transplantasi ginjal mungkin diperlukan. Penting untuk mendapatkan diagnosis dan perawatan sejak dini jika Anda mengalami gejala gagal ginjal. Perawatan yang tepat dapat membantu mengelola kondisi dan mencegah kemajuan lebih lanjut. Berkonsultasilah dengan dokter atau ahli nefrologi untuk evaluasi dan perencanaan perawatan yang sesuai."
        },
    ],
    ("Mual", "Demam", "Urine Berbau Busuk"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Batu Ginjal*",
            "details": "Batu ginjal adalah endapan keras yang terbentuk dalam ginjal dari zat-zat yang terdapat dalam urine. Ukuran dan bentuk batu ginjal dapat bervariasi, dan mereka dapat berada dalam ginjal atau bergerak melalui saluran kemih. Batu ginjal dapat menyebabkan rasa sakit dan ketidaknyamanan jika mereka menyumbat saluran kemih atau menyebabkan iritasi pada dinding saluran kemih. \n \n Diagnosis dan Pengobatan Batu Ginjal: \n \n Analisis Urin: Untuk memeriksa kandungan zat dan partikel yang dapat membentuk batu. Pemeriksaan Darah: Untuk menilai fungsi ginjal dan tingkat zat tertentu dalam darah. Pemeriksaan Pencitraan: CT scan atau ultrasound untuk melihat ukuran dan lokasi batu ginjal. Pengobatan Batu Ginjal: Konsumsi Cairan: Minum banyak air untuk membantu mengencerkan urine dan mencegah pembentukan batu baru. Analgesik: Obat penghilang rasa sakit dapat membantu mengatasi nyeri. Pengelolaan Gaya Hidup: Perubahan diet dan gaya hidup untuk mencegah pembentukan batu baru. Eswl (Extracorporeal Shock Wave Lithotripsy): Metode non-invasif menggunakan gelombang kejut untuk memecah batu ginjal. Pembedahan: Jika batu ginjal terlalu besar atau tidak dapat diatasi dengan metode non-invasif. Bila Anda mengalami gejala batu ginjal, penting untuk segera berkonsultasi dengan dokter untuk evaluasi dan pengelolaan yang tepat. Perawatan dapat disesuaikan dengan ukuran dan jenis batu ginjal, serta faktor-faktor risiko individu."
        },
    ],
    ("Sesak Napas", "Batuk", "Demam"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Pneumonia*",
            "details": "Pneumonia adalah infeksi pada paru-paru yang dapat disebabkan oleh berbagai mikroorganisme seperti bakteri, virus, jamur, atau parasit. Kondisi ini dapat mempengaruhi satu atau kedua paru-paru dan menyebabkan peradangan pada kantong udara (alveoli) di dalam paru-paru. Pneumonia dapat berkisar dari ringan hingga berat, tergantung pada jenis patogen penyebab dan kondisi kesehatan pasien. \n \n Diagnosis dan Pengobatan Pneumonia: \n \n Pemeriksaan Fisik: Dokter akan memeriksa gejala dan tanda klinis pneumonia. Pemeriksaan Darah: Untuk menilai tingkat sel darah putih dan deteksi tanda-tanda infeksi. Pemeriksaan Radiologi: Foto rontgen dada atau CT scan paru-paru dapat membantu memvisualisasikan perubahan pada paru-paru. Sputum Test: Pemeriksaan dahak untuk mengidentifikasi patogen penyebab. Oksigen Terapi: Diberikan jika ada kesulitan bernapas. Antibiotik atau Antivirus: Bergantung pada penyebab pneumonia (bakteri atau virus). Obat Antiinflamasi: Untuk meredakan gejala dan peradangan. Istirahat dan Cairan: Istirahat yang cukup dan konsumsi cairan yang baik untuk membantu pemulihan. Vaksinasi: Vaksin pneumonia dan vaksin influenza dapat membantu mencegah beberapa jenis pneumonia. Penting untuk segera mencari bantuan medis jika Anda atau seseorang yang Anda kenal mengalami gejala pneumonia, terutama jika gejala berat atau jika ada faktor risiko tertentu seperti usia lanjut, sistem kekebalan tubuh yang melemah, atau kondisi kesehatan kronis. Pneumonia dapat berkembang menjadi kondisi yang serius dan memerlukan perawatan medis yang tepat."
        },
    ],
    ("Sesak Napas", "Batuk", "Nyeri Dada"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Kanker Paru*",
            "details": "Kanker paru-paru adalah kondisi kanker yang terjadi ketika sel-sel di dalam paru-paru berkembang secara tidak terkendali. Ada dua jenis kanker paru-paru utama: kanker paru-paru non-kecil dan kanker paru-paru kecil. Kanker paru-paru non-kecil merupakan jenis yang paling umum. \n \n Diagnosis dan Pengobatan Kanker Paru-paru: \n \n Tes Pencitraan: CT scan, MRI, atau PET scan untuk memvisualisasikan struktur paru-paru dan mendeteksi adanya tumor. Biopsi: Pengambilan sampel jaringan untuk pemeriksaan mikroskopis. Pemeriksaan Sputum: Memeriksa dahak untuk mengetahui adanya sel kanker. Tes Fungsi Paru-paru: Untuk menilai kapasitas paru-paru. Staging Kanker: Menentukan sejauh mana kanker telah menyebar. \n \n Pengobatan Kanker Paru-paru: \n \n Pembedahan: Mengangkat tumor dan sebagian paru-paru jika mungkin. Kemoterapi: Penggunaan obat-obatan untuk membunuh sel kanker. Radioterapi: Menggunakan sinar-X untuk merusak dan membunuh sel kanker. Terapi Targeted: Obat-obatan yang ditargetkan pada sel kanker tertentu. Imunoterapi: Meningkatkan sistem kekebalan tubuh untuk melawan kanker. Palliative Care: Pelayanan kesehatan yang bertujuan untuk meningkatkan kualitas hidup pasien. Penting untuk mendapatkan diagnosis dan perawatan sejak dini jika Anda atau seseorang yang Anda kenal mengalami gejala kanker paru-paru. Tim medis akan merancang rencana perawatan yang sesuai berdasarkan jenis dan stadium kanker. Pencegahan melalui menghindari faktor risiko, seperti merokok, juga penting untuk mengurangi risiko kanker paru-paru."
        },
    ],
    ("Sesak Napas", "Batuk", "Lemas"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Asma*",
            "details": "Asma adalah penyakit saluran pernapasan kronis yang ditandai oleh peradangan dan penyempitan pada saluran udara. Hal ini dapat menyebabkan kesulitan bernapas, batuk, dan sesak napas. Gejala asma dapat bervariasi dari ringan hingga berat, dan sering kali muncul dan memburuk dalam situasi tertentu. \n \n Diagnosis dan Pengobatan Asma: \n \n Tes Spirometri: Mengukur volume udara yang dapat dikeluarkan dari paru-paru. Tes Fungsi Paru-paru: Menilai kapasitas dan fungsi paru-paru. Riwayat Medis dan Gejala: Dokter akan menanyakan riwayat medis dan gejala yang dialami. Tes Alergi: Mengidentifikasi alergen yang mungkin menjadi pemicu. \n \n Pengobatan Asma: \n \n Inhaler: Alat bantu untuk menyampaikan obat-obatan secara langsung ke saluran pernapasan. Obat-obatan Kontrol: Digunakan secara teratur untuk mengendalikan peradangan dan mencegah gejala. Obat-obatan Penguat: Digunakan untuk meredakan gejala akut atau selama serangan asma. Manajemen Lingkungan: Menghindari pencetus asma yang dapat memperburuk gejala. Pendidikan dan Perencanaan Asma: Memahami kondisi dan mengembangkan rencana tindakan untuk mengatasi gejala. Terapi Fisik: Olah fisik dan latihan pernapasan untuk meningkatkan fungsi paru-paru. Penting untuk mendapatkan pengelolaan asma yang sesuai dengan kondisi dan gejala masing-masing individu. Berkonsultasilah dengan dokter atau ahli alergi dan imunologi untuk mendapatkan diagnosis yang tepat dan rencana pengobatan yang efektif."
        },
    ],
    ("Sesak Napas", "Nyeri Dada", "Kesemutan"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Kolesterol*",
            "details": "Kolesterol adalah suatu senyawa lemak yang ditemukan di seluruh tubuh dan juga ditemukan dalam makanan tertentu. Kolesterol memiliki peran penting dalam pembentukan sel-sel tubuh, produksi hormon, dan produksi zat empedu yang membantu pencernaan lemak. Namun, kadar kolesterol yang tinggi dalam darah dapat meningkatkan risiko penyakit jantung dan pembuluh darah. \n \n Pengukuran Kolesterol: \n \n Total Kolesterol: Kombinasi antara LDL, HDL, dan sejumlah kecil trigliserida. LDL Kolesterol: Kolesterol 'jahat' yang dapat menyumbat arteri. HDL Kolesterol: Kolesterol 'baik' yang membantu membersihkan arteri. Trigliserida: Jenis lemak dalam darah. \n \n Pengelolaan Kolesterol Tinggi: \n \n Perubahan Gaya Hidup: Pola Makan Sehat: Mengonsumsi makanan rendah lemak jenuh dan kolesterol. Olahraga Teratur: Aktivitas fisik dapat meningkatkan kadar HDL. Menjaga Berat Badan Ideal: Menurunkan berat badan dapat membantu mengontrol kadar kolesterol. Obat-obatan: Statins: Menghambat produksi kolesterol dalam hati. Fibrates, Niacin, dan Obat Lainnya: Digunakan untuk mengatur kadar kolesterol dan trigliserida. Pantauan Rutin: Tes darah untuk memantau kadar kolesterol secara berkala. Penting untuk berkonsultasi dengan profesional kesehatan untuk mengevaluasi risiko kolesterol tinggi dan merencanakan strategi pengelolaan yang sesuai berdasarkan kondisi kesehatan dan faktor risiko individu. Perubahan gaya hidup dan pengobatan yang tepat dapat membantu mengontrol kadar kolesterol dan mencegah risiko penyakit jantung."
        },
    ],
    ("Sesak Napas", "Nyeri Dada", "Mudah Lelah"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Jantung Koroner*",
            "details": "Penyakit jantung koroner (PJK), juga dikenal sebagai penyakit arteri koroner (PAK) atau aterosklerosis koroner, adalah suatu kondisi di mana pembuluh darah koroner yang memasok darah dan oksigen ke otot jantung mengalami penyempitan atau penyumbatan. Kondisi ini disebabkan oleh penumpukan plak kolesterol dan bahan lain di dinding arteri, membentuk gumpalan yang dapat menghambat aliran darah ke jantung.\n \n Diagnosis dan Pengobatan Jantung Koroner: \n \n Elektrokardiogram (EKG): Merekam aktivitas listrik jantung. Tes Darah: Untuk menilai kadar kolesterol dan enzim jantung. Tes Pencitraan Jantung: Seperti angiografi koroner atau CT scan jantung. Pengobatan Jantung Koroner: Obat-obatan: Seperti statin, aspirin, beta-blocker, atau nitrat. Pembatasan Garam dan Diet Rendah Lemak: Untuk mengontrol tekanan darah dan kadar kolesterol. Prosedur Invasif: Seperti angioplasti atau bypass jantung dalam kasus yang lebih serius. Perubahan Gaya Hidup: Olahraga Teratur: Untuk meningkatkan kesehatan jantung. Berhenti Merokok: Merokok dapat merusak arteri dan mempercepat perkembangan penyakit. Pencegahan dan manajemen penyakit jantung koroner melibatkan pengelolaan faktor risiko, perubahan gaya hidup sehat, dan pengobatan yang tepat. Penting untuk berkonsultasi dengan dokter untuk evaluasi risiko pribadi dan merencanakan pendekatan pengelolaan yang sesuai. Jika Anda mengalami gejala seperti nyeri dada atau sesak napas, segera cari pertolongan medis."
        },
        {
            "message": "*Kemungkinan anda mengalami gejala Jantung Aritmia*",
            "details": "Aritmia adalah istilah umum yang digunakan untuk menggambarkan gangguan irama jantung. Jantung normalnya berdetak dengan irama yang teratur, tetapi pada aritmia, detak jantung dapat menjadi terlalu cepat (takikardia), terlalu lambat (bradikardia), atau tidak teratur. Beberapa aritmia mungkin tidak menimbulkan gejala dan tidak memerlukan perawatan, sedangkan yang lain dapat menjadi kondisi serius yang memerlukan perhatian medis. \n \n Diagnosis dan Pengobatan Aritmia: \n \n Elektrokardiogram (EKG): Merekam aktivitas listrik jantung untuk mendeteksi ketidaknormalan. Holter Monitor atau Event Monitor: Alat pemantauan jantung dalam jangka waktu yang lebih lama. Echocardiogram: Pemeriksaan gambaran ultrasound jantung. Tes Darah: Untuk menilai elektrolit dan fungsi tiroid. Kateterisasi Elektrofisiologi (EPS): Memasukkan kateter ke dalam jantung untuk memetakan sinyal listrik. \n \n Pengobatan Aritmia: \n \n Obat-obatan: Seperti beta-blocker, antiaritmia, atau antikoagulan tergantung pada jenis aritmia dan faktor risiko. Prosedur Invasif: Ablasi Kateter: Menghancurkan jaringan yang menyebabkan aritmia. Pemasangan Pacemaker atau Defibrillator: Untuk mengontrol irama jantung. Pembedahan: Dalam beberapa kasus, pembedahan mungkin diperlukan untuk mengatasi penyebab aritmia. Penting untuk mencari perhatian medis jika Anda mengalami gejala aritmia. Penanganan dan pengobatan harus disesuaikan dengan jenis dan penyebab aritmia serta kondisi kesehatan umum pasien. Seorang ahli jantung atau spesialis elektrofisiologi jantung dapat membantu menilai dan merencanakan penanganan yang sesuai."
        },
    ],
    ("Sesak Napas", "Sakit Kepala", "Demam"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Bronkitis*",
            "details": "Bronkitis adalah peradangan pada saluran udara utama yang mengarah ke paru-paru, yang disebut bronkus. Ada dua jenis bronkitis, yaitu bronkitis akut dan kronis. \n \n Pengobatan: \n \n Berhenti merokok (jika merokok adalah penyebabnya). Penggunaan bronkodilator untuk melebarkan saluran udara. Terapi oksigen pada kasus yang lebih serius. Pemberian vaksin influenza dan pneumonia. \n \n Penting untuk berkonsultasi dengan profesional kesehatan untuk diagnosis dan penanganan yang tepat. Meskipun bronkitis sering disebabkan oleh infeksi virus dan sembuh dengan sendirinya, beberapa kasus bronkitis kronis memerlukan manajemen jangka panjang dan perhatian medis yang berkelanjutan."
        },
    ],
    ("Sesak Napas", "Sakit Kepala", "Gangguan Penglihatan"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Hipertensi*",
            "details": "Hipertensi, atau tekanan darah tinggi, adalah kondisi di mana tekanan darah dalam arteri tubuh meningkat secara persisten. Tekanan darah dinyatakan dalam dua angka: tekanan sistolik (tekanan saat jantung berkontraksi) dan diastolik (tekanan saat jantung beristirahat antara detak jantung). Hipertensi dapat menyebabkan masalah kesehatan serius jika tidak dikontrol. \n \n Pengelolaan dan Pengobatan: \n \n Perubahan Gaya Hidup: Diet rendah garam dan tinggi potassium. Menjaga berat badan yang sehat. Aktivitas fisik teratur. Batasi konsumsi alkohol dan berhenti merokok. Obat-obatan: Jika perubahan gaya hidup tidak cukup, dokter dapat meresepkan obat antihipertensi seperti diuretik, ACE inhibitors, beta-blocker, atau calcium channel blockers. Pantauan Teratur: Pemantauan tekanan darah secara teratur untuk memastikan kontrol yang baik. Penting untuk berkonsultasi dengan dokter untuk evaluasi risiko pribadi dan perencanaan penanganan yang sesuai. Pengelolaan hipertensi melibatkan kombinasi perubahan gaya hidup dan, jika diperlukan, penggunaan obat-obatan. Kepatuhan dengan rencana pengobatan dan perubahan gaya hidup dapat membantu mengontrol tekanan darah dan mengurangi risiko komplikasi."
        },
    ],
    ("Sesak Napas", "Diare", "Kesemutan"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Amiloidosis*",
            "details": "Amiloidosis adalah kelompok penyakit langka yang disebabkan oleh penumpukan protein abnormal yang disebut amiloid dalam berbagai organ dan jaringan tubuh. Protein amiloid dapat menyebabkan kerusakan dan gangguan fungsi organ yang terkena. Ada beberapa jenis amiloidosis, dan gejalanya dapat bervariasi tergantung pada organ atau jaringan yang terlibat. \n \n Pengobatan: \n \n Terapi Imunoglobulin: Untuk amiloidosis AL, terapi yang menggunakan imunoglobulin dapat membantu mengurangi produksi protein berlebih. Kemoterapi: Dapat digunakan untuk mengurangi produksi sel plasma yang menghasilkan protein berlebih. Terapi Targeted: Dapat ditujukan pada jenis amiloidosis tertentu. Pemindahan Organ: Pada kasus yang parah, pemindahan organ seperti transplantasi hati atau jantung mungkin diperlukan. Penting untuk mendapatkan diagnosis dini dan pengobatan yang tepat dari dokter yang berpengalaman dalam merawat amiloidosis. Perawatan akan disesuaikan dengan jenis amiloidosis, organ yang terlibat, dan tingkat keparahan penyakit. Karena amiloidosis adalah penyakit langka, pengelolaan dan perawatannya dapat memerlukan kerjasama tim medis yang terampil dan spesialis."
        },
    ],
    ("Mudah Lelah", "Nyeri Perut", "Lemas"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Sirosis Hati*",
            "details": "Sirosis hati adalah kondisi parah dan kronis di mana jaringan hati yang sehat digantikan oleh jaringan parut (fibrosis). Ini biasanya terjadi sebagai akibat dari kerusakan hati yang terus-menerus dan merusak, yang dapat disebabkan oleh berbagai faktor. Sirosis hati dapat mempengaruhi fungsi hati secara keseluruhan dan menyebabkan komplikasi serius. \n \n Diagnosis dan Pengobatan: \n \n Diagnosis: Tes darah untuk mengukur fungsi hati. Pemeriksaan gambar seperti USG, CT scan, atau MRI. Biopsi hati untuk mengkonfirmasi diagnosis dan menilai tingkat fibrosis. Pengobatan: Mengelola penyebab mendasar seperti hepatitis atau alkoholisme. Pengobatan untuk mengurangi komplikasi, seperti diuretik untuk mengatasi cairan berlebih. Transplantasi hati mungkin diperlukan pada kasus yang parah. Perubahan Gaya Hidup: Berhenti atau mengurangi konsumsi alkohol. Menjaga berat badan sehat. Mengelola kondisi seperti diabetes dan tekanan darah tinggi. \n \n Penting untuk mendapatkan diagnosis dan perawatan dari profesional kesehatan yang berkualifikasi. Sirosis hati adalah kondisi serius dan perlu dielola secara komprehensif. Jika Anda atau seseorang yang Anda kenal mengalami gejala sirosis hati, segera konsultasikan dengan dokter untuk penilaian dan rencana pengobatan yang sesuai."
        },
    ],
    ("Mudah Lelah", "Nyeri Perut", "Mata Menguning"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Hepatitis*",
            "details": "Hepatitis adalah peradangan pada hati yang dapat disebabkan oleh infeksi virus, paparan zat toksik, atau masalah kekebalan tubuh. Ada beberapa jenis hepatitis, dan yang paling umum adalah hepatitis A, hepatitis B, dan hepatitis C. \n \n Diagnosis dan Pengobatan: \n \n Diagnosis: Tes Darah: Untuk mendeteksi keberadaan virus dan mengevaluasi fungsi hati. Biopsi Hati: Pada beberapa kasus untuk menilai kerusakan hati. Pengobatan: Hepatitis A: Tidak ada pengobatan khusus, tubuh umumnya dapat pulih sendiri. Fokus pada istirahat dan hidrasi. Hepatitis B dan C: Antiviral dan obat-obatan lainnya untuk mengurangi perkembangan penyakit. Vaksinasi: Vaksin Hepatitis A dan Hepatitis B efektif untuk mencegah infeksi. Manajemen Gejala: Menjaga asupan nutrisi yang baik. Istirahat yang cukup. \n \n Penting untuk mendapatkan perawatan medis jika Anda mengalami gejala hepatitis atau memiliki risiko tertular. Pencegahan melalui vaksinasi dan tindakan pencegahan kontak dengan darah yang terinfeksi sangat penting, terutama untuk hepatitis B dan C. Jika Anda memiliki kekhawatiran atau gejala, segera berkonsultasi dengan dokter."
        },
    ],
    ("Mudah Lelah", "Batuk", "Berkeringat di Malam Hari"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Tuberkulosis*",
            "details": "Tuberkulosis (TB) adalah penyakit infeksi bakteri yang disebabkan oleh Mycobacterium tuberculosis. TB biasanya menyerang paru-paru, tetapi juga dapat memengaruhi bagian tubuh lain seperti ginjal, tulang, atau otak. Penyakit ini dapat menyebar melalui udara ketika seseorang dengan TB aktif batuk atau bersin, melepaskan bakteri ke udara yang dapat dihirup oleh orang lain. \n \n Diagnosis Tuberkulosis: \n \n Tes Kulit (Mantoux atau PPD): Suntikan kecil diberikan di bawah kulit dan kemudian dilihat setelah 48-72 jam untuk menilai reaksi. Tes Darah: Mengukur keberadaan bakteri atau respons kekebalan tubuh terhadap TB. Sinar-X Dada: Untuk melihat adanya lesi atau infeksi pada paru-paru. Sputum Test: Mengidentifikasi bakteri TB dalam dahak. \n \n Pengobatan Tuberkulosis: \n \n Antibiotik: Pengobatan TB melibatkan penggunaan kombinasi antibiotik selama periode yang lama (biasanya 6 bulan atau lebih). Pengobatan Kompleks: Pasien harus mengikuti rencana pengobatan secara ketat untuk mencegah resistensi obat."
        },
    ],
    ("Mudah Lelah", "Nyeri Sendi", "Ruam Pada Kulit"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Lupus*",
            "details": "Lupus adalah penyakit autoimun di mana sistem kekebalan tubuh menyerang jaringan dan organ tubuh sendiri, menyebabkan peradangan dan kerusakan. Lupus dapat mempengaruhi berbagai bagian tubuh, termasuk kulit, sendi, ginjal, otak, jantung, dan organ-organ lainnya. \n \n Diagnosis dan Pengobatan Lupus: \n \n Diagnosis: Pemeriksaan Fisik. Riwayat Kesehatan dan Gejala. Tes Darah untuk mendeteksi antibodi yang dapat menunjukkan keberadaan lupus. Pengobatan: Obat Antiinflamasi: Untuk mengurangi peradangan dan mengatasi gejala. Obat Modifikasi Penyakit (DMARDs): Untuk mengontrol aktivitas lupus. Obat Steroid: Untuk mengurangi peradangan pada kasus yang lebih parah. Imunosupresan: Untuk menekan respons kekebalan tubuh. Manajemen Gaya Hidup: Perlindungan Matahari: Menggunakan tabir surya untuk melindungi kulit dari sinar matahari. Istirahat yang Cukup: Untuk mengatasi kelelahan. Olahraga yang Teratur: Sesuai dengan kondisi kesehatan individu. \n \n  Lupus adalah penyakit autoimun di mana sistem kekebalan tubuh menyerang jaringan dan organ tubuh sendiri, menyebabkan peradangan dan kerusakan. Lupus dapat mempengaruhi berbagai bagian tubuh, termasuk kulit, sendi, ginjal, otak, jantung, dan organ-organ lainnya. Jenis-jenis Lupus: Lupus Eritematosus Sistemik (LES): Bentuk lupus yang paling umum dan seringkali merusak berbagai bagian tubuh. Dapat mempengaruhi kulit, sendi, ginjal, jantung, paru-paru, otak, dan organ-organ lainnya. Lupus Eritematosus Diskoid (LED): Fokus utamanya adalah pada kulit. Menyebabkan lesi berbentuk cakram atau melingkar pada kulit. Lupus Neonatal: Merupakan jenis lupus yang jarang terjadi. Terjadi ketika ibu dengan lupus memiliki antibodi yang dapat menyebabkan lupus pada bayi. Gejala Lupus: Gejala lupus dapat bervariasi, dan tidak semua orang dengan lupus mengalami gejala yang sama. Beberapa gejala umum meliputi: Kelelahan yang Berlebihan: Demam: Nyeri Sendi: Rambut Rontok: Ruam Kulit: Sakit Dada dan Masalah Jantung: Masalah Ginjal: Gangguan Neurologis: Penyebab Lupus: Penyebab lupus tidak sepenuhnya diketahui, tetapi faktor-faktor berikut dapat berperan: Genetika: Ada kecenderungan genetik untuk lupus. Jika ada riwayat keluarga dengan lupus, risiko seseorang untuk mengembangkan penyakit ini dapat meningkat. Hormon: Wanita lebih mungkin terkena lupus daripada pria, dan fluktuasi hormon, terutama estrogen, dapat memainkan peran dalam perkembangan lupus. Lingkungan: Faktor lingkungan, seperti paparan sinar matahari dan infeksi, juga dapat mempengaruhi perkembangan lupus. Diagnosis dan Pengobatan Lupus: Diagnosis: Pemeriksaan Fisik. Riwayat Kesehatan dan Gejala. Tes Darah untuk mendeteksi antibodi yang dapat menunjukkan keberadaan lupus.Pengobatan: Obat Antiinflamasi: Untuk mengurangi peradangan dan mengatasi gejala. Obat Modifikasi Penyakit (DMARDs): Untuk mengontrol aktivitas lupus. Obat Steroid: Untuk mengurangi peradangan pada kasus yang lebih parah. Imunosupresan: Untuk menekan respons kekebalan tubuh. Manajemen Gaya Hidup: Perlindungan Matahari: Menggunakan tabir surya untuk melindungi kulit dari sinar matahari. Istirahat yang Cukup: Untuk mengatasi kelelahan. Olahraga yang Teratur: Sesuai dengan kondisi kesehatan individu. Penting untuk mendapatkan diagnosis dan pengobatan dari dokter, terutama dari reumatologis yang berpengalaman dalam mengelola penyakit autoimun seperti lupus. Pemantauan dan perawatan rutin sangat penting untuk mengelola gejala dan mencegah kerusakan organ jangka panjang."
        },
    ],
    ("Mudah Lelah", "Sakit Kepala", "Kulit Pucat"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Anemia*",
            "details": "Anemia adalah kondisi medis yang terjadi ketika kadar hemoglobin atau jumlah sel darah merah dalam tubuh berada di bawah batas normal. Hemoglobin adalah protein dalam sel darah merah yang membawa oksigen ke seluruh tubuh. Kurangnya hemoglobin dapat mengakibatkan kurangnya pasokan oksigen ke jaringan dan organ, menyebabkan gejala dan masalah kesehatan. \n \n Diagnosis dan Pengobatan Anemia: \n \n Diagnosis: Tes Darah: Untuk mengukur kadar hemoglobin, jumlah sel darah merah, dan parameter lainnya. Pemeriksaan Fisik: Termasuk pemeriksaan kulit, mata, dan tanda-tanda lain anemia. Pengobatan: Suplemen Besi atau Vitamin: Untuk anemia defisiensi besi atau defisiensi vitamin tertentu. Transfusi Darah: Pada kasus anemia yang parah. Pengobatan Penyebab: Jika anemia disebabkan oleh penyakit kronis atau kondisi medis lainnya. Perubahan Gaya Hidup: Diet Seimbang: Makan makanan yang kaya zat besi, vitamin B12, dan asam folat. Manajemen Kondisi Penyebab: Jika anemia disebabkan oleh kondisi medis tertentu."
        },
    ],
    ("Diare", "Sakit Kepala", "Nyeri Otot"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Malaria*",
            "details": "Malaria adalah penyakit menular yang disebabkan oleh parasit Plasmodium dan ditularkan melalui gigitan nyamuk Anopheles yang terinfeksi. Ini merupakan penyakit yang umum terjadi di daerah tropis dan subtropis di seluruh dunia, terutama di Afrika sub-Sahara, Amerika Latin, dan Asia. \n \n Diagnosis dan Pengobatan Malaria: \n \n Diagnosis: Tes Darah: Untuk mendeteksi parasit Plasmodium dalam darah. Mikroskopis: Pemeriksaan sediaan darah di bawah mikroskop untuk mengidentifikasi jenis Plasmodium. Pengobatan: Antimalaria: Berbagai obat antimalaria digunakan, dan pilihan tergantung pada jenis Plasmodium dan keparahan infeksi. Pencegahan dan Pengobatan Khusus untuk Malaria Berat: Pada kasus malaria berat, perawatan di rumah sakit mungkin diperlukan."
        },
    ],
    ("Diare", "Penurunan Berat Badan", "Tinja Berminyak"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Celiac*",
            "details": "Celiac atau celiac disease adalah penyakit autoimun yang memengaruhi saluran pencernaan, terutama usus halus, dan disebabkan oleh reaksi negatif terhadap gluten. Gluten adalah protein yang ditemukan dalam gandum, barley, dan rye. Pada individu dengan celiac disease, konsumsi gluten menyebabkan kerusakan pada lapisan usus halus dan interferensi dengan penyerapan nutrisi. \n \n Diagnosis dan Pengobatan Celiac: \n \n Diagnosis: Tes Darah: Untuk mendeteksi antibodi terkait celiac. Biopsi Usus Halus: Dilakukan melalui endoskopi untuk memeriksa kerusakan pada lapisan usus halus. Pengobatan: Diet Bebas Gluten: Langkah utama pengobatan adalah menghindari gluten sepenuhnya dalam diet. Suplemen Nutrisi: Jika ada defisiensi nutrisi."
        },
    ],
    ("Diare", "Nyeri Perut", "Mudah Marah"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Penyakit Addison*",
            "details": "Penyakit Addison, juga dikenal sebagai insufisiensi korteks adrenal primer, adalah kondisi medis yang terjadi ketika kelenjar adrenal tidak dapat memproduksi cukup hormon kortisol dan kadang-kadang hormon aldosteron. Kelenjar adrenal adalah dua kelenjar kecil yang terletak di atas ginjal dan memainkan peran penting dalam mengatur berbagai fungsi tubuh.\n \n Diagnosis dan Pengobatan Penyakit Addison: \n \n Diagnosis: Tes Darah: Untuk mengukur kadar hormon kortisol dan aldosteron. Uji Stimulasi ACTH: Untuk mengukur respons kelenjar adrenal terhadap hormon ACTH yang merangsang produksi kortisol. Pengobatan: Terapi Hormon Pengganti: Pemberian kortisol dan aldosteron untuk menggantikan kekurangan hormon.Pengobatan Penyebab: Jika penyebabnya adalah infeksi atau penyakit tertentu.Manajemen Gaya Hidup: Diet tinggi garam untuk mengatasi kekurangan aldosteron."
        },
    ],
    ("Diare", "Bau Mulut", "Sulit Buang Gas"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Penyakit Ileus*",
            "details": "Ileus adalah kondisi di mana pergerakan normal usus terhambat atau terhenti. Ini dapat terjadi pada bagian saluran pencernaan, seperti usus halus atau usus besar. Ileus dapat bersifat sementara (fungsional) atau bersifat obstruktif (strukturnya terhalang). \n \n Diagnosis dan Pengobatan Ileus: \n \n Diagnosis: Pemeriksaan Fisik: Menilai gejala dan tanda-tanda ileus.Pemeriksaan Gambaran: Melalui X-ray atau CT scan untuk melihat obstruksi atau perubahan pada usus. Pengobatan: Manajemen Cairan: Untuk menggantikan kehilangan cairan dan elektrolit. Nasogastric (NG) Tube: Untuk mengeluarkan gas dan cairan dari usus dan mengurangi distensi abdomen. Obat-obatan: Dapat mencakup obat anti-mual, analgesik, atau obat yang merangsang aktivitas usus. Manajemen Penyebab: Jika ileus disebabkan oleh kondisi tertentu, seperti adhesi atau tumor."
        },
    ],
    ("Demam", "Nyeri Sendi", "Hilang Nafsu Makan"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Artritis Reumatoid*",
            "details": "Artritis Reumatoid (AR) adalah penyakit autoimun yang menyerang sendi dan jaringan di sekitarnya. Pada AR, sistem kekebalan tubuh menyerang secara keliru jaringan sendi, menyebabkan peradangan yang dapat merusak sendi seiring waktu. Ini adalah penyakit kronis yang sering mempengaruhi sendi simetris, artinya jika satu sendi terkena, kemungkinan besar sendi sebelahnya juga akan terpengaruh. \n \n Diagnosis dan Pengobatan Artritis Reumatoid: \n \n Diagnosis: Pemeriksaan Fisik dan Riwayat Kesehatan: Untuk menilai gejala dan tanda-tanda AR. Pemeriksaan Darah: Untuk mendeteksi faktor reumatoid dan tanda-tanda peradangan. Gambaran Radiologi: Untuk mengevaluasi kerusakan sendi. Pengobatan: Obat Antiinflamasi Nonsteroid (NSAID): Untuk mengurangi peradangan dan nyeri. Obat Modifikasi Penyakit (DMARDs): Untuk menghentikan atau memperlambat kerusakan sendi. Steroid: Untuk mengurangi peradangan. Fisioterapi dan Latihan: Untuk mempertahankan fleksibilitas dan kekuatan sendi. Manajemen Gaya Hidup: Perawatan nutrisi, olahraga, dan istirahat yang cukup."
        },
    ],
    ("Demam", "Sakit Tenggorokan", "Bersin-Bersin"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Influenza*",
            "details": "Influenza, yang umumnya dikenal sebagai flu, adalah infeksi virus pernapasan yang disebabkan oleh virus influenza. Flu dapat menyebabkan gejala ringan hingga parah, dan pada beberapa kasus, dapat berujung pada komplikasi serius.  \n \n Penyebaran dan Pencegahan: Flu menyebar melalui tetesan kecil yang keluar dari hidung dan mulut orang yang terinfeksi saat mereka batuk, bersin, atau berbicara. Penyebaran juga dapat terjadi melalui menyentuh permukaan yang terkontaminasi oleh virus dan kemudian menyentuh wajah, terutama hidung atau mulut. Langkah-langkah pencegahan termasuk: Vaksinasi: Vaksinasi tahunan adalah metode pencegahan utama dan sangat dianjurkan, terutama bagi kelompok risiko tinggi. Cuci Tangan: Mencuci tangan secara teratur dengan sabun dan air mengurangi risiko penularan. Menjaga Jarak: Hindari kontak dekat dengan orang yang sakit. Menutup Hidung dan Mulut: Tutup hidung dan mulut Anda dengan tisu atau siku Anda saat batuk atau bersin. Menjaga Kebersihan Lingkungan: Bersihkan permukaan yang sering disentuh, seperti gagang pintu dan sakelar lampu. Pengobatan: Istirahat dan Hidrasi: Istirahat yang cukup dan minum banyak cairan membantu tubuh untuk pulih. Obat Simtomatik: Obat-obatan bebas seperti parasetamol atau ibuprofen dapat membantu meredakan gejala seperti demam dan nyeri.Antivirus: Beberapa obat antivirus tertentu dapat diresepkan oleh dokter untuk mengurangi durasi dan keparahan gejala flu pada beberapa kasus. Penting untuk mencari perhatian medis jika Anda mengalami gejala flu yang parah, terutama jika Anda termasuk dalam kelompok risiko tinggi seperti anak-anak kecil, orang tua, atau individu dengan kondisi kesehatan yang melemahkan."
        },
    ],
    ("Demam", "Benjolan di Punggung", "Punggung Bungkuk"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Spondilitis TB*",
            "details": "Spondilitis tuberkulosis (TB) adalah kondisi yang melibatkan peradangan tulang belakang (vertebrae) akibat infeksi Mycobacterium tuberculosis. TB adalah infeksi bakteri yang dapat menyerang berbagai bagian tubuh, termasuk paru-paru, tulang belakang, dan bagian lain dari sistem muskuloskeletal. \n \n Diagnosis dan Pengobatan Spondilitis TB: \n \n Diagnosis: Pemeriksaan Imajinologi: Seperti sinar-X, CT scan, atau MRI untuk melihat perubahan pada tulang belakang. Tes Laboratorium: Tes darah dan tes tuberkulin untuk mendeteksi adanya infeksi tuberkulosis. Pengobatan: Terapi Antibiotik: Pengobatan TB yang umumnya melibatkan penggunaan antibiotik, seperti isoniazid, rifampicin, ethambutol, dan pyrazinamide. Terapi ini biasanya berlangsung untuk jangka waktu yang cukup lama, seringkali beberapa bulan hingga lebih dari setahun. Pembedahan: Pada beberapa kasus, terutama jika ada risiko kerusakan tulang belakang yang signifikan atau kompresi pada saraf, pembedahan mungkin diperlukan. Pembedahan dapat melibatkan pengangkatan materi yang terinfeksi atau fusi tulang untuk memperkuat dan menstabilkan tulang belakang. Pemulihan dan Rehabilitasi: Setelah pengobatan dan pembedahan, rehabilitasi fisik dapat membantu meningkatkan kekuatan otot dan fleksibilitas serta mengembalikan fungsi normal."
        },
    ],
    ("Batuk", "Sakit Tenggorokan", "Tenggorokan Kering"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Laringitis*",
            "details": "Laringitis adalah peradangan pada laring atau pita suara, yang merupakan bagian dari saluran pernapasan atas. Kondisi ini seringkali disebabkan oleh infeksi virus, tetapi dapat juga disebabkan oleh iritasi atau cedera pada pita suara.\n \n Diagnosis dan Pengobatan Laringitis: \n \n Diagnosis: Pemeriksaan Fisik: Dokter dapat memeriksa tenggorokan dan pita suara. Anamnesis: Dokter akan bertanya tentang gejala dan faktor-faktor pemicu. Pengobatan: Istirahat Suara: Memberikan istirahat pada pita suara dengan menghindari berbicara terlalu keras atau bernyanyi. Minum Cairan yang Banyak: Meningkatkan asupan cairan untuk menjaga kelembapan pada pita suara. Obat Pereda Nyeri dan Batuk: Menggunakan obat pereda nyeri atau sirup batuk yang direkomendasikan oleh dokter. Penghindaran Pemicu: Menghindari paparan asap rokok dan zat iritan lainnya. Pemulihan Alami: Laringitis umumnya akan pulih dengan sendirinya dalam beberapa hari sampai beberapa minggu. Pertimbangan Antibiotik: Jika laringitis disebabkan oleh infeksi bakteri, dokter dapat meresepkan antibiotik."
        },
    ],
    ("Batuk", "Bersin", "Ruam Pada Kulit"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Alergi Imunologi*",
            "details": "Alergi imunologi adalah respons sistem kekebalan tubuh yang tidak tepat atau berlebihan terhadap zat yang seharusnya tidak menyebabkan reaksi pada kebanyakan orang. Zat yang menyebabkan reaksi alergi disebut alergen. Reaksi alergi dapat melibatkan berbagai organ dan jaringan dalam tubuh dan dapat berkisar dari ringan hingga parah.\n \n Diagnosis dan Pengobatan Alergi Imunologi: \n \n Diagnosis: Tes Kulit: Untuk mengidentifikasi alergen yang menyebabkan reaksi. Tes Darah: Misalnya, tes RAST atau uji imunoglobulin E (IgE) untuk mengukur tingkat antibodi alergi dalam darah. Pengobatan: Antihistamin: Mengurangi gejala gatal, bersin, dan hidung berair. Bronkodilator: Digunakan untuk mengatasi gejala asma. Epinefrin: Untuk penanganan darurat anafilaksis. Imunoterapi: Terapi desensitisasi untuk membangun toleransi terhadap alergen. Pencegahan: Menghindari kontak dengan alergen dapat membantu mencegah reaksi alergi."
        },
    ],
    ("Nyeri Perut", "Penurunan Berat Badan", "Nyeri Panggul"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Kista Ovarium*",
            "details": "Kista ovarium adalah kantong cairan yang berkembang di dalam atau di sekitar ovarium, organ reproduksi wanita yang menghasilkan telur dan hormon. Kista ovarium bisa bersifat jinak (non-kanker) atau bersifat ganas (kanker), dan seringkali mereka tidak menimbulkan gejala dan terdeteksi secara kebetulan selama pemeriksaan rutin atau pemeriksaan lainnya. \n \n Diagnosis dan Pengobatan Kista Ovarium: \n \n Diagnosis: Pemeriksaan Fisik dan Riwayat Kesehatan: Dokter akan melakukan pemeriksaan fisik dan bertanya tentang gejala yang dialami. Pemeriksaan Imajinologi: Seperti ultrasonografi, CT scan, atau MRI untuk melihat gambaran ovarium. Pengobatan: Pemantauan: Kista kecil yang tidak menimbulkan gejala seringkali hanya diamati. Obat-obatan: Dapat diresepkan untuk mengatasi gejala atau mengendalikan pertumbuhan kista. Pembedahan: Diperlukan jika kista besar, mengganggu fungsi ovarium, atau berpotensi bersifat ganas"
        },
    ],
    ("Nyeri Perut", "Infeksi Saluran Kemih", "Mudah Memar"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Ginjal Polikistik*",
            "details": "Penyakit Ginjal Polikistik (Polycystic Kidney Disease atau PKD) adalah kelainan genetik yang ditandai oleh pertumbuhan kantong-kantong cairan (kista) di dalam ginjal. Kista-kista ini dapat berkembang seiring waktu dan menyebabkan pembesaran dan kerusakan ginjal. \n \n Diagnosis dan Pengobatan Ginjal Polikistik: \n \n Diagnosis: Pemeriksaan Imajinologi: CT scan atau MRI untuk melihat gambaran ginjal dan kista. Tes Darah dan Urine: Untuk menilai fungsi ginjal dan mendeteksi tanda-tanda komplikasi. Pengobatan: Manajemen Hipertensi: Untuk mengendalikan tekanan darah. Pemantauan dan Perawatan Komplikasi: Mengatasi masalah yang muncul, seperti infeksi atau perdarahan dalam kista. Pemantauan Rutin: Terutama bagi individu dengan risiko tinggi atau yang memiliki riwayat keluarga dengan PKD. Dialisis dan Transplantasi Ginjal: Diperlukan pada tahap lanjut ketika fungsi ginjal sangat terpengaruh."
        },
    ],
    ("Mata Merah", "Pandangan Kabur", "Selaput Pterigium Menebal"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Pterigium*",
            "details": "Pterigium adalah pertumbuhan jaringan membran mukosa yang abnormal yang dapat muncul di permukaan mata. Ini biasanya tumbuh dari bagian putih mata (sklera) ke arah kornea, yang merupakan lapisan jernih di bagian depan mata. Pterigium dapat muncul pada satu atau kedua mata, dan meskipun pertumbuhannya bersifat jinak, dapat menyebabkan beberapa gejala dan gangguan visual. \n \n Pengobatan Pterigium: \n \n Obat Tetes Mata: Dokter dapat meresepkan tetes mata untuk mengurangi iritasi dan peradangan. Tindakan Pembedahan: Pilihan utama pengobatan adalah pembedahan jika pterigium menyebabkan gejala yang parah atau mengganggu penglihatan. Prosedur pembedahan dapat melibatkan pengangkatan pterigium dan transplantasi jaringan dari bagian putih mata yang tidak terkena (konjungtiva). Pencegahan: Melindungi mata dari paparan sinar matahari dengan menggunakan kacamata hitam yang memberikan perlindungan UV. Menggunakan pelindung mata saat berada di lingkungan berdebu atau berangin."
        },
    ],
    ("Mata Merah", "Pandangan Kabur", "Mata Bengkak"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Keratitis*",
            "details": "Keratitis adalah peradangan pada kornea, yang merupakan lapisan transparan yang melindungi bagian depan mata dan membantu fokus cahaya ke dalam mata. Keratitis dapat disebabkan oleh berbagai faktor, termasuk infeksi, cedera, atau reaksi alergi. Keratitis dapat mempengaruhi penglihatan dan memerlukan perawatan medis segera. \n \n Pengobatan Keratitis: \n \n Obat Tetes Mata Antibiotik atau Antivirus: Bergantung pada penyebabnya, dokter dapat meresepkan tetes mata antibiotik atau antivirus. Obat Pereda Nyeri: Obat pereda nyeri dapat diberikan untuk meredakan gejala nyeri. Obat Antiinflamasi: Obat antiinflamasi dapat membantu mengurangi peradangan. Pemakaian Lensa Kontak dan Lensa Mata: Penggunaan lensa kontak atau lensa mata dapat dilarang selama pengobatan untuk memberikan kesempatan mata untuk pulih. Pembedahan: Pada beberapa kasus yang parah, pembedahan mungkin diperlukan, seperti transplantasi kornea."
        },
    ],
    ("Gangguan Penglihatan", "Sensitif Cahaya", "Penglihatan Ganda"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Katarak*",
            "details": "Katarak adalah kondisi di mana lensa mata yang biasanya jernih menjadi keruh, menyebabkan penglihatan menjadi kabur atau buram. Katarak umumnya terjadi akibat penuaan alami, tetapi faktor-faktor seperti cedera mata, penyakit tertentu, atau penggunaan obat tertentu juga dapat memicu perkembangan katarak. \n \n Pengobatan Katarak: \n \n Pembedahan Katarak: Pembedahan katarak adalah satu-satunya metode pengobatan yang efektif untuk mengatasi katarak yang signifikan. Pada prosedur ini, lensa mata yang keruh diangkat dan diganti dengan lensa buatan (implan intraokular). Perawatan Awal: Pada tahap awal, penggunaan kacamata atau penyesuaian resep kacamata mungkin membantu meningkatkan penglihatan."
        },
    ],
    ("Nyeri Otot", "Penurunan Berat Badan", "Mudah Kepanasan"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Hipertiroidisme*",
            "details": "Hipertiroidisme adalah kondisi medis yang terjadi ketika kelenjar tiroid menghasilkan terlalu banyak hormon tiroid. Hormon tiroid, yang disebut tiroksin (T4) dan triiodotironin (T3), mengatur berbagai fungsi tubuh, termasuk tingkat metabolisme. Jika terlalu banyak hormon tiroid dihasilkan, itu dapat mempengaruhi banyak sistem dalam tubuh.\n \n Diagnosis dan Pengobatan Hipertiroidisme: \n \n Diagnosis: Pemeriksaan Darah: Untuk mengukur tingkat hormon tiroid (T3 dan T4) dan hormon stimulasi tiroid (TSH). Pemeriksaan Gambaran: Seperti pemeriksaan ultrasonografi tiroid atau scintigrafi tiroid. Pengobatan: Obat Anti-Tiroid: Untuk menghambat produksi hormon tiroid. Terapi Radioaktif: Menggunakan yodium radioaktif untuk menghancurkan sebagian kelenjar tiroid. Pembedahan: Pengangkatan sebagian atau seluruh kelenjar tiroid (tiroidectomy)."
        },
    ],
    ("Kesemutan", "Rentan Sakit", "Nyeri Tulang"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Mieloma Multipel*",
            "details": "Mieloma multipel adalah jenis kanker darah yang berasal dari sel plasma, jenis sel darah putih yang bertanggung jawab untuk memproduksi antibodi. Mieloma multipel ditandai oleh pertumbuhan tidak terkontrol dari sel plasma di sumsum tulang, yang dapat menyebabkan kerusakan pada tulang dan menghasilkan protein yang merugikan organ dan jaringan.\n \n Diagnosis Mieloma Multipel: \n \n Pemeriksaan Darah: Melibatkan pemeriksaan jumlah sel darah, elektrolit, dan protein dalam darah. Tes Urine: Untuk mendeteksi protein abnormal yang mungkin dihasilkan oleh sel plasma. Biopsi Sumsum Tulang: Pengambilan sampel dari sumsum tulang untuk menilai jumlah dan bentuk sel plasma. Pemindaian Tulang: Untuk mendeteksi kerusakan atau lesi pada tulang. \n \n Pengobatan Mieloma Multipel: \n \n Terapi Obat: Penggunaan obat-obatan seperti imunomodulator, steroid, dan inhibitor proteasom untuk menghentikan pertumbuhan sel kanker. Terapi Sel Punca: Transplantasi sel punca dapat digunakan untuk menggantikan sumsum tulang yang rusak dengan sumsum tulang yang sehat. Terapi Radiasi: Untuk mengobati area spesifik yang mungkin terkena. Pengelolaan Gejala dan Komplikasi: Perawatan suportif seperti pengobatan nyeri, manajemen infeksi, dan penanganan komplikasi lainnya."
        },
    ],
    ("Mata Menguning", "Pendarahan Usus", "Pembesaran Limpa"): [
        {
            "message": "*Kemungkinan anda mengalami gejala Hati Alkoholik*",
            "details": "Hati alkoholik, atau hepatopati alkoholik, adalah kondisi yang terjadi akibat konsumsi alkohol yang berlebihan dan berkepanjangan. Konsumsi alkohol yang tinggi dapat menyebabkan kerusakan serius pada hati, dan hati alkoholik dapat berkembang menjadi penyakit hati yang lebih serius seperti sirosis hati. \n \n Diagnosis dan Pengobatan Hati Alkoholik: \n \n Diagnosis: Tes Darah: Untuk mengukur tingkat enzim hati dan fungsi hati. Pemeriksaan Citra: Seperti ultrasound atau CT scan untuk menilai kondisi hati. Biopsi Hati: Pengambilan sampel jaringan hati untuk menilai sejauh mana kerusakan. Pengobatan: Berhenti Minum Alkohol: Langkah terpenting adalah menghentikan konsumsi alkohol sepenuhnya. Manajemen Komplikasi: Pengobatan dapat melibatkan manajemen komplikasi seperti asites, perdarahan, atau disfungsi hati lainnya. Perubahan Gaya Hidup dan Nutrisi: Diet seimbang dan penghindaran faktor risiko lainnya."
        },
    ]
}


if 'login' not in st.session_state:
    st.session_state.login = False

if st.session_state.login:
    class HealthCheckerApp:
        def __init__(self, data, output_data):
            self.data = data
            self.output_data = output_data
            self.is_clicked = False
            self.selected_data = []

        def selectData(self):
            st.title('Silahkan Pilih Gejala yang Anda Rasakan Untuk Mendeteksi Jenis Penyakit')

            if not self.is_clicked:
                self.selected_data = []
                
            if not hasattr(st.session_state, 'is_clicked'):
                st.session_state.is_clicked = False

            if not hasattr(st.session_state, 'data'):
                st.session_state.data = []
        
            st.session_state.q1 = st.multiselect("Gejala apa yang anda rasakan ?", list(self.data.keys()))
            if len(st.session_state.data) == 0:
                st.session_state.data.extend(st.session_state.q1)

            if st.session_state.q1:
                st.session_state.q2 = st.multiselect(f"Gejala apa yang anda rasakan setelah {st.session_state.q1[0]}", list(self.data[st.session_state.q1[0]].keys()))
                if len(st.session_state.data) == 1:
                    st.session_state.data.extend(st.session_state.q2)

                if st.session_state.q2:
                    st.session_state.q3 = st.multiselect(f"Gejala apa yang anda rasakan setelah {st.session_state.q2[0]}", self.data[st.session_state.q1[0]][st.session_state.q2[0]])
                    if len(st.session_state.data) == 2:
                        st.session_state.data.extend(st.session_state.q3)

        def display(self):
            col1, col2, col3 = st.columns(3)

            count = 0
            if col1.button("Select"):
                self.is_clicked = True
            

            if st.button("Tampilkan Penyakit"):
                selected = tuple(st.session_state.data)

            if col3.button("Reset"):
                st.session_state.data.clear()
                
                if selected in self.output_data:
                    for output in self.output_data[selected]:
                        count += 1
                        st.warning(f"{count}. *{output['message']}*")
                        st.warning(f"{output['details']}")
                else:
                    st.warning("Tidak ada informasi terkait data yang dipilih.")

        def run(self):
            self.selectData()
            self.display()


    health_checker_app = HealthCheckerApp(Data, OutputData)
    health_checker_app.run()
else:
    st.title("Anda Harus Login Terlebih Dahulu !!!")