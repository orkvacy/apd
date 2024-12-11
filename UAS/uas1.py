
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prettytable import PrettyTable


# 1. Membaca dataset
gymDF = pd.read_csv('gym_membership.csv')

# 2. Menampilkan deskripsi data
def descData():
    print("===== Deskripsi Data =====")
    tabeldesc = PrettyTable()
    tabeldesc.field_names = ["Kolom"] + list(gymDF.describe().columns)
    for index, row in gymDF.describe().iterrows():
        tabeldesc.add_row([index] + row.tolist())
    print(tabeldesc)
    
    infoTable = PrettyTable()
    infoTable.field_names = ["Kolom", "Tipe Data", "Jumlah Non-Null"]
    for column, dtype in gymDF.dtypes.items():
        kosong = gymDF[column].isna().sum()
        infoTable.add_row([column, dtype, kosong])
    print("\nInformasi kolom:")
    print(infoTable)
    input("Tekan enter untuk melanjutkan")

def head():
    print("===== 10 Data Pertama =====")
    headTable = PrettyTable()
    headTable.field_names = ["ID", "Umur", "Gender", "Tipe Membership", "Check-in", "Check-out", "Waktu di Gym"]
    for i, row in gymDF.head(10).iterrows():
        headTable.add_row([row['id'], row['Age'], row['gender'], row['abonoment_type'],
                            row['avg_time_check_in'], row['avg_time_check_out'], row['avg_time_in_gym']])
    print(headTable)
    input("Tekan enter untuk melanjutkan")

# 4. Mengurutkan dan menampilkan data
def longest():
    print("===== Data Terurut Berdasarkan Waktu di Gym (Top 10) =====")
    sortingGymDF = gymDF.sort_values('avg_time_in_gym', ascending=False).head(10)
    longestTable = PrettyTable()
    longestTable.field_names = ["ID", "Umur", "Gender", "Waktu di Gym"]
    for idx, row in sortingGymDF.iterrows():
        longestTable.add_row([row['id'], row['Age'], row['gender'], row['avg_time_in_gym']])
    print(longestTable)
    input("Tekan enter untuk melanjutkan")

# 5. Menampilkan jumlah data yang kosong
def na():
    print("===== Jumlah Data Kosong per Kolom =====")
    naTable = PrettyTable()
    naTable.field_names = ["Kolom", "Jumlah Data Kosong"]
    missing = gymDF.isna().sum()
    for column, count in missing.items():
        naTable.add_row([column, count])
    print(naTable)
    input("Tekan enter untuk melanjutkan")

def visualisas():
    print("===== Analisis Berdasarkan Kategori Umur =====")
    gymDF['age_category'] = gymDF['Age'].apply(lambda x: '1-18 tahun' if x <= 18 else '18+ tahun')

    umurr = gymDF.groupby('age_category').agg({
        'id': 'count',
        'avg_time_in_gym': ['mean', 'min', 'max']
    }).round(2)

    print("Statistik per kategori umur:")
    for category in umurr.index:
        print(f"\nKategori: {category}")
        print(f"Jumlah member: {umurr.loc[category, ('id', 'count')]} orang")
        print(f"Rata-rata waktu: {umurr.loc[category, ('avg_time_in_gym', 'mean')]} menit")
        print(f"Waktu minimum: {umurr.loc[category, ('avg_time_in_gym', 'min')]} menit")
        print(f"Waktu maksimum: {umurr.loc[category, ('avg_time_in_gym', 'max')]} menit")

    gymDF['age_category'] = gymDF['Age'].apply(lambda x: '1-18 tahun' if x <= 18 else '18+ tahun')

    # Waktu di gym berdasarkan kategori umur dan gender
    plt.figure(figsize=(10, 5))
    sns.boxplot(x='age_category', y='avg_time_in_gym', hue='gender', data=gymDF)
    plt.title('Distribusi Waktu di Gym Berdasarkan Umur dan Gender')
    plt.xlabel('Kategori Umur')
    plt.ylabel('Waktu di Gym (menit)')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    print("\n===== Statistik Waktu Gym Berdasarkan Umur =====")
    stats = gymDF.groupby('age_category')['avg_time_in_gym'].agg(['count', 'mean', 'min', 'max'])
    stats = stats.round(2)
    print(stats)

    # Histogram
    plt.figure(figsize=(15, 7))
    sns.histplot(gymDF['Age'], kde=True, bins=20, color='skyblue')
    plt.title('Distribusi member gym berdasarkan umur', fontsize=17)
    plt.xlabel('Umur', fontsize=13)
    plt.ylabel('Frekuensi', fontsize=13)
    plt.show()

    # Perbandingan dalam Kelompok Umur 1-18 dan 18+
    filterUmur = gymDF.groupby(['age_category', 'abonoment_type']).size().unstack().fillna(0)
    print("\n===== Perbandingan Membership dalam Kelompok Umur =====")
    print(filterUmur)
    filterUmur.T.plot(kind='bar', figsize=(10, 6))
    plt.title('Perbandingan Membership dalam Kelompok Umur')
    plt.xlabel('Tipe Membership')
    plt.ylabel('Jumlah Membership')
    plt.xticks(rotation=0)
    plt.legend(title='Kelompok Umur')
    plt.tight_layout()
    plt.show()


    plt.figure(figsize=(10, 6))
    sns.boxplot(data=gymDF[gymDF['personal_training'] == True], x='gender', y='Age', showfliers=False)
    plt.title('Perbandingan Gender yang Melakukan Personal Training')
    plt.ylabel('Usia')
    plt.xlabel('Gender')
    plt.tight_layout()
    plt.show()

    filterData = gymDF[gymDF['personal_training'] == True]
    filterData = filterData[['gender', 'Age', 'age_category', 'personal_training']]

    plt.figure(figsize=(10, 6))

    sns.boxplot(data=filterData, x='age_category', y='Age', hue='gender', showfliers=False)



    plt.title('Perbandingan Laki-Laki dan Perempuan Menggunakan Personal Trainer\n (1-18 Tahun dan 18+ Tahun)')
    plt.ylabel('Usia')
    plt.xlabel('Kelompok Usia')
    plt.legend(title='Gender')
    plt.show()
    plt.show(block=True) #membuat program akan menunggu sampai grafik di tutup oleh pengguna