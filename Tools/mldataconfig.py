import csv
import progressbar
from astropy.io import fits
import numpy as np
import gc



##########################################################################################
#                                                                                        #
#    Function: dataasplit()                                                              #
#    Inputs: data .csv (should be same as output of exofinder()), index to split dataset #
#    Return: split datasets and full set                                                 #
#    Notes: output format is a list                                                      #
#                                                                                        #  
##########################################################################################
def datasplit(convdat, splitpoint):
    kepid = []
    url = []
    desig = []
    with open(convdat, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            kepid.append(row[0])
            url.append(row[1])
            desig.append(row[2])
    full = zip(kepid, url, desig)
    full = [list(ele) for ele in full]
    split1 = full[1:splitpoint]
    split2 = full[splitpoint:]
    return split1, split2, full

##########################################################################################
#                                                                                        #
#    Function: chunks()                                                                  #
#                                                                                        #
#    Notes: Self explanatory. Returns list of chunks from lst split with n members       #
#                                                                                        #  
##########################################################################################
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

        
##########################################################################################
#                                                                                        #
#    Function: getfluxes()                                                               #
#    Inputs: input datalist, output .csv                                                 #
#    Return: none                                                                        #
#    Notes: See Light_Curve_Demo notebook for internal functionality                     #
#                                                                                        #  
##########################################################################################
        
def getfluxes(dat, output):
    with open(output,'ab') as f:
        bar = progressbar.ProgressBar(maxval=len(dat)).start()
        for idx, i in enumerate(dat):
            ret = []
            k2_bjds = []
            pdcsap_fluxes = []
            fits_file = i[1]
            with fits.open(fits_file, mode="readonly") as hdulist:    
                k2_bjds = hdulist[1].data['TIME']
                #sap_fluxes = hdulist[1].data['SAP_FLUX']
                pdcsap_fluxes = hdulist[1].data['PDCSAP_FLUX']
            hdulist.close()
            del hdulist

            flux = np.transpose(pdcsap_fluxes)    
            ret = np.insert(pdcsap_fluxes, 0, i[0], axis=0)
            ret = np.insert(ret, 1, i[2], axis=0)
            #print('Finished: '+ i[0])
            np.savetxt(f, ret.reshape(1, ret.shape[0]), delimiter=",")
            del ret, k2_bjds, pdcsap_fluxes, fits_file, flux, i
            bar.update(idx)
        gc.collect()

##########################################################################################
#                                                                                        #
#    Function: normalize()                                                               #
#                                                                                        #
#    Notes: Self explanatory.                                                            #
#                                                                                        #  
##########################################################################################        
        
def normalize(data):
    data_mean = data.mean(axis=0)
    data_std = data.std(axis=0)
    return (data - data_mean) / data_std