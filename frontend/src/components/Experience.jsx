import React, { useState, useEffect, useCallback } from 'react';
import { FiCalendar, FiMapPin, FiRefreshCw } from 'react-icons/fi';
import { getExperiences } from '../services/api';
import './Experience.css';

const Experience = () => {
  const [experiences, setExperiences] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchExperiences = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await getExperiences();
      setExperiences(Array.isArray(data) ? data : []);
    } catch (err) {
      console.error('Failed to fetch experiences:', err);
      setError('Unable to load experiences from the server. Please try again later!');
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchExperiences();
  }, [fetchExperiences]);

  return (
    <section id="experience" className="experience-section">
      <div className="container">
        <h2 className="section-title">Experience</h2>

        {loading ? (
          <div className="experience-list">
            {[1, 2].map((item) => (
              <div key={item} className="state-skeleton-card" style={{ minHeight: '180px' }} />
            ))}
          </div>
        ) : error ? (
          <div className="state-container glass-card">
            <p className="state-error">{error}</p>
            <button type="button" className="btn btn-outline" onClick={fetchExperiences}>
              <FiRefreshCw style={{ marginRight: '0.5rem' }} /> Retry
            </button>
          </div>
        ) : experiences.length === 0 ? (
          <div className="state-container glass-card">
            <p>No professional experiences listed yet.</p>
          </div>
        ) : (
          <div className="experience-list">
            {experiences.map((exp) => (
              <div key={exp.id || `${exp.organization}-${exp.role}`} className="experience-card glass-card">
                <div className="experience-header">
                  <div className="experience-title-group">
                    <h3 className="experience-role">{exp.role}</h3>
                    <span className="experience-org">{exp.organization}</span>
                  </div>

                  <div className="experience-meta">
                    {exp.mode && (
                      <span className="mode-badge">
                        <FiMapPin /> {exp.mode}
                      </span>
                    )}
                    {exp.timeline && (
                      <span className="timeline-badge">
                        <FiCalendar /> {exp.timeline}
                      </span>
                    )}
                  </div>
                </div>

                {exp.description && (
                  <p className="experience-desc">{exp.description}</p>
                )}
              </div>
            ))}
          </div>
        )}
      </div>
    </section>
  );
};

export default Experience;
