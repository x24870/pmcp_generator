from bmcDesginReader import sheetReader
from pmcp_parser import PMCP_Parser
from adc_hdlr import adc_handler

class Pmcp_generator():
    def __init__(self, f_sheet, f_pmcp):
        # Read BMC design sheet to get following information:
        # 1. ADC
        # 2. Temperature
        self.reader = sheetReader()
        self.reader.read_bmc_design_sheet(f_sheet)

        # Load PMCP file and get <devcfg> root
        self.parser = PMCP_Parser(f_pmcp)

    def update_pmcp(self, f_sheet, f_pmcp):
        # Update <devcfg> root(ADC, temperature)
        # 1. updating ADC
        self.adc_handler = adc_handler.adc_hdlr(os.path.join(os.getcwd(), 'adc_hdlr'))
        self.adc_handler.update_ADC(self.reader.get_ADC_info(), self.parser.get_devcfg_root())


if __name__ == '__main__':
    generator = Pmcp_generator('BMC_design.xlsx', 'Wolfpass.pmc')