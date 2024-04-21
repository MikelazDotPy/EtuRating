import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faCalculator} from "@fortawesome/free-solid-svg-icons";
import {useState} from "react";
import SingleDisciplineSection from "@/components/NavBar/Calculator/SingleDisciplineSection";
import {FacultiesData} from "../../../../stores/FacultiesStore";
import {observer} from "mobx-react";

const CalculatorSection = observer(({}) => {

    const [show, setShow] = useState(false);

    return (
        <>
            <div className="flex mt-3 space-x-10 align-middle">
                <FontAwesomeIcon icon={faCalculator} className="text-overall-purple text-[20px] ml-[5px] mt-2"/>
                <h2 className="text-[24px] text-overall-purple"
                    onClick={() => {
                        setShow(!show)
                    }}
                >Калькулятор</h2>
            </div>
            {show && <div className="ml-5 mt-5">
                <div className="text-[14px] text-gray-500">Данные для поступления</div>
                <SingleDisciplineSection id={1}/>
                <SingleDisciplineSection id={2}/>
                <SingleDisciplineSection id={3}/>
                <div
                    className="text-overall-purple cursor-pointer hover:text-purple-900 transition-[500ms] mt-7 text-[18px]"
                    onClick={() => FacultiesData.clearExamPoints()}
                >
                    Очистить список
                </div>
            </div>}
        </>
    )
})

export default CalculatorSection