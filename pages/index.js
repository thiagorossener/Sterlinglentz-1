import { useEffect, useState } from "react"
import Image from "next/image"

import Header from "@/components/Header"
import Page from "@/components/Page"
import Sidebar from "@/components/Sidebar"

import { projects } from "@/data/projects"

export default function Home() {
  const [currentProject, setCurrentProject] = useState()

  useEffect(() => {
    document.body.classList.add("is-home")
    return () => {
      document.body.classList.remove("is-home")
      document.body.classList.remove(currentProject?.themeClass)
    }
  })

  const handleProjectChange = (newProject) => {
    if (currentProject) {
      document.body.classList.remove(currentProject.themeClass)
    }
    if (newProject) {
      document.body.classList.add(newProject.themeClass)
    }
    setCurrentProject(newProject)
  }

  return (
    <>
      <Header onClickHome={() => handleProjectChange(null)} />
      <Sidebar
        projects={projects}
        activeProject={currentProject}
        onChangeProject={handleProjectChange}
      />
      <Page hide={!!currentProject}>
        <h1 className="font-emily text-7xl text-white lg:text-8xl">
          No bridge too far, no mountain too high
        </h1>
        <div className="mt-4 max-w-lg text-xl lg:text-2xl">
          <p>
            I create brands that magnify the power and promise of the human
            experience.
          </p>
        </div>
        <p className="mt-9 text-lg text-crimson lg:text-xl">
          Let’s do something bold...
        </p>
        <div className="relative -mx-10 -mt-20 lg:static lg:mx-0 lg:mt-0">
          <Image
            className="absolute right-0 top-0 -z-1"
            src="/images/portrait-1.jpg"
            width={585}
            height={585}
            alt="Portrait"
          />
          <Image
            className="absolute left-0 top-[180px] -z-1 w-[225px] lg:left-auto lg:right-[380px] lg:top-[250px] lg:w-auto"
            src="/images/portrait-2.jpg"
            width={288}
            height={433}
            alt="Portrait"
          />
        </div>
      </Page>
      {projects.map((project) => {
        return (
          <Page
            key={project.name}
            image={project.background}
            hide={currentProject !== project}
          >
            {project.component}
          </Page>
        )
      })}
    </>
  )
}
