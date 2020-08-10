import os,sys

#grid_rows=['40']
#grid_rows= ['5']
grid_rows= ['50']
grid_cols =  grid_rows
grids_ll = [x+'x'+y for (x,y) in zip(grid_rows,grid_cols)]
print(grids_ll)
htc_ll = ['0.01']
#htc_ll = ['1e5']
chiplabel='M3D'
folder = '../M3D_covert/'
lcf = folder + 'lcf_files/'+chiplabel
modelParams = folder+'modelParams_files/modelParams_M3D.config'
runName = 'MyToolRun'
grid_folder = folder+'results/'+chiplabel+"/"



for grids in grids_ll:
    log_file = folder + "logs/"+chiplabel+"_"+grids+".log"
    scp_folder="/projectnb/peaclab-cri-cooling/EDAToolDevelopment/Zihao_ToolCopy/steady_temperature/"
    modelParamsFile = modelParams
    for htc in htc_ll:
        configFile = folder+'config_files/M3D.config'
        #configFile = folder+'config_files/default_htc_'+htc+'_'+'10mm'+'.config'
        lcf_file = lcf+'_lcf.csv'	
        outfile = chiplabel+"_"+grids+'.grid.steady'
        grid_file = grid_folder+outfile
        scp_file = folder+outfile
        os.system('M3D.sh '+ lcf_file + ' ' + configFile + ' ' + modelParamsFile + ' ' + grid_file + ' ' + scp_file + ' ' + log_file)

