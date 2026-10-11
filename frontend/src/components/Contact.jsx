import React, { useState } from 'react';
import './Contact.css';
import { sendMessage } from '../services/api';

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: '',
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [status, setStatus] = useState({ message: '', type: '' });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const validate = () => {
    const trimmedName = formData.name.trim();
    const trimmedEmail = formData.email.trim();
    const trimmedMessage = formData.message.trim();

    if (trimmedName.length < 2 || trimmedName.length > 50) {
      return 'Name must be between 2 to 50 characters long.';
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(trimmedEmail) || trimmedEmail.length > 254) {
      return 'Please enter a valid email address.';
    }

    if (trimmedMessage.length < 1 || trimmedMessage.length > 400) {
      return 'Message must not be blank and may not exceed 400 characters.';
    }

    return null;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (isSubmitting) return;

    const validationError = validate();
    if (validationError) {
      setStatus({ message: validationError, type: 'error' });
      return;
    }

    try {
      setIsSubmitting(true);
      setStatus({ message: '', type: '' });

      await sendMessage({
        name: formData.name.trim(),
        email: formData.email.trim(),
        message: formData.message.trim(),
      });

      setStatus({ message: 'Thank you! Your message has been sent successfully.', type: 'success' });
      setFormData({ name: '', email: '', message: '' });
    } catch (err) {
      console.error('Contact form submission error:', err);
      setStatus({
        message: 'Failed to send message. Please try again later.',
        type: 'error',
      });
    } finally {
      setIsSubmitting(false);
      setTimeout(() => setStatus({ message: '', type: '' }), 6000);
    }
  };

  return (
    <section id="contact" className="contact-section">
      <div className="container">
        <div className="contact-wrapper glass-card">
          <div className="contact-info">
            <h2 className="section-title" style={{ textAlign: 'left' }}>Get In Touch</h2>
            <p>
              I'm currently open for new opportunities. Whether you have a question 
              or just want to say hi, I'll surely to get back to you!
            </p>
          </div>

          <form className="contact-form" onSubmit={handleSubmit} noValidate>
            {status.message && (
              <div
                className={`status-message ${status.type}`}
                role="alert"
                style={{
                  padding: '12px 16px',
                  marginBottom: '15px',
                  borderRadius: '8px',
                  textAlign: 'center',
                  backgroundColor:
                    status.type === 'success' ? 'rgba(46, 204, 113, 0.15)' : 'rgba(231, 76, 60, 0.15)',
                  color: status.type === 'success' ? '#2ecc71' : '#f87171',
                  border: `1px solid ${
                    status.type === 'success' ? 'rgba(46, 204, 113, 0.3)' : 'rgba(231, 76, 60, 0.3)'
                  }`,
                  fontSize: '0.95rem',
                }}
              >
                {status.message}
              </div>
            )}

            <div className="form-group">
              <input
                type="text"
                id="name"
                name="name"
                placeholder="Your Name"
                required
                maxLength={50}
                value={formData.name}
                onChange={handleChange}
                disabled={isSubmitting}
              />
            </div>

            <div className="form-group">
              <input
                type="email"
                id="email"
                name="email"
                placeholder="Your Email"
                required
                maxLength={254}
                value={formData.email}
                onChange={handleChange}
                disabled={isSubmitting}
              />
            </div>

            <div className="form-group">
              <textarea
                id="message"
                name="message"
                rows="5"
                placeholder="Your Message (max 400 characters)"
                required
                maxLength={400}
                value={formData.message}
                onChange={handleChange}
                disabled={isSubmitting}
              />
            </div>

            <button
              type="submit"
              className="btn btn-primary submit-btn"
              disabled={isSubmitting}
            >
              {isSubmitting ? 'Sending...' : 'Send Message'}
            </button>
          </form>
        </div>
      </div>
    </section>
  );
};

export default Contact;
