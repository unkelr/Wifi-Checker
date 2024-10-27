import os
import subprocess
import webbrowser

def install(package):
    subprocess.check_call(["pip", "install", package])

try:
    import speedtest
except ImportError:
    install('speedtest-cli')
    import speedtest

try:
    from colorama import Fore, Style, init
except ImportError:
    install('colorama')
    from colorama import Fore, Style, init

init(autoreset=True)
os.system('cls && title Network Speed Test')

def speed_test():
    st = speedtest.Speedtest()

    try:
        print(Style.RESET_ALL + Fore.MAGENTA + Style.BRIGHT + "Finding the best server...")
        st.get_best_server()

        print(Fore.MAGENTA + Style.BRIGHT + "Testing download speed...")
        download_speed = st.download() / 1_000_000  
        print(Fore.MAGENTA + Style.BRIGHT + "Testing upload speed...")
        upload_speed = st.upload() / 1_000_000  
        print(Fore.MAGENTA + Style.BRIGHT + "Testing ping...")
        ping = st.results.ping

        print(Fore.MAGENTA + Style.BRIGHT + "\n=== Internet Speed Test Results ===")
        print(Fore.MAGENTA + Style.BRIGHT + f"Download Speed:{Style.DIM} {download_speed:.2f} mbps{Style.RESET_ALL}")
        print(Fore.MAGENTA + Style.BRIGHT + f"Upload Speed:{Style.DIM} {upload_speed:.2f} mbps{Style.RESET_ALL} ")
        print(Fore.MAGENTA + Style.BRIGHT + f"Ping:{Style.DIM} {ping:.2f} ms{Style.RESET_ALL}")

    except speedtest.ConfigRetrievalError as e:
        print(Fore.MAGENTA + Style.BRIGHT + "Error retrieving configuration. Please check your network settings.")
        print(Fore.MAGENTA + Style.BRIGHT + f"Details: {e}{Style.RESET_ALL}")
    except Exception as e: 
        print(Fore.MAGENTA + Style.BRIGHT + "An unexpected error occurred.")
        print(Fore.MAGENTA + Style.BRIGHT + f"Details:{Style.DIM} {e}{Style.RESET_ALL}")

print(Fore.MAGENTA + Style.BRIGHT + f"""

1. Check Speed
2. Discord
3. Quit

""")

choice = input(Fore.MAGENTA + Style.BRIGHT + f"->{Style.DIM} ")

if choice == '1':
    speed_test()
elif choice == '2':
    webbrowser.open("https://discord.gg/shopc")
elif choice == '3':
    print(Fore.MAGENTA + Style.DIM + "Quitting...")
else:
    print(Fore.MAGENTA + Style.BRIGHT + "Invalid choice. Please select 1, 2, or 3.")
