"use client"

import React from "react";
import Image from "next/image";

import FacultiesSVG from "../../../public/graduation-hat 1.svg"
import FacultiesList from "@/components/NavBar/FacultiesList";
import Search from "@/components/NavBar/Search";
import UwuLogo from "../../../public/UwuLogo.png"

const NavBar = React.memo(() => {
    return (
        <div>
            <Image
                src={UwuLogo}
                alt="university web utility"
                className="mb-6 mt-2"
            ></Image>
            <Search/>
            <div className="flex gap-x-4 mb-7 mt-8 align-middle">
                <Image src={FacultiesSVG} alt={"Факультеты"} className="mr-5"/>
                <h2 className="text-[24px] text-overall-purple">Факультеты</h2>
            </div>
            <div className="flex space-x-[59px]">
                <div className="w-[1px] h-auto bg-overall-grey"></div>
                <div className="flex-grow">
                    <FacultiesList/>
                </div>
            </div>
        </div>
    );
})

export default NavBar