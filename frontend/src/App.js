import React, { useEffect, useState } from "react";
import io from "socket.io-client";

const socket = io("http://localhost:5000"); // Flask backend

function App() {
  const [incidents, setIncidents] = useState([]);

  // Fetch existing incidents from backend
  useEffect(() => {
    fetch("http://localhost:5000/api/incidents")
      .then((res) => res.json())
      .then((data) => setIncidents(data))
      .catch((err) => console.error("Error fetching incidents:", err));
  }, []);

  // Listen for live alerts from Flask Socket.IO
  useEffect(() => {
    socket.on("new_alert", (data) => {
      setIncidents((prev) => [data, ...prev]); // prepend new alert
    });
    return () => socket.off("new_alert");
  }, []);

  return (
    <div
      style={{
        backgroundColor: "#0d1117",
        color: "#e6edf3",
        minHeight: "100vh",
        padding: "20px",
        fontFamily: "Segoe UI, sans-serif",
      }}
    >
      <h1 style={{ textAlign: "center", color: "#58a6ff" }}>
        🧠 Real-Time Intrusion Detection Dashboard
      </h1>

      <table
        style={{
          width: "100%",
          borderCollapse: "collapse",
          marginTop: "20px",
          background: "#161b22",
        }}
      >
        <thead>
          <tr style={{ background: "#21262d" }}>
            <th style={th}>Time</th>
            <th style={th}>Source IP</th>
            <th style={th}>Destination IP</th>
            <th style={th}>Type</th>
            <th style={th}>Details</th>
          </tr>
        </thead>
        <tbody>
          {incidents.map((inc, i) => (
            <tr key={i} style={{ borderBottom: "1px solid #30363d" }}>
              <td style={td}>{inc.timestamp}</td>
              <td style={td}>{inc.src_ip}</td>
              <td style={td}>{inc.dst_ip}</td>
              <td style={td}>{inc.type}</td>
              <td style={td}>{inc.details}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

const th = {
  padding: "10px",
  borderBottom: "2px solid #30363d",
  color: "#58a6ff",
  textAlign: "left",
};

const td = {
  padding: "10px",
  color: "#c9d1d9",
};

export default App;

