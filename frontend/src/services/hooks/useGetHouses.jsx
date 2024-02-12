import { getHouses } from "../api/api";
import { useQuery } from "react-query";

function useGetHouse() {
  return useQuery({ queryKey: ["houses"], queryFn: getHouses });
}

export default useGetHouse;
