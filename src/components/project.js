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
                <div id='HWSets'>
                    <div className='HWSet'>
                    <HardwareSet name='Hardware Set 1' 
                                capacity ='2000' 
                                HW1={this.props.HW1} 
                                HW2={this.props.HW2}/>
                    </div>
                    <div className='HWSet'>
                    <HardwareSet name='Hardware Set 2' 
                                capacity ='2000' 
                                HW1={this.props.HW1} 
                                HW2={this.props.HW2}/>
                    </div>
                </div>
            </div>

        )
    }
}

export default Project;