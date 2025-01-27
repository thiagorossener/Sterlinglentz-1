import "@/styles/globals.css"
import Head from "next/head"
import { DefaultSeo } from "next-seo"
import site from "@/data/site.json"

export default function App({ Component, pageProps }) {
  return (
    <>
      <Head>
        <meta
          name="viewport"
          content="width=device-width, initial-scale=1"
        ></meta>
        <meta name="msapplication-TileColor" content="#000000"></meta>
        <meta name="theme-color" content="#ffffff"></meta>
        <link
          rel="stylesheet"
          href="https://use.typekit.net/rcb7iqw.css"
        ></link>
      </Head>
      <DefaultSeo
        title={site.title}
        description={site.description}
        openGraph={{
          type: "website",
          locale: site.locale,
          url: `${site.url}/`,
          siteName: site.name,
          images: [
            {
              url: "",
              width: 1200,
              height: 630,
              alt: "Sterling Lentz",
            },
          ],
        }}
        twitter={{
          cardType: "summary_large_image",
        }}
      />
      <Component {...pageProps} />
    </>
  )
}
