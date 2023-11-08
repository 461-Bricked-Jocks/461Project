import React from 'react'
import "../styles/projects.css";

class Projects extends React.Component {

    constructor(props){
        super(props)
        let params = new URLSearchParams(window.location.search);
        let userToken = params.get("Token")
        this.checkUserAuth(userToken)
        // let username = params.get('Username');
        // let password = params.get('Password');
        this.createProject = this.createProject.bind(this)
        this.joinProject = this.joinProject.bind(this)
        this.nameHandler = this.nameHandler.bind(this)
        this.descriptionHandler = this.descriptionHandler.bind(this)
        this.createProjectIDHandler = this.createProjectIDHandler.bind(this)
        this.joinExistingProjectIDHandler = this.joinExistingProjectIDHandler.bind(this)
        this.state = {
          name: "",
          description: "",
          createProjectID: "",
          joinExistingProjectID: "",
          createProjectSuccess: false,
          joinProjectSuccess: false,
          token: userToken
        }
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
            return true
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

      nameHandler(){
        var newName = document.getElementById("name").value
        console.log("User is trying to create project with name: ", newName)
        this.setState({
            name: newName
        })
      }

      descriptionHandler(){
        var newDescription = document.getElementById("description").value
        console.log("User is trying to create project with description: ", newDescription)
        this.setState({
          description: newDescription
        })
      }

      createProjectIDHandler(){
        var newCreateProjectIDHandler = document.getElementById("createProjectID").value
        console.log("User is trying to create project id: ", newCreateProjectIDHandler)
        this.setState({
          createProjectID: newCreateProjectIDHandler
        })
      }

      joinExistingProjectIDHandler(){
        var newJoinExistingProjectID = document.getElementById("joinExistingProjectID").value
        console.log("User is trying to join project id: ", newJoinExistingProjectID)
        this.setState({
          joinExistingProjectID: newJoinExistingProjectID
        })
      }

      createProject(){
        // window.location.search
        // "http://127.0.0.1:8000/login"
        fetch("http://127.0.0.1:8000/login",{
          method: "POST",
          mode: "cors",
          headers:{
            'content-Type':'application/json'
          },
          body: JSON.stringify({
            Name: this.state.name,
            Description: this.state.description,
            CreateProjectId: this.state.createProjectID,
          })
    
        })
          .then(response => response.json())
          // .then(data => this.handler(data["Access"]))
          .then((createProjectSuccess) => {
            //whatever the doc sends me
            var Access = createProjectSuccess['Access']
            console.log(Access)
            this.setState({
                createProjectSuccess : Access
            })
          })
          setTimeout(() => {
            //need to redirect to other page
            if(this.state.createProjectSuccess === true){
              window.alert("successfully created project")
              window.location.replace(`/Projects?ProjectName=${this.state.name}&Description=${this.state.description}&ProjectID=${this.state.createProjectID}`)
              
            }else{
              alert("Cannot Sucessfully Create New Project")
            }
          }, 500); // 2000 milliseconds = 2 seconds
          
    
    
      }

      joinProject(){
        fetch("http://127.0.0.1:8000/login",{
          method: "POST",
          mode: "cors",
          headers:{
            'content-Type':'application/json'
          },
          body: JSON.stringify({
            joinExistingProjectID: this.state.joinExistingProjectID
          })
    
        })
          .then(response => response.json())
          // .then(data => this.handler(data["Access"]))
          .then((joinProjectSuccess) => {
            //whatever the doc sends me
            var Access = joinProjectSuccess['Access']
            console.log(Access)
            this.setState({
                joinProjectSuccess : Access
            })
          })
          setTimeout(() => {
            //need to redirect to other page
            if(this.state.joinProjectSuccess === true){
              window.alert("successfully joined project")
              window.location.replace(`/Projects?joinExistingProjectID=${this.state.joinExistingProjectID}`)
            }else{
              alert("Cannot Successfully Join the Project ID:" , this.state.joinExistingProjectID)
            }
          }, 500); // 2000 milliseconds = 2 seconds
          
    
    
      }

    handleClick = () => {
        const params = new URLSearchParams(window.location.search);
        const username = params.get('Username');
        const password = params.get('Password');
        const queryString = window.location.search;
        console.log(queryString)
        console.log(username);
        console.log(password);
    }

    redirectToLogin() {
      // Redirect to login page
      window.location.href = '/';
    }

    render() {
            return (
        <div id = "back">

            <div id = "project">
                <h1>Create new Project</h1>
                <label>Name   </label>
                {/* <input type='text' name='user' ></input> */}
                <input id ="name" type='text' value={this.name} onChange={this.nameHandler}></input>
                {/* <input type='text' name='user' ></input> */}
                <br />
                <label>Description   </label>
                {/* <input type='text' name='user'></input> */}
                <input id ="description" type='text' value={this.description} onChange={this.descriptionHandler}></input>
                <br />
                <label>Project ID   </label>
                {/* <input type='text' name='user'></input> */}
                <input id ="createProjectID" type='text' value={this.createProjectID} onChange={this.createProjectIDHandler}></input>
                <br />
                <button onClick={this.createProject} id='createProjectBtn'>Create Project</button>
                {/* <button>Create Project</button> */}
                <br></br>
                <h1>Use Existing Project</h1>
                <label>Project ID   </label>
                {/* <input type='text' name='user'></input> */}
                <input id ="joinExistingProjectID" type='text' value={this.joinExistingProjectID} onChange={this.joinExistingProjectIDHandler}></input>
                <br />
                {/* <button>Join</button> */}
                <button onClick={this.joinProject} id='joinProjectBtn'>join</button>

                <button onClick={this.handleClick}>test</button>
                <button id='logOffButton' onClick={this.redirectToLogin}>Log Off</button>

                <br></br>
            </div>

        </div>
    );
    }
}

export default Projects;