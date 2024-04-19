import {FacultiesData} from "../../../../stores/FacultiesStore";
import {useEffect, useState} from "react";
import SingleSemester from "@/components/SpecPage/Semester/SingleSemester";

const SemestersList = ({URL}) => {


    const [data, setData] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            FacultiesData.getSpecialityInfo(URL).then(
                data => {
                    setData(data)
                }
            )
        }
        fetchData()
    }, []);

    return (
        <div className={"mt-8"}>
            {data && data.semesters.map((semester, id) => {
                return <SingleSemester key={id} data={semester}/>
            })}
        </div>
    )
}

export default SemestersList