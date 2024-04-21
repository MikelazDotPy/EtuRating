'use client';

import { useEffect, useState } from 'react';
import { FacultiesData } from "../../../../stores/FacultiesStore";
import SpecList from "@/components/specialitiesList/SpecialitesList";
import {observer} from "mobx-react";


const Page = observer(() => {
    const [facultyData, setFacultyData] = useState(null);

    const URL = window.location.href.split("/")
    const URL_ID = URL[URL.length - 1]

    useEffect(() => {
        const getData = async () => {
            console.log(URL_ID, FacultiesData.examPoints[0].points)
            const data = await FacultiesData.fetchFacultiesData(URL_ID, FacultiesData.examPoints)
            setFacultyData(data)
            console.log(facultyData)
        }
        getData()
    }, [URL_ID, FacultiesData.selectedFacultyId, FacultiesData.mainPageInfo]);

    return (
        <div className="mt-10">

            <div className="flex space-x-5 items-center">
                <div className={"text-[26px]"}>СПБГЭТУ "ЛЭТИ"</div>
                {facultyData && <h3 className={"text-[22px]"}>{facultyData.name}</h3>}
            </div>
            {facultyData && <SpecList specialitiesData={facultyData}/>}
        </div>
    );
})

export default Page;