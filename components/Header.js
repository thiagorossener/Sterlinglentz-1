import { useState } from "react"
import Link from "next/link"
import MenuOverlay from "@/components/MenuOverlay"
import cx from "classnames"
import { AnimatePresence, motion } from "motion/react"

const Header = ({ onClickHome }) => {
  const [isMenuOpen, setMenuOpen] = useState(false)
  return (
    <header className="header">
      <div className="px-10 lg:px-[10vw]">
        <motion.nav
          className="relative z-20 flex items-center justify-between"
          initial="closed"
          animate={isMenuOpen ? "open" : "closed"}
        >
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
          <MenuToggle onClick={() => setMenuOpen(!isMenuOpen)} />
        </motion.nav>
        <AnimatePresence initial={false}>
          {isMenuOpen && (
            <MenuOverlay
              onClickItem={() => setMenuOpen(false)}
              transition={{ duration: 0.25 }}
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              isOpen={isMenuOpen}
            />
          )}
        </AnimatePresence>
      </div>
    </header>
  )
}

const MenuToggle = ({ onClick }) => {
  const Path = (props) => (
    <motion.path
      fill="transparent"
      strokeWidth="1"
      stroke="currentColor"
      strokeLinecap="round"
      {...props}
    />
  )

  return (
    <button
      className="flex h-10 w-10 items-center justify-center text-green-spring lg:hidden"
      onClick={onClick}
    >
      <svg width="23" height="23" viewBox="0 0 23 23">
        <Path
          variants={{
            closed: { d: "M 2 2.5 L 20 2.5" },
            open: { d: "M 3 16.5 L 17 2.5" },
          }}
        />
        <Path
          d="M 2 9.423 L 20 9.423"
          variants={{
            closed: { opacity: 1 },
            open: { opacity: 0 },
          }}
          transition={{ duration: 0.1 }}
        />
        <Path
          variants={{
            closed: { d: "M 2 16.346 L 20 16.346" },
            open: { d: "M 3 2.5 L 17 16.346" },
          }}
        />
      </svg>
    </button>
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
