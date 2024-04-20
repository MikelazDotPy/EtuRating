"use client"

import React from "react";
import Image from "next/image";

import Search from "@/components/NavBar/Search";
import UwuLogo from "../../../public/UwuLogo.png"
import FacultetsSection from "@/components/NavBar/Faculties/FacultetsSection";
import CalculatorSection from "@/components/NavBar/Calculator/CalculatorSection";

const NavBar = React.memo(() => {
    return (
        <div>
            <Image
                src={UwuLogo}
                alt="university web utility"
                className="mb-6 mt-2"
            ></Image>
            <Search/>
            <FacultetsSection/>
            <CalculatorSection/>
        </div>
    );
})

export default NavBar