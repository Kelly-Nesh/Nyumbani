import './App.css'
import { createBrowserRouter, Outlet } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css'
import { LAYOUT } from './components/base_imports.jsx'
import Home from './components/home/home.jsx'

const { Container, Spinner } = LAYOUT

function Layout () {
  return (
    <Container fluid>
      <Outlet />
    </Container>
  )
}
const router = createBrowserRouter([
  {
    path: '',
    element: <Layout />,
    children: [
      { path: '', element: <Home /> }
    ]
  }
])
export default router

export function LoadingScreen () {
  return (
    <div className='vh-100 d-flex justify-content-center align-items-center'>
      <Spinner animation='border' variant='info' />
    </div>
  )
}
