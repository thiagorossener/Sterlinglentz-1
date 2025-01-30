import Image from "next/image"
import cx from "classnames"

const Page = ({ image, hide, children }) => {
  return (
    <div className={cx("page", hide ? "opacity-0" : "z-10 opacity-100")}>
      <div className="page-background">
        {image && (
          <Image
            className="h-full w-full"
            src={image}
            layout="fill"
            objectFit="cover"
            alt="Background Image"
          />
        )}
      </div>
      <div className="page-container">
        <div
          className={cx(
            "page-content",
            hide ? "translate-y-10" : "translate-y-0"
          )}
        >
          {children}
        </div>
      </div>
    </div>
  )
}

export default Page
