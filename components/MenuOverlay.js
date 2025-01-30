import Link from "next/link"
import { useEffect, useRef } from "react"

const MenuOverlay = ({ onClickItem }) => {
  return (
    <div className="fixed left-0 top-0 z-10 h-screen w-screen pt-52 text-3xl lg:hidden">
      <Background />
      <ul className="relative z-10 flex flex-col items-center space-y-12">
        <li>
          <Link
            className="text-sand transition-colors hover:text-white"
            href="/about"
            onClick={onClickItem}
          >
            My Story
          </Link>
        </li>
        <li>
          <Link
            className="text-sand transition-colors hover:text-white"
            href="/"
            onClick={onClickItem}
          >
            Contact
          </Link>
        </li>
      </ul>
    </div>
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
