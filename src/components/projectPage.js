import React from 'react'
import "../styles/projectPage.css";
import Project from './project';

class ProjectPage extends React.Component{
    constructor(props){
        super(props)
        let params = new URLSearchParams(window.location.search)
        let username = params.get("Username")
        this.create = this.create.bind(this)

        this.state = {
            user : username,
            projectsArr : []
        }
        
        fetch("http://127.0.0.1:8000/projectPage",{
            method: "POST",
            mode: "cors",
            headers:{
                'content-Type':'application/json'
            },
            body: JSON.stringify({
                Username: username
            })
        })
        .then(response => response.json())
        // .then(data => this.handler(data["Access"]))
        .then((success) => {
            //var Access = success['Access']
            var Access = true
            //var projects = [["1","testing",[[2000,1000,20],[2000,1500,32]]],["2","testing",[2000,1000,250],[2000,1500,200]]]
            var projects = success['projectList']
        
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
            <Project name={project[0]} description={project[1]} HW1={project[2][0]} HW2={project[2][1]}></Project>
        ));
        return list
    }
    create(){
        window.location.replace(`/Projects?Username=${this.state.user}`)
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