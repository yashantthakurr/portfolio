import React from 'react';
import { FaReact, FaNodeJs, FaHtml5, FaCss3Alt, FaPython, FaJava, FaGitAlt } from 'react-icons/fa';
import { SiJavascript, SiMysql, SiSpringboot, SiFastapi, SiNumpy, SiPandas } from 'react-icons/si';
import './About.css';

const About = () => {
  const skills = [
    { name: 'HTML5', icon: <FaHtml5 color="#E34F26" /> },
    { name: 'CSS3', icon: <FaCss3Alt color="#1572B6" /> },
    { name: 'JavaScript', icon: <SiJavascript color="#F7DF1E" /> },
    { name: 'React', icon: <FaReact color="#61DAFB" /> },
    { name: 'Node.js', icon: <FaNodeJs color="#339933" /> },
    { name: 'Git', icon: <FaGitAlt color="#F05032" /> },
    { name: 'Java', icon: <FaJava color="#E76F00" /> },
    { name: 'Python', icon: <FaPython color="#3776AB" /> },
    { name: 'FastAPI', icon: <SiFastapi color="#05998B" /> },
    { name: 'NumPy', icon: <SiNumpy color="#013243" /> },
    { name: 'Pandas', icon: <SiPandas color="#150458" /> },
    { name: 'MySQL', icon: <SiMysql color="#4479A1" /> },
  ];

  return (
    <section id="about" className="about-section">
      <div className="container">
        <h2 className="section-title">About Me</h2>
        
        <div className="about-content">
          <div className="about-text glass-card">
            <h3>My Journey</h3>
            <p>
              Python and Java Developer with experience in building real-time web applications and solving complex algorithmic problems. Aspiring AI/ML Engineer currently mastering Python’s data science stack (Pandas, NumPy) to bridge the gap between traditional software development and machine learning.
            </p>
            <p>
              When I'm not coding, you'll find me exploring new design trends and  
              experimenting with web animations.
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

