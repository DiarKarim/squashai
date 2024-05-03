<?php
// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the form fields
    $fullname = trim($_POST["fullname"]);
    $email = trim($_POST["email"]);
    $message = trim($_POST["message"]);

    // Check if all fields are filled
    if (!empty($fullname) && !empty($email) && !empty($message)) {
        // Set the recipient email address
        $to = "thesquashai@gmail.com"; // Replace with your email address

        // Set the email subject
        $subject = "Contact Form Submission from $fullname";

        // Compose the email message
        $email_message = "Name: $fullname\n";
        $email_message .= "Email: $email\n\n";
        $email_message .= "Message:\n$message";

        // Set the email headers
        $headers = "From: $fullname <$email>\r\n";
        $headers .= "Reply-To: $email\r\n";

        // Send the email
        if (mail($to, $subject, $email_message, $headers)) {
            // Email sent successfully
            echo json_encode(["success" => true, "message" => "Thank you! Your message has been sent."]);
        } else {
            // Failed to send email
            echo json_encode(["success" => false, "message" => "Oops! Something went wrong. Please try again later."]);
        }
    } else {
        // Missing required fields
        echo json_encode(["success" => false, "message" => "Please fill out all fields."]);
    }
} else {
    // Redirect if accessed directly
    header("Location: index.html");
    exit;
}
?>
