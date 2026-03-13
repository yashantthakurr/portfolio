import React, { useState} from 'react';
import './Contact.css';
import { supabase } from '../supabaseClient';

const Contact = () => {
  const [name,setName] = useState("");
  const [email,setEmail] = useState("");
  const [message,setMessage] = useState("");
  const [status, setStatus] = useState({ message: "", type: "" });

  const handleSubmit = async (e) => {
    e.preventDefault();

    const { data, error } = await supabase
      .from('messages')
      .insert([{name: name, email: email, message: message}]);

    if (error) {
      setStatus({ message: "Message not sent.", type: "error" });
      setName("");
      setEmail("");
      setMessage("");
      console.log(error);
    }
    else {
      setStatus({ message: "Message sent successfully!", type: "success" });
      setName("");
      setEmail("");
      setMessage("");
    }

    setTimeout(() => setStatus({ message: "", type: "" }), 5000);
  };

  return (
    <section id="contact" className="contact-section">
      <div className="container">
        <div className="contact-wrapper glass-card">
          <div className="contact-info">
            <h2 className="section-title" style={{textAlign: 'left'}}>Get In Touch</h2>
            <p>
              I'm currently open for new opportunities. Whether you have a question 
              or just want to say hi, I'll try my best to get back to you!
            </p>
          </div>
          
          <form className="contact-form" onSubmit={handleSubmit}>
            {status.message && (
              <div className={`status-message ${status.type}`} style={{
                padding: '10px',
                marginBottom: '15px',
                borderRadius: '8px',
                textAlign: 'center',
                backgroundColor: status.type === 'success' ? 'rgba(46, 204, 113, 0.15)' : 'rgba(231, 76, 60, 0.15)',
                color: status.type === 'success' ? '#2ecc71' : '#e74c3c',
                border: `1px solid ${status.type === 'success' ? 'rgba(46, 204, 113, 0.3)' : 'rgba(231, 76, 60, 0.3)'}`
              }}>
                {status.message}
              </div>
            )}
            <div className="form-group">
              <input type="text" id="name" placeholder="Your Name" required value = {name} onChange={(e)=>setName(e.target.value)}/>
            </div>
            <div className="form-group">
              <input type="email" id="email" placeholder="Your Email" required value = {email} onChange={(e)=>setEmail(e.target.value)}/>
            </div>
            <div className="form-group">
              <textarea id="message" rows="5" placeholder="Your Message" required value = {message} onChange={(e)=>setMessage(e.target.value)}></textarea>
            </div>
            <button type="submit" className="btn btn-primary submit-btn">Send Message</button>
          </form>
        </div>
      </div>
    </section>
  );
};

export default Contact;
