import Image from "next/image"
import cx from "classnames"

const Sidebar = ({ projects, activeProject, onChangeProject }) => {
  const activeIndex = projects.indexOf(activeProject)
  const nextIndex = activeIndex === projects.length - 1 ? 0 : activeIndex + 1
  const nextProject = projects[nextIndex]
  return (
    <div className="fixed bottom-9 right-9 z-20 h-16 w-16 lg:bottom-0 lg:left-[10vw] lg:right-0 lg:h-[65vh] lg:w-[210px]">
      <aside className="h-full w-full lg:w-auto lg:overflow-auto lg:pl-11">
        <ul className="h-full w-full lg:space-y-8">
          {projects.map((project) => (
            <li
              key={project.name}
              className={cx({
                "hidden lg:block": project.name !== nextProject.name,
              })}
            >
              <button
                className="block h-16 w-16 rounded-full active:translate-x-px active:translate-y-px"
                onClick={() => onChangeProject(project)}
              >
                <span className="sr-only">{project.name}</span>
                <Image
                  className="h-full w-full"
                  src={project.icon}
                  width={64}
                  height={64}
                  alt="Project Icon"
                />
              </button>
            </li>
          ))}
        </ul>
      </aside>
    </div>
  )
}

export default Sidebar
