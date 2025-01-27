import Image from "next/image"
import Link from "next/link"
import ProjectIcon from "@/components/ProjectIcon"

const FundamentalArtifact = () => {
  return (
    <>
      <ProjectIcon
        src="/images/fa-icon.png"
        alt="Fundamental Artifact Icon"
        bgClass="bg-sand"
      />
      <div className="text-swiss-coffee text-xs uppercase tracking-[0.1em] lg:text-base">
        Launching summer 2025
      </div>
      <Image
        className="mt-4 w-[65rem]"
        src="/images/fa-logo.svg"
        width={1035}
        height={40}
        alt="Fundamental Artifact Logo"
      />
      <div className="text-sand mt-10 max-w-lg text-xl lg:text-2xl">
        <p>
          I circled the earth, twice, to design and curate a collection of
          fundamental artifacts. These lifestyle goods harken back to the
          earliest roots of human civilization, and at the same time peer
          forward into a distant future far from earth.
        </p>
      </div>
      <Link className="button button-fa mt-7" href="/">
        Get notified
      </Link>
    </>
  )
}

export default FundamentalArtifact
