### Introduction

This documentation outlines the identification and resolution of security vulnerabilities within the "Insecure Messaging App," developed using Django. The assessment aims to demonstrate a grasp of common web app security concerns and the application of secure coding practices, including elements from the Secure Development Lifecycle (SDLC).

### Vulnerabilities Identified

#### 1. Cross-Site Scripting (XSS)

**Issue:** The original app rendered messages without properly escaping user-generated content in the `list_messages.html` template, creating a Cross-Site Scripting vulnerability. This allowed potential execution of harmful scripts when viewing messages.

**Code Sample:**
```html
<ul>
    <li>{{ message.sender }}: {{ message.content }}</li>
</ul>
```

#### 2. Insecure Authentication

**Issue:** The "Compose Message" feature lacked proper authentication and authorization checks. This made it accessible to anyone, compromising app security.

**Code Sample:**
```python
def compose_message(request):
    # No authentication or authorization check
    if request.method == 'POST':
        sender = request.POST['sender']
        content = request.POST['content']
        Message.objects.create(sender=sender, content=content)
    return render(request, 'messaging_app/compose_message.html')
```

### Vulnerability Mitigation

#### 1. Cross-Site Scripting (XSS) Fix

**Solution:** To counter the XSS risk, we employed the following secure coding practice:

In `list_messages.html`, by using the `safe` filter, user-generated content is designated as safe HTML:

```html
<ul>
    {% for message in messages %}
        <li>{{ message.sender }}: {{ message.content|safe }}</li>
    {% endfor %}
</ul>
```

**SDLC Component - Design and Implementation:** This practice aligns with the SDLC principle of secure design and implementation, ensuring that user input is correctly validated and escaped before rendering.

#### 2. Insecure Authentication Fix

**Solution:** To address the insecure authentication, we integrated the following secure coding practice:

In `messaging_app/views.py`, the `@login_required` decorator mandates user authentication to access the "Compose Message" view:

```python
from django.contrib.auth.decorators import login_required

@login_required
def compose_message(request):
    if request.method == 'POST':
        sender = request.POST['sender']
        content = request.POST['content']
        Message.objects.create(sender=sender, content=content)
    return render(request, 'messaging_app/compose_message.html')
```

**SDLC Component - Implementation and Testing:** This approach aligns with the SDLC principle of secure coding, where authentication checks are implemented and tested thoroughly before deployment.

### Conclusion

This assessment showcases the detection and remediation of intentional vulnerabilities in the "Insecure Messaging App." Vulnerabilities like Cross-Site Scripting and Insecure Authentication were identified and rectified by implementing secure coding practices, drawing from elements of the Secure Development Lifecycle (SDLC). These efforts bolstered app security, emphasizing the significance of secure coding principles in building resilient web applications.

---

## Summary

This document highlights the discovery and resolution of security vulnerabilities within the "Insecure Messaging App." Vulnerabilities such as Cross-Site Scripting (XSS) and Insecure Authentication were identified and effectively addressed using secure coding practices, incorporating key principles from the Secure Development Lifecycle (SDLC). This project underscores the importance of secure coding techniques and comprehensive development methodologies in ensuring the robustness and safety of web applications.
