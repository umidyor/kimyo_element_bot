from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent.parent

def clean_data(df):
    df['Turi'] = df['Turi'].fillna("No'malum")
    df['boil'] = df['boil'].fillna("No'malum")
    df['Turi'] = df['Turi'].str.replace('colorless gas', 'rangsiz gaz').str.replace(
        'exhibiting a red-orange glow when placed in a high-voltage electric field',
        "yuqori kuchlanishli elektr maydoniga joylashtirilganda qizil-to'q sariq rangdagi porlashni namoyish etadi")
    df['Turi'] = df['Turi'].str.replace('silvery-white', 'oq kumushsimon').str.replace('white-gray metallic',
                                                                                       "oq-kulrang metall").str.replace(
        'black-brown', 'qora-jigarrang').str.replace('liquid or solid', 'suyuq yoki qattiq').str.replace(
        'exhibiting an orange-red glow when placed in a high voltage electric field',
        "yuqori kuchlanishli elektr maydoniga joylashtirilganda to'q sariq-qizil nurni namoyon qiladi")
    df['Turi'] = df['Turi'].str.replace('silvery white metallic', "kumush oq metall").str.replace('shiny grey solid',
                                                                                                  "porloq kulrang qattiq").str.replace(
        'silvery gray metallic', "kumush kulrang metall").str.replace(
        'crystalline, reflective with bluish-tinged faces',
        "kristalli, ko'k rangli yuzlar bilan aks ettiruvchi").str.replace(
        'colourless, waxy white, yellow, scarlet, red, violet, black',
        "rangsiz, mumsimon oq, sariq, qizil, qizil, binafsha, qora")
    df['Turi'] = df['Turi'].str.replace('lemon yellow sintered microcrystals',
                                        "limon sariq sinterlangan mikrokristallar").str.replace(
        'exhibiting a lilac/violet glow when placed in a high voltage electric field',
        "yuqori kuchlanishli elektr maydoniga joylashtirilganida lilak/binafsha rang porlashni namoyon qiladi").str.replace(
        'silvery gray', "kumushsimon kulrang").str.replace('silvery white', 'kumushsimon oq').str.replace(
        'silvery grey-white metallic', "kumush kulrang-oq metall").str.replace('blue-silver-grey metal',
                                                                               "ko'k-kumush-kulrang metall").str.replace(
        'silvery metallic', "kumushsimon metall")
    df['Turi'] = df['Turi'].str.replace('lustrous metallic with a grayish tinge',
                                        "kulrang tusli yorqin metall").str.replace('hard lustrous gray metal',
                                                                                   "qattiq yorqin kulrang metall")
    df['Turi'] = df['Turi'].str.replace('lustrous, metallic, and silver with a gold tinge',
                                        "oltin tusli yorqin, metall va kumush").str.replace(
        'red-orange metallic luster', "qizil-to'q sariq rangli metall yorqinlik").str.replace('silver-gray',
                                                                                              "kumush-kulrang").str.replace(
        'silver-white', "kumush-oq").str.replace('grayish-white', "kulrang-oq").str.replace('metallic grey',
                                                                                            "metall kulrang").str.replace(
        'black, red, and gray (not pictured) allotropes',
        "qora, qizil va kulrang (rasmda yo'q) allotroplar").str.replace(
        'exhibiting a whitish glow in a high electric field',
        "yuqori elektr maydonida oq rangli porlashni namoyon qiladi").str.replace('grey white',
                                                                                  "kulrang oq").str.replace(
        'gray metallic, bluish when oxidized', "kulrang metall, oksidlanganda mavimsi").str.replace('gray metallic',
                                                                                                    "kulrang metall")
    df['Turi'] = df['Turi'].str.replace('silvery bluish-kulrang metall', "kumush mavimsi-kulrang metall").str.replace(
        'silvery lustrous gray', "kumush yorqin kulrang").str.replace('oq kumushsimon (beta, β) or gray (alpha, α)',
                                                                      'oq kumushsimon (beta, b) yoki kulrang (alfa, a)').str.replace(
        'lustrous metallic gray, violet as a gas', "Yaltiroq metall kulrang, gaz kabi binafsha rang").str.replace(
        'exhibiting a blue glow when placed in a high voltage electric field',
        "yuqori kuchlanishli elektr maydoniga joylashtirilganida ko'k porlashni namoyon qiladi").str.replace(
        'silvery gold', "kumush oltin").str.replace('grayish white', "kulrang oq").str.replace('metallic',
                                                                                               "metall").str.replace(
        'steel gray', "po'lat kulrang").str.replace('gray blue', "kulrang ko'k").str.replace('lustrous',
                                                                                             'yaltiroq').str.replace(
        'silvery-grayish', "kumush-kulrang").str.replace('silvery, blue cast', "kumush, ko'k rangli quyma")
    df['Turi'] = df['Turi'].str.replace('yellow', "sariq").str.replace('silvery', "kumushsimon").str.replace(
        'metall gray', "metall kulrang").str.replace('silver', 'kumush').str.replace('unknown, probably metall',
                                                                                     "noma'lum, ehtimol metall").str.replace(
        'occasionally glows green or red in discharge tubes',
        "tushirish quvurlarida vaqti-vaqti bilan yashil yoki qizil yonadi").str.replace("often with black tarnish",
                                                                                        "ko'pincha qora dog'lar bilan").str.replace(
        'bright, kumushsimon metall luster', "yorqin, kumushsimon metall yorqinligi").str.replace(
        'kumushsimon oq, tarnishing to dark gray in air',
        "kumushsimon oq, havoda to'q kulrang rangga bo'yalgan").str.replace(
        'kumushsimon metall, glows purple in the dark',
        "kumushsimon metall, qorong'uda binafsha rangda porlaydi").str.replace('kumushsimon-colored',
                                                                               "kumushsimon rangli")
    df['category'] = df['category'].str.replace('diatomic nonmetal', "diatomik bo'lmagan metall").str.replace(
        'noble gas', "nobil gaz").str.replace('alkali metal', "ishqoriy metall").str.replace('alkaline earth metal',
                                                                                             "ishqoriy tuproq metall").str.replace(
        'metalloid', "metalloid").str.replace('polyatomic nonmetal', "ko'p atomli metall bo'lmagan").str.replace(
        'post-transition metal', "o'tishdan keyingi metall").str.replace('transition metal',
                                                                         "o'tish metalli").str.replace('lanthanide',
                                                                                                       "lantanoid").str.replace(
        'actinide', "aktinoid")
    df['category'] = df['category'].str.replace('unknown, probably transition metal',
                                                "noma'lum, ehtimol o'tish metali").str.replace(
        'unknown, probably post-transition metal', "noma'lum, ehtimol o'tishdan keyingi metall").str.replace(
        'unknown, probably metalloid', "noma'lum, ehtimol metalloid").str.replace('unknown, predicted to be noble gas',
                                                                                  "noma'lum, nobel gaz bo'lishi taxmin qilingan").str.replace(
        'unknown, but predicted to be an alkali metal', "noma'lum, ammo ishqoriy metal bo'lishi taxmin qilingan")
    df['phase'] = df['phase'].str.replace('Gas', 'Gaz').str.replace('Solid', 'Qattiq').str.replace('Liquid', 'Suyuq')
    return df


def search_data(name, lang):
    name = name.strip().capitalize()
    if lang == 'uz':
        data = pd.read_csv(f'{BASE_DIR}/data/main_data.csv')
        df = clean_data(data)
        if name in df["Element"].unique():
            try:
                y = df[df['Element'] == f'{name}'].reset_index(drop=True)
                return f"✅Element: {name}\nFormulasi: {y['symbol'].values[0]}\n✅Turi: {y['Turi'].values[0]}\n✅Oilasi: {y['block'].values[0]}\n✅Atom massasi: {y['atom_mass'].values[0]}\n✅Qaynash nuqtasi: {y['boil'].values[0]} °C\n✅Kategoriyasi: {y['category'].values[0]}\n✅Yaratuvchisi: {y['discovered_by'].values[0]}\n✅Erish nuqtasi: {y['melt'].values[0]} °C\n✅Molyar issiqlik: {y['molar_heat'].values[0]}\n✅Kimning sharafiga: {y['named_by'].values[0]}\n✅Tartib raqami: {y['number'].values[0]}\n✅Davri: {y['period'][0]}\n✅Guruhi: {y['group'].values[0]}\n✅Agregat holati: {y['phase'].values[0]}\n✅Elektron qavatlari: {y['shells'].values[0]}\n✅Elektron konfiguratsiyasi: {y['electron_configuration'].values[0]}\n✅Semantik elektron konfiguratsiyasi: {y['electron_configuration_semantic'].values[0]}\n✅Elektronga yaqinlik: {y['electron_affinity'].values[0]}\n✅Elektromanfiyligi: {y['electronegativity_pauling'].values[0]}\n✅Ionlanish energiyasi: {y['ionization_energies'].values[0]}\n✅CPK-Hex: {y['cpk-hex'].values[0]}\n✅Qo'shimcha manba: {y['source'].values[0]}\n✅Elektron joylashuvi: {y['bohr_model_image'].values[0]}\n✅3D elektron joylashuvi: {y['bohr_model_3d'].values[0]}\n✅Spektral rasmi: {y['spectral_img'].values[0]}\n✅Element aniq rasmi: {y['image.url'].values[0]}\n"
            except IndexError as index:
                raise index
        elif name in df["symbol"].unique():
            try:
                y = df[df['symbol'] == f'{name}'].reset_index(drop=True)
                return f"✅Formulasi: {name}\n✅Element nomi: {y['Element'].values[0]}\n✅Turi: {y['Turi'].values[0]}\n✅Oilasi: {y['block'].values[0]}\n✅Atom massasi: {y['atom_mass'].values[0]}\n✅Qaynash nuqtasi: {y['boil'].values[0]} °C\n✅Kategoriyasi: {y['category'].values[0]}\n✅Yaratuvchisi: {y['discovered_by'].values[0]}\n✅Erish nuqtasi: {y['melt'].values[0]} °C\n✅Molyar issiqlik: {y['molar_heat'].values[0]}\n✅Kimning sharafiga: {y['named_by'].values[0]}\n✅Tartib raqami: {y['number'].values[0]}\n✅Davri: {y['period'][0]}\n✅Guruhi: {y['group'].values[0]}\n✅Agregat holati: {y['phase'].values[0]}\n✅Elektron qavatlari: {y['shells'].values[0]}\n✅Elektron konfiguratsiyasi: {y['electron_configuration'].values[0]}\n✅Semantik elektron konfiguratsiyasi: {y['electron_configuration_semantic'].values[0]}\n✅Elektronga yaqinlik: {y['electron_affinity'].values[0]}\n✅Elektromanfiyligi: {y['electronegativity_pauling'].values[0]}\n✅Ionlanish energiyasi: {y['ionization_energies'].values[0]}\n✅CPK-Hex: {y['cpk-hex'].values[0]}\n✅Qo'shimcha manba: {y['source'].values[0]}\n✅Elektron joylashuvi: {y['bohr_model_image'].values[0]}\n✅3D elektron joylashuvi: {y['bohr_model_3d'].values[0]}\n✅Spektral rasmi: {y['spectral_img'].values[0]}\n✅Element aniq rasmi: {y['image.url'].values[0]}\n"
            except IndexError as index:
                raise index
        elif name=="/start":
            return f"Siz botni qayta ishga tushirdingiz."
        else:
            return f"Afsuski😕 Bu {name} haqida ma'lumot yo'q❌ yoki siz sintaktik xatolik qildingiz."
    else:
        df = pd.read_csv(f'{BASE_DIR}/data/kimyo_2.csv')
        if name in df["name"].unique():
            y = df[df['name'] == f'{name}'].reset_index(drop=True)
            return {
                'about': f"✅Element: {name}\n✅Symbol: {y['symbol'].values[0]}\n✅Appearance: {y['appearance'].values[0]}\n✅Block: {y['block'].values[0]}\n✅Atom mass: {y['atomic_mass'].values[0]}\n✅Boil: {y['boil'].values[0]} °C\n✅Category: {y['category'].values[0]}\n✅Yaratuvchisi: {y['discovered_by'].values[0]}\n✅Melt: {y['melt'].values[0]} °C\n✅Molar heat: {y['molar_heat'].values[0]}\n✅Named by: {y['named_by'].values[0]}\n✅Number: {y['number'].values[0]}\n✅Period: {y['period'][0]}\n✅Group: {y['group'].values[0]}\n✅Phase: {y['phase'].values[0]}\n✅Shells: {y['shells'].values[0]}\n✅Electron configuration: {y['electron_configuration'].values[0]}\n✅Electron configuration semantic: {y['electron_configuration_semantic'].values[0]}\n✅Electron affinity: {y['electron_affinity'].values[0]}\n✅Electronegativity pauling: {y['electronegativity_pauling'].values[0]}\n✅Ionization energies: {y['ionization_energies'].values[0]}\n✅CPK-Hex: {y['cpk-hex'].values[0]}\n✅Source: {y['source'].values[0]}\n✅Bohr model image: {y['bohr_model_image'].values[0]}\n✅Bohr model 3d: {y['bohr_model_3d'].values[0]}\n✅Spectral image: {y['spectral_img'].values[0]}\n✅A clear image of the item: {y['image.url'].values[0]}\n",
                'summary': f"Summary:\n{y['summary'].values[0]}"}
        elif name in df["symbol"].unique():
            y = df[df['symbol'] == f'{name}'].reset_index(drop=True)
            return {
                "about": f"✅Symbol: {name}\n✅Element: {y['name'].values[0]}\n✅Appearance: {y['appearance'].values[0]}\n✅Block: {y['block'].values[0]}\n✅Atom mass: {y['atomic_mass'].values[0]}\n✅Boil: {y['boil'].values[0]} °C\n✅Category: {y['category'].values[0]}\n✅Yaratuvchisi: {y['discovered_by'].values[0]}\n✅Melt: {y['melt'].values[0]} °C\n✅Molar heat: {y['molar_heat'].values[0]}\n✅Named by: {y['named_by'].values[0]}\n✅Number: {y['number'].values[0]}\n✅Period: {y['period'][0]}\n✅Group: {y['group'].values[0]}\n✅Phase: {y['phase'].values[0]}\n✅Shells: {y['shells'].values[0]}\n✅Electron configuration: {y['electron_configuration'].values[0]}\n✅Electron configuration semantic: {y['electron_configuration_semantic'].values[0]}\n✅Electron affinity: {y['electron_affinity'].values[0]}\n✅Electronegativity pauling: {y['electronegativity_pauling'].values[0]}\n✅Ionization energies: {y['ionization_energies'].values[0]}\n✅CPK-Hex: {y['cpk-hex'].values[0]}\n✅Source: {y['source'].values[0]}\n✅Bohr model image: {y['bohr_model_image'].values[0]}\n✅Bohr model 3d: {y['bohr_model_3d'].values[0]}\n✅Spectral image: {y['spectral_img'].values[0]}\n✅A clear image of the item: {y['image.url'].values[0]}\n",
                'summary': f"Summary:\n{y['summary'].values[0]}"}
        elif name=='/start':
            return f"You have restarted the bot."
        else:
            return f"It's a pity😕 There is no information❌ about this {name} or you have made a syntax error."
