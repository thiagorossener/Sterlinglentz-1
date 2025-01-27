import cx from "classnames"
import Image from "next/image"

const ProjectIcon = ({ bgClass, src, alt }) => {
  return (
    <>
      <div className="relative mb-10 inline-block lg:hidden">
        <div
          className={cx(
            "absolute left-0 top-0 -z-1 h-full w-full rounded-full opacity-50 blur-xl",
            bgClass
          )}
        ></div>
        <div className="shadow-icon absolute left-1/2 top-1/2 h-[90%] w-[90%] -translate-x-1/2 -translate-y-1/2 rounded-full"></div>
        <Image
          className="rounded-full"
          src={src}
          width={64}
          height={64}
          alt={alt}
        />
      </div>
      <hr className="mb-6 h-px w-4/5 border-0 bg-[var(--divider-color)] lg:hidden" />
    </>
  )
}

export default ProjectIcon
