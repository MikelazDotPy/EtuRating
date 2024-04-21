import {FacultiesData} from "../../../../stores/FacultiesStore";
import {useEffect, useState} from "react";
import SingleSemester from "@/components/SpecPage/Semester/SingleSemester";
import {observer} from "mobx-react";

const SemestersList = observer((data) => {

    // const [data, setData] = useState(null);

    return (
        <div className={"mt-8"}>
            {data.data.map((sem, index) => {
                return <SingleSemester data={sem} key={index} />
            })}
        </div>
    )
})

export default SemestersList