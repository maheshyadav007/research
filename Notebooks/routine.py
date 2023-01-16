import shutil
import os

curr_dir_names = os.listdir()

# for name in curr_dir_names:
#     if name.endswith('.zip'):
#         filename = name
#         extract_dir = name[:-4]
#         shutil.unpack_archive(filename, extract_dir)

for name in curr_dir_names:
    if not name.endswith('.zip') and not name.endswith('.py'):
        
        if 'NTK' not in name:
            os.makedirs(f'{name}/all_figs', exist_ok=True)
            for file in os.listdir(name):
                if file.endswith('.png') or file.endswith('.pdf'):
                    if file.startswith('DLGN') or file.startswith('MLP'):
                        shutil.move(f'{name}/{file}', f'{name}/all_figs/{file[:50]}.png')
                    else:
                        shutil.move(f'{name}/{file}', f'{name}/all_figs/{file}')
        else:
            os.makedirs(f'{name}/all_NTK_figs', exist_ok=True)
            for file in os.listdir(name):
                if file.endswith('.png') or file.endswith('.pdf'):
                    if file.startswith('DLGN') or file.startswith('MLP'):
                        shutil.move(f'{name}/{file}', f'{name}/all_NTK_figs/{file[:50]}.png')
                    else:
                        shutil.move(f'{name}/{file}', f'{name}/all_NTK_figs/{file}')
for name in curr_dir_names:
    if not name.endswith('.zip') and not name.endswith('.py'):
        open(f'{name}/graphs.md', 'w').close()
        f = open(f'{name}/graphs.md', 'a')
        # for file in os.listdir(f'{name}/all_figs'):
            
        #     if not file.startswith('DLGN'):
        f.write(f'<p align="center"> <img src= all_figs/acc_epoch.png /> </p>')
        f.write('\n')
        f.write(f'<p align="center"> <img src= all_figs/acc_step.png /> </p>')
        f.write('\n')
        f.write(f'<p align="center"> <img src= all_figs/acc_epoch_modified.png /> </p>')
        f.write('\n')
        f.write(f'<p align="center"> <img src= all_figs/acc_step_modified.png /> </p>')
        f.write('\n')
        f.write(f'<p align="center"> <img src= all_figs/active_epoch_modified.png /> </p>')
        f.write('\n')
        f.write(f'<p align="center"> <img src= all_figs/active_steps_modified.png /> </p>')
        f.write('\n')
        # f.write(f'<p align="center"> <img src= all_figs/{loss_step.png} /> </p>')
        f.close()
        
        if 'NTK' not in name:
            open(f'{name}/overlap_kernel.md', 'w').close()
            f = open(f'{name}/overlap_kernel.md', 'a')
            for file in os.listdir(f'{name}/all_figs'):
                if file.startswith('DLGN') or file.startswith('MLP'):
                    f.write(f'<p align="center"> <img src= all_figs/{file} /> </p>')
                    f.write('\n')
            # f.write(f'<p align="center"> <img src= all_figs/{loss_step.png} /> </p>')
            f.close()
        else:
            open(f'{name}/NTK.md', 'w').close()
            f = open(f'{name}/NTK.md', 'a')
            for file in os.listdir(f'{name}/all_NTK_figs'):
                if file.startswith('DLGN') or file.startswith('MLP'):
                    f.write(f'<p align="center"> <img src= all_NTK_figs/{file} /> </p>')
                    f.write('\n')
            # f.write(f'<p align="center"> <img src= all_figs/{loss_step.png} /> </p>')
            f.close()
