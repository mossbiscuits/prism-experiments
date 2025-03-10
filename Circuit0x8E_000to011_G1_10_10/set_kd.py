import subprocess
import timeit

kd_vals = ['0.0005', '0.00075', '0.001']
models = ['Circuit0x8E_000to011_G1_10_10_bound.sm']
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

for model in models:
    for kd_PhlF in kd_vals:
        for kd_YPF in kd_vals:
            for kd_HlyIIR in kd_vals:
                for kd_BetI in kd_vals:
                    for kd_AmtR in kd_vals:
                        command = [
                            '/usr/bin/time',
                            'prism',
                            str(model),
                            '-prop',
                            str(prop),
                            '-const',
                            'kd_PhlF=' + str(kd_PhlF) +
                            ',kd_YPF=' + str(kd_YPF) +
                            ',kd_HlyIIR=' + str(kd_HlyIIR) +
                            ',kd_BetI=' + str(kd_BetI) +
                            ',kd_AmtR=' + str(kd_AmtR),
                            '-exportresults',
                            str(exportResults),
                            '-cuddmaxmem',
                            str(maxmem)
                        ]
                        print(" ".join(command))
                        op = subprocess.check_output(command)
                        print(str(op).replace("\\n", "\n"))
                        exit()
