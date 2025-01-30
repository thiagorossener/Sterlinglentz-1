const { fontFamily } = require("tailwindcss/defaultTheme")

const round = (num) =>
  num
    .toFixed(7)
    .replace(/(\.[0-9]+?)0+$/, "$1")
    .replace(/\.0$/, "")
const em = (px, base) => `${round(px / base)}em`

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
        // Gray Scale
        white: "#ffffff",
        "dove-gray": "#676767",
        tundora: "#454545",
        black: "#000000",
        // Gradient
        "swiss-coffee": "#DDDAD9",
        bizarre: "#EDE3D5",
        sand: "#BAB3AA",
        "green-spring": "#B0B6AB",
        gold: "#E9D58B",
        crimson: "#CB4A4A",
        "golden-fizz": "#F0FC36",
        "bitter-lemon": "#CFDC06",
        "black-squeeze": "#E4F2F4",
        orient: "#00607A",
        "blue-chill": "#02657A",
        mirage: "#1d2d34",
        midnight: "#110F0F",
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
      typography: (theme) => ({
        xl: {
          css: {
            color: theme("colors.midnight"),
            lineHeight: 1.25,
            h1: {
              fontWeight: 700,
              color: theme("colors.midnight"),
            },
            h2: {
              fontWeight: 700,
              color: theme("colors.midnight"),
            },
            h3: {
              fontWeight: 700,
              color: theme("colors.midnight"),
            },
            h4: {
              fontWeight: 700,
              color: theme("colors.midnight"),
            },
            h5: {
              fontWeight: 700,
              color: theme("colors.midnight"),
            },
            h6: {
              fontWeight: 700,
              color: theme("colors.midnight"),
            },
            p: {
              marginTop: em(40, 20),
              marginBottom: em(40, 20),
            },
            blockquote: {
              marginTop: em(96, 30),
              marginBottom: em(40, 18),
              paddingLeft: em(145, 20),
            },
            "blockquote p": {
              margin: 0,
            },
            figcaption: {
              fontSize: em(16, 18),
              fontStyle: "italic",
              color: theme("colors.dove-gray"),
              textAlign: "center",
            },
            ul: {
              listStyleType: "disc",
            },
            ol: {
              listStyleType: "decimal",
            },
            a: {
              color: theme("colors.crimson"),
              transition: "color 150ms cubic-bezier(0.4, 0, 0.2, 1)",
            },
            "a:hover": {
              opacity: 0.5,
            },
            img: {
              marginLeft: "auto",
              marginRight: "auto",
            },
            iframe: {
              width: "100%",
            },
            table: {
              tableLayout: "auto",
              textAlign: "left",
              marginTop: em(32, 18),
              marginBottom: em(32, 18),
              marginLeft: "auto",
              marginRight: "auto",
              fontSize: em(20, 20),
              lineHeight: round(30 / 20),
            },
            thead: {
              borderBottomWidth: "1px",
              borderBottomColor: "var(--tw-prose-th-borders)",
            },
            "thead th": {
              color: "var(--tw-prose-headings)",
              fontWeight: "600",
              verticalAlign: "bottom",
            },
            "tbody tr": {
              borderBottomWidth: "1px",
              borderBottomColor: "var(--tw-prose-td-borders)",
            },
            "tbody tr:last-child": {
              borderBottomWidth: "0",
            },
            "tbody td": {
              verticalAlign: "baseline",
            },
            tfoot: {
              borderTopWidth: "1px",
              borderTopColor: "var(--tw-prose-th-borders)",
            },
            "tfoot td": {
              verticalAlign: "top",
            },
          },
        },
      }),
    },
  },
  plugins: [require("@tailwindcss/typography")],
}
