import React, { useState, useEffect, useCallback } from 'react';
import { FiGithub, FiExternalLink, FiRefreshCw } from 'react-icons/fi';
import { getProjects } from '../services/api';
import './Projects.css';

const formatUrl = (url) => {
  if (url === null || url === undefined) return null;
  if (typeof url !== 'string') return null;

  const trimmed = url.trim();
  const lower = trimmed.toLowerCase();

  if (
    trimmed === '' ||
    lower === 'null' ||
    lower === 'none' ||
    lower === 'not available' ||
    lower === 'n/a' ||
    lower === 'undefined'
  ) {
    return null;
  }

  if (trimmed.startsWith('http://') || trimmed.startsWith('https://')) {
    return trimmed;
  }

  return `https://${trimmed}`;
};


const Projects = () => {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchProjects = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await getProjects();
      setProjects(Array.isArray(data) ? data : []);
    } catch (err) {
      console.error('Failed to fetch projects:', err);
      setError('Unable to load projects from the server. Please try again later!');
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchProjects();
  }, [fetchProjects]);

  return (
    <section id="projects" className="projects-section">
      <div className="container">
        <h2 className="section-title">Projects</h2>

        {loading ? (
          <div className="projects-grid">
            {[1, 2, 3].map((item) => (
              <div key={item} className="state-skeleton-card" />
            ))}
          </div>
        ) : error ? (
          <div className="state-container glass-card">
            <p className="state-error">{error}</p>
            <button type="button" className="btn btn-outline" onClick={fetchProjects}>
              <FiRefreshCw style={{ marginRight: '0.5rem' }} /> Retry
            </button>
          </div>
        ) : projects.length === 0 ? (
          <div className="state-container glass-card">
            <p>No projects available right now.</p>
          </div>
        ) : (
          <div className="projects-grid">
            {projects.map((project) => {
              const tags = Array.isArray(project.technologies)
                ? project.technologies
                : [];
              const githubUrl = formatUrl(project.github);
              const liveDemoUrl = formatUrl(project.live_demo);

              return (
                <div key={project.id || project.title} className="project-card glass-card">
                  <div className="project-content">
                    <h3 className="project-title">{project.title}</h3>
                    <p className="project-desc">{project.description}</p>

                    {tags.length > 0 && (
                      <div className="project-tags">
                        {tags.map((tag, i) => (
                          <span key={i} className="tag">{tag}</span>
                        ))}
                      </div>
                    )}

                    {(githubUrl || liveDemoUrl) && (
                      <div className="project-links">
                        {githubUrl && (
                          <a
                            href={githubUrl}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="icon-link"
                            aria-label={`GitHub repository for ${project.title}`}
                          >
                            <FiGithub />
                          </a>
                        )}
                        {liveDemoUrl && (
                          <a
                            href={liveDemoUrl}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="icon-link"
                            aria-label={`Live demo for ${project.title}`}
                          >
                            <FiExternalLink />
                          </a>
                        )}
                      </div>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </section>
  );
};

export default Projects;
