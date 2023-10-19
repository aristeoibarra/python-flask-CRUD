/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/templates/**/*.html"],
  theme: {
    extend: {
      fontFamily: {
        body: ["Montserrat", "serif"]
      },
      colors: {
        haiti: {
          50: "#eff1fe",
          100: "#e1e6fe",
          200: "#c9d0fc",
          300: "#a8b2f9",
          400: "#858af4",
          500: "#6c68ec",
          600: "#5c4cdf",
          700: "#503dc5",
          800: "#41349f",
          900: "#38317e",
          950: "#1a1638"
        }
      }
    }
  },
  plugins: []
};
