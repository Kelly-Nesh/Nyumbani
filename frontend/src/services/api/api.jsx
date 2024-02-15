import axios from "axios";
import { cl } from "../../components/base_imports";

const HOST = window.location.hostname;
const API_URL = `http://${HOST}:8000/`;

export async function getData({ queryKey }) {
  const [_, item, slug] = queryKey;
  const url = slug ? item + slug : item;
  return await axios.get(API_URL + url).then((res) => {
    return res.data;
  });
}
