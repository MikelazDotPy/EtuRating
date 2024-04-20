"use client"

import { FacultiesData } from "../../../../../stores/FacultiesStore";
import { useEffect, useState } from "react";
import SpecPage from "@/components/SpecPage/SpecPage";

const SpecialityPage = () => {
    const [SpecInfo, setSpecInfo] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            const URL = window.location.href.split("/");
            const result = await FacultiesData.getSpecialityInfo(URL[URL.length - 1]);
            setSpecInfo(result);
        };
        fetchData();
    }, []);

    if (!SpecInfo) {
        return <div>Loading...</div>;
    }

    return (
        <div className={"w-full"}>
            <SpecPage data={SpecInfo}/>
        </div>
    );
};

export default SpecialityPage;