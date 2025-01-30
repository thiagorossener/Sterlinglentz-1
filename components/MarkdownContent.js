import { forwardRef } from "react"
import Link from "next/link"
import { isExternalUrl } from "@/lib/utils"
import Markdown from "react-markdown"
import rehypeRaw from "rehype-raw"
import Image from "next/image"

const MarkdownContent = forwardRef(({ children }, ref) => {
  const components = {
    // <p></p>
    p: (props) => {
      const { node } = props

      // <img />
      if (node.children[0].tagName === "img") {
        const { src, alt, width, height } = node.children[0].properties

        return (
          <Image
            src={isExternalUrl(src) ? src : `/images/posts/${src}`}
            width={width || 800}
            height={height || 800}
            alt={alt || ""}
            unoptimized={isExternalUrl(src)}
          />
        )
      }

      return <p>{props.children}</p>
    },
    // <a></a>
    a: ({ href, children }) => {
      if (isExternalUrl(href)) {
        return (
          <Link href={href} rel="noopener noreferrer" target="_blank">
            {children}
          </Link>
        )
      }
      return <Link href={href}>{children}</Link>
    },
    // <iframe></iframe>
    iframe: ({ allowFullScreen, allowTransparency, node, ...rest }) => {
      return (
        <iframe
          allowFullScreen={allowFullScreen === "true" ? true : false}
          allowtransparency={allowTransparency}
          {...rest}
        ></iframe>
      )
    },
  }

  const rehypePlugins = [rehypeRaw]
  return (
    <article className="prose lg:prose-xl" ref={ref}>
      <Markdown components={components} rehypePlugins={rehypePlugins}>
        {children}
      </Markdown>
    </article>
  )
})

MarkdownContent.displayName = "MarkdownContent"

export default MarkdownContent
