import os
import subprocess

kd_vals = [0.0005, 0.00075, 0.001]
template = 'Circuit0x8E_000to011_G1_10_10_bound.sm'
prop = 'Circuit0x8E_G1.csl'
exportResults = 'stdout'
maxmem = '8000000'

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
                    with open(template, "r") as template_file:
                        with open(model_name, "w") as new_model:
                            for line in template_file:
                                if "const double kd_PhlF;" in line:
                                    new_model.write("const double kd_PhlF = {:.6f};".format(kd_PhlF))
                                elif "const double kd_YPF;" in line:
                                    new_model.write("const double kd_YPF = {:.6f};".format(kd_YPF))
                                elif "const double kd_HlyIIR;" in line:
                                    new_model.write("const double kd_HlyIIR = {:.6f};".format(kd_HlyIIR))
                                elif "const double kd_BetI;" in line:
                                    new_model.write("const double kd_BetI = {:.6f};".format(kd_BetI))
                                elif "const double kd_AmtR;" in line:
                                    new_model.write("const double kd_AmtR = {:.6f};".format(kd_AmtR))
                                else:
                                    new_model.write(line.strip())
                                new_model.write("\n")
                    command = [
                        'sstamina',
                        str(model_name),
                        str(prop),
                    ]
                    print("  " + " ".join(command))
                    result_log = open(result_name, "w")
                    error_log = open(error_name, "w")
                    subprocess.call(command, stdout=result_log, stderr=error_log)
                    result_log.close()
                    error_log.close()
                    if os.path.isfile(error_name) and os.path.getsize(error_name) == 0:
                        os.remove(error_name)
                    
