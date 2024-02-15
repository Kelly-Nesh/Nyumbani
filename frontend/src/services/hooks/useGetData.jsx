import { getData } from "../api/api";
import { useQuery } from "react-query";

function useGetData(item, slug) {
  return useQuery({ queryKey: ["houses", item, slug], queryFn: getData });
}

export default useGetData;
