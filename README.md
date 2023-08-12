# SecuringInsecureCode

This documentation outlines the identification and resolution of security vulnerabilities within the "Insecure Messaging App," developed using Django. 

The assessment aims to demonstrate a grasp of common web app security concerns and the application of secure coding practices.

# Vulnerabilities Identified
1. Cross-Site Scripting (XSS)

Issue: The original app rendered messages without properly escaping user-generated content in the list_messages.html template, creating a Cross-Site Scripting vulnerability. This allowed potential execution of harmful scripts when viewing messages.

Code Sample:

<ul>
    <li>{{ message.sender }}: {{ message.content }}</li>
</ul>



2. Insecure Authentication

Issue: The "Compose Message" feature lacked proper authentication and authorization checks. This made it accessible to anyone, compromising app security.

Code Sample:

def compose_message(request):
    # No authentication or authorization check
    if request.method == 'POST':
        sender = request.POST['sender']
        content = request.POST['content']
        Message.objects.create(sender=sender, content=content)
    return render(request, 'messaging_app/compose_message.html')

# Vulnerability Mitigation
#1. Cross-Site Scripting (XSS) Fix

Solution: To counter the XSS risk, we employed the following secure coding practice:

In list_messages.html, by using the safe filter, user-generated content is designated as safe HTML:

<ul>
    {% for message in messages %}
        <li>{{ message.sender }}: {{ message.content|safe }}</li>
    {% endfor %}
</ul>




2. Insecure Authentication Fix

Solution: To address the insecure authentication, we integrated the following secure coding practice:

In messaging_app/views.py, the @login_required decorator mandates user authentication to access the "Compose Message" view:

from django.contrib.auth.decorators import login_required

@login_required
def compose_message(request):
    if request.method == 'POST':
        sender = request.POST['sender']
        content = request.POST['content']
        Message.objects.create(sender=sender, content=content)
    return render(request, 'messaging_app/compose_message.html')

# Conclusion
This assessment showcases the detection and remediation of intentional vulnerabilities in the "Insecure Messaging App." Vulnerabilities like Cross-Site Scripting and Insecure Authentication were identified and rectified by implementing secure coding practices. These efforts bolstered app security, emphasizing the significance of secure coding principles in building resilient web applications.

# Summary
This document highlights the discovery and resolution of security vulnerabilities within the "Insecure Messaging App." Vulnerabilities such as Cross-Site Scripting (XSS) and Insecure Authentication were identified and effectively addressed using secure coding practices. This project underscores the importance of secure coding techniques in ensuring the robustness and safety of web applications.
