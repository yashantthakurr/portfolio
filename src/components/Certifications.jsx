import React from 'react';
import { FiExternalLink } from 'react-icons/fi';
import { FaCertificate } from 'react-icons/fa';
import './Projects.css';

const Certifications = () => {
  const certData = [
    {
      title: 'Deloitte Australia - Data Analytics Job Simulation',
      issuer: 'Deloitte',
      date: '2026',
      tags: ['Tableau', 'Data Analysis'],
      link: 'https://www.theforage.com/completion-certificates/9PBTqmSxAf6zZTseP/io9DzWKe3PTsiS6GG_9PBTqmSxAf6zZTseP_697efc91167b81f6ee32f5dd_1769934235044_completion_certificate.pdf' // Add your certificate link here
    },
    {
      title: 'Digital Marketing',
      issuer: 'HubSpot Academy',
      date: '2026',
      tags: ['Digital Marketing', 'Digital Media'],
      link: 'https://app-na2.hubspot.com/academy/achievements/bbqgrxyx/en/1/yashant-thakur/digital-marketing'
    },
    {
      title: 'Prompt Engineering for Everyone',
      issuer: 'IBM',
      date: '2026',
      tags: ['Prompt Engineering'],
      link: 'https://courses.cognitiveclass.ai/certificates/f3ee3c7baf6b455d99b5b2c4a38aeabf'
    },
    {
      title: 'Introduction to Generative AI Studio',
      issuer: 'Google',
      date: '2026',
      tags: ['Generative AI'],
      link: 'https://simpli.app.link/CXXuz4k2ZZb'
    },
    {
      title: 'National Entrepreneurship Challenge 2025',
      issuer: 'E-Cell, IIT Bombay',
      date: '2026',
      tags: ['Research Skills', 'Project Management'],
      link: 'https://www.ecell.in/certificate/certi?email=yashant.thakur2007@gmail.com&year=2025-2026'
    }
  ];

  return (
    <section id="certifications" className="projects-section">
      <div className="container">
        <h2 className="section-title">Certifications</h2>
        
        <div className="projects-grid">
          {certData.map((cert, index) => (
            <div key={index} className="project-card glass-card">
              <div className="project-content">
                <div className="cert-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                   <FaCertificate style={{ color: '#00d2ff', fontSize: '1.5rem' }} />
                   <span style={{ fontSize: '0.8rem', color: '#9CA3AF' }}>{cert.date}</span>
                </div>
                
                <h3 className="project-title" style={{ marginTop: '1rem' }}>{cert.title}</h3>
                <p className="project-desc" style={{ fontStyle: 'italic', marginBottom: '0.5rem' }}>
                  Issued by: {cert.issuer}
                </p>

                <div className="project-tags">
                  {cert.tags.map((tag, i) => (
                    <span key={i} className="tag">{tag}</span>
                  ))}
                </div>

                <div className="project-links">
                  <a href={cert.link} target="_blank" rel="noreferrer" className="icon-link">
                    <FiExternalLink /> View Certificate
                  </a>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Certifications;