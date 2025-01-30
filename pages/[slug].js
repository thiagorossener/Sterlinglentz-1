import { getAllPostIds, getPostData } from "@/lib/posts"
import MarkdownContent from "@/components/MarkdownContent"
import Header from "@/components/Header"
import Page from "@/components/Page"
import site from "@/data/site.json"

export default function Post({ title, subtitle, markdown }) {
  return (
    <>
      <Header />
      <Page>
        <h1 className="max-w-5xl text-3xl font-bold text-midnight lg:text-6xl">
          {title}
        </h1>
        {subtitle && (
          <div className="mt-1 max-w-3xl text-lg lg:text-2xl">{subtitle}</div>
        )}
        <div className="mt-10 lg:mt-20">
          <MarkdownContent>{markdown}</MarkdownContent>
        </div>
        <footer className="mt-24 pb-12 text-sm text-sand lg:mt-48 lg:pb-24">
          {site.title} &copy; {new Date().getFullYear()}
        </footer>
      </Page>
    </>
  )
}

export async function getStaticPaths() {
  const paths = getAllPostIds()
  return {
    paths,
    fallback: false,
  }
}

export async function getStaticProps({ params }) {
  const postData = await getPostData(params.slug)
  return {
    props: postData,
  }
}
