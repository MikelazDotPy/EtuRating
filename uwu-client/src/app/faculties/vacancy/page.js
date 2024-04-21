"use client"

// pages/faculties/vacancy.js

import {useEffect, useState} from "react";
import {FacultiesData} from "../../../../stores/FacultiesStore";
import Vacansy from "@/app/faculties/vacancy/Vacansy";

export default function Vacancy() {
    const URL = window.location.href;
    const queryParam = URL.split("?")[1]

    const [data, setData] = useState(null);

    useEffect(() => {
        const fetchVacancy = async () => {
            const res = await FacultiesData.getVacancy(queryParam)
            setData(res)
            if (data) {
            }
        }
        fetchVacancy()
    }, [URL])

    return (
        <div>
            {/*<h1>{data && data[1].title}</h1>*/}
            <h2 className="mt-[95px] text-[26px]">Профессии, доступные после обучения</h2>
            <div className="mt-7">{data && data.map(obj => <Vacansy skills={obj}/>)}</div>

        </div>
    );
}