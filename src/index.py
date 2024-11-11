from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print(
         "Luonnin jälkeen:"
         +f"\nMehuvarasto: {mehua}"
         +f"\nOlutvarasto: {olutta}"
         +"\nOlut getterit:"
         +f"\nsaldo = {olutta.saldo}"
         +f"\ntilavuus = {olutta.tilavuus}"
         +f"\npaljonko_mahtuu = {olutta.paljonko_mahtuu()}"
         +"\nMehu setterit:"
         +"\nLisätään 50.7"
         +f"\nMehuvarasto: {mehua}"
         +"\nOtetaan 3.14"
         +f"\nMehuvarasto: {mehua}"
        )

    mehua.lisaa_varastoon(50.7)
    mehua.ota_varastosta(3.14)

    print(
        "Virhetilanteita:"
        +"\nVarasto(-100.0);"
        +f"\n{Varasto(-100.0)}"
        +"\nVarasto(100.0, -50.7)"
        +f"\n{Varasto(100.0, -50.7)}"
        +f"\nOlutvarasto: {olutta}"
        +"\nolutta.lisaa_varastoon(1000.0)"
        )

    olutta.lisaa_varastoon(1000.0)
    print(
        f"Olutvarasto: {olutta}"
        +f"Mehuvarasto: {mehua}"
        +"\nmehua.lisaa_varastoon(-666.0)"
        )

    mehua.lisaa_varastoon(-666.0)
    print(
        f"Mehuvarasto: {mehua}"
        +f"Olutvarasto: {olutta}"
        +"\nolutta.ota_varastosta(1000.0)"
        +f"saatiin {olutta.ota_varastosta(1000.0)}"
        +f"Olutvarasto: {olutta}"
        +f"Mehuvarasto: {mehua}"
        +"mehua.otaVarastosta(-32.9)"
        +f"saatiin {mehua.ota_varastosta(-32.9)}"
        +f"Mehuvarasto: {mehua}"
        )


if __name__ == "__main__":
    main()
