/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        'bold': ['Roboto-Bold', 'sans-serif'],
        'regular': ['Roboto-Regular', 'sans-serif'],
        'light': ['Roboto-Light', 'sans-serif'],
      },
      colors: {
        'gray_p': '#2F2E2E',
        'header_p': '#131313',
      }
    },
  },
  plugins: [
    require('@tailwindcss/aspect-ratio'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('flowbite/plugin'),
  ],
}

