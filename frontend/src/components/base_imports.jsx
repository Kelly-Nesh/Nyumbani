import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Spinner from 'react-bootstrap/Spinner';
import Form from 'react-bootstrap/Form';
import Alert from 'react-bootstrap/Alert';
export const BASE_URL = 'http://192.168.14.153:8000';
export const HEADERS = { headers: { Authorization: 'Token' } };

export const cl = console.log;

export const LAYOUT = {
  Alert,
  Container,
  Row,
  Col,
  Button,
  Card,
  Form
};
