import React, { useState } from 'react';
import { JsonToTable } from "react-json-to-table";
import './App.css';

function App() {

  const [load, setLoading] = useState(false); //load prompt when retrieving data
  const [data, setData] = useState(null);

  const handleSubmit = (e) => {
    setLoading(true);
    e.preventDefault();

    const filename = e.target[0].value;

    async function getData() {
      const response = await fetch('/' + filename, {  //GET request through proxy
        headers: {
          'Content-Type': 'application/json'
        }
      });

      const json = await response.json();

      setLoading(false);
      setData(json);
    }

    getData();
  }

  function RenderLoad() {
    if(load) {
      return <p>Retrieving data...</p>
    }
    else {
      return null;
    }
    
  }

  function noData() {
    return (
      <header className="App-header">
        <RenderLoad/>
        <form onSubmit={handleSubmit}>
          <input type="text" placeholder="Filename with filetype"></input>
          <button type="submit">Get Data</button>
        </form>
      </header>
    )
  }

  function SetRender() {
    if(data == null) {
      return noData();
    }
    else {
      return <JsonToTable json={data}/>
    }
  }

  return (
    <div className="App">
      <SetRender/>   
    </div>
  );
}

export default App;
