"use client"

import Discipline from "@/components/SpecPage/Semester/Discipline";
import {useState} from "react";

const SingleSemester = ({data}) => {

    const [Shown, setShown] = useState(false);

    return (
        <div>
            <h4 className={"text-[20px] mt-5 cursor-pointer"}
                onClick={() => {
                    setShown(!Shown)
                }}
            >{data.disciplines.length > 0 && "•" + data.title}</h4>
            {data.disciplines.length > 0 && <div className={"w-auto h-[1px] bg-black"}></div>}
            <div>{Shown && data.disciplines.map((desciplineInfo) => {
                return desciplineInfo && <Discipline data={desciplineInfo}/>
            })}
            </div>
            {Shown &&
                <div>
                    <h4 className="text-[18px] ml-5 mt-4">
                        Дифф-зачеты
                    </h4>
                    {data.div_zaceths.map(obj => {
                        return <div className="mt-2 ml-10">{obj}</div>
                    })}
                    <h4 className="text-[18px] ml-5 mt-4">
                        Зачеты
                    </h4>
                    {data.zaceths.map(obj => {
                        return <div className="mt-2 ml-10">{obj}</div>
                    })}
                    <h4 className="text-[18px] ml-5 mt-4">
                        Экзамены
                    </h4>
                    {data.exams.map(obj => {
                        return <div className="mt-2 ml-10">{obj}</div>
                    })}
                    <h4 className="mt-4 ml-5 text-[20px]">{data.kursah ? `Курсовая работа по: ${data.kursah}` : "Нет курсовой"}</h4>
                </div>}
        </div>
    )
}

export default SingleSemester