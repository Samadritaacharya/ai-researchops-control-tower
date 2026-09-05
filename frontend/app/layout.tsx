import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'AI ResearchOps — Governance Command Center',
  description: 'Interactive AI delivery governance for uncertainty, RAID, RACI, experiments, steering, and product handover.',
}

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>
}
