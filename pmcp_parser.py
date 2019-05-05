import os
import xml.etree.ElementTree as ET



class PMCP_Parser():
    def __init__(self, filename):
        self.tree = ET.parse(filename)
        self.root = self.tree.getroot()

    def clear_all_devices(self, remain_asd2500_chip=True):
        devcfg_root = self.root.find('devcfg')

        for device in devcfg_root.findall('device'):
            if 'AST2500' in device.find('name').text:
                continue
            devcfg_root.remove(device)

        for device in devcfg_root.findall('device_connection'):
            if 'AST2500' in device.find('name').text:
                continue
            devcfg_root.remove(device)
        return

    def gen_prefix(self):
        xml_head = '<?xml version= "1.0" encoding="ISO-8859-1"?>\n<?MDS version= "1.8"?>'
        return
        
    def get_devcfg_root(self):
        devcfg_root = self.root.find('devcfg')
        newTree = ET.ElementTree()
        newTree._setroot(devcfg_root)
        return newTree
        #newTree.write('test.xml')

    def test(self):
        devcfg_root = self.root.find('devcfg')
        print(devcfg_root)
        for i in devcfg_root:
            print(i.tag)

if __name__ == "__main__":
    parser = PMCP_Parser('Wolfpass.pmc')
    parser.test()
    #parser.clear_all_devices()
    #parser.tree.write('output.xml')
    #parser.test()
