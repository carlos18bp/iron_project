<template>
  <form class="p-4 pl-8 flex flex-col space-y-4 w-1/2" @submit.prevent="onSubmit">
    <div class="flex space-x-8">
      <div class="w-1/2">
        <label
          for="first_name"
          class="block font-regular mb-2 text-sm font-medium text-gray-900">
          First name <span class="text-red-600">*</span>
        </label>
        <input
          v-model="contactFormData.firstName"
          type="text"
          id="first_name"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-orange-400 focus:border-blue-500 block w-full"
          placeholder="Type your first name"
          required
        />
      </div>

      <div class="w-1/2">
        <label
          for="last_name"
          class="block font-regular mb-2 text-sm font-medium text-gray-900">
          Last name <span class="text-red-600">*</span>
        </label>
        <input
          v-model="contactFormData.lastName"
          type="text"
          id="last_name"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-orange-400 focus:border-blue-500 block w-full"
          placeholder="Type your last name"
          required
        />
      </div>
    </div>

    <div>
      <label for="email" class="block font-regular mb-2 text-sm font-medium text-gray-900">
        Email address <span class="text-red-600">*</span>
      </label>
      <input
        v-model="contactFormData.email"
        type="email"
        id="email"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-orange-400 focus:border-blue-500 block w-full"
        placeholder="Type your email"
        required
      />
    </div>

    <div>
      <label
        for="subject"
        class="block mb-2 text-sm font-medium text-gray-900">
        Subject <span class="text-red-600">*</span>
      </label>
      <input
        v-model="contactFormData.subject"
        type="text"
        id="subject"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-orange-400 focus:border-blue-500 block w-full"
        placeholder="Type subject"
        required
      />
    </div>

    <div>
      <label
        for="project"
        class="block mb-2 text-sm font-medium text-gray-900">
        Tell us a little bit about your project <span class="text-red-600">*</span>
      </label>
      <textarea
        v-model="contactFormData.description"
        id="project"
        rows="4"
        class="block p-2.5 text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-orange-400 focus:border-blue-500 w-full"
        placeholder="Write your thoughts here..."
        required
      >
      </textarea>
    </div>

    <div class="flex">
      <div class="flex flex-col w-1/2">
        <label
          for="project"
          class="block mb-2 text-sm font-medium text-gray-900">
          What type of project are you interested in? <span class="text-red-600">*</span>
        </label>
        <div class="flex items-center">
          <input
            v-model="contactFormData.checkboxProjects.balconies"
            id="balconies-checkbox"
            type="checkbox"
            class="w-4 h-4 text-orange-400 bg-gray-100 border-gray-300 rounded focus:ring-orange-400"
          />
          <label
            for="balconies-checkbox"
            class="ms-2 text-sm font-medium text-gray-900">
            Balconies
          </label>
        </div>
        <div class="flex items-center">
          <input
            v-model="contactFormData.checkboxProjects.doors"
            id="doors-checkbox"
            type="checkbox"
            class="w-4 h-4 text-orange-400 bg-gray-100 border-gray-300 rounded focus:ring-orange-400"
          />
          <label
            for="doors-checkbox"
            class="ms-2 text-sm font-medium text-gray-900">
            Doors
          </label>
        </div>
        <div class="flex items-center">
          <input
            v-model="contactFormData.checkboxProjects.fences"
            id="fences-checkbox"
            type="checkbox"
            class="w-4 h-4 text-orange-400 bg-gray-100 border-gray-300 rounded focus:ring-orange-400"
          />
          <label
            for="fences-checkbox"
            class="ms-2 text-sm font-medium text-gray-900">
            Fences
          </label>
        </div>
        <div class="flex items-center">
          <input
            v-model="contactFormData.checkboxProjects.furniture"
            id="furniture-checkbox"
            type="checkbox"
            class="w-4 h-4 text-orange-400 bg-gray-100 border-gray-300 rounded focus:ring-orange-400"
          />
          <label
            for="furniture-checkbox"
            class="ms-2 text-sm font-medium text-gray-900">
            Furniture
          </label>
        </div>
        <div class="flex items-center">
          <input
            v-model="contactFormData.checkboxProjects.gates"
            id="gates-checkbox"
            type="checkbox"
            class="w-4 h-4 text-orange-400 bg-gray-100 border-gray-300 rounded focus:ring-orange-400"
          />
          <label
            for="gates-checkbox"
            class="ms-2 text-sm font-medium text-gray-900">
            Gates
          </label>
        </div>
        <div class="flex items-center">
          <input
            v-model="contactFormData.checkboxProjects.homeDecor"
            id="home-decor-checkbox"
            type="checkbox"
            class="w-4 h-4 text-orange-400 bg-gray-100 border-gray-300 rounded focus:ring-orange-400"
          />
          <label
            for="home-decor-checkbox"
            class="ms-2 text-sm font-medium text-gray-900">
            Home Decor
          </label>
        </div>
        <div class="flex items-center">
          <input
            v-model="contactFormData.checkboxProjects.lighting"
            id="lighting-checkbox"
            type="checkbox"
            class="w-4 h-4 text-orange-400 bg-gray-100 border-gray-300 rounded focus:ring-orange-400"
          />
          <label
            for="lighting-checkbox"
            class="ms-2 text-sm font-medium text-gray-900">
            Lighting
          </label>
        </div>
        <div class="flex items-center">
          <input
            v-model="contactFormData.checkboxProjects.railings"
            id="railings-checkbox"
            type="checkbox"
            class="w-4 h-4 text-orange-400 bg-gray-100 border-gray-300 rounded focus:ring-orange-400"
          />
          <label
            for="railings-checkbox"
            class="ms-2 text-sm font-medium text-gray-900">
            Railings
          </label>
        </div>
        <div class="flex items-center">
          <input
            v-model="contactFormData.checkboxProjects.restoration"
            id="restoration-checkbox"
            type="checkbox"
            class="w-4 h-4 text-orange-400 bg-gray-100 border-gray-300 rounded focus:ring-orange-400"
          />
          <label
            for="restoration-checkbox"
            class="ms-2 text-sm font-medium text-gray-900">
            Restoration
          </label>
        </div>
        <div class="flex items-center">
          <input
            v-model="contactFormData.checkboxProjects.sculptures"
            id="sculptures-checkbox"
            type="checkbox"
            class="w-4 h-4 text-orange-400 bg-gray-100 border-gray-300 rounded focus:ring-orange-400"
          />
          <label
            for="sculptures-checkbox"
            class="ms-2 text-sm font-medium text-gray-900">
            Sculptures
          </label>
        </div>
        <div class="flex items-center">
          <input
            v-model="contactFormData.checkboxProjects.wineCellars"
            id="wine-cellars-checkbox"
            type="checkbox"
            class="w-4 h-4 text-orange-400 bg-gray-100 border-gray-300 rounded focus:ring-orange-400"
          />
          <label
            for="wine-cellars-checkbox"
            class="ms-2 text-sm font-medium text-gray-900">
            Wine Cellars
          </label>
        </div>
        <div class="flex items-center">
          <input
            v-model="contactFormData.checkboxProjects.other"
            id="other-checkbox"
            type="checkbox"
            class="w-4 h-4 text-orange-400 bg-gray-100 border-gray-300 rounded focus:ring-orange-400"
          />
          <label
            for="other-checkbox"
            class="ms-2 text-sm font-medium text-gray-900">
            Other
          </label>
        </div>
      </div>

      <div class="flex flex-col">
        <label
          for="project"
          class="block mb-2 text-sm font-medium text-gray-900">
          Are you a home owner, designer, architect pr contractor? <span class="text-red-600">*</span>
        </label>
        <div class="flex items-center">
          <input
            v-model="contactFormData.checkboxProfessions.homeOwner"
            id="home-owner-checkbox"
            type="checkbox"
            class="w-4 h-4 text-orange-400 bg-gray-100 border-gray-300 rounded focus:ring-orange-400"
          />
          <label
            for="home-owner-checkbox"
            class="ms-2 text-sm font-medium text-gray-900">
            Home Owner
          </label>
        </div>
        <div class="flex items-center">
          <input
            v-model="contactFormData.checkboxProfessions.designer"
            id="designer-checkbox"
            type="checkbox"
            class="w-4 h-4 text-orange-400 bg-gray-100 border-gray-300 rounded focus:ring-orange-400"
          />
          <label
            for="designer-checkbox"
            class="ms-2 text-sm font-medium text-gray-900">
            Designer
          </label>
        </div>
        <div class="flex items-center">
          <input
            v-model="contactFormData.checkboxProfessions.architect"
            id="architect-checkbox"
            type="checkbox"
            class="w-4 h-4 text-orange-400 bg-gray-100 border-gray-300 rounded focus:ring-orange-400"
          />
          <label
            for="architect-checkbox"
            class="ms-2 text-sm font-medium text-gray-900">
            Architect
          </label>
        </div>
        <div class="flex items-center">
          <input
            v-model="contactFormData.checkboxProfessions.contact"
            id="contractor-checkbox"
            type="checkbox"
            class="w-4 h-4 text-orange-400 bg-gray-100 border-gray-300 rounded focus:ring-orange-400"
          />
          <label
            for="contractor-checkbox"
            class="ms-2 text-sm font-medium text-gray-900">
            Contractor
          </label>
        </div>
        <div class="flex items-center">
          <input
            v-model="contactFormData.checkboxProfessions.other"
            id="other-checkbox"
            type="checkbox"
            class="w-4 h-4 text-orange-400 bg-gray-100 border-gray-300 rounded focus:ring-orange-400"
          />
          <label
            for="other-checkbox"
            class="ms-2 text-sm font-medium text-gray-900">
            Other
          </label>
        </div>
      </div>
    </div>

    <div>
      <label
        for="phone-input"
        class="block mb-2 text-sm font-medium text-gray-900">
        Phone number <span class="text-red-600">*</span>
      </label>
      <div
        class="flex items-center space-x-4">
        <svg
          class="w-4 h-4 text-gray-500"
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          fill="currentColor"
          viewBox="0 0 19 18">
          <path
            d="M18 13.446a3.02 3.02 0 0 0-.946-1.985l-1.4-1.4a3.054 3.054 0 0 0-4.218 0l-.7.7a.983.983 0 0 1-1.39 0l-2.1-2.1a.983.983 0 0 1 0-1.389l.7-.7a2.98 2.98 0 0 0 0-4.217l-1.4-1.4a2.824 2.824 0 0 0-4.218 0c-3.619 3.619-3 8.229 1.752 12.979C6.785 16.639 9.45 18 11.912 18a7.175 7.175 0 0 0 5.139-2.325A2.9 2.9 0 0 0 18 13.446Z"
          />
        </svg>
        <input
          v-model="contactFormData.contact"
          type="text"
          id="phone-input"
          aria-describedby="helper-text-explanation"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-orange-400 focus:border-blue-500 block w-full"
          placeholder="Type your phone number"
          required
        />
      </div>
    </div>

    <div>
      <label
        for="hear_about_us"
        class="block mb-2 text-sm font-medium text-gray-900">
        How did your hear about us? <span class="text-red-600">*</span>
      </label>
      <select
        v-model="contactFormData.hearAboutUs"
        id="hear_about_us"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-orange-400 focus:border-blue-500 block w-full">
        <option disabled selected>Choose an option</option>
        <option value="Web page">Web page</option>
        <option value="Instagram">Instagram</option>
        <option value="Friend">Friend</option>
        <option value="Internet">Internet</option>
        <option value="Other">Other</option>
      </select>

      <button
        type="submit"
        class="mt-8 text-white bg-gray_p hover:bg-black px-8 py-4 font-regular text-1xl uppercase">
        Submit
      </button>
    </div>
  </form>
</template>

<script setup>
  import { reactive, onMounted } from "vue";
  import { submitHandler } from "@/shared/submit_handler";

  let geetest = '';

  const contactFormData = reactive({
    firstName: "",
    lastName: "",
    email: "",
    contact: "",
    subject: "",
    description: "",
    checkboxProjects: {},
    checkboxProfessions: {
      'Home Owner': false,
      'Designer': false,
      'Architect': false,
      'Contractor': false,
      'Other': false
    },
    hearAboutUs: "Choose an option",
  });
  
  /**
   * Submit event.
   */
  const onSubmit = () => {
    geetest.showBox()
  };
  
  /**
   * Clean review form
   */
  const cleanForm = () => {
    contactFormData.firstName = "";
    contactFormData.lastName = "";
    contactFormData.email = "";
    contactFormData.contact = "";
    contactFormData.subject = "";
    contactFormData.description = "";
    contactFormData.checkboxProjects = {};
    contactFormData.checkboxProfessions = {};
    contactFormData.hearAboutUs = "Choose an option";
  };
  onMounted ( () => {
  initGeetest4(
    {
      // Omit required configuration parameters

      product: "bind",
      captchaId: "1a4ad98cb6ead7c70d67784d91461598",
        },
        function (captchaObj) {
          geetest = captchaObj;
          captchaObj
            .onReady(function () {
              // please call the showCaptcha method to show the CAPTCHA when it is ready
            })
            .onSuccess(function () {
              submitHandler(contactFormData, "Submited!");
              cleanForm();
            })
            .onError(function () {
              //your code
            });
        }
      );
    })
</script>
