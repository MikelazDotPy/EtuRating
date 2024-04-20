import Labels from "@/components/specialitiesList/labels";
import Link from "next/link";

const SpecInList = ({name, department, id, type, faculty}) => {
    return (
        <div className="px-6 py-4 bg-white">
            <div className="text-[20px]">{name}</div>
            <Labels labelsList={...[department, type, faculty]}/>
            <div className="inline-block mt-5 text-[14px] py-[6px] px-3 bg-overall-purple rounded-xl text-white">
                <Link href={`specialities/${id}`}>Узнать подробнее</Link>
            </div>
        </div>
    )
}

export default SpecInList