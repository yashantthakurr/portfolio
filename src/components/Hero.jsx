import React from 'react';
import { FiArrowRight } from 'react-icons/fi';
import './Hero.css';

const Hero = () => {
  return (
    <section id="home" className="hero-section">
      <div className="container hero-content">
        <div className="hero-text-wrapper glass-card">
          <p className="greeting text-gradient">Hi, I'm Yashant Thakur</p>
          <h1 className="hero-title">Software<br />Developer</h1>
          <p className="hero-subtitle">
            Turning logic into life through code. Focused on building high-quality, user-centric software solutions using modern frameworks and industry best practices.
          </p>
          <div className="hero-cta">
            <a href="#projects" className="btn btn-primary">
              View Work <FiArrowRight className="btn-icon" />
            </a>
            <a href="#contact" className="btn btn-outline">Let's Talk</a>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
