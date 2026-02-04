import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
    console.log('Leaderboard API endpoint:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Leaderboard data fetched:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Leaderboard processed data:', leaderboardData);
        setLeaderboard(leaderboardData);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching leaderboard:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="container mt-5">
        <div className="d-flex justify-content-center">
          <div className="spinner-border text-success" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="container mt-5">
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">Error!</h4>
          <p>{error}</p>
        </div>
      </div>
    );
  }

  const getMedalIcon = (rank) => {
    switch(rank) {
      case 1:
        return '🥇';
      case 2:
        return '🥈';
      case 3:
        return '🥉';
      default:
        return rank;
    }
  };

  return (
    <div className="container mt-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2 className="mb-0">🏆 Leaderboard</h2>
        <span className="badge bg-warning text-dark fs-6">{leaderboard.length} Competitors</span>
      </div>
      <div className="table-responsive">
        <table className="table table-striped table-hover table-bordered">
          <thead className="table-dark">
            <tr>
              <th scope="col" className="text-center">Rank</th>
              <th scope="col">User</th>
              <th scope="col">Team</th>
              <th scope="col" className="text-center">Total Points</th>
              <th scope="col" className="text-center">Total Calories</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.length > 0 ? (
              leaderboard.map((entry, index) => (
                <tr key={entry._id || entry.id} className={index < 3 ? 'table-warning' : ''}>
                  <th scope="row" className="text-center fs-4">
                    {getMedalIcon(entry.rank || index + 1)}
                  </th>
                  <td>
                    <strong>{entry.user_name || 'N/A'}</strong>
                  </td>
                  <td>
                    {entry.team_id ? (
                      <span className="badge bg-primary">{entry.team_id}</span>
                    ) : (
                      <span className="badge bg-secondary">No Team</span>
                    )}
                  </td>
                  <td className="text-center">
                    <span className="badge bg-success fs-6">{entry.total_activities || 0}</span>
                  </td>
                  <td className="text-center">
                    <span className="badge bg-danger fs-6">{entry.total_calories || 0}</span>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="5" className="text-center text-muted">
                  No leaderboard data available
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Leaderboard;
