import { useState } from "react"
import Image from "next/image"
import Link from "next/link"
import MenuOverlay from "@/components/MenuOverlay"
import cx from "classnames"

const Header = ({ onClickHome }) => {
  const [isMenuOpen, setMenuOpen] = useState(false)
  return (
    <header className="header">
      <div className="px-10 lg:px-[10vw]">
        <div className="relative z-20 flex items-center justify-between">
          <div className="flex gap-x-28">
            <HomeLink
              className={cx("font-emily text-4xl", {
                "text-white lg:text-inherit": isMenuOpen,
              })}
              onClick={onClickHome}
            >
              Sterling Lentz
            </HomeLink>
            <span className="mt-1.5 hidden text-xl text-[var(--header-text-color)] lg:inline-block">
              Writer, creative director, and founder
            </span>
          </div>
          <div className="hidden space-x-7 text-xl lg:block">
            <Link
              className="text-[var(--header-text-color)] transition-colors hover:text-[var(--header-link-hover)]"
              href="/about"
            >
              My Story
            </Link>
            <Link
              className="text-[var(--header-text-color)] transition-colors hover:text-[var(--header-link-hover)]"
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
        {isMenuOpen && <MenuOverlay onClickItem={() => setMenuOpen(false)} />}
      </div>
    </header>
  )
}

const HomeLink = ({ children, onClick, ...props }) => {
  if (onClick) {
    return (
      <button onClick={onClick} {...props}>
        {children}
      </button>
    )
  }
  return (
    <Link href="/" {...props}>
      {children}
    </Link>
  )
}

export default Header
