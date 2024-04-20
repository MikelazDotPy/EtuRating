/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx,mdx}", // Применяем стили ко всем файлам в папке src и ее подпапках
  ],
  theme: {
    extend: {
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
            "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      colors: {
        "overall-purple": "#7653FC",
        "overall-grey": "#dfdfdf",
        "dark-grey": "#3B434E",
      },
      screens: {
        'mobile': '300px',
        // => @media (min-width: 640px) { ... }

        // => @media (min-width: 1024px) { ... }

        'desktop': '1280px',
        // => @media (min-width: 1280px) { ... }
        }
      },
  },
  plugins: [],
};