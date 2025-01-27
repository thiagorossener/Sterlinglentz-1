const { fontFamily } = require("tailwindcss/defaultTheme")

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./projects/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        canto: ["canto", ...fontFamily.serif],
        emily: ["emily-austin", ...fontFamily.sans],
      },
      colors: {
        black: "#000000",
        midnight: "#110F0F",
        mirage: "#1d2d34",
        tundora: "#454545",
        white: "#ffffff",
        sand: "#BAB3AA",
        bizarre: "#EDE3D5",
        "swiss-coffee": "#DDDAD9",
        crimson: "#CB4A4A",
        "golden-fizz": "#F0FC36",
        "bitter-lemon": "#CFDC06",
        "green-spring": "#B0B6AB",
        orient: "#00607A",
        "blue-chill": "#02657A",
        "black-squeeze": "#E4F2F4",
        gold: "#E9D58B",
      },
      boxShadow: {
        icon: "0px 4px 4px 0px rgba(0, 0, 0, 0.27)",
      },
      zIndex: {
        "-1": "-1",
      },
      container: {
        center: true,
        padding: "1.25rem",
      },
    },
  },
}
