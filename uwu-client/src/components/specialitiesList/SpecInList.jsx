import Labels from "@/components/specialitiesList/labels";
import Link from "next/link";
import {observer} from "mobx-react";

const SpecInList = observer(({name, department, id, type, faculty, plan_id}) => {
    return (
        <div className="px-6 py-4 bg-white">
            <div className="text-[20px]">{name}</div>
            <Labels labelsList={...[department, type, faculty]}/>
            <div className="inline-block mt-5 text-[14px] py-[6px] px-3 bg-overall-purple rounded-xl text-white">
                <Link href={`specialities/${plan_id}`}>Узнать подробнее</Link>
            </div>
        </div>
    )
})

export default SpecInList