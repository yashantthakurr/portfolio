
const VITE_API_BASE_URL = (import.meta.env.VITE_API_BASE_URL).replace(/\/+$/, '');

async function request(endpoint, options = {}) {
  const url = `${VITE_API_BASE_URL}${endpoint.startsWith('/') ? '' : '/'}${endpoint}`;

  const defaultHeaders = {
    'Accept': 'application/json',
  };

  if (options.body && typeof options.body === 'string') {
    defaultHeaders['Content-Type'] = 'application/json';
  }

  const response = await fetch(url, {
    ...options,
    headers: {
      ...defaultHeaders,
      ...options.headers,
    },
  });

  if (!response.ok) {
    let errorMessage = `Request failed with status ${response.status}`;
    try {
      const errorData = await response.json();
      if (typeof errorData?.detail === 'string') {
        errorMessage = errorData.detail;
      } else if (Array.isArray(errorData?.detail) && errorData.detail.length > 0) {
        errorMessage = errorData.detail.map((err) => err.msg || JSON.stringify(err)).join(', ');
      }
    }
    catch (err) {
      void err;
    }
    throw new Error(errorMessage);
  }

  return response.json();
}

export async function getProjects() {
  return request('/api/v1/projects/');
}

export async function getCertificates() {
  return request('/api/v1/certificates/');
}

export async function getExperiences() {
  return request('/api/v1/experiences/');
}

export async function sendMessage(messageData) {
  return request('/api/v1/messages/', {
    method: 'POST',
    body: JSON.stringify(messageData),
  });
}
