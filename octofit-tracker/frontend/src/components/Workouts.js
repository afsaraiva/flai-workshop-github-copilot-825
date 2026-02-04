import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    console.log('Workouts API endpoint:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts data fetched:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Workouts processed data:', workoutsData);
        setWorkouts(workoutsData);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
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

  const getDifficultyBadge = (difficulty) => {
    const difficultyMap = {
      'Beginner': 'success',
      'Intermediate': 'warning',
      'Advanced': 'danger'
    };
    return difficultyMap[difficulty] || 'secondary';
  };

  return (
    <div className="container mt-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2 className="mb-0">💪 Workout Suggestions</h2>
        <span className="badge bg-success fs-6">{workouts.length} Workouts</span>
      </div>
      <div className="row">
        {workouts.length > 0 ? (
          workouts.map(workout => (
            <div key={workout.id} className="col-md-6 col-lg-4 mb-4">
              <div className="card h-100 shadow-sm">
                <div className="card-header bg-success text-white">
                  <h5 className="card-title mb-0">{workout.name}</h5>
                </div>
                <div className="card-body">
                  <div className="mb-3">
                    <span className="badge bg-info me-2">{workout.category}</span>
                    <span className={`badge bg-${getDifficultyBadge(workout.difficulty_level)}`}>
                      {workout.difficulty_level}
                    </span>
                  </div>
                  <p className="card-text">
                    {workout.description || 'No description available'}
                  </p>
                  <hr />
                  <div className="d-flex justify-content-between align-items-center">
                    <div>
                      <strong className="text-primary">⏱️ Duration:</strong>
                      <br />
                      <span className="badge bg-primary">{workout.duration} min</span>
                    </div>
                    <div className="text-end">
                      <strong className="text-danger">🔥 Calories:</strong>
                      <br />
                      <span className="badge bg-danger">{workout.calories_estimate}</span>
                    </div>
                  </div>
                </div>
                <div className="card-footer">
                  <button className="btn btn-sm btn-outline-success w-100">
                    Start Workout
                  </button>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="alert alert-info" role="alert">
              No workout suggestions available
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Workouts;
