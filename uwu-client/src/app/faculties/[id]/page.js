'use client';

import { useEffect, useState } from 'react';
import { FacultiesData } from "../../../../stores/FacultiesStore";
import SpecList from "@/components/specialitiesList/SpecialitesList";

const Page = () => {
    const [url, setUrl] = useState('');
    const [facultyData, setFacultyData] = useState(null);

    useEffect(() => {
        setUrl(window.location.href);
        const FacultyType = url[url.length - 1];
        FacultiesData.fetchFacultiesData(FacultyType)
            .then(data => {
                setFacultyData(data)
                console.log(data.specialities)
            });
    }, [url]);

    return (
        <div className="mt-10">
            <div className="flex space-x-5 items-center">
                <div className={"text-[26px]"}>СПБГЭТУ "ЛЭТИ"</div>
                {facultyData && <h3 className={"text-[22px]"}>{facultyData.facultyTitle}</h3>}
            </div>
            {facultyData && <SpecList specialitiesData={facultyData.specialities}/>}
        </div>
    );
}

export default Page;