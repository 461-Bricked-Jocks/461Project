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
                <h3 className='projName'>Project: {this.props.name}</h3>
                <button className='leave'>Leave project</button>
                <p className='description'>Description: {this.props.description}</p>
                <div id='HWSets'>
                    <div className='HWSet'>
                    <HardwareSet name='Hardware Set 1' 
                                capacity ='2000' 
                                HW={this.props.HW1}/>
                    </div>
                    <div className='HWSet'>
                    <HardwareSet name='Hardware Set 2' 
                                capacity ='2000' 
                                HW={this.props.HW2}/>
                    </div>
                </div>
            </div>
        )
    }
}

export default Project;