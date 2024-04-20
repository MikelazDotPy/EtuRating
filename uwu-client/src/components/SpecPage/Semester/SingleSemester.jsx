"use client"

import Discipline from "@/components/SpecPage/Semester/Discipline";
import {useState} from "react";

const SingleSemester = ({data}) => {

    const [isShown, setIsShown] = useState(false);

    return (
        <div className="w-full mt-[11px]">
            <div
                className="text-[24px] text-overall-purple"
                onClick={() => {setIsShown(!isShown)}}
            >{data.title}</div>
            <div className={"ml-5 mt-3"}>
                {data.disciplines.map(discipline => {
                    return <Discipline discipline={discipline} isShown={isShown} />
                })}
            </div>
        </div>
    )
}

export default SingleSemester