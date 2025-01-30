const Link = ({ children, ...props }) => {
  if (props.href) {
    ;<Link {...props}>{children}</Link>
  }
  return <button {...props}>{children}</button>
}

export default Link
