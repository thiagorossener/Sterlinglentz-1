import Image from "next/image"
import Link from "next/link"
import ProjectIcon from "@/components/ProjectIcon"

const TheoryLab = () => {
  return (
    <>
      <ProjectIcon
        src="/images/theory-icon.png"
        alt="Theory Lab Icon"
        bgClass="bg-bitter-lemon"
      />
      <Image
        className="w-[19rem] lg:w-[27rem]"
        src="/images/theory-logo.svg"
        width={1170}
        height={96}
        alt="Theory Lab Logo"
      />
      <div className="text-green-spring mt-10 max-w-lg text-xl lg:text-2xl">
        <p>
          Emergent technologies like AI, quantum computing, and robotics demand
          an equally revolutionary shift in design paradigms. The visual
          language of tech: repetitive grids, lines, and plexus webs, has
          remained largely stagnant for over 40 years. Theory Lab aims to change
          that through novel creative approaches that capture the awe and wonder
          of the technology itself.
        </p>
      </div>
      <Link className="button button-theory mt-7" href="/">
        Work with us
      </Link>
    </>
  )
}

export default TheoryLab
