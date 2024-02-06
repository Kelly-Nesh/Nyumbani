import './home.css';
import { cl, LAYOUT } from '../base_imports.jsx';
import Carousel from 'react-bootstrap/Carousel';
import { CiBookmarkPlus } from 'react-icons/ci';
const { Container, Row, Col } = LAYOUT;

function Home () {
  const houses = [];
  for (let i = 0; i <= 5; i++) {
    houses.push(
    <Col sm={6} lg={4} className='m-0 p-0 pb-3 house' key={i}>
      <div className=''>{/* heading */}
        <div className='d-inline-block profile-pic m-2'><img src='/src/assets/profile.jpg' className='rounded-circle w-100 h-100' /></div>
        <div className='d-inline-block house-header reset'>
          <h2>Parles Realestate</h2>
          <small className='text-muted'>1wk&nbsp;7 Followers</small>
        </div>
      </div>
      <div>
        <Carousel controls={false} indicators={false} interval={null}>
          <Carousel.Item>
            <img src='/src/assets/main.jpg' className='w-100' />
            <Carousel.Caption
              className='ps-3 w-100 text-start reset'
            >
              <h3 className='d-inline-block'>KES 20,000</h3><p className='d-inline-block'>&nbsp;every month</p>
            </Carousel.Caption>
          </Carousel.Item>
           <Carousel.Item>
            <img src='/src/assets/main.jpg' className='w-100' />
            <Carousel.Caption
              className='ps-3 w-100 text-start reset'
            >
              <h3 className='d-inline-block'>KES 20,000</h3><p className='d-inline-block'>&nbsp;every month</p>
            </Carousel.Caption>
          </Carousel.Item>
        </Carousel>
      </div>
      <div>
        <div className=' d-flex justify-content-between m-3'>
          <div className='reset'>
            <h4>Palm ridge</h4>
            <p>Runda, Nairobi</p>
          </div>
          <div className='reset'>
            <CiBookmarkPlus className='display-6 icon' />
          </div>
        </div>
        <div>
          <Row className='w-100 justify-content-between'>
            <Col xs={3} className='house-details reset my-1 mx-2'>
              <h5>2</h5>
              <p>Bedrooms</p>
            </Col>
            <Col xs={3} className='house-details reset my-1 mx-2'>
              <h5>1</h5>
              <p>Bathrooms</p>
            </Col>
            <Col xs={3} className='house-details reset my-1 mx-2'>
              <h5>No</h5>
              <p>Pets Allowed</p>
            </Col>
          </Row>
        </div>
      </div>
    </Col>)
  }
  return (
    <Row className=''>
      {houses}
    </Row>
  );
}

export default Home;
