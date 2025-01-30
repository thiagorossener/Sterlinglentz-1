export function isExternalUrl(url) {
  if (url.startsWith("http")) {
    return true
  }
  return false
}
