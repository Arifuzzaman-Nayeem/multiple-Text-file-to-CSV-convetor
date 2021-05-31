import pandas as pd

class df_gen:
    def __init__(self,name,rot_lenght,mom_length):
        self.n,self.rl,self.ml = name,rot_lenght,mom_length
        print('Start generating :',self.n)
    def create_df(self):
        self.file_name = self.n+'-Result.txt'
        self.text = open(self.file_name).read()
        self.lines = self.text.split('\n')
        self.df = pd.DataFrame({'Time': [], 'Disp(mm)': [], 'Force(N)': []})
        for self.i in range (4,len(self.lines)):
            self.a = self.lines[self.i].split()
            if self.a != []:
                self.a, self.b, self.c = self.a
                self.df.loc[str(self.i-4)] = [float(self.a), float(self.b)*-1, float(self.c)*-1]
        print('Complete generating :', self.n)
    def moment_rot_gen(self):
        self.create_df()
        self.df['Rotation'] = self.df['Disp(mm)']/self.rl
        self.df['Moment(kN/M)'] = self.df['Force(N)']*self.ml*10**-6
        self.df = self.df.drop(['Time'],axis = 'columns')
        return self.df


name_list = ['CH_Test_C310','CH_Test_C355','CH_Test_C460','CH_Test_S310','CH_Test_S355','CH_Test_S460','CH_Test_C310-M','CH_Test_C355-M','CH_Test_C460-M','CH_Test_S310-M','CH_Test_S355-M','CH_Test_S460-M']
moment_length = 2500
rotational_length = 2700


final_df = pd.DataFrame()
dummy_df = pd.DataFrame({'none' : ['-']})
for i in range (0,len(name_list)):
    df = df_gen(name_list[i],rotational_length,moment_length).moment_rot_gen()
    final_df = pd.concat([final_df,df],axis='columns')

final_df.to_csv('Result_csv.csv')