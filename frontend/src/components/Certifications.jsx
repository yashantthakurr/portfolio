import React, { useState, useEffect, useCallback } from 'react';
import { FiExternalLink, FiRefreshCw } from 'react-icons/fi';
import { FaCertificate } from 'react-icons/fa';
import { getCertificates } from '../services/api';
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


const Certifications = () => {
  const [certificates, setCertificates] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchCertificates = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await getCertificates();
      setCertificates(Array.isArray(data) ? data : []);
    } catch (err) {
      console.error('Failed to fetch certificates:', err);
      setError('Unable to load certifications from the server. Please try again later!');
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchCertificates();
  }, [fetchCertificates]);

  return (
    <section id="certifications" className="projects-section">
      <div className="container">
        <h2 className="section-title">Certifications</h2>

        {loading ? (
          <div className="projects-grid">
            {[1, 2, 3].map((item) => (
              <div key={item} className="state-skeleton-card" />
            ))}
          </div>
        ) : error ? (
          <div className="state-container glass-card">
            <p className="state-error">{error}</p>
            <button type="button" className="btn btn-outline" onClick={fetchCertificates}>
              <FiRefreshCw style={{ marginRight: '0.5rem' }} /> Retry
            </button>
          </div>
        ) : certificates.length === 0 ? (
          <div className="state-container glass-card">
            <p>No certifications available right now.</p>
          </div>
        ) : (
          <div className="projects-grid">
            {certificates.map((cert) => {
              const skills = Array.isArray(cert.skills) ? cert.skills : [];
              const certUrl = formatUrl(cert.certificate_link);

              return (
                <div key={cert.id || cert.name} className="project-card glass-card">
                  <div className="project-content">
                    <div
                      className="cert-header"
                      style={{
                        display: 'flex',
                        justifyContent: 'space-between',
                        alignItems: 'center',
                      }}
                    >
                      <FaCertificate style={{ color: '#00d2ff', fontSize: '1.5rem' }} />
                      {cert.issued_year && (
                        <span style={{ fontSize: '0.8rem', color: '#9CA3AF' }}>
                          {cert.issued_year}
                        </span>
                      )}
                    </div>

                    <h3 className="project-title" style={{ marginTop: '1rem' }}>
                      {cert.name}
                    </h3>

                    {cert.issued_by && (
                      <p
                        className="project-desc"
                        style={{ fontStyle: 'italic', marginBottom: '0.5rem', flexGrow: 0 }}
                      >
                        Issued by: {cert.issued_by}
                      </p>
                    )}

                    {skills.length > 0 && (
                      <div className="project-tags">
                        {skills.map((skill, i) => (
                          <span key={i} className="tag">{skill}</span>
                        ))}
                      </div>
                    )}

                    {certUrl && (
                      <div className="project-links">
                        <a
                          href={certUrl}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="icon-link"
                          style={{ display: 'inline-flex', alignItems: 'center', gap: '0.4rem', fontSize: '1.3rem' }}
                        >
                          <FiExternalLink /> View Certificate
                        </a>
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

export default Certifications;
