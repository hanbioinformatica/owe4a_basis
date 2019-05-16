from Bio.Blast import NCBIXML

sequence = "CGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTGATGAGACCGTGGAATAAA"

# print("BLASTEN")
# result_handle = NCBIWWW.qblast("blastn", "nr", sequence)
# print("Geblast")
#
# bestand = open("blast_report.xml", "w")
# resultaat_xml = result_handle.readlines()
# bestand.writelines(resultaat_xml)
# bestand.close()

result_handle = open("blast_report.xml", "r")
blast_records = NCBIXML.parse(result_handle)
blast_record = next(blast_records)

for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        print("-"*80)
        print("sequence: ", alignment.title)
        print("lengte:   ", alignment.length)
        print("e-value:  ", hsp.expect)
        print(hsp.query)
        print(hsp.match)
        print(hsp.sbjct)
