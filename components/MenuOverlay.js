import Link from "next/link"
import { useEffect, useRef } from "react"
import { motion } from "motion/react"

const MenuOverlay = ({ onClickItem, isOpen, ...props }) => {
  const ulVariants = {
    open: {
      transition: { staggerChildren: 0.07, delayChildren: 0.1 },
    },
    closed: {
      transition: { staggerChildren: 0.05, staggerDirection: -1 },
    },
  }

  const liVariants = {
    open: {
      y: 0,
      opacity: 1,
      transition: {
        y: { stiffness: 1000, velocity: -100 },
      },
    },
    closed: {
      y: 50,
      opacity: 0,
      transition: {
        y: { stiffness: 1000 },
      },
    },
  }

  useEffect(() => {
    window.scrollTo(0, 0)
    document.body.classList.add("is-menu-open")
    return () => {
      document.body.classList.remove("is-menu-open")
    }
  })

  return (
    <motion.div
      className="fixed left-0 top-0 z-10 h-screen w-screen pt-52 text-3xl lg:hidden"
      {...props}
    >
      <Background />
      <motion.ul
        className="relative z-10 flex flex-col items-center space-y-12"
        variants={ulVariants}
        initial="closed"
        animate="open"
        exit="closed"
      >
        <motion.li variants={liVariants}>
          <Link
            className="text-green-spring transition-colors hover:text-white"
            href="/about"
            onClick={onClickItem}
          >
            My Story
          </Link>
        </motion.li>
        <motion.li variants={liVariants}>
          <Link
            className="text-green-spring transition-colors hover:text-white"
            href="/"
            onClick={onClickItem}
          >
            Contact
          </Link>
        </motion.li>
      </motion.ul>
    </motion.div>
  )
}

const Background = () => {
  const circleContainer = useRef()

  const createCircle = () => {
    let circle = document.createElement("div")
    circle.classList.add("circle")

    if (Math.random() > 0.35) {
      circle.classList.add("bg-mirage") // Light
    } else {
      circle.classList.add("bg-midnight") // Dark
    }

    circle.style.setProperty("--pos-x", Math.floor(Math.random() * 100) + "%")
    circle.style.setProperty("--pos-y", Math.floor(Math.random() * 100) + "%")
    circle.style.setProperty("--end-x", Math.floor(Math.random() * 100) + "%")
    circle.style.setProperty("--end-y", Math.floor(Math.random() * 100) + "%")

    setTimeout(() => {
      circle.remove()
    }, 8500)

    if (circleContainer.current) {
      circleContainer.current.appendChild(circle)
    }
  }

  const createCircles = () => {
    createCircle()
    createCircle()
    createCircle()
    createCircle()
    createCircle()
  }

  useEffect(() => {
    createCircles()
    setInterval(createCircles, 1000)
  })

  return (
    <div className="absolute left-0 top-0 flex h-screen w-screen items-center justify-center bg-midnight">
      <div
        className="absolute left-0 top-0 h-screen w-screen blur-[5vw]"
        ref={circleContainer}
      ></div>
    </div>
  )
}

export default MenuOverlay
