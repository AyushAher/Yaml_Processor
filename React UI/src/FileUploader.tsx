import React, { ChangeEvent, useEffect, useState } from "react";
import axios from "axios";

const FileUpload: React.FC = () => {
  const [apiUrl, setApiUrl] = useState("/");
  const [file, setFile] = useState<File | null>(null);
  const [userName, setUserName] = useState("");

  useEffect(() => {
    axios.get("/env.json").then((x) => {
      setApiUrl(x.data.apiUrl);
    });
  }, []);

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    const selectedFile = event.target.files && event.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
    }
  };

  const handleUpload = (e: any) => {
    e.preventDefault();
    if (!file || !userName) return;

    const formData = new FormData();
    formData.append("file", file);
    formData.append("username", userName);

    // Send the file using Axios
    axios
      .post(`${apiUrl}/api/upload`, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
      .then(() => {
        setFile(null);
        setUserName("");
      })
      .catch((error) => {
        console.error("Error uploading file:", error);
      });
  };

  return (
    <main className="main-container">
      <div className="container">
        <div className="d-flex justify-content-center">
          <div className="card mt-4" style={{ width: "50rem" }}>
            <div className="card-header">
              <h6>Manage `Ramson Developers` Server through YAML</h6>
            </div>
            <form onSubmit={handleUpload} autoComplete="false">
              <div className="card-body">
                <div className="col-md-12 mb-3">
                  <label htmlFor="userName">UserName</label>
                  <input
                    type="text"
                    name="userName"
                    id="userName"
                    className="form-control"
                    value={userName}
                    required
                    onChange={(e) => setUserName(e.target.value)}
                  />
                </div>
                <div className="col-md-12 mt-3">
                  <input
                    className="form-control"
                    type="file"
                    required
                    accept=".yaml"
                    onChange={handleFileChange}
                  />
                </div>
              </div>
              <div className="card-footer">
                <button type="submit" className="btn btn-success">
                  Upload
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </main>
  );
};

export default FileUpload;
