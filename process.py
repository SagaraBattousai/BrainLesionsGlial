import sys
import os
import re

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import ganondorf.data.format_image_data as fid


def rename_files():
  scan_re = re.compile('.*Anatomic-.*\.nii')
  mask_re = re.compile('.*MaskTumor-.*\.nii')
  for root, sub, files in os.walk('.'):
    
    if sub != []:
      continue

    for fname in files:
      
      fname = os.path.join(x, fname)
      
      if scan_re.match(fname) != None:  
        nname = os.path.join(x, "Scan.nii")
      elif mask_re.match(fname) != None:
        nname = os.path.join(x, "Mask.nii")
      else:
        continue
      
      os.rename(fname, nname)




if __name__ == '__main__':
  # if len(sys.argv) > 1:
  #   fid.convert_dir_images_to_nii(sys.argv[1])
  # else:
  #   fid.convert_dir_images_to_nii()

  for root, dirnames, fnames in os.walk('.'):
    if dirnames != []:
      continue

    if next(filter(lambda filename: filename.endswith(".dcm"), fnames), False):

      print(root)

      fid.convert_dir_images_to_nii(
          outname=f'{root}/../../{os.path.basename(root)}.nii', dirname=root)




