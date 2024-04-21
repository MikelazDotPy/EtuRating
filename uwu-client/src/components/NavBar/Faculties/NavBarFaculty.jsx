import React from "react";
import { observer } from "mobx-react";
import styled from "styled-components";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";

import { FacultiesData } from "../../../../stores/FacultiesStore";
import {faArrowRight} from "@fortawesome/free-solid-svg-icons/faArrowRight";
import Link from "next/link";

export const Faculty = observer(({ faculty }) => {
    const specialities = faculty.specialities || [];

    const handleFacultyClick = () => {
        if (FacultiesData.selectedFacultyId === faculty.id) {
            FacultiesData.changeActiveFaculty(null)
        } else {
            FacultiesData.changeActiveFaculty(faculty);
        }
    };

    const classList = FacultiesData.selectedFacultyId === faculty.id ? " text-overall-purple text-[16px]" : " text-[16px]";

    return (
        <div>
            <FacultyInList
                onClick={handleFacultyClick}
                className={classList + " space-x-3 text-gray-600"}
            >
                {/*<div>{faculty.title}</div>*/}
                <Link href={`/faculties/${faculty.id}`}> {/* поменять на id*/}
                    <div>{faculty.title}</div>
                </Link>
            </FacultyInList>
            {FacultiesData.selectedFacultyId === faculty.id && (
                <div className="flex flex-col">
                    {specialities.map(speciality => (
                        <SpecialityInList
                            href={`/faculties/specialities/${speciality.URL}`}
                            key={speciality.id}
                            className="ml-6 text-[14px]"
                        >
                            {speciality.title}
                        </SpecialityInList>
                    ))}
                </div>
            )}
        </div>
    );
});

const FacultyInList = styled.div`
    display: flex;
    margin-top: 12px;
`;

const SpecialityInList = styled.a`
    margin-top: 10px;

    //animation: fadein 1000ms ease-in-out forwards;

    @keyframes fadein {
        from { opacity: 0.7; }
        to   { opacity: 1; }
    }
`;