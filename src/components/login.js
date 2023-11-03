import React from 'react'
import "./login.css";
// import { render } from '@testing-library/react';




class Login extends React.Component {
  constructor(props){
    super(props)
    this.login = this.login.bind(this)
    this.passwordHandler = this.passwordHandler.bind(this)
    this.usernameHandler = this.usernameHandler.bind(this)
    // this.checkIn = this.checkIn.bind(this)
    // this.checkOut = this.checkOut.bind(this)
    // this.join = this.join.bind(this)
    // this.handleTextField = this.handleTextField.bind(this)
    this.state = {
      user: "",
      pass: ""
    }
  }
  passwordHandler(){
    var newPass = document.getElementById("password").value
    this.setState({
      pass: newPass
    })
    

  }
  usernameHandler(){
    var newUser = document.getElementById("username").value
    this.setState({
      user: newUser
    })
  }
  login(){
    console.log(this.state.user)
    console.log(this.state.pass)
  }

  render(){
    return (
      <div id = "back">
  
        <div id = "login">
          <h1>Bricked Jocks</h1>
          <label>Username   </label>
          <input id="username" type='text' name='user' value={this.user} onChange={this.usernameHandler}></input>
          <br/><br/>
          <label>Password</label>
          <input id="password" type='password' name='user' value={this.pass} onChange={this.passwordHandler}></input>
          <br/><br/>
          <button onClick={this.login} id='loginBtn'>Login</button>
          <br/><br/>
          <a href=''>Forgot Password</a>
          <br/><br/>
          <a href='/Create-User'>Create New Account</a> <br />
        </div>
      </div>
    )
  }
  
}

export default Login;