import { Resend } from "resend";

const resend = new Resend(process.env.RESEND_API_KEY);

export default async function handler(req, res) {

  const payload = req.body;

  const name = payload.record.name;
  const email = payload.record.email;
  const message = payload.record.message;

  try {

    await resend.emails.send({
      from: "Portfolio <onboarding@resend.dev>",
      to: "yashant.thakur2007@gmail.com",
      subject: "New Portfolio Message",
      html: `
        <h2>New Message</h2>
        <p><b>Name:</b> ${name}</p>
        <p><b>Email:</b> ${email}</p>
        <p><b>Message:</b> ${message}</p>
      `
    });

    res.status(200).json({ success: true });

  } catch (error) {
    res.status(500).json({ error: "Email failed" });
  }
}
