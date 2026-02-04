import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import logo from './octofitapp-small.png';
import Users from './components/Users';
import Teams from './components/Teams';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">
              <img src={logo} alt="OctoFit Logo" className="navbar-brand-logo" />
              OctoFit Tracker
            </Link>
            <button 
              className="navbar-toggler" 
              type="button" 
              data-bs-toggle="collapse" 
              data-bs-target="#navbarNav" 
              aria-controls="navbarNav" 
              aria-expanded="false" 
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <Link className="nav-link" to="/users">Users</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">Teams</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">Activities</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">Workouts</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={
            <div className="container mt-5">
              <div className="jumbotron p-5 mb-4 bg-light rounded-3 border border-success">
                <div className="container-fluid py-5">
                  <h1 className="display-4 fw-bold">Welcome to OctoFit Tracker! 🏋️</h1>
                  <p className="lead fs-4">Track your fitness activities, compete with your team, and reach your goals.</p>
                  <hr className="my-4 border-success" />
                  <p className="fs-5">Use the navigation menu above to explore users, teams, activities, leaderboard, and workout suggestions.</p>
                  <div className="d-grid gap-2 d-md-flex justify-content-md-start mt-4">
                    <Link to="/activities" className="btn btn-success btn-lg px-4 me-md-2">
                      View Activities
                    </Link>
                    <Link to="/leaderboard" className="btn btn-outline-primary btn-lg px-4">
                      See Leaderboard
                    </Link>
                  </div>
                </div>
              </div>
              
              <div className="row row-cols-1 row-cols-md-3 g-4 mt-3">
                <div className="col">
                  <Link to="/users" className="text-decoration-none">
                    <div className="card h-100 border-info shadow-sm" style={{cursor: 'pointer'}}>
                      <div className="card-body text-center">
                        <h3 className="card-title">👤 Users</h3>
                        <p className="card-text">View all registered users and their profiles!</p>
                        <span className="btn btn-info">View Users</span>
                      </div>
                    </div>
                  </Link>
                </div>
                <div className="col">
                  <Link to="/teams" className="text-decoration-none">
                    <div className="card h-100 border-primary shadow-sm" style={{cursor: 'pointer'}}>
                      <div className="card-body text-center">
                        <h3 className="card-title">👥 Teams</h3>
                        <p className="card-text">Join or create a team and compete together!</p>
                        <span className="btn btn-primary">View Teams</span>
                      </div>
                    </div>
                  </Link>
                </div>
                <div className="col">
                  <Link to="/activities" className="text-decoration-none">
                    <div className="card h-100 border-success shadow-sm" style={{cursor: 'pointer'}}>
                      <div className="card-body text-center">
                        <h3 className="card-title">🏃 Activities</h3>
                        <p className="card-text">Track your workouts and fitness progress!</p>
                        <span className="btn btn-success">Track Activities</span>
                      </div>
                    </div>
                  </Link>
                </div>
                <div className="col">
                  <Link to="/leaderboard" className="text-decoration-none">
                    <div className="card h-100 border-danger shadow-sm" style={{cursor: 'pointer'}}>
                      <div className="card-body text-center">
                        <h3 className="card-title">🏆 Leaderboard</h3>
                        <p className="card-text">Check out the top performers and rankings!</p>
                        <span className="btn btn-danger">View Leaderboard</span>
                      </div>
                    </div>
                  </Link>
                </div>
                <div className="col">
                  <Link to="/workouts" className="text-decoration-none">
                    <div className="card h-100 border-warning shadow-sm" style={{cursor: 'pointer'}}>
                      <div className="card-body text-center">
                        <h3 className="card-title">💪 Workouts</h3>
                        <p className="card-text">Get personalized workout suggestions!</p>
                        <span className="btn btn-warning">View Workouts</span>
                      </div>
                    </div>
                  </Link>
                </div>
              </div>
            </div>
          } />
          <Route path="/users" element={<Users />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
