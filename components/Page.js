import Image from "next/image"
import cx from "classnames"

const Page = ({ image, children, show }) => {
  return (
    <div
      className={cx(
        "fixed left-0 top-0 h-screen w-screen transition-opacity duration-[250ms]",
        show ? "z-10 opacity-100" : "opacity-0"
      )}
    >
      <div className="bg-midnight absolute left-0 top-0 -z-1 h-full w-full transition-opacity duration-[250ms]">
        {image && (
          <Image
            className="h-full w-full"
            src={image}
            layout="fill"
            objectFit="cover"
          />
        )}
      </div>
      <div className="w-full pt-48 lg:absolute lg:bottom-0 lg:left-0 lg:h-[65vh] lg:px-10 lg:pl-[22vw] lg:pr-7 lg:pt-0">
        <div
          className={cx(
            "relative px-10 transition-all duration-[250ms] lg:h-full lg:border-l lg:border-[var(--divider-color)] lg:pl-16 lg:pr-0",
            show ? "translate-y-0" : "translate-y-10"
          )}
        >
          {children}
        </div>
      </div>
    </div>
  )
}

export default Page
