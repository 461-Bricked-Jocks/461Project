import React from 'react'
import "./login.css";

export default function CreateUser() {
  return (
    <div id = "back">

      <div id = "login">
        <h1>Bricked Jocks</h1>
        <label>Username   </label>
        <input type='text' name='user'></input>
        <br/><br/>
        <label>Password</label>
        <input type='password' name='user'></input>
        <br/><br/>
        <label>Re-enter Password</label>
        <input type='password' name='user'></input>
        <br/><br/>
        <button>Login</button>
        <br/><br/>
        <a href=''>Forgot Password</a>
        <br/><br/>
        <a href='/'>Sign in</a> <br />
      </div>

    </div>
  )
}