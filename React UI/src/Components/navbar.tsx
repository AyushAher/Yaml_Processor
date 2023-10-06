import { Outlet } from "react-router-dom";

export default function Navbar() {
  return (
    <div>
      <nav className="navbar navbar-expand-lg">
        <div className="container-fluid">
          <img
            className="navbar-brand logo me-4"
            src="/Images/Logo-Img.png"
            alt="Hyperspan Logo"
          />
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <a className="me-auto navbar-brand" href="#">
            YAML Management
          </a>
        </div>
      </nav>
      <Outlet />
    </div>
  );
}
