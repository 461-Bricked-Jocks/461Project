import React from 'react'
import "../styles/login.css";
import { BrowserRouter as Routes, Route, useNavigate, Link, Navigate } from "react-router-dom";
import Projects from './projects';

class HardwareSet extends React.Component{
    constructor(props){
        super(props)
        this.checkIn = this.checkIn.bind(this)
        this.checkOut = this.checkOut.bind(this)
        // this.join = this.join.bind(this)
        // this.handleTextField = this.handleTextField.bind(this)
        this.state = {
            checkedOut: 0,
            TextFieldValue: 0,
            butt: "Join",
            data: {}
        }
    }
    checkOut(){
        let input = Number(document.getElementById("amount").value)
        console.log(input)
        let newCheckedOut = this.state.checkedOut + input
        console.log(newCheckedOut)
        
        if(newCheckedOut <= this.props.capacity){
            this.setState({
            checkedOut: newCheckedOut
            })
        }
    }
    checkIn(){
        let input = Number(document.getElementById("amount").value)
        let newCheckedOut = this.state.checkedOut - input
        if(newCheckedOut >= 0){
          this.setState({
            checkedOut: newCheckedOut
          })
        }
    }
    


    render(){
        return(
            <div>
                <h3 className='HW'>{this.props.name}:</h3>
                <h4 className='HW'>Capacity: {this.props.capacity}</h4>
                <h4 className='HW'>checkedOut: {this.state.checkedOut}</h4>
                <br/>
                <button  
                    variant='contained' 
                    onClick={this.checkIn}
                    className="Button">
                    Check-In
                </button>
                <br/>
                <br/>
                <button  
                    variant='contained' 
                    onClick={this.checkOut}
                    className="Button">
                    Check-out
                </button>
                {/* <button id='join' onClick={this.join}>{this.state.butt}</button> */}
                <br/>
                <input
                    label="amount" 
                    type='number'
                    id='amount'
                    // value={this.state.TextFieldValue}
                    // onChange={this.handleTextField}
                    />
                <br/>
                {/* <TextField variant="outlined" label="amount" className='TextField'/> */}
                {/* <h3 className='HW'>HardWare Set 2:</h3>
                <h4 className='HW'>Capacity: {this.props.capacity}</h4>
                <h4 className='HW'>checkedOut: {this.state.checkedOut}</h4>
                <br/>
                <button  
                    variant='contained' 
                    onClick={this.checkIn}
                    className="Button">
                    Check-In
                </button>
                <br/>
                <br/>
                <button  
                    variant='contained' 
                    onClick={this.checkOut}
                    className="Button">
                    Check-out
                </button> */}
            </div>

        )
    }
}

export default HardwareSet;