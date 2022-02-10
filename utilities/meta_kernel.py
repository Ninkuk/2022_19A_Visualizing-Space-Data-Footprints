import imp
import os
import re

kernel_file_extensions = {
    "SPK": [".bsp", ".xsp"],
    "PCK": [".tpc", ".bpc", ".xpc"],
    "IK": [".ti"],
    "FK": [".tf"],
    "LSK": [".tls"],
    "CK": [".bc", ".xc"],
    "SCLK": [".tsc"],
    "MK": [".tm"],
    "DSK": [".bds"],
    "DBK": [".bdb", ".xdb"]
}


def create_dynamic_meta_kernel(meta_kernel_name):
    meta_kernel_file = f"./kernels/{meta_kernel_name.replace('.tm', '')}.tm"

    kernels = os.listdir('./kernels/')

    with open(meta_kernel_file, 'w') as meta_kernel:
        kernels_to_load = []

        for kernel in kernels:
            if os.path.isdir(f"./kernels/{kernel}"):
                allowed_extensions = kernel_file_extensions[kernel.upper()]
                for file in os.listdir(f'./kernels/{kernel}/'):
                    [kernels_to_load.append(f"'kernels/{kernel}/{file}'") for extension in allowed_extensions if file.endswith(extension)]

        kernels_string = ",\n\t".join(kernels_to_load)

        meta_kernel.writelines([r"\begindata", "\n", f"KERNELS_TO_LOAD = ({kernels_string})", "\n", r"\begintext"])

    return(meta_kernel_file)


if __name__ == "__main__":
    create_dynamic_meta_kernel()
