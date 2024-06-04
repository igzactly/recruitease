from flask import Blueprint,render_template,request
import json
import admin.admin_model as admin_model
admin=Blueprint("admin",__name__,url_prefix="/admin")

#page Loaders
@admin.route("/")
def dashboard():
    return render_template("dashboard.html")

@admin.route("/allAdmins")
def allAdmins():
    return render_template("admins.html")

@admin.route("/appconfig")
def appconfig():
    return render_template("appconfig.html")

@admin.route("/privilegegroups")
def privilegegroups():
    return render_template("privilegegroups.html")


#operations

@admin.route("/addAdmin",methods=["POST"])
def addAdmin():
    data=request.form["postdata"]
    userData=json.loads(data[1:-1])
    response={"data":admin_model.add(userData["name"],userData["phone"],userData["email"],userData["privilege_id"],userData["location"]),"message":"Admin Added successfully !"}
    return json.dumps(response)

@admin.route("/updateAdmin",methods=["POST"])
def updateAdmin():
    data=request.form["postdata"]
    userData=json.loads(data[1:-1])
    response={"data":admin_model.update(userData["id"],userData["name"],userData["phone"],userData["email"],userData["privilege_id"],userData["location"]),"message":"Admin Updated successfully !"}
    return json.dumps(response)

@admin.route("/getAllAdmin",methods=['POST'])
def getAllAdmin():
    response={"data":admin_model.getAllAdmin(),"message":"Admin fecthed successfully !"}
    return json.dumps(response)

@admin.route("/getAdminDetails",methods=['POST'])
def getAdminDetails():
    try:
        data=request.form["postdata"]
        userData=json.loads(data[1:-1])
        print(userData)
        response={"data":admin_model.get(userData["id"]),"message":"Login Successful !"}
        return json.dumps(response)
    except Exception as e:
        print(e.message, e.args)
        return False

@admin.route("/disableAdmin",methods=['POST'])
def disableAdmin():
    return "Disable Admin"

@admin.route("/enableAdmin",methods=['POST'])
def enableAdmin():
    return "Enable Admin"

@admin.route("/permanentlyDeleteAdmin",methods=['POST'])
def permanentlyDeleteAdmin():
    return "Delete  Admin"



#privilegeGroups


@admin.route("/getAllPrivilegeGroups",methods=['POST'])
def getAllPrivilegeGroups():
    response={"data":admin_model.getAllPrivilegeGroups(),"message":"Admin fecthed successfully !"}
    return json.dumps(response)

@admin.route("/getAllActivePrivilegeGroups",methods=['POST'])
def getAllActivePrivilegeGroups():
    response={"data":admin_model.getAllActivePrivilegeGroups(),"message":"Admin fecthed successfully !"}
    return json.dumps(response)


@admin.route("/addPrivilegeGroup",methods=["POST"])
def addPrivilegeGroup():
    data=request.form["postdata"]
    userData=json.loads(data[1:-1])
    response={"data":admin_model.addPrivilegeGroup(userData["name"],userData["privilegeBits"]),"message":"Admin Added successfully !"}
    return json.dumps(response)



@admin.route("/updatePrivilegeGroup",methods=["POST"])
def updatePrivilegeGroup():
    data=request.form["postdata"]
    userData=json.loads(data[1:-1])
    response={"data":admin_model.updatePrivilegeGroup(userData["id"],userData["name"],userData["privilegeBits"]),"message":"Admin Updated successfully !"}
    return json.dumps(response)

@admin.route("/disbalePrivilegeGroup",methods=['POST'])
def disbalePrivilegeGroup():
    return "Disable Admin"

@admin.route("/enablePriviegeGroup",methods=['POST'])
def enablePriviegeGroup():
    return "Enable Admin"


@admin.route("/getPrivilegeGroupDetails",methods=['POST'])
def getPrivilegeGroupDetails():
    try:
        data=request.form["postdata"]
        userData=json.loads(data[1:-1])
        print(userData)
        response={"data":admin_model.getPrivilegeGroupDetails(userData["id"]),"message":"Details Fetched Successfully !"}
        return json.dumps(response)
    except Exception as e:
        print(e.message, e.args)
        return False