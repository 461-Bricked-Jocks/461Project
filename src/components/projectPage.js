import React from 'react'
import "../styles/projectPage.css";
import Project from './project';

class ProjectPage extends React.Component{
    constructor(props){
        super(props)
        let params = new URLSearchParams(window.location.search)
        let username = params.get("Username")
        let password = params.get("Password")
        let userToken = params.get("Token")
        this.checkUserAuth(userToken)
        this.create = this.create.bind(this)

        this.state = {
            user : username,
            pass : password,
            token : userToken,
            projectsArr : []
        }
        
        fetch("http://127.0.0.1:8000/login",{
            method: "POST",
            mode: "cors",
            headers:{
                'content-Type':'application/json'
            },
            body: JSON.stringify({
                Username: username,
                Password: password
            })
        })
        .then(response => response.json())
        // .then(data => this.handler(data["Access"]))
        .then((success) => {
        
          var Access = success['Access']
          var projects = [["jesus","testing","0","34"],["hello","testing","0","34"]]
        //   var projects = success['Projects']
        
          projects = this.makeList(projects)
          console.log(Access)
          this.setState({
            success : Access,
            projectsArr : projects
          })
        })
              
    }
    makeList(arr){
        let list = arr.map((project) => (
            <Project name={project[0]} description={project[1]} HW1={project[2]} HW2={project[3]}></Project>
        ));
        return list
    }
    create(){
        // console.log(this.state.userToken)
        window.location.replace(`/Projects?Token=${this.state.token}`)
        // window.location.replace(`/Projects?Username=${this.state.user}&Password=${this.state.pass}`)
    }

    redirectToLogin() {
        // Redirect to login page
        window.location.href = '/';
      }

      checkUserAuth(token){
        fetch("http://127.0.0.1:8000/isUserAuth", {
          method: "GET",
          headers: {
            'x-access-token': token  // Send the token as a header
          }
        })
        .then(response => response.json())
        .then((data) => {
          if(data.auth === true) {
            console.log("User is authenticated");
            // Perform actions based on authentication verification
            console.log("Should redirect")
            // window.location.replace(`/Projects-Page?Token=${token}`)
    
            // window.location.replace(`/Projects-Page?Token=${this.state.token}`)
            return 
          } else {
            console.log("User is not authenticated");
            this.redirectToLogin()
            return 
          }
        })
        .catch((error) => {
          console.error('Error:', error);
        });
      }  


    render(){
        return(
            <div className='projectPage'>
                <div className='projectPage2'>
                    <header>
                        <h1>Projects</h1>
                        <button id='createProj' onClick={this.create}>Create/Join Project</button>
                        <button id='logOffButton' onClick={this.redirectToLogin}>Log Off</button>
                        <hr></hr>
                    </header>
                    <ul>
                        {this.state.projectsArr}
                    </ul>
                </div>
            </div>

        )
    }
}

export default ProjectPage