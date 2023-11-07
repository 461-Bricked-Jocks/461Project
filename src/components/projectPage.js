import React from 'react'
import "../styles/projectPage.css";
import Project from './project';

class ProjectPage extends React.Component{
    constructor(props){
        super(props)
        let params = new URLSearchParams(window.location.search)
        let username = params.get("Username")
        let password = params.get("Password")
        this.create = this.create.bind(this)

        this.state = {
            user : username,
            pass : password,
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
        window.location.replace(`/Projects?Username=${this.state.user}&Password=${this.state.pass}`)
    }


    render(){
        return(
            <div className='projectPage'>
                <div className='projectPage2'>
                    <header>
                        <h1>Projects</h1>
                        <button id='createProj' onClick={this.create}>Create/Join Project</button>
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