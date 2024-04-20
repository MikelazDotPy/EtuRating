"use client"

import React, { useState, useEffect } from 'react';
import { Dropdown } from 'rsuite';
import { DispciplinesExams, FacultiesData } from "../../../../stores/FacultiesStore";

const SingleDisciplineSection = ({ id }) => {
    const [titleString, setTitleString] = useState("Предмет");
    const [examPoints, setExamPoints] = useState(null);

    const changePoints = (e) => {
        setExamPoints(e.target.value)
        FacultiesData.changeExamType(id, titleString);
    };

    return (
        <div className="mt-4">
            <Dropdown title={titleString} className="text-gray-800 bg-white p-2">
                {DispciplinesExams.map(exam => (
                    <Dropdown.Item
                        key={exam}
                        className="text-gray-600 ml-4 mt-[6px] cursor-pointer"
                        onClick={() => {
                            setTitleString(exam);
                            console.log(exam)
                            console.log(examPoints)
                            FacultiesData.changeExamType(id, exam);
                        }}
                    >
                        {exam}
                    </Dropdown.Item>
                ))}
            </Dropdown>
            <input
                type="text"
                value={examPoints}
                className="outline-none mt-2"
                onChange={changePoints}
                placeholder={"Баллы"}
            />
        </div>
    );
};

export default SingleDisciplineSection;