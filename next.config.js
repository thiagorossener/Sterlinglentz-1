/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: false, // It's "false" to avoid duplicated pageviews on GA4
  trailingSlash: true,
  webpack(config) {
    config.module.rules.push({
      test: /\.svg$/i,
      issuer: /\.[jt]sx?$/,
      use: ["@svgr/webpack"],
    })
    return config
  },
}

module.exports = nextConfig
