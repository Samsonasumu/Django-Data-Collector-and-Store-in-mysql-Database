function showDataProtectionStatement() {
    const fontSize = "1px"; // You can adjust this value to your preference (e.g., 12px, 16px)
  
    const popupContent = `
      <div id="data-protection-popup" style="font-size: ${fontSize}">
        <h2>Data Protection Statement</h2>
        <p>Your privacy is important to us. Here's our data protection statement:
    
          This web app is committed to protecting the privacy of its users. This Data Protection Statement explains how we collect, use, disclose and protect the personal information you provide to us when you use our app.
    
          1. Information We Collect
    
          We collect the following personal information from users:
          geographical, academic and personal information
          2. How We Use Your Information
    
          We use the information we collect to:
    
          Provide and improve our services
          Process your requests and applications
          Communicate with you about our services and important updates
          Analyze user trends and behavior to improve our app
          Comply with legal and regulatory requirements
          3. Data Sharing and Disclosure
    
          We will not share or sell your personal information to third parties without your consent, except in the following cases:
    
          To comply with legal or regulatory requirements 
          To protect the rights, safety, or property of ourselves or others
          To provide services on our behalf (e.g., data storage)
          4. Data Security
    
          We take reasonable steps to protect your personal information from unauthorized access, disclosure, alteration, or destruction. However, no internet transmission or electronic storage is completely secure.   
    
          5. Data Retention
    
          We will retain your personal information for as long as necessary to fulfill the purposes for which it was collected, or as required by law.   
    
          6. Your Rights
    
          You have the right to access, correct, or delete your personal information. You can also withdraw your consent to the processing of your personal information.   
    
          7. Children's Privacy
    
          Our app is not intended for children under the age of 13. We do not knowingly collect personal information from children under 13.   
    
          8. Changes to this Statement
    
          We may update this Data Protection Statement from time to time. We will notify you of any changes by posting the new Data Protection Statement on our app.
    
          9. Contact Us
    
          If you have any questions about this Data Protection Statement, please contact us at [abc@gmail.com  ].
    
          Users must agree to the Data Protection Policy before using the app.
    
          Consent:
          I, the undersigned, hereby authorize and consent to Vihiga county and/or its appointed
          agents using my personal data to conduct the Background and/or Reference Checks set out in this Form, and
          for the said purposes. I confirm that I have provided my consent voluntarily.     
        </p>
        <button onclick="closePopup()">Close</button>
      </div>
    `;
  
    document.body.insertAdjacentHTML('beforeend', popupContent);
  
    const popup = document.getElementById('data-protection-popup');
    popup.style.display = 'block';
  }
  
  // Function to close the popup
  function closePopup() {
    const popup = document.getElementById('data-protection-popup');
    popup.style.display = 'none';
  }