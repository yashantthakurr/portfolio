import React from 'react';
import { FiGithub, FiTwitter, FiLinkedin, FiInstagram } from 'react-icons/fi';
import './Footer.css';

const Footer = () => {
  return (
    <footer className="footer-section">
      <div className="container footer-content">
        <div className="footer-brand">
          <span className="logo text-gradient">Portfolio</span>
          <p>Building digital softwares and experiences.</p>
        </div>
        
        <div className="social-links">
          <a href="https://github.com/yashantthakurr/" className="social-icon"><FiGithub /></a>
          <a href="https://x.com/yashantthakurr" className="social-icon"><FiTwitter /></a>
          <a href="https://www.linkedin.com/in/yashant-thakur-561992381/" className="social-icon"><FiLinkedin /></a>
          <a href="https://www.instagram.com/yashantthakurr/" className="social-icon"><FiInstagram /></a>
        </div>
        
        <div className="footer-bottom">
          <p>Designed & Made by Yashant Thakur</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
