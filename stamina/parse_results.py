import os
import subprocess

kd_vals = [0.0005, 0.00075, 0.001]
template = 'Circuit0x8E_000to011_G1_10_10_bound.sm'
prop = 'Circuit0x8E_G1.csl'

csv_file = open("results.csv", "w")
csv_file.write("kd_PhlF,kd_YPF,kd_HlyIIR,kd_BetI,kd_AmtR,Pmin,Pmax,Window\n")

# prism Circuit0x8E_000to011_G1_10_10.sm -prop Circuit0x8E_G1.csl -const kd_PhlF=,kd_YPF=,kd_HlyIIR=,kd_BetI=,kd_AmtR= -exportresults stdout
# prism Circuit0x8E_000to011_G1_10_10_bound.sm -prop Circuit0x8E_G1.csl -const kd_PhlF=,kd_YPF=,kd_HlyIIR=,kd_BetI=,kd_AmtR= -exportresults stdout

# kd_PhlF
# kd_YPF
# kd_HlyIIR
# kd_BetI
# kd_AmtR



for kd_PhlF in kd_vals:
    for kd_YPF in kd_vals:
        for kd_HlyIIR in kd_vals:
            for kd_BetI in kd_vals:
                for kd_AmtR in kd_vals:
                    file_name = str(kd_PhlF).replace("0.","") + "_" + str(kd_YPF).replace("0.","") + "_" + str(kd_HlyIIR).replace("0.","") + "_" + str(kd_BetI).replace("0.","") + "_" + str(kd_AmtR).replace("0.","") + "_0x8e"
                    model_name = file_name + ".sm"
                    result_name = file_name + ".result"
                    error_name = file_name + ".error"
                    with open(result_name, "r") as result_file:
                        for line in result_file:
                            if "Minimum" in line:
                                Pmin = float(line.split(":")[1].strip())
                            elif "Maximum" in line:
                                Pmax = float(line.split(":")[1].strip())
                            elif "Window" in line:
                                Window = float(line.split(":")[1].strip())
                        csv_file.write(f"{kd_PhlF},{kd_YPF},{kd_HlyIIR},{kd_BetI},{kd_AmtR},{Pmin},{Pmax},{Window}\n")
