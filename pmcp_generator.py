from bmcDesginReader import sheetReader
from pmcp_parser import PMCP_Parser

class Pmcp_generator():
    def __init__(self, f_sheet, f_pmcp):
        # Read BMC design sheet to get following information:
        # 1. ADC
        # 2. Temperature
        reader = sheetReader()
        reader.read_bmc_design_sheet(f_sheet)

        # Load PMCP file and get <devcfg> root
        parser = PMCP_Parser(f_pmcp)

    def update_pmcp(self, f_sheet, f_pmcp):
        # Update <devcfg> root(ADC, temperature)
        pass



if __name__ == '__main__':
    generator = Pmcp_generator('BMC_design.xlsx', 'Wolfpass.pmc')