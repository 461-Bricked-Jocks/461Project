// import logo from './logo.svg';
import './App.css';
import Login from './components/login'
import Projects from './components/projects.js';
import CreateUser from './components/CreatUser';
import ProjectPage from './components/projectPage';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import React from 'react';

// function App() {
//   return (
//     <div className="App">
//       <Login />
//     </div>
//   );
// }

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Login />}>
                    {/*<Route path="projects" element={<Projects />} />*/}
                    {/*/!*{ <Route path="*" element={<NoPage />} />}*!/*/}
                </Route>
                <Route path="/projects" element={<Projects />}>
                    {/*<Route path="projects" element={<Projects />} />*/}
                    {/*/!*{ <Route path="*" element={<NoPage />} />}*!/*/}
                </Route>
                <Route path="/Create-User" element={<CreateUser />}>
                    {/*<Route path="projects" element={<Projects />} />*/}
                    {/*/!*{ <Route path="*" element={<NoPage />} />}*!/*/}
                </Route>
                <Route path="/Projects-Page" element={<ProjectPage />}>
                    {/*<Route path="projects" element={<Projects />} />*/}
                    {/*/!*{ <Route path="*" element={<NoPage />} />}*!/*/}
                </Route>
            </Routes>
        </BrowserRouter>
    );
}

export default App;
