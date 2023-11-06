import React from 'react'
import "../styles/projectPage.css";
import HardwareSet from './hardwareSets';

class Project extends React.Component{
    
    constructor(props){
        super(props)
    }

    render(){
        return(
            <div className="project">
                <h3 id='projName'>Project: {this.props.name}</h3>
                <HardwareSet capacity ='2000' HW1={this.props.HW1} HW2={this.props.HW2}></HardwareSet>
            </div>

        )
    }
}

export default Project;