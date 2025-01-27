import { useState } from "react"
import Image from "next/image"
import Link from "next/link"
import MenuOverlay from "@/components/MenuOverlay"

const Header = ({ onHomeClick }) => {
  const [isMenuOpen, setMenuOpen] = useState(false)
  return (
    <header className="fixed left-0 top-16 z-30 w-full lg:top-[10vh]">
      <div className="px-10 lg:px-[10vw]">
        <div className="relative z-20 flex items-center justify-between">
          <div className="flex gap-x-28">
            <div
              className="font-emily text-4xl text-white"
              onClick={onHomeClick}
              role="button"
            >
              Sterling Lentz
            </div>
            <span className="mt-1.5 hidden text-xl text-[var(--header-text-color)] lg:inline-block">
              Writer, creative director, and founder
            </span>
          </div>
          <div className="hidden space-x-7 text-xl lg:block">
            <Link
              className="text-[var(--header-text-color)] transition-colors hover:text-white"
              href="/"
            >
              My Story
            </Link>
            <Link
              className="text-[var(--header-text-color)] transition-colors hover:text-white"
              href="/"
            >
              Contact
            </Link>
          </div>
          <button
            className="flex h-10 w-10 items-center justify-center active:translate-x-px active:translate-y-px lg:hidden"
            onClick={() => setMenuOpen(!isMenuOpen)}
          >
            {isMenuOpen ? (
              <Image
                src="/icons/close-icon.svg"
                width={32}
                height={32}
                alt="Close Icon"
              />
            ) : (
              <Image
                src="/icons/menu-icon.svg"
                width={32}
                height={32}
                alt="Menu Icon"
              />
            )}
          </button>
        </div>
        {isMenuOpen && <MenuOverlay />}
      </div>
    </header>
  )
}

export default Header
