from kauppa import Kauppa
from kirjanpito import kirjanpito as default_kirjanpito
#from varasto import Varasto
#from pankki import Pankki
#from viitegeneraattori import Viitegeneraattori

def main():
    #varasto = Varasto.get_instance()
    #pankki = Pankki.get_instance()
    #viitegeneraattori = Viitegeneraattori.get_instance()
    #kauppa = Kauppa(varasto, pankki, viitegeneraattori)

    #viitegeneraattori = Viitegeneraattori()
    kirjanpito = default_kirjanpito #Kirjanpito()
    #varasto = Varasto(kirjanpito)
    #pankki = Pankki(kirjanpito)
    #kauppa = Kauppa(varasto, pankki, viitegeneraattori)

    kauppa = Kauppa()

    # kauppa hoitaa yhden asiakkaan kerrallaan seuraavaan tapaan:
    kauppa.aloita_asiointi()
    kauppa.lisaa_koriin(1)
    kauppa.lisaa_koriin(3)
    kauppa.lisaa_koriin(3)
    kauppa.poista_korista(1)
    kauppa.tilimaksu("Pekka Mikkola", "1234-12345")

    # seuraava asiakas
    kauppa.aloita_asiointi()

    for _ in range(0, 24):
        kauppa.lisaa_koriin(5)

    kauppa.tilimaksu("Arto Vihavainen", "3425-1652")

    # kirjanpito
    for tapahtuma in kirjanpito.tapahtumat:
        print(tapahtuma)


if __name__ == "__main__":
    main()
