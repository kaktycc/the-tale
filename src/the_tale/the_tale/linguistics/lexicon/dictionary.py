# coding: utf-8

from utg.words import WordForm, Word, Properties
from utg.relations import WORD_TYPE
from utg.data import VERBOSE_TO_PROPERTIES
from utg.dictionary import Dictionary

from the_tale.linguistics.lexicon import exceptions


def noun(forms, properties, countable=None):

    if (len(forms) == 12):
        forms = forms + forms[6:]

    properties = Properties(*[VERBOSE_TO_PROPERTIES[prop.strip()] for prop in properties.split(',')])

    if len(forms) != Word.get_forms_number(type=WORD_TYPE.NOUN):
        raise exceptions.WrongFormNumberError()

    return WordForm(Word(type=WORD_TYPE.NOUN, forms=forms, properties=properties))


def text(form):
    return WordForm(Word(type=WORD_TYPE.TEXT, forms=[form], properties=Properties()))


forms = [ noun(['герой', 'героя', 'герою', 'героя', 'героем', 'герое',
                'герои', 'героев', 'героям', 'героев', 'героями', 'героях'], 'од,мр'),
          noun(['привидение', 'привидения', 'привидению', 'привидение', 'привидением', 'привидении',
                'привидения', 'привидений', 'привидениям', 'привидения', 'привидениями', 'привидениях'], 'од,ср'),
          noun(['героиня', 'героини', 'героине', 'героиню', 'героиней', 'героине',
                'героини', 'героинь', 'героиням', 'героинь', 'героинями', 'героинях'], 'од,жр'),
          noun(['рыцарь', 'рыцаря', 'рыцарю', 'рыцаря', 'рыцарем', 'рыцаре',
                'рыцари', 'рыцарей', 'рыцарям', 'рыцарей', 'рыцарями', 'рыцарях'], 'од,мр'),
          noun(['призрак', 'призрака', 'призраку', 'призрака', 'призраком', 'призраке',
                'призраки', 'призраков', 'призракам', 'призраков', 'призраками', 'призраках'], 'од,мр'),
          noun(['чудовище', 'чудовища', 'чудовищу', 'чудовище', 'чудовищем', 'чудовище',
                'чудовища', 'чудовищ', 'чудовищам', 'чудовищ', 'чудовищами', 'чудовищах'], 'од,ср'),
          noun(['русалка', 'русалки', 'русалке', 'русалку', 'русалкой', 'русалке',
                'русалки', 'русалок', 'русалкам', 'русалок', 'русалками', 'русалках'], 'од,жр'),
          noun(['боец', 'бойца', 'бойцу', 'бойца', 'бойцом', 'бойце',
                'бойцы', 'бойцов', 'бойцам', 'бойцов', 'бойцами', 'бойцах'], 'од,мр'),
          noun(['жираф', 'жирафа', 'жирафу', 'жирафа', 'жирафом', 'жирафе',
                'жирафы', 'жирафов', 'жирафам', 'жирафов', 'жирафами', 'жирафах'], 'од,мр'),
          noun(['чучело', 'чучела', 'чучелу', 'чучело', 'чучелом', 'чучеле',
                'чучела', 'чучел', 'чучелам', 'чучела', 'чучелами', 'чучелах'], 'но,ср'),
          noun(['зебра', 'зебры', 'зебре', 'зебру', 'зеброй', 'зебре',
                'зебры', 'зебр', 'зебрам', 'зебр', 'зебрами', 'зебрах'], 'од,жр'),
          noun(['слон', 'слана', 'слону', 'слона', 'слоном', 'слоне',
                'слоны', 'слонов', 'слонам', 'слонов', 'слонами', 'слонах'], 'од,мр'),
          noun(['гусь', 'гуся', 'гусю', 'гуся', 'гусем', 'гусе',
                'гуси', 'гусей', 'гусям', 'гусей', 'гусями', 'гусях'], 'од,мр'),
          noun(['пугало', 'пугала', 'пугалу', 'пагуло', 'пугалом', 'пунале',
                'пугала', 'пугалах', 'пугалам', 'пугала', 'пугалами', 'пугалах'], 'од,ср'),
          noun(['свинья', 'свиньи', 'свинье', 'свинью', 'свиньёй', 'свинье',
                'свиньи', 'свиней', 'свиньям', 'свиней', 'свиньями', 'свиньях'], 'од,жр'),
          noun(['волк', 'волка', 'волку', 'волка', 'волком', 'волке',
                'волки', 'волков', 'волкам', 'волков', 'волками', 'волках'], 'од,мр'),
          noun(['Минск', 'Минска', 'Минску', 'Минск', 'Минском', 'Минске',
                '', '', '', '', '', ''], 'но,мр,ед'),
          noun(['Простоквашино', 'Простоквашина', 'Простоквашину', 'Простоквашино', 'Простоквашином', 'Простоквашине',
                '', '', '', '', '', ''], 'но,ср,ед'),
          noun(['Вилейка', 'Вилейки', 'Вилейке', 'Вилейку', 'Вилейкой', 'Вилейке',
                '', '', '', '', '', ''], 'но,жр,ед'),
          noun(['', '', '', '', '', '',
                'Барановичи', 'Барановичей', 'Барановичам', 'Барановичи', 'Барановичами', 'Барановичах'], 'но,мн'),
          noun(['Тагил', 'Тагила', 'Тагилу', 'Тагил', 'Тагилом', 'Тагиле',
                '', '', '', '', '', ''], 'од,мр,ед'),
          noun(['Чугуево', 'Чугуева', 'Чугуеву', 'Чугуево', 'Чугуевом', 'Чугуеве',
                '', '', '', '', '', ''], 'но,ср,ед'),
          noun(['Рига', 'Риги', 'Риге', 'Ригу', 'Ригой', 'Риге',
                '', '', '', '', '', ''], 'од,жр,ед'),
          noun(['', '', '', '', '', '',
                'Афины', 'Афин', 'Афинам', 'Афины', 'Афинами', 'Афинах'], 'но,мн'),
          noun(['Магадан', 'Магадана', 'Магадану', 'Магадан', 'Магаданом', 'Магадане',
                '', '', '', '', '', ''], 'но,мр,ед'),
          noun(['Бородино', 'Бородина', 'Бородину', 'Бородино', 'Бородином', 'Бородине',
                '', '', '', '', '', ''], 'но,ср,ед'),
          noun(['Уфа', 'Уфы', 'Уфе', 'Уфу', 'Уфой', 'Уфе',
                '', '', '', '', '', ''], 'но,жр,ед'),
          noun(['', '', '', '', '', '',
                'Чебоксары', 'Чебоксар', 'Чебоксарам', 'Чебоксары', 'Чебоксарами', 'Чебоксарах'], 'но,мн'),
          noun(['нож', 'ножа', 'ножу', 'нож', 'ножом', 'ноже',
                'ножи', 'ножей', 'ножам', 'ножи', 'ножами', 'ножах'], 'но,мр'),
          noun(['ядро', 'ядра', 'ядру', 'ядро', 'ядром', 'ядре',
                'ядра', 'ядер', 'ядрам', 'ядра', 'ядрами', 'ядрах'], 'но,ср'),
          noun(['пепельница', 'пепельницы', 'пепельнице', 'пепельницу', 'пепельницей', 'пепельнице',
                'пепельницы', 'пепельниц', 'пепельницам', 'пепельницы', 'пепельницами', 'пепельниц'], 'но,жр'),
          noun(['', '', '', '', '', '',
                'ножницы', 'ножниц', 'ножницам', 'ножницы', 'ножницами', 'ножницах'], 'но,мн'),
          noun(['кинжал', 'кинжала', 'кинжалу', 'кинжал', 'кинжалом', 'кинжале',
                'кинжалы', 'кинжалов', 'кинжалам', 'кинжалы', 'кинжалами', 'кинжалах'], 'но,мр'),
          noun(['окно', 'окна', 'окну', 'окно', 'окном', 'окне',
                'окна', 'окон', 'окнам', 'окна', 'окнами', 'окнах'], 'но,ср'),
          noun(['мечта', 'мечты', 'мечте', 'мечту', 'мечтой', 'мечте',
                'мечты', 'мечт', 'мечтам', 'мечты', 'мечтами', 'мечтах'], 'но,жр'),
          noun(['', '', '', '', '', '',
                'макароны', 'макарон', 'макаронам', 'макароны', 'макаронами', 'макаронами'], 'но,мн'),
          noun(['меч', 'меча', 'мечу', 'меч', 'мечом', 'мече',
                'мечи', 'мечей', 'мечам', 'мечи', 'мечами', 'мечах'], 'но,мр'),
          noun(['варенье', 'варенья', 'варенью', 'варенье', 'вареньем', 'варенье',
                'вареньях', 'варений', 'вареньям', 'варенья', 'вареньями', 'вареньях'], 'но,ср'),
          noun(['чашка', 'чашки', 'чашке', 'чашку', 'чашкой', 'чашке',
                'чашки', 'чашке', 'чашкам', 'чашки', 'чашками', 'чашках'], 'но,жр'),
          noun(['', '', '', '', '', '',
                'дрова', 'дров', 'дровам', 'дрова', 'дровами', 'дровах'], 'но,мн'),
          noun(['форт', 'форта', 'форту', 'форт', 'фортом', 'форте',
                'форты', 'фортов', 'фортам', 'форты', 'фортами', 'фортах'], 'но,мр'),
          noun(['захолустье', 'захолустья', 'захолустью', 'захолустье', 'захолустьем', 'захолустье',
                'захолустья', 'захолустий', 'захолустьям', 'захолустья', 'захолустьями', 'захолустий'], 'но,ср'),
          noun(['святыня', 'святыни', 'святыне', 'святыню', 'святыней', 'святыне',
                'святыни', 'святынь', 'святыням', 'святыне', 'святынями', 'святынях'], 'но,жр'),
          noun(['мемориал', 'мемориала', 'мемориалу', 'мемориал', 'мемориалом', 'мемориала',
                'мемориалы', 'мемориалов', 'мемориалам', 'мемориалы', 'мемориалами', 'мемориалах'], 'но,мр'),
          noun(['замок', 'замка', 'замку', 'замок', 'замком', 'замке',
                'замки', 'замков', 'замкам', 'замки', 'замками', 'замках'], 'но,мр'),
          noun(['пристанище', 'пристанища', 'пристанищу', 'пристанище', 'пристанищем', 'пристанище',
                'пристанища', 'пристанищ', 'пристанища', 'пристанища', 'пристанищами', 'пристанищах'], 'но,ср'),
          noun(['земля', 'земли', 'земле', 'землю', 'землёй', 'земле',
                'земли', 'земель', 'землям', 'земли', 'землями', 'землях'], 'но,жр'),
          noun(['колония', 'колонии', 'колонии', 'колонию', 'колонией', 'колонии',
                'колонии', 'колоний', 'колониям', 'колонии', 'колониями', 'колониях'], 'но,жр'),
          noun(['человек', 'человека', 'человеку', 'человека', 'человеком', 'человеке',
                'люди', 'людей', 'людям', 'людей', 'людьми', 'людях',
                'человек', 'человек', 'человекам', 'человек', 'человеками', 'человеках'], 'од,мр'),
          noun(['эльф', 'эльфа', 'эльфу', 'эльфа', 'эльфом', 'эльфе',
                'эльфы', 'эльфов', 'эльфам', 'эльфов', 'эльфами', 'эльфах'], 'од,мр'),
          noun(['орк', 'орка', 'орку', 'орка', 'орком', 'орке',
                'орки', 'орков', 'оркам', 'орков', 'орками', 'орках'], 'од,мр'),
          noun(['гоблин', 'гоблина', 'гоблину', 'гоблина', 'гоблином', 'гоблине',
                'гоблины', 'гоблинов', 'гоблинам', 'гоблинов', 'гоблинами', 'гоблинах'], 'од,мр'),
          noun(['дварф', 'дварфа', 'дварфу', 'дварфа', 'дварфом', 'дварфе',
                'дварфы', 'дварфов', 'дварфам', 'дварфов', 'дварфами', 'дварфах'], 'од,мр'),
          text('любой текст'),
          text('текст текст текст'),
          text('какой-то текст'),
          text('18 сухого месяца 183 года')
    ]


DICTIONARY = Dictionary(words=[form.word for form in forms])
