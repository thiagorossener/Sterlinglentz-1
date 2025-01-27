import Image from "next/image"
import Link from "next/link"
import ProjectIcon from "@/components/ProjectIcon"

const BHBC = () => {
  return (
    <>
      <ProjectIcon
        src="/images/bhbc-icon.png"
        alt="BHBC Icon"
        bgClass="bg-gold"
      />
      <Image
        className="w-24 lg:w-60"
        src="/images/bhbc-logo.svg"
        width={233}
        height={181}
        alt="BHBC Logo"
      />
      <div className="mt-10 max-w-lg text-xl text-white lg:text-2xl">
        <p>
          Broken Heart Boys Club is a resource for young men from from broken
          homes to learn inner awareness, grit, and strength of character in the
          face of impossible odds.
        </p>
      </div>
      <Link
        className="button button-bhbc mt-7"
        href="https://www.brokenheartboysclub.com/"
        target="_blank"
      >
        Visit the site
      </Link>
    </>
  )
}

export default BHBC
