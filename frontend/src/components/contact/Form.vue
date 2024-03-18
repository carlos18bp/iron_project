<template>
  <form class="p-4 flex flex-col space-y-4 w-1/2">
    <div class="flex space-x-8">
      <div class="w-1/2">
        <label
          for="first_name"
          class="block mb-2 text-sm font-medium text-gray-900"
          >First name</label
        >
        <input
          type="text"
          id="first_name"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full"
          placeholder="Type your first name"
          required
        />
      </div>

      <div class="w-1/2">
        <label
          for="last_name"
          class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
          >Last name</label
        >
        <input
          type="text"
          id="last_name"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full"
          placeholder="Type your last name"
          required
        />
      </div>
    </div>

    <div>
      <label for="email" class="block mb-2 text-sm font-medium text-gray-900"
        >Email address</label
      >
      <input
        type="email"
        id="email"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full"
        placeholder="Type your email"
        required
      />
    </div>

    <div>
      <label
        for="subject"
        class="block mb-2 text-sm font-medium text-gray-900"
        >Subject</label
      >
      <input
        type="text"
        id="subject"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full"
        placeholder="Type subject"
        required
      />
    </div>

    <div>
      <label
        for="project"
        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >Tell us a little bit about your project</label
      >
      <textarea
        id="project"
        rows="4"
        class="block p-2.5 text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 w-full"
        placeholder="Write your thoughts here..."
        required
      >
      </textarea>
    </div>

    <div class="flex flex-col">
      <label
        for="project"
        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >What type of project are you interested in?</label
      >
      <div class="flex items-center">
        <input
          id="balconies-checkbox"
          type="checkbox"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500"
        />
        <label
          for="balconies-checkbox"
          class="ms-2 text-sm font-medium text-gray-900"
          >Balconies</label
        >
      </div>
      <div class="flex items-center">
        <input
          id="doors-checkbox"
          type="checkbox"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500"
        />
        <label
          for="doors-checkbox"
          class="ms-2 text-sm font-medium text-gray-900"
          >Doors</label
        >
      </div>
      <div class="flex items-center">
        <input
          id="fences-checkbox"
          type="checkbox"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500"
        />
        <label
          for="fences-checkbox"
          class="ms-2 text-sm font-medium text-gray-900"
          >Fences</label
        >
      </div>
      <div class="flex items-center">
        <input
          id="furniture-checkbox"
          type="checkbox"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500"
        />
        <label
          for="furniture-checkbox"
          class="ms-2 text-sm font-medium text-gray-900"
          >Furniture</label
        >
      </div>
      <div class="flex items-center">
        <input
          id="gates-checkbox"
          type="checkbox"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500"
        />
        <label
          for="gates-checkbox"
          class="ms-2 text-sm font-medium text-gray-900"
          >Gates</label
        >
      </div>
      <div class="flex items-center">
        <input
          id="home-decor-checkbox"
          type="checkbox"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500"
        />
        <label
          for="home-decor-checkbox"
          class="ms-2 text-sm font-medium text-gray-900"
          >Home Decor</label
        >
      </div>
      <div class="flex items-center">
        <input
          id="lighting-checkbox"
          type="checkbox"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500"
        />
        <label
          for="lighting-checkbox"
          class="ms-2 text-sm font-medium text-gray-900"
          >Lighting</label
        >
      </div>
      <div class="flex items-center">
        <input
          id="balconies-checkbox"
          type="checkbox"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500"
        />
        <label
          for="balconies-checkbox"
          class="ms-2 text-sm font-medium text-gray-900"
          >Balconies</label
        >
      </div>
      <div class="flex items-center">
        <input
          id="railings-checkbox"
          type="checkbox"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500"
        />
        <label
          for="railings-checkbox"
          class="ms-2 text-sm font-medium text-gray-900"
          >Railings</label
        >
      </div>
      <div class="flex items-center">
        <input
          id="restoration-checkbox"
          type="checkbox"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500"
        />
        <label
          for="restoration-checkbox"
          class="ms-2 text-sm font-medium text-gray-900"
          >Restoration</label
        >
      </div>
      <div class="flex items-center">
        <input
          id="sculptures-checkbox"
          type="checkbox"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500"
        />
        <label
          for="sculptures-checkbox"
          class="ms-2 text-sm font-medium text-gray-900"
          >Sculptures</label
        >
      </div>
      <div class="flex items-center">
        <input
          id="wine-cellars-checkbox"
          type="checkbox"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500"
        />
        <label
          for="wine-cellars-checkbox"
          class="ms-2 text-sm font-medium text-gray-900"
          >Wine Cellars</label
        >
      </div>
      <div class="flex items-center">
        <input
          id="other-checkbox"
          type="checkbox"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500"
        />
        <label
          for="other-checkbox"
          class="ms-2 text-sm font-medium text-gray-900"
          >Other</label
        >
      </div>
    </div>

    <div class="flex flex-col">
      <label
        for="project"
        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >What type of project are you interested in?</label
      >
      <div class="flex items-center">
        <input
          id="home-owner-checkbox"
          type="checkbox"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500"
        />
        <label
          for="home-owner-checkbox"
          class="ms-2 text-sm font-medium text-gray-900"
          >Home Owner</label
        >
      </div>
      <div class="flex items-center">
        <input
          id="designer-checkbox"
          type="checkbox"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500"
        />
        <label
          for="designer-checkbox"
          class="ms-2 text-sm font-medium text-gray-900"
          >Designer</label
        >
      </div>
      <div class="flex items-center">
        <input
          id="architect-checkbox"
          type="checkbox"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500"
        />
        <label
          for="architect-checkbox"
          class="ms-2 text-sm font-medium text-gray-900"
          >Architect</label
        >
      </div>
      <div class="flex items-center">
        <input
          id="contractor-checkbox"
          type="checkbox"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500"
        />
        <label
          for="contractor-checkbox"
          class="ms-2 text-sm font-medium text-gray-900"
          >Contractor</label
        >
      </div>
      <div class="flex items-center">
        <input
          id="other-checkbox"
          type="checkbox"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500"
        />
        <label
          for="other-checkbox"
          class="ms-2 text-sm font-medium text-gray-900"
          >Other</label
        >
      </div>
    </div>

    <div>
      <label
        for="phone-input"
        class="block mb-2 text-sm font-medium text-gray-900"
        >Phone number</label
      >
      <div
        class="flex items-center space-x-4">
        <svg
          class="w-4 h-4 text-gray-500 dark:text-gray-400"
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          fill="currentColor"
          viewBox="0 0 19 18">
          <path
            d="M18 13.446a3.02 3.02 0 0 0-.946-1.985l-1.4-1.4a3.054 3.054 0 0 0-4.218 0l-.7.7a.983.983 0 0 1-1.39 0l-2.1-2.1a.983.983 0 0 1 0-1.389l.7-.7a2.98 2.98 0 0 0 0-4.217l-1.4-1.4a2.824 2.824 0 0 0-4.218 0c-3.619 3.619-3 8.229 1.752 12.979C6.785 16.639 9.45 18 11.912 18a7.175 7.175 0 0 0 5.139-2.325A2.9 2.9 0 0 0 18 13.446Z"
          />
        </svg>
        <input
          type="text"
          id="phone-input"
          aria-describedby="helper-text-explanation"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full"
          pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
          placeholder="123-456-7890"
          required
        />
      </div>
    </div>

    <div>
      <label
        for="hear_about_us"
        class="block mb-2 text-sm font-medium text-gray-900">
        Select an option
      </label>
      <select
        id="hear_about_us"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full">
        <option selected>Choose an option</option>
        <option value="Web page">Web page</option>
        <option value="Instagram">Instagram</option>
        <option value="Friend">Friend</option>
        <option value="Internet">Internet</option>
        <option value="Other">Other</option>
      </select>
    </div>
  </form>
</template>

<script setup>
</script>
