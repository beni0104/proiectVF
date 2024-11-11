import subprocess
from datetime import datetime
from pathlib import Path

# functie pentru a obtine numarul de fisiere din fiecare folder - nr de input-uri din fiecare familie
def get_file_count(folder_path):
    return len([f for f in Path(folder_path).iterdir() if f.is_file()])

def run_benchmark_in_minisat(minisat_path, family_name, input_file, max_time):
    # setam numele fisierului pentru rezultat si cel pentru statistici
    result_file = f"results/{family_name}/outputs/result_{input_file.stem}.cnf"
    stats_file = f"results/{family_name}/statistics/statistics_{input_file.stem}.stats"
    
    # construim comanda pentru rularea minisat
    # 2>&1 - atat iesirea standard cat si iesirea pentru eroare sa fie redirectionate catre fisierul pentru statistici
    command = f"{minisat_path} {input_file} {result_file} > {stats_file} 2>&1"

    start_time = datetime.now()
    print(f"Am inceput la {start_time}")

    # lansam procesul si asteptam pana se termina sau pana expira timpul alocat
    process = subprocess.Popen(command, shell = True)

    try:
        process.wait(timeout = max_time)
        end_time  = datetime.now()
        print(f"Am incheiat la {end_time}")

        print(f"Benchmark {input_file} completat cu succes.")
    except subprocess.TimeoutExpired:
        process.kill()  # incheiem procesul daca timpul a expirat

        # mesajul din fisierele de result si statistics daca procesul nu s-a incheiat cu succes
        with open(result_file, "w") as result_output, open(stats_file, "w") as stats_output:
            result_output.write("Benchmark neterminat: Timeout\n")
            stats_output.write("Benchmark neterminat: Timeout\n")
        

def main(main_folder_path, minisat_path):
    # iteram subdirectoarele pentru fiecare familie
    for family_folder in Path(main_folder_path).iterdir():
        if family_folder.is_dir():
            print(f"Incepem benchmark-urile pentru familia: {family_folder.name}")

            # calculam numarul de fișiere din directorul respectiv
            file_count = get_file_count(family_folder)
            if file_count == 0:
                print(f"Nu sunt fisiere în folderul {family_folder.name}.")
                continue

            # calculam timpul alocat pentru fiecare fisier din familie
            max_time_per_file = (24 * 60 * 60) // file_count
            print(f"Avem de rulat {file_count} fisiere")
            print(f"Timp alocat per fisier: {max_time_per_file // 60} minute")

            # iteram prin fiecare fisier
            for input_file in family_folder.iterdir():
                if input_file.is_file():
                    print(f"Rulez benchmark pentru fisierul: {input_file.name}")
                    # run_benchmark_in_minisat(minisat_path, family_folder.name, input_file, max_time_per_file)

            print(f"Toate benchmark-urile din familia {family_folder.name} au fost rulate.")

    print("Toate benchmark-urile au fost rulate.")
    

if __name__ == '__main__':
    folder_path = f"C:/minisat/build/benchmarks"
    minisat_path = "C:/minisat/build/minisat.exe"
    main(folder_path, minisat_path)