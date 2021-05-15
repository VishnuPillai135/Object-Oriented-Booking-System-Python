from .Provider import Provider
from .BookingSystem import BookingSystem
from .AdminSystem import AdminSystem
from .AuthenticationManager import AuthenticationManager
from .Patient import Patient, Admin
from .Location import Centre

def bootstrap_system(auth_manager):

    admin_system = AdminSystem(auth_manager)
    system = BookingSystem(admin_system, auth_manager)
    provnum = 1531
    #(name, email, service, phone, provnum)
    John = Provider("John","john123@gmail.com","GP","040223403","1531",["8:00","8:30","9:00","9:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30"],1)
    Harrison = Provider("Harrison","harrison123@gmail.com","pharmacist","041143708","1369",["8:00","8:30","9:00","9:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30"],3)
    Zelia = Provider("Zelia","zelia123@gmail.com","GP","04376054","9807",["8:00","8:30","9:00","9:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30"],4)
    Josh = Provider("Josh","josh123@gmail.com","physiotherapist","0428976432","6564",["8:00","8:30","9:00","9:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30"],5)
    Xuan = Provider("Xuan","xuan123@gmail.com"," pathologist","0476345678","3456",["8:00","8:30","9:00","9:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30"],4)
    David = Provider("David","david123@gmail.com","pharmacist","0486245721","3456",["8:00","8:30","9:00","9:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30"],3)
    Nate = Provider("Nate","nate123@gmail.com"," pathologist","0486245721","3456",["8:00","8:30","9:00","9:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30"],2)
    system.add_provider(John)
    system.add_provider(Harrison)
    system.add_provider(Zelia)
    system.add_provider(Josh)
    system.add_provider(Xuan)
    system.add_provider(David)
    system.add_provider(Nate)
    
    for name in ["Zac", "George", "Ian"]:
        # Username Password Email Name Phone Medicare
        system.add_patient(Patient(name, 'pass',"needhelp@gmail.com",name, "0428768345","1531"))
        
    Poke1 = Centre("Poke Centre 1","Asquith",[John, Harrison],5)
    Poke2 = Centre("Royal Prince Gold","Hornsby",[Josh],4)
    RPG = Centre("Royal Prince Silver","Hornsby",[David,Josh],3)
    RPS = Centre("Poke Centre 2","Asquith",[John],4)
    RPA = Centre("Royal Prince Alfred","Wahroonga",[Xuan],5)
    TheSan = Centre("The San","Wahroonga",[Harrison],1)
    AG = Centre("Asquith General","Asquith",[Zelia],2)
    HG = Centre("Hornsby General","Hornsby",[Nate],3)
    DS = Centre("Discount Surgery","Hornsby",[David],4)
    John.add_centres([Poke1,RPS])    
    Josh.add_centres([Poke2,RPG])
    David.add_centres([RPG,DS])
    Harrison.add_centres([Poke1,TheSan])
    Zelia.add_centres([AG])
    Nate.add_centres([HG])
    Xuan.add_centres([RPA])
    
    
    system.add_location(Poke1)
    system.add_location(Poke2)
    system.add_location(RPG)
    system.add_location(RPS) 
    system.add_location(RPA)
    system.add_location(TheSan)
    system.add_location(AG)
    system.add_location(HG)
    system.add_location(DS)
    
    
    admin_system.add_admin(Admin('ian', '123',"needhelp@gmail.com",name, "0428768345"))

    return system
    
    

