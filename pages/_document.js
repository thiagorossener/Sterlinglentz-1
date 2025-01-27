import { Html, Head, Main, NextScript } from "next/document"
import site from "@/data/site"

export default function Document() {
  return (
    <Html lang={site.language}>
      <Head />
      <body>
        <Main />
        <NextScript />
        <noscript
          dangerouslySetInnerHTML={{
            __html: `<iframe src="https://www.googletagmanager.com/ns.html?id=${process.env.NEXT_PUBLIC_GTM_ID}" height="0" width="0" style="display: none; visibility: hidden;"></iframe>`,
          }}
        />
      </body>
    </Html>
  )
}
