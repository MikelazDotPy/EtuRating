import {useState} from "react";

const Discipline = ({data}) => {

    const [show, setShow] = useState(false);

    return (
        <>
            <div className="flex justify-between items-center ml-5">
                <h5 className={"text-gray-700 mt-1 text-[14] max-w-[800px]"}
                    onClick={() => {
                        setShow(!show)
                    }}
                >○ {data.title}</h5>
                <div className={"flex w-[300px] justify-between"}>
                    <div className={"text-gray-600"}>Зачетных единиц: {data.ze}</div>
                    <div className={""}>Часов: {data.hours}</div>
                </div>
            </div>
            <div className={"w-[750px] ml-[50px]"}>
                {show && data.destiption !== "None" && <div className={"text-gray-500 mt-1 mb-2"} onClick={() => {setShow(false)}}>{data.desctiption}</div>}
            </div>
        </>
    )
}

export default Discipline