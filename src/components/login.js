import React from 'react'
import "./login.css";

export default function Login() {
  return (
    <div id = "back">

      <div id = "login">
        <h1>Bricked Jocks</h1>
        <label>Username   </label>
        <input type='text' name='user'></input>
        <br/><br/>
        <label>Password   </label>
        <input type='password' name='user'></input>
        <br/><br/>
        <button>Login</button>
        <br/><br/>
        <a href=''>Forgot Password</a>
        <br/><br/>
        <a href='/Create-User'>Create New Account</a> <br />
      </div>
    </div>
  )
}