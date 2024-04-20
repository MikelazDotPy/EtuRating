import {useState} from "react";
import Link from 'next/link'

const Discipline = ({discipline, isShown}) => {

    const [showDescription, setShowDescription] = useState(false);

    return (
        <>
            {isShown &&
            <div className="flex justify-between items-center w-full mt-4">
                <div
                    onClick={() => {setShowDescription(!showDescription)}}
                >{discipline.title}</div>
                <div className={"flex"}>
                    <div className="ml-10">Зачетных единиц: {discipline.creditUnit}</div>
                    <div className="ml-10">Часов: {discipline.hours}</div>
                </div>
            </div>}
            {showDescription && isShown &&
                <div className="mt-3 ml-5 flex flex-col space-y-2">
                    <div>{discipline.description}</div>
                    <Link href={`/abstract/${discipline.title}`} className="text-overall-purple">Смотреть конспекты</Link>
                </div>
            }
        </>
    )
}

export default Discipline