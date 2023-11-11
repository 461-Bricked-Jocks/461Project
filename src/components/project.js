import React from 'react'
import "../styles/projectPage.css";
import HardwareSet from './hardwareSets';

class Project extends React.Component{
    
    constructor(props){
        super(props)
        this.leave = this.leave.bind(this)
        this.state = {
            projName : this.props.name,
            user: this.props.user,
            success: false
        }
    }
    leave(){
        console.log(this.state.user)
        console.log(this.state.projName)
        fetch("http://127.0.0.1:8000/leaveProject",{
            method: "POST",
            mode: "cors",
            headers:{
                'content-Type':'application/json'
            },
            body: JSON.stringify({
                Username: this.state.user,
                projectName: this.state.projName
            })
        })
        .then(response => response.json())
        // .then(data => this.handler(data["Access"]))
        .then((success) => {
            var Access = success['Access']
            //var Access = true
            console.log("test")
            console.log(Access)
            this.setState({
                success : Access,
            })
        })
        setTimeout(() => {
            if(this.state.success === true){
            window.alert(`successfully left Project: ${this.props.name}`)
            window.location.replace(`/Projects-Page?Username=${this.state.user}`)
            }else{
            alert("error leaving Project")
            window.location.replace(`/Projects-Page?Username=${this.state.user}`)
            }
        }, 500);
    }

    render(){
        return(
            <div className="project">
                <h3 className='projName'>Project: {this.props.name}</h3>
                <button className='leave' onClick={this.leave}>Leave project</button>
                <p className='description'>Description: {this.props.description}</p>
                <div id='HWSets'>
                    <div className='HWSet'>
                    <HardwareSet name='Hardware Set 1' 
                                projectName = {this.props.name}
                                HWProps={this.props.HW1}/>
                    </div>
                    <div className='HWSet'>
                    <HardwareSet name='Hardware Set 2' 
                                projectName = {this.props.name}
                                HWProps={this.props.HW2}/>
                    </div>
                </div>
            </div>
        )
    }
}

export default Project;