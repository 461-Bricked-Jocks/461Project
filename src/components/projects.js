import React from 'react'
import "../styles/projects.css";

export default function Projects() {
    return (
        <div id = "back">

            <div id = "project">
                <h1>Create new Project</h1>
                <label>Name   </label>
                <input type='text' name='user'></input>
                <br />
                <label>Description   </label>
                <input type='text' name='user'></input>
                <br />
                <label>Project ID   </label>
                <input type='text' name='user'></input>
                <br />
                <button>Enter</button>
                <br></br>
                <h1>Use Existing Project</h1>
                <label>Project ID   </label>
                <input type='text' name='user'></input>
                <br />
                <button>Enter</button>
                <br></br>
            </div>

        </div>
    )
}