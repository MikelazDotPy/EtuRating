"use client"

import React from "react";
import Image from "next/image";

import Search from "@/components/NavBar/Search";
import UwuLogo from "../../../public/UwuLogo.png"
import FacultetsSection from "@/components/NavBar/Faculties/FacultetsSection";
import CalculatorSection from "@/components/NavBar/Calculator/CalculatorSection";
import Link from "next/link";;
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faBagShopping} from "@fortawesome/free-solid-svg-icons";

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
            <div className="text-[22px] text-overall-purple mt-7">
                <FontAwesomeIcon icon={faBagShopping}></FontAwesomeIcon>
                <Link href={"/extra_study"} className={"ml-10"}>Доп образование</Link>
            </div>
        </div>
    );
})

export default NavBar