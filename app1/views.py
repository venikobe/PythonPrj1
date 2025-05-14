from django.shortcuts import render
from .forms import TaskForm

def mainPage(request):
    template = 'main.html'
    return render(request, template)

def task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data["year"]
            century = form.cleaned_data["century"]
            return taskAnswer(request, year, century)
    else:
        form = TaskForm()
    template = 'task.html'
    context = {'form': form}
    return render(request, template, context)


def taskAnswer(request, year, century):
    taskStr = f'Встречаются ли года {year}, в столетии {century}'
    years = year.split()
    ans = 0
    for i in range(len(years)):
        if ((int(years[i]) > (int(century)*100-99)) & (int(years[i]) <= (int(century)*100))):
            ans += 1
    template = 'answer.html'
    context = {'answer': ans, 'question': taskStr}
    return render(request, template, context)


def AigisArticle(request):
    template = 'article.html'
    context = { 'img':{'imgurl': 'https://static.wikia.nocookie.net/megamitensei/images/2/22/P3_Aigis.png/revision/latest/scale-to-width-down/1000?cb=20230205053002',
                       'title': 'Aigis',
                       'description': "Aigis from Persona 3 Original"},
               'section1': {'name': 'Aigis',
                            'text': "Aigis (romanized as Aegis in Japanese) is a character from Persona 3. She is an Anti-Shadow Suppression Weapon (seemingly the last one in existence) and a member of S.E.E.S. who also attends Gekkoukan High School. She is a machine that gradually awakens to human emotions. She is also the main protagonist of The Answer, the epilogue of FES, and its remake as part of the Persona 3 Reload Expansion Pass, Episode Aigis - The Answer."
                            },
                'section2': { 'name': 'Personality',
                             'text': "Initial personality is simply a robot designed to obey orders, although she is drawn to the protagonist and states that it is very important for her to be by his side, going so far as to hug them in front of everyone. Her desire to protect the protagonist is so strong, in fact, that she was able to overcome Ikutsuki's programming and free the entire team from their shackles, when Ikutsuki had attempted to sacrifice them to bring forth the Fall. As a result of having no emotions, Aigis' social skills are more-or-less non-existent; it's frequently noted on-screen that while she may look human, she is far from passing as such. She is prone to doing very strange and socially unacceptable things, such as breaking into the protagonist's room to wake him up and requesting to be on standby in their room, which Yukari calls her out for. A video recording shows that she has a habit of breaking into his dorm room at night in order to check on him, even going so far as to keep a record of how long it takes her to pick the lock, In Falling Down, she even goes so far as to sneak into the boys' rooms during the group's stay in Kyoto, claiming it was unfair that she and the protagonist weren't in the same room. Lack of social grace notwithstanding, Aigis is nonetheless very polite to everybody, always using the honorific '-san' when addressing them. In the original Japanese version, she often ends her sentences with 'de arimasu' prior to developing emotions.",
                            },
                'section3': { 'name' : "Etymology",
                            'text' : "In Greek mythology, the aegis is a shield worn by Pallas Athena. Pallas is an epithet taken by Athena after accidentally killing Pallas, daughter of Triton. In Pallas' memory, Athena erected Palladium, a statue in dedication of Pallas. More corporeal accounts of the aegis describe it as a grotesquely ornamented mantle worn over the shoulders and breast, less commonly a buckler bearing a Gorgon's head, or even simultaneously fulfilling both roles. One theory places the aegis as the remains of Pallas protecting Athena after death. However, an aegis is recorded to have been worn by Zeus and various Greek heroes on occasion, even Mt. Olympus itself is said to be shrouded by the aegis. In reality, there is no central narrative or tradition, but the aegis, whatever it specifically was, represents the protection of the gods. This is referenced by Aigis desiring to spend her days defending the protagonist, and, in her words, 'always protect him.' This reference is bolstered by the fact that the protagonist's ultimate Persona is Messiah, a being who, in world religions, is considered a deity who shall bring salvation to the world upon its end.",
                }
                            }
    return render(request, template, context)

def MakotoArticle(request):
    template = 'article.html'
    context = { 'img':{'imgurl': 'https://static.wikia.nocookie.net/megamitensei/images/c/c1/P3_Protagonist.png/revision/latest?cb=20230205054436',
                       'title': 'Makoto Yuki',
                       'description': "Makoto from Persona 3 Original"},
               'section1': {'name': 'Makoto Yuki',
                            'text': "The protagonist of Persona 3, canonically known as Makoto Yuki (having been used in other media and later confirmed as the default name in the 2023 re-release of Persona 3 Portable),[1][2][3] is a transfer student enrolling in Gekkoukan High School in Iwatodai City. He is an orphan whose parents died on the Moonlight Bridge in their car during a fatal incident a decade prior to the game."
                            },
                'section2': { 'name': 'Personality',
                             'text': "In Persona 3, he is a silent protagonist, aside from technically speaking in battle in certain instances. While being a silent protagonist, he is very stoic, reserved and calm, gathered by the fact that he's faced death and his own mortality; he remains unmoved when walking under a green sky and being surrounded by blood pools and coffins everywhere at the beginning of Persona 3 or even when guns are pointed at him (such as by Aigis herself). He appears very introverted, distant and aloof since he only observes the conversations of his party members and only speaks when someone is directed at him for his opinion on the matter. At one point, Yukari Takeba raises her voice at him in frustration, calling him 'Mr. Perfect' and saying nothing ever fazes him. She then apologizes for her behavior; he comforts her and she says that he 'really is one-of-a-kind.' His teacher, Isako Toriumi, comments that he is 'kinda quiet, but real mature and intense looking (and hawt)' and that he uses proper grammar and punctuation online. Junpei Iori comments that all he does is wander around and talk to people, referencing what is commonly done during gameplay.",
                            },
                'section3': { 'name' : "Etymology",
                            'text' : "The name given to the protagonist in the film series, 'Makoto Yuuki,' can be interpreted as 'true courage.' The name given to him in the manga series, 'Minato Arisato,' is translated as '有 (ari/aru/yuu) = exist, 里 (sato) = village, 湊 (minato) = harbor.' Both of these names allude to his role in the story.",
                }
                            }
    return render(request, template, context)

def KotoneArticle(request):
    template = 'article.html'
    context = { 'img':{'imgurl': 'https://static.wikia.nocookie.net/megamitensei/images/3/31/Protagonist_%28Female%29.png/revision/latest?cb=20230205052924',
                       'title': 'Kotone Shiomi',
                       'description': "Kotone from Persona 3 Original"},
               'section1': {'name': 'Kotone Shiomi',
                            'text': "The female protagonist of Persona 3 Portable, canonically known as Kotone Shiomi (having originated from the stage play and later clarified as the default name in the 2023 re-release of the game),[1][2][3] is a transfer student enrolling in Gekkoukan High School on Tatsumi Port Island. She is an orphan whose parents died on the Moonlight Bridge in their car during a fatal incident a decade prior to the game."
                            },
                'section2': { 'name': 'Personality',
                             'text': "Unlike the male protagonist or Megami Tensei protagonists in general, she is very bubbly, funny, upbeat and cheerful. Her dialogue choices exhibit a broad spectrum of emotions, ranging from sarcasm, joking tones, utter seriousness and otherwise depending on the player's choice. She is outspoken, blunt and literal when responding and getting her points across. She is a sharp contrast to the male protagonist who is very reserved and concise where she, on the other hand, is not afraid to interject into conversations where her male counterpart would remain silent. In addition, she is more likely to resort to violence when provoked, especially in defense of her friends, as seen in her Hermit Social Link. She is often described by the S.E.E.S members as a very tomboyish leader who takes risks to save her friends.",
                            },
                'section3': { 'name' : "Design",
                            'text' : "Kotone has auburn hair, which she always has in a high ponytail, along with silver barrettes which form the Roman numeral XXII (22), possibly referencing that the Fool Arcana is not only Arcana 0, but also Arcana 22 with the numbers increasing while going back to the first card after The World (Arcana 21). Since she's the polar opposite of the male protagonist, it would make sense for the male protagonist to be Fool 0 while the female is Fool 22. She is seemingly shorter than the default male protagonist. She has a pale complexion and striking red eyes (and longer lashes than the other characters, like Aigis).",
                }
                            }
    return render(request, template, context)

def FuukaArticle(request):
    template = 'article.html'
    context = { 'img':{'imgurl': 'https://static.wikia.nocookie.net/megamitensei/images/8/81/Fuuka_Yamagishi.png/revision/latest?cb=20230205052918',
                       'title': 'Fuuka Yamagishi',
                       'description': "Fuuka from Persona 3 Original"},
               'section1': {'name': 'Fuuka Yamagishi',
                            'text': "Fuuka Yamagishi is one of the main characters from Persona 3. She is a student at Gekkoukan High School and a member of the Specialized Extracurricular Execution Squad."
                            },
                'section2': { 'name': 'Personality',
                             'text': "Initially, Fuuka is a very reserved, shy and timid girl who rarely speaks up. Before she joined S.E.E.S., this made her an easy target for school bullies, to the point of Natsuki Moriyama locking her in the school gym, which resulted in her getting trapped in Tartarus. However, she is also a friendly student once others open up to her and very kind-hearted, even more so than Yukari. She is very polite, and almost always uses honorifics when addressing people. Usually cool, calm, and collected (particularly in the movie) and despite being quiet and not being involved with fighting and physical combat, she tries to help her friends in any way possible such as using her Persona's abilities to scan the statistics and weaknesses of Shadows, showing her to be very diligent and dedicated. Her Arcana is the Priestess, which fits with her ability to easily contemplate and analyze things. It also reflects her independence, which is shown by her being able to survive in Tartarus for ten hours by herself, when S.E.E.S. were barely able to last an hour in there at that point.",
                            },
                'section3': { 'name' : "Etymology",
                            'text' : "The name Fuuka means 'wind' (風) (fuu) and 'flower' (花) (ka). The meaning of the name would be verified if Shuji Ikutsuki is spoken to on 6/14 in Persona 3 Reload.",
                }
                            }
    return render(request, template, context)



def about(request):
    template = 'about.html'
    context = {
        'my': {
            'name': 'Аштаева Полина Дмитриевна',
            'phone': '+79185828998',
            'mail': 'kekanadujara@gmail.com',
            'imgurl': 'https://sun9-7.userapi.com/impg/LOtRmR00sLHaznn3EmGkwquS9MYIiarrOWINLg/lGH9PlXF5lU.jpg?size=561x662&quality=95&sign=da6df9ece3d8d51bbd883cf706c33e59&type=album'
        },
        'op': {
            'name': 'Геймдизайн',
            'description': 'Сегодня видеоигры — это больше, чем простое развлечение; их можно воспринимать как сложную модель, волшебное зеркало, которое отражает человеческие взаимоотношения, общественные процессы и окружающий нас мир в целом.',
            'ruk': {
                'name': 'Казаков Анатолий Сергеевич',
                'mail': 'akazakov@hse.ru',
                'imgurl' :'https://www.hse.ru/pubs/share/thumb/896871043:c190x190+0+0:r380x380!.jpg'
            },
            'manager': {
                'name': 'Матвиенко Бамба Владимировна',
                'mail': 'bmatvienko@hse.ru',
                'imgurl' :'https://www.hse.ru/pubs/share/thumb/896558347:c720x720+0+0:r380x380!.jpeg'
            }
        },
        'fr1': {
            'name': 'Столпер Яна',
            'phone': '+79255126532',
            'mail': 'yastolper@edu.hse.ru',
            'imgurl': 'https://sun9-11.userapi.com/impg/2rgLiiMeEkBwWuesSsI4Vq-wVnCBv4Uy6En43Q/7NfdMuTJ7i4.jpg?size=954x800&quality=96&sign=88e8ac67f81d817b6d2af1e9d1057ede&type=album'
        },
        'fr2': {
            'name': 'Медведев Аарон',
            'phone': '+79169462267',
            'mail': 'admedvedev@edu.hse.ru',
            'imgurl': 'https://sun9-60.userapi.com/impg/iTc4xI3IbHUiGCkaoAjiopcUZUC1AcsPBEO9WQ/ponBG-5Wxic.jpg?size=604x453&quality=96&sign=97e069bd2060a83ea0fb8158e6f20393&type=album'
        },
    }
    return render(request, template, context)
