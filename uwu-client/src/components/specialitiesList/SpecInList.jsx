import Labels from "@/components/specialitiesList/labels";
import Link from "next/link";
import {observer} from "mobx-react";

const SpecInList = observer(({name, department, id, type, faculty, plan_id}) => {
    return (
        <div className="px-6 py-4 bg-white">
            <div className="text-[20px]">{name}</div>
            <Labels labelsList={...[department, type, faculty]}/>
            <div className="flex space-x-7">
                <div className="inline-block mt-7 text-[14px] py-[6px] px-3 bg-overall-purple rounded-xl text-white">
                    <Link href={`specialities/${plan_id}`}>Узнать подробнее</Link>
                </div>
                <div className={"inline-block mt-7 text-[16px] py-[6px] px-3 rounded-xl text-overall-purple border"}>
                    <Link href={`vacancy?id=${plan_id}`}>Работа</Link>
                </div>
            </div>
        </div>
    )
})

export default SpecInList