"use client"

import Image from "next/image";
import FacultiesSVG from "../../../../public/graduation-hat 1.svg";
import FacultiesList from "@/components/NavBar/Faculties/FacultiesList";
import React from "react";

const FacultetsSection = () => {

    const [show, setShow] = React.useState(false);

    return (
        <>
            <div className="flex gap-x-4 mb-7 mt-8 align-middle">
                <Image src={FacultiesSVG} alt={"Факультеты"} className="mr-5"/>
                <h2 className="text-[24px] text-overall-purple"
                onClick={() => {setShow(!show)}}
                >Факультеты</h2>
            </div>
            {show && <div className="flex space-x-[59px]">
                <div className="w-[1px] h-auto bg-overall-grey"></div>
                <div className="flex-grow">
                    <FacultiesList/>
                </div>
            </div>}
        </>
    )
}

export default FacultetsSection;