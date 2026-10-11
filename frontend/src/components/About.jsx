import React from 'react';
import { FaPython, FaJava, FaGithub } from 'react-icons/fa';
import { SiSpringboot, SiFastapi, SiPostgresql, SiRedis, SiDocker } from 'react-icons/si';
import './About.css';

const About = () => {
  const skills = [
    { name: 'Python', icon: <FaPython color="#3776AB" /> },
    { name: 'Java', icon: <FaJava color="#E76F00" /> },
    { name: 'FastAPI', icon: <SiFastapi color="#05998B" /> },
    { name: 'Spring Boot', icon: <SiSpringboot color="#6DB33F" /> },
    { name: 'PostgreSQL', icon: <SiPostgresql color="#4169E1" /> },
    { name: 'Redis', icon: <SiRedis color="#DC382D" /> },
    { name: 'Docker', icon: <SiDocker color="#1D63ED" /> },
    { name: 'GitHub', icon: <FaGithub color="#FFFFFF" /> },
  ];

  return (
    <section id="about" className="about-section">
      <div className="container">
        <h2 className="section-title">About Me</h2>
        
        <div className="about-content">
          <div className="about-text glass-card">
            <h2>Who am I?</h2>
            <p>
              I'm a software developer focused on building reliable backend systems and scalable APIs using Python, FastAPI, Java, and Spring Boot.
              I enjoy designing RESTful APIs, implementing secure authentication and authorization, working with relational databases, and improving application performance through caching and efficient database operations.
            </p>
          </div>
          
          <div className="skills-grid">
            {skills.map((skill, index) => (
              <div key={index} className="skill-card glass-card">
                <div className="skill-icon">{skill.icon}</div>
                <span className="skill-name">{skill.name}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;
