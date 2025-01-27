import Image from "next/image"
import Link from "next/link"
import ProjectIcon from "@/components/ProjectIcon"

const Virtuous = () => {
  return (
    <>
      <ProjectIcon
        src="/images/virtuos-icon.png"
        alt="Virtuos Icon"
        bgClass="bg-black-squeeze"
      />
      <Image
        className="w-32 lg:w-[34rem]"
        src="/images/virtuos-logo.svg"
        width={536}
        height={127}
        alt="Virtuos Logo"
      />
      <div className="text-black-squeeze mt-10 max-w-lg text-xl lg:text-2xl">
        <p>
          Join Gilad Sommer, author, philosopher, and Director of the Chicago
          School at New Acropolis, and myself as we discuss how the art of{" "}
          <em>living philosophy</em> — turning knowledge into action — can
          transform our lives, and our world.
        </p>
      </div>
      <Link className="button button-virtuos mt-7" href="/" target="_blank">
        Listen on your favorite podcast app
      </Link>
    </>
  )
}

export default Virtuous
