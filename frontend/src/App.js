// Importing modules
import { useState, useEffect } from "react";
import "./App.css";
 
function App() {
    // usestate for setting a javascript
    // object for storing and using data
    const [data, setData] = useState(null);
 
    // Using useEffect for single rendering
    useEffect(() => {
        let ignore = false
        setData(null)
        // Using fetch to fetch the api from 
        // flask server it will be redirected to proxy
        fetch("http://127.0.0.1:5000/test").then((res) =>
            res.json().then((data) => {
                if (!ignore) {
                    // Setting a data from api
                    setData(data);
                }
            })
        );
        return () => {
            ignore = true
        }
    }, [data]);
 
    return (
        <div className="App">
            <header className="App-header">
                <h1>React and flask</h1>
                {/* Calling a data from setdata for showing */}
                <p>{data.message}</p>
 
            </header>
        </div>
    );
}
 
export default App
