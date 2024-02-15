import "./App.css";
import { createBrowserRouter, Outlet } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import { LAYOUT } from "./components/base_imports.jsx";
import Home from "./components/home/home.jsx";
import Agent from "./components/agent/agent.jsx";

const { Container, Spinner } = LAYOUT;

function Layout() {
  return (
    <Container fluid>
      <div className="row sticky-top bg-white p-3">
        <div className="col-4">
          <a href="/" className="text-decoration-none text-black">
            Houses
          </a>
        </div>
        <div className="col-4">
          <a href="/agents" className="text-decoration-none text-black">
            Agents
          </a>
        </div>
        <div className="col-4">
          <a href="/saved" className="text-decoration-none text-black">
            Saved
          </a>
        </div>
      </div>
      <Outlet />
    </Container>
  );
}
const router = createBrowserRouter([
  {
    path: "",
    element: <Layout />,
    children: [
      { path: "", element: <Home /> },
      {
        path: "agents",
        children: [
          { path: "", element: <Agent /> },
          { path: ":agent", element: <Agent /> },
        ],
      },
      { path: "saved", element: <Home /> },
    ],
  },
]);
export default router;

export function LoadingScreen() {
  return (
    <div className="vh-100 d-flex justify-content-center align-items-center">
      <Spinner animation="border" variant="info" />
    </div>
  );
}
