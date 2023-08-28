from blog_pages.models import Experience, Education, Skill, Language, Certification, Project, Hobby, Resume

experience1 = Experience(title="Proficient .",company="BGA Bilgi Güvenliği A.Ş", location="Istanbul, Turkey", start_date="2022-08-01", end_date="2022-10-01", description="Extensive knowledge of Windows, iOS, and Linux operating systems...")

experience1.save()


experience2 = Experience(title="Freelancing Script Writer", company="Freelancer", location="Istanbul, Turkey", start_date="2023-01-01", description="Developed and implemented scripted solutions to automate the setup...")

experience2.save()




education1 = Education(degree="Bachelor of Science", field_of_study="Software Engineering", institution="Bahcesehir University", location="Istanbul, Turkey",description="Developed and implemented scripted solutions to automate the setup...", start_date="2023-01-01", end_date="2023-01-01")

education1.save()




skill1 = Skill(name="Analytical and Critical Thinking", proficiency="Advanced")
skill1.save()

skill2 = Skill(name="Pandas and NumPy", proficiency="Intermediate")
skill2.save()




language1 = Language(name="English", proficiency="Fluent")
language1.save()

language2 = Language(name="Turkish", proficiency="Native")
language2.save()




certification1 = Certification(title="Introduction to Artificial Intelligence (AI)", organization="Your Organization", description="Certificate Description", date="2023-01-01")
certification1.save()


project1 = Project(title="Stock Market Trade Bot", description="Developing a sophisticated stock market trade bot that integrates AI and generative AI techniques", start_date="2023-01-01", end_date="2023-01-01", currently_working=False
)
project1.save()


hobby1 = Hobby(name="Football")
hobby1.save()

resume1 = Resume(name="Said Mustafa Said")
resume1.save()

resume1.experiences.add(experience1, experience2)
resume1.save()

resume1.education.add(education1)
resume1.save()

resume1.skills.add(skill1, skill2)
resume1.save()

resume1.languages.add(language1, language2)
resume1.save()

resume1.certifications.add(certification1)
resume1.save()

resume1.projects.add(project1)
resume1.save()

resume1.hobbies.add(hobby1)
resume1.save()





