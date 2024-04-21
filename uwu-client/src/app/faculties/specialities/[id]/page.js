"use client"

import { FacultiesData } from "../../../../../stores/FacultiesStore";
import { useEffect, useState } from "react";
import SpecPage from "@/components/SpecPage/SpecPage";
import specPage from "@/components/SpecPage/SpecPage";
import {observer} from "mobx-react";

const SpecialityPage = observer(() => {
    const [SpecInfo, setSpecInfo] = useState(null);
    const [URL_PARAM, setURL_PARAM] = useState(null)

    useEffect(() => {
        const fetchData = async () => {
            const URL = window.location.href.split("/");
            setURL_PARAM(URL[URL.length - 1]);
            console.log(URL_PARAM)
            const result = await FacultiesData.getSpecialityInfo(URL_PARAM);
            // console.log(result)
            setSpecInfo(result);
            // console.log(SpecInfo);
        };
        fetchData();
    }, [URL_PARAM, URL]);


    if (!SpecInfo) {
        return <div>Loading...</div>;
    }

    return (
        <div className={"w-full"}>
            <SpecPage data={SpecInfo}/>
        </div>
    );
});

export default SpecialityPage;