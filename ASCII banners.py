from pyfiglet import Figlet, figlet_format
def main():
    fig = Figlet()
    fonts = list(fig.getFonts())
    banner = input("Enter the banner text:\n")
    print()
    for i in range(10):
        print(f"{1+i}- {fonts[i]}")
    while True:
        try:
            font = int(input("Enter the font number from the following list:\n"))
            if  font < 1 or font > 10 or fonts[font-1] not in fonts :
                raise ValueError
        except ValueError:
            print("enter a valid number or font number from 1 to 10")
            print()
        else:
            fig.setFont(font = fonts[font-1])
            print(f"Your styled ASCII art:\n{fig.renderText(banner)}")
            break
        
    
    
    
main()