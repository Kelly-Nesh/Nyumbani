import "./home.css";
import { cl, LAYOUT } from "../base_imports.jsx";
import Carousel from "react-bootstrap/Carousel";
import { CiBookmarkPlus } from "react-icons/ci";
import { GiCheckMark } from "react-icons/gi";
import Button from "react-bootstrap/esm/Button.js";
import useGetHouse from "../../services/hooks/useGetHouses.jsx";
import { useEffect, useState } from "react";
import Spinner from "react-bootstrap/esm/Spinner.js";
import { GrClose } from "react-icons/gr";
const { Row, Col, Alert } = LAYOUT;

function Home() {
  const { data, isLoading, isError } = useGetHouse();
  const [houses, setHouses] = useState([]);

  useEffect(() => {
    if (data) {
      setHouses(data);
    }
  }, [data]);

  if (isLoading) return <Spinner variant="success" />;
  if (isError) return <Alert variant="warning">Something went wrong</Alert>;

  const controls = window.innerWidth > 992 ? true : false;

  const mappedHouses = houses.map((h, idx) => {
    cl(h.images);
    h.images.push(
      { image: `https://picsum.photos/id/${idx * 3}/1000` },
      { image: `https://picsum.photos/id/${idx * 5}/1000` }
    );
    return (
      <Col sm={6} lg={4} className="p-0 pb-3 house" key={h.slug}>
        <Row className="m-auto">
          <Col xs={4} className="">
            <img
              src="/src/assets/profile.jpg"
              className="rounded-circle w-100 h-100"
            />
          </Col>
          <Col
            xs={8}
            className="d-flex flex-column justify-content-center pe-0 reset"
          >
            <h2>{h.agent.name}</h2>
            <small className="text-muted">1wk&nbsp;7 Followers</small>
          </Col>
        </Row>
        <div>
          <Carousel controls={controls} interval={null}>
            {h.images.map(({ image }, idx) => {
              cl(image);
              return (
                <Carousel.Item key={idx}>
                  <img src={image} className="w-100" />
                  <Carousel.Caption className="ps-3 w-100 text-start reset">
                    <h3 className="d-inline-block">KES {h.price}</h3>
                    <p className="d-inline-block">&nbsp;every month</p>
                  </Carousel.Caption>
                </Carousel.Item>
              );
            })}
          </Carousel>
        </div>
        <div>
          <div className=" d-flex justify-content-between m-3">
            <div className="reset">
              <h4>{h.name}</h4>
              <p>{h.location.name}</p>
            </div>
            <div className="reset text-end">
              <p className="d-inline me-2">
                {h.available ? (
                  <>
                    <GiCheckMark /> Available
                  </>
                ) : (
                  <>
                    <GrClose /> Unavailable
                  </>
                )}
              </p>
              <br />
              <CiBookmarkPlus className="display-6 icon" />
            </div>
          </div>
          <div>
            <Row className="w-100 justify-content-between">
              <Col xs={3} className="house-details reset my-1 mx-2">
                <h5>{h.bedrooms}</h5>
                <p>Bedrooms</p>
              </Col>
              <Col xs={3} className="house-details reset my-1 mx-2">
                <h5>{h.bathrooms}</h5>
                <p>Bathrooms</p>
              </Col>
              <Col xs={3} className="house-details reset my-1 mx-2">
                <h5></h5>
                <p>Pets {h.pets_allowed && "Not"} Allowed</p>
              </Col>
              <Col className="text-end">
                <Button variant="success" className="py-2 px-3">
                  Contact
                </Button>
              </Col>
            </Row>
          </div>
        </div>
      </Col>
    );
  });

  return (
    <Row className="gy-3 gap-4 justify-content-around ">{mappedHouses}</Row>
  );
}

export default Home;

function CarouselItem({ images, price }) {
  const mi = [];
  for (let i = 0; i <= 5; i++) {
    mi.push(
      <Carousel.Item className={i == 0 ? "active" : ""}>
        <img src="https://picsum.photos/500" className="w-100" />
        <Carousel.Caption className="ps-3 w-100 text-start reset">
          <h3 className="d-inline-block">KES {price}</h3>
          <p className="d-inline-block">&nbsp;every month</p>
        </Carousel.Caption>
      </Carousel.Item>
    );
  }
  return mi;
}
