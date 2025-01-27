import Image from "next/image"
import Link from "next/link"
import ProjectIcon from "@/components/ProjectIcon"

const MaintainTheStandard = () => {
  return (
    <>
      <ProjectIcon
        src="/images/mts-icon.png"
        alt="Maintain The Standard Icon"
        bgClass="bg-black-squeeze"
      />
      <Image
        className="w-[63rem]"
        src="/images/mts-logo.svg"
        width={1825}
        height={96}
        alt="Maintain The Standard Logo"
      />
      <div className="text-black-squeeze mt-10 max-w-lg text-xl lg:text-2xl">
        <p>
          We are renewing faith in the timeless philosophical principles that
          inspire human progress. These classical values: justice, truth, unity,
          compassion, service, are the true pillars of all great nations. They
          must be maintained.
        </p>
      </div>
      <Link className="button button-mts mt-7" href="/">
        Read on Substack
      </Link>
    </>
  )
}

export default MaintainTheStandard
