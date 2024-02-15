import React, { useState, useEffect } from "react";
import useGetData from "../../services/hooks/useGetData";
import Spinner from "react-bootstrap/esm/Spinner";
import { LAYOUT, cl } from "../base_imports";
import { Link } from "react-router-dom";

const { Alert, Container, Row, Col } = LAYOUT;

const Agent = () => {
  const { data, isLoading, isError } = useGetData("agent");
  const [agents, setAgents] = useState([]);

  useEffect(() => {
    if (data) {
      setAgents(data);
    }
  }, [data]);

  if (isLoading) {
    return <Spinner />;
  }

  if (isError) {
    return <Alert variant="warning">Something went wrong</Alert>;
  }

  cl(agents);
  return (
    <Row className="gy-3">
      {agents.map((a) => {
        return (
          <Col xs={12} sm={6} lg={4} key={a.slug}>
            <img
              src="https://picsum.photos/id/117/1000"
              className="w-100 object-fit-cover"
              style={{ height: "20rem" }}
            />
            <Link to={a.slug} className="text-decoration-none text-black h3">
              {a.name}
            </Link>
            <p className="mb-0">{a.phone_number}</p>
            <small className="text-mute">Click to copy number.</small>
          </Col>
        );
      })}
    </Row>
  );
};

export default Agent;
