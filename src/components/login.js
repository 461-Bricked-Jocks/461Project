import React from 'react'
import "../styles/login.css";
import { BrowserRouter as Routes, Route, useNavigate, Link, Navigate } from "react-router-dom";
import Projects from './projects';
// import { render } from '@testing-library/react';




class Login extends React.Component {
  constructor(props){
    super(props)
    this.login = this.login.bind(this)
    this.passwordHandler = this.passwordHandler.bind(this)
    this.usernameHandler = this.usernameHandler.bind(this)
    this.state = {
      user: "",
      pass: "",
      success: false
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
    fetch("http://127.0.0.1:8000/login",{
      method: "POST",
      mode: "cors",
      headers:{
        'content-Type':'application/json'
      },
      body: JSON.stringify({
        Username: this.state.user,
        Password: this.state.pass
      })

    })
      .then(response => response.json())
      // .then(data => this.handler(data["Access"]))
      .then((success) => {
        var Access = success['Access']
        var EncryptedUser = success['Username']
        var EncryptedPass = success['Password']
        console.log(Access)
        this.setState({
          success : Access,
          // user : EncryptedUser,
          // pass : EncryptedPass
        })
      })
      setTimeout(() => {
        if(this.state.success === true){
          window.alert("successfully signed in")
          window.location.replace(`/Projects-Page?Username=${this.state.user}&Password=${this.state.pass}`)
        }else{
          alert("Incorrect username or password")
        }
      }, 500); // 2000 milliseconds = 2 seconds
      


  }
  test(){
    window.location.replace("/Projects?Username=abc123&Password=pass123");
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
          {/* <button onClick={this.test}>test</button> */}
          <br/><br/>
          <Link to={"/projects"}>Forgot Password</Link>
          <br/><br/>
          <Link to='/Create-User'>Create New Account</Link> <br />
        </div>
      </div>
    )
  }
  
}

export default Login;