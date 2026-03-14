import React from 'react';
import { FiGithub, FiExternalLink } from 'react-icons/fi';
import './Projects.css';

const Projects = () => {
  const projectData = [
    {
      title: 'Currency Converter Web Application',
      description: 'Built a Python-based web application to convert currencies using real-time exchange rates from external APIs.',
      tags: ['Python', 'Streamlit', 'RestAPI'],
      github: 'https://github.com/yashantthakurr/quick-currency-converter',
      live: 'https://quickcurrencyconverter.streamlit.app/'
    },
    {
      title: 'Naruto Jutsu AR',
      description: 'Turn your webcam into a Naruto Jutsu Simulator! Here you can perform Rasenshuriken and Chidori.',
      tags: ['HTML5', 'CSS3', 'JavaScript'],
      github: 'https://github.com/yashantthakurr/dattebayo',
      live: 'https://yashantthakurr.github.io/dattebayo/'
    },
    {
      title: 'Personal Portfolio',
      description: 'A versatile portfolio showcasing innovative projects, and demonstrating technical proficiency.',
      tags: ['React.js', 'Vite', 'Vercel', 'Supabase'],
      github: 'https://github.com/yashantthakurr/portfolio',
      live: 'https://yashantportfolio.vercel.app/'
    },
    {
      title: 'Data Structures and Algorithms Implementation',
      description: 'Implemented core data structures including linked lists, stacks, queues, binary trees, and hash tables from scratch.',
      tags: ['Java'],
      github: 'https://github.com/yashantthakurr/dsa-in-java'
    }
  ];

  return (
    <section id="projects" className="projects-section">
      <div className="container">
        <h2 className="section-title">Projects</h2>
        
        <div className="projects-grid">
          {projectData.map((project, index) => (
            <div key={index} className="project-card glass-card">
              <div className="project-content">
                <h3 className="project-title">{project.title}</h3>
                <p className="project-desc">{project.description}</p>
                <div className="project-tags">
                  {project.tags.map((tag, i) => (
                    <span key={i} className="tag">{tag}</span>
                  ))}
                </div>
                <div className="project-links">
                  <a href={project.github} className="icon-link"><FiGithub /></a>
                  <a href={project.live} className="icon-link"><FiExternalLink /></a>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Projects;
