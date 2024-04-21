"use client"

import React, { useState, useEffect } from 'react';
import { Dropdown } from 'rsuite';
import { DispciplinesExams, FacultiesData } from "../../../../stores/FacultiesStore";
import {observer} from "mobx-react";

const SingleDisciplineSection = observer(({id}) => {
    const [titleString, setTitleString] = useState("Предмет");
    const [examPoints, setExamPoints] = useState(null);

    const changePoints = (e) => {
        const newPoints = e.target.value;
        setExamPoints(newPoints);
        FacultiesData.changeExamPoints(id, newPoints);
    };

    return (
        <div className="mt-4">
            <Dropdown title={titleString} className="text-gray-800 bg-white p-2">
                {DispciplinesExams.map((exam, number) => (
                    <Dropdown.Item
                        key={number}
                        className="text-gray-600 ml-4 mt-[8px] cursor-pointer w-full h-8"
                        onClick={() => {
                            setTitleString(exam.russian);
                            FacultiesData.changeExamType(id, exam);
                        }}
                    >
                        {exam.russian}
                    </Dropdown.Item>
                ))}
            </Dropdown>
            <input
                type="text"
                value={examPoints || ""}
                className="pl-2 outline-none mt-2 w-full h-10"
                onChange={changePoints}
                placeholder={"Баллы"}
            />
        </div>
    )
})


export default SingleDisciplineSection;