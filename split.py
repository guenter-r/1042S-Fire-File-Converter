import re

def qsplit(element):
    dict = {}
    dict['Record Type'] = element[0]
    dict['Return Type Indicator'] = element[1]
    dict['Pro Rata Basis Reporting'] = element[2]
    dict['Income Code'] = element[3:4]
    dict['Gross Income'] = element[5:16]
    dict['Withholding Allowance'] = element[17:28]
    dict['Net Income'] = element[29:40]
    dict['Chapter 3 TaxRate'] = element[41:43]
    dict['Chapter 3 Exemption Code'] = element[44:46]
    dict['Recipients Country of Residence Code for Tax Purposes'] = element[47:48]
    dict['Chapter 4 Tax Rate'] = element[49:51]
    dict['Chapter 4 Exemption Code'] = element[52:54]
    dict['Limitation on Benefits (LOB) Code '] = element[55:56]
    #dict['Reserved'] = element[57:58]
    dict['Amount Repaid'] = element[59:70]
    dict['Recipient Account Number'] = element[71:90]
    #dict['Reserved'] = element[91:92]
    dict['Recipients Name'] = element[93:212]
    dict['Recipients Street'] = element[213:292]
    dict['Recipients City'] = element[293:332]
    dict['Recipients State'] = element[333:334]
    dict['Recipients Province Code'] = element[335:336]
    dict['Recipients Country Code'] = element[337:338]
    dict['Postal or ZIP Code'] = element[339:347]
    dict['Recipients U.S. TIN'] = element[348:356]
    #dict['Reserved'] = element[357]
    dict['U.S. Federal Tax Withheld'] = element[358:369]
    dict['Withholding By Other Agents '] = element[370:381]
    dict['Total Withholding Credit'] = element[382:393]
    #dict['Reserved'] = element[394:399]
    dict['NQI/FLW-THR/PTP Name'] = element[400:519]
    #dict['Reserved'] = element[520:521]
    dict['NQI/FLW-THR/PTP Street'] = element[522:561]
    dict['NQI/FLW-THR/PTP City'] = element[602:641]
    dict['NQI/FLW-THR/PTP State Code'] = element[642:643]
    dict['NQI/FLW-THR/PTP Province Code'] = element[644:645]
    dict['NQI/FLW-THR/PTP Country Code'] = element[646:647]
    dict['NQI/FLW-THR/PTP Postal Code or ZIP Code'] = element[648:656]
    dict['NQI/FLW-THR/PTP U.S. TIN'] = element[657:665]
    dict['Payers Name'] = element[666:705]
    dict['Payers U.S. TIN'] = element[706:714]
    dict['State Income Tax Withheld'] = element[715:726]
    dict['Payers State Tax Number'] = element[727:736]
    dict['Payers State Code'] = element[737:738]
    dict['Special Data Entries'] = element[737:738]
    #dict['Reserved'] = element[760]
    dict['Recipients Foreign Tax I.D. Number'] = element[761:782]
    dict['Chapter Indicator'] = element[783]
    #dict['Reserved'] = element[784]
    dict['Recipients Chapter 3 Status Code'] = element[785:786]
    dict['Recipients Chapter 4 Status Code'] = element[787:788]
    dict['Tax Not dep./w IRS Pursuant EscrowP Ind.'] = element[789]
    dict['Recipients GIIN'] = element[790:808]
    dict['Amended Return Indicator'] = element[809]
    dict['Recipients Date of Birth '] = element[810:817]
    dict['Tax Paid by Withholding Agent'] = element[818:829]
    dict['Intermediary or FTE GIIN'] = element[830:848]
    dict['Intermediarys or FTEs Chapter 3 Status Code'] = element[849:850]
    dict['Intermediarys or FTEs Chapter 4 Status Code'] = element[851:852]
    dict['Intermediarys or FTEs Foreign Tax ID Number'] = element[853:874]
    dict['Payers GIIN'] = element[875:893]
    dict['Primary Withholding Agents Name'] = element[894:973]
    dict['Primary Withholding Agents EIN'] = element[974:982]
    dict['Payers Status 3 Status Code'] = element[983:984]
    dict['Payers Status 4 Status Code'] = element[985:986]
    dict['Unique Form Identifier'] = element[987:996]
    dict['Amendment Number'] = element[997]
    dict['Withholding Occurred in a Subsequent Year to a Partnership INT ind.'] = element[998]
    #dict['Reserved'] = element[999:1009]
    dict['Record Sequence Number'] = element[1010:1018]
    #dict['Blank'] = element[1018:1019]
    #d['Record Type'] = element.QRec()[0]

    # regex replacing blank fields with ''
    #for key,val in dict.items():
    #    dict[key] = re.sub('\s+','',dict[key])

    return dict
