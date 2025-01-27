import TheoryLab from "@/projects/TheoryLab"
import FundamentalArtifact from "@/projects/FundamentalArtifact"
import MaintainTheStandard from "@/projects/MaintainTheStandard"
import BHBC from "@/projects/BHBC"
import Virtuous from "@/projects/Virtuos"

export const projects = [
  {
    name: "Theory Lab",
    background: "/images/theory-background.jpg",
    icon: "/images/theory-icon.png",
    themeClass: "theme-theory",
    component: <TheoryLab />,
  },
  {
    name: "Fundamental Artifact",
    background: "/images/fa-background.jpg",
    icon: "/images/fa-icon.png",
    themeClass: "theme-fa",
    component: <FundamentalArtifact />,
  },
  {
    name: "Maintain The Standard",
    background: "/images/mts-background.jpg",
    icon: "/images/mts-icon.png",
    themeClass: "theme-mts",
    component: <MaintainTheStandard />,
  },
  {
    name: "BHBC",
    background: "/images/bhbc-background.jpg",
    icon: "/images/bhbc-icon.png",
    themeClass: "theme-bhbc",
    component: <BHBC />,
  },
  {
    name: "Virtuous",
    background: "/images/virtuos-background.jpg",
    icon: "/images/virtuos-icon.png",
    themeClass: "theme-virtuos",
    component: <Virtuous />,
  },
]
