from app import app,create_admin

#-------------------------------------------------------------- App Run --------------------------------------------------#

if __name__=="__main__":
    create_admin()  # Creates admin When Database Is Created
    app.run(debug=True)    # Remove Debugging options When Deploying the Project
