import React from 'react'
import "../styles/projectPage.css";
import HardwareSet from './hardwareSets';

class Project extends React.Component{
    
    // constructor(props){
    //     super(props)
    // }
    leave(){
        fetch("http://127.0.0.1:8000/leaveProject",{
            method: "POST",
            mode: "cors",
            headers:{
                'content-Type':'application/json'
            },
            body: JSON.stringify({
                Username: this.props.user,
                projectName: this.props.name
            })
        })
        .then(response => response.json())
        // .then(data => this.handler(data["Access"]))
        .then((success) => {
            var Access = success['Access']
            console.log(Access)
            this.setState({
                success : Access,
            })
        })
        setTimeout(() => {
            if(this.state.success === true){
            window.alert(`successfully left Project: ${this.props.name}`)
            }else{
            alert("error leaving Project")
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