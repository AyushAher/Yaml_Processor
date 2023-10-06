import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
import Navbar from "./Components/navbar";
import FileUpload from "./FileUploader";
import { BrowserRouter, Route, Routes } from "react-router-dom";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route element={<Navbar />}>
            <Route path="/manage" element={<FileUpload />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
