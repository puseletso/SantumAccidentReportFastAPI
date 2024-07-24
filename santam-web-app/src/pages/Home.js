import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div>
      <h1>Welcome to the Santam Accident Report App</h1>
      <nav>
        <ul>
          <li><Link to="/add-report">Add Accident Report</Link></li>
          <li><Link to="/reports">View Accident Reports</Link></li>
        </ul>
      </nav>
    </div>
  );
}

export default Home;
