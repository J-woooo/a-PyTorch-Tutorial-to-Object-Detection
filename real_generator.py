#real_generator
import numpy as np
import numpy
import os
import nibabel as nib
import matplotlib.pyplot as plt
import cv2

root = "/data/hcc_bounded/hcc_bounded/"

file_nums = list(range(1055,1056))

for file_num in file_nums:
        file = "Anonymize_" + str(file_num).zfill(4)+"/"
        path_data = root+file
        try:
            Precontrast = os.path.join(root, 'R_Anonymize_'+str(file_num).zfill(4)+'.nii')
            Arterial = os.path.join(root, 'A_Anonymize_'+str(file_num).zfill(4)+'.nii')
            Portal = os.path.join(root, 'P_Anonymize_'+str(file_num).zfill(4)+'.nii')
         
            
            r = nib.load(Precontrast).get_fdata()
            a = nib.load(Arterial).get_fdata()
            p = nib.load(Portal).get_fdata()
    
            height, width, channel  = p.shape
            
            matrix = cv2.getRotationMatrix2D((width/2, height/2), 270, 1)
            pre_img = cv2.warpAffine(r, matrix, (width, height))
            art_img = cv2.warpAffine(a, matrix, (width, height))
            por_img = cv2.warpAffine(p, matrix, (width, height)) 
            
        
            #make directory
        
            folder_root = "/home/jwbae/hcc_bounded_image/"
            def createFolder(folder_root):
                try:
                    if not os.path.exists(folder_root):
                        os.makedirs(folder_root)
                except OSError:
                        print('Error: Creating directory. ' + folder_root)
            createFolder(folder_root+file)
            length = por_img.shape[-1]
            #print & save image
            for i in range(0,length):
                print("[",file_num,"] ",str(i+1)+"/"+str(length))
                plt.subplot(131)
                fig = plt.figure(1)
                plt.axis("off") # delete axis
                plt.title('Precontrast '+str(i)) # PreContrast
                plt.imshow(pre_img[::,::,i],cmap = "gray")
        
                plt.subplot(132)
                plt.axis("off") # delete axis
                plt.title('Arterial '+str(i)) # Arterial
                plt.imshow(pre_img[::,::,i],cmap = "gray")
        
                plt.subplot(133)
                plt.axis("off") # delete axis
                plt.title('Portal '+str(i)) # Portal
                plt.imshow(por_img[::,::,i],cmap = "gray")
                plt.show()
        
                a = np.expand_dims(pre_img[::,::,i],-1)
                b = np.expand_dims(art_img[::,::,i],-1)
                c = np.expand_dims(por_img[::,::,i],-1)
        
                arr = np.concatenate((c,b,a), axis=-1)
                plt.imshow(arr, cmap ="gray")
        
                plt.axis('off')
                plt.xticks([]), plt.yticks([])
                plt.tight_layout()
                plt.subplots_adjust(left = 0, bottom = 0, right = 1, top = 1, hspace = 0, wspace = 0)
            
                cv2.imwrite(folder_root+file+'/'+str(file_num)+"_"+str(i).zfill(4)+'.png',arr) 
        except:
         # continue
          print("No File : {}".format(file_num))                
               
