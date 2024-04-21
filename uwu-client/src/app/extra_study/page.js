"use client"

import {FacultiesData} from "../../../stores/FacultiesStore";
import {useEffect, useState} from "react";
import ExtraStudyCard from "@/app/extra_study/ExtraStudyCard";

export default function Page() {

    const [data, setData] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            const res = await FacultiesData.getExtraEducationData()
            setData(res)
            console.log(res)
        }
        fetchData()
    }, []);

    return (
        <div>
            <h3 className="text-[26px] mt-10">Дополнительное образование для студентов</h3>
            {data && data.map(object => {
                return <ExtraStudyCard data={object}/>
            })}
        </div>
    )}