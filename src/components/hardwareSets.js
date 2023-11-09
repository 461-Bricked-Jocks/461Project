import React from 'react'
import "../styles/login.css";


class HardwareSet extends React.Component{
    constructor(props){
        super(props)
        this.checkIn = this.checkIn.bind(this)
        this.checkOut = this.checkOut.bind(this)
        this.handleTextField = this.handleTextField.bind(this)
        this.state = {
            capacity: this.props.HWProps[0],
            availability: this.props.HWProps[1],
            checkedOut: this.props.HWProps[2],
            TextFieldValue: 0,
            butt: "Join",
            data: {}
        }
    }

    checkOut(){
        let input = Number(this.state.TextFieldValue)
        fetch("http://127.0.0.1:8000/checkOut",{
            method: "POST",
            mode: "cors",
            headers:{
                'content-Type':'application/json'
            },
            body: JSON.stringify({
                projectName: this.props.projectName,
                HardwareSet : this.props.name,
                qty : input
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
            if(this.state.success === false){
                window.alert(`You cannot checkout more than available`)
            }
            window.location.replace(`/Projects-Page?Username=${this.state.user}`)
        }, 500);
        // console.log(input)
        // let newCheckedOut = this.state.checkedOut + input
        // console.log(newCheckedOut)
        
        // if(newCheckedOut <= this.props.capacity){
        //     this.setState({
        //     checkedOut: newCheckedOut
        //     })
        // }
    }
    checkIn(){

        let input = Number(this.state.TextFieldValue)

        fetch("http://127.0.0.1:8000/checkIn",{
            method: "POST",
            mode: "cors",
            headers:{
                'content-Type':'application/json'
            },
            body: JSON.stringify({
                projectName: this.props.projectName,
                HardwareSet : this.props.name,
                qty : input
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
            if(this.state.success === false){
                window.alert(`You cannot checkIn more than you have`)
            }
            window.location.replace(`/Projects-Page?Username=${this.state.user}`)
        }, 500);


        // let newCheckedOut = this.state.checkedOut - input
        // if(newCheckedOut >= 0){
        //   this.setState({
        //     checkedOut: newCheckedOut
        //   })
        // }
    }
    handleTextField(event){
        var newVal = event.target.value
        this.setState({
            TextFieldValue : newVal
        })
    }
    


    render(){
        return(
            <div>
                <h3 className='HW'>{this.props.name}:</h3>
                <h4 className='HW'>Capacity: {this.state.capacity}</h4>
                <h4 className='HW'>Available: {this.state.availability}</h4>
                <h4 className='HW'>Checked Out: {this.state.checkedOut}</h4>
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
                <label>Amount:  </label>
                <input
                    label="amount" 
                    type='number'
                    id='amount'
                    value={this.state.TextFieldValue}
                    onChange={this.handleTextField}
                    />
                <br/>
            </div>

        )
    }
}

export default HardwareSet;