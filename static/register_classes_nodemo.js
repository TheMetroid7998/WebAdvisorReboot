(function () {
  /** Convert form fields into a plain JS object */
  function formToJson(form) {
    const data = {};
    const formData = new FormData(form);

    for (const [key, value] of formData.entries()) {
      const field = form.elements.namedItem(key);

      if (!field) continue; // Defensive: skip unexpected keys
      data[key] = field.type === 'checkbox' ? field.checked : value;
    }

    return data;
  }

  /** Submit PUT request with JSON body */
  async function registerUser(endpoint, payload) {
    const response = await fetch(endpoint, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      throw new Error(`HTTP error ${response.status}`);
    }
    return response.json();
  }

  /** Main handler for Save button */
  async function handleSave(event) {
    event.preventDefault(); // Prevent accidental form submission if button is inside <form>

    const form = document.getElementById('registerForm');
    if (!form) {
      console.error("registerForm not found.");
      return alert("Internal error: form missing.");
    }

    const data = formToJson(form);
    const userId = data.user_id;
    const courseId = data.course_id;

    if (!userId) {
      console.error("User ID is missing.");
      return alert("Error: User ID is missing.");
    }

    try {
      console.log("Submitting JSON:", data);

      const result = await registerUser(`/user/${userId}`, data);

      console.log("Success:", result);
      alert("Registered for classes!");
    } catch (err) {
      console.error("Failed to register for any/all courses!:", err);
      alert("Failed to register user for courses. See console for details.");
    }
  }

  /** Attach button handler on DOM ready */
  document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('saveButton');
    if (btn) {
      btn.addEventListener('click', handleSave);
      console.log("Save button initialized.");
    } else {
      console.error("saveButton not found!");
    }
  });
})();