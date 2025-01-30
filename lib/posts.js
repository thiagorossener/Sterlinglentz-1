import fs from "fs"
import path from "path"
import matter from "gray-matter"

const postsDirectory = path.join(process.cwd(), "posts")

export function getAllPostIds() {
  const fileNames = fs.readdirSync(postsDirectory)

  // Returns an array that looks like this:
  // [
  //   {
  //     params: {
  //       slug: 'ssg-ssr'
  //     }
  //   },
  //   {
  //     params: {
  //       slug: 'pre-rendering'
  //     }
  //   }
  // ]
  return fileNames.map((fileName) => {
    return {
      params: {
        slug: fileName.replace(/\.md$/, ""),
      },
    }
  })
}

export async function getPostData(slug) {
  const fileNames = fs.readdirSync(postsDirectory)
  const fileName = fileNames.filter((fileName) => {
    return fileName.endsWith(`${slug}.md`)
  })[0]
  const fullPath = path.join(postsDirectory, fileName)
  const fileContents = fs.readFileSync(fullPath, "utf8")

  // Use gray-matter to parse the post metadata section
  const matterResult = matter(fileContents)

  // Get markdown content
  const markdown = matterResult.content

  // Combine the data with the id
  return {
    slug,
    markdown,
    ...matterResult.data,
  }
}
