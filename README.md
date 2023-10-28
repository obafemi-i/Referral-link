# Referral-link

- API for users to sign up for a newsletter using their email and nickname

- Only unique emails are accepted, users can't sign up with already signed up emails

- A code is generated for each user. When a code is generated, the database is searched, if the generated code already exists, the function to generate the code is recursively called. The function only terminates when a unique code is generated.

- Using users' nickname and the unique generated code, a unique referral link is generated for each user.
