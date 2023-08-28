from blog_pages.models import Experience, Education, Skill, Language, Certification, Project, Hobby, Resume

# Create experiences
experience1 = Experience(title="Proficient in computer systems with a focus on security and penetration testing...",
                        company="BGA Bilgi Güvenliği A.Ş", location="Istanbul, Turkey",
                        start_date="2022-08-01", end_date="2022-10-01",
                        description="Extensive knowledge of Windows, iOS, and Linux operating systems...")
experience1.save()

experience2 = Experience(title="Freelancing Script Writer", company="Freelancer", location="Istanbul, Turkey",
                        start_date="2023-01-01", currently_working=True,
                        description="Developed and implemented scripted solutions to automate the setup...")
experience2.save()

# Create education
education1 = Education(degree="Bachelor of Science", field_of_study="Software Engineering",
                    institution="Bahcesehir University", location="Istanbul, Turkey",
                    start_date="Your Start Date", end_date="Your End Date")
education1.save()

# Create skills
skill1 = Skill(name="Analytical and Critical Thinking", proficiency="Advanced")
skill1.save()

skill2 = Skill(name="Pandas and NumPy", proficiency="Intermediate")
skill2.save()

# ... Similar creation for other skills

# Create languages
language1 = Language(name="English", proficiency="Fluent")
language1.save()

language2 = Language(name="Turkish", proficiency="Native")
language2.save()

# ... Similar creation for other languages

# Create certifications
certification1 = Certification(title="Introduction to Artificial Intelligence (AI)",
                            organization="Your Organization", description="Certificate Description",
                            date="Certificate Date")
certification1.save()

# ... Similar creation for other certifications

# Create a Resume instance
resume1 = Resume(name="Said Mustafa Said")
resume1.experiences.add(experience1, experience2)
resume1.education.add(education1)
resume1.skills.add(skill1, skill2)
resume1.languages.add(language1, language2)
# ... Add other related fields (certifications, projects, hobbies)
resume1.save()
