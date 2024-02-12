import axios from "axios";
import { cl } from "../../components/base_imports";

const HOST = window.location.hostname;
const API_URL = `http://${HOST}:8000/`;

export async function getHouses() {
  return await axios.get(API_URL + "house").then((res) => {
    return res.data;
  });
}
