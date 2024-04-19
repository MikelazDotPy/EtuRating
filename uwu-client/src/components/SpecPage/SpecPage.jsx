import Labels from "@/components/specialitiesList/labels";
import SemestersList from "@/components/SpecPage/Semester/SemestersList";

const SpecPage = ({data}) => {
    return (
        <div className="mt-6">
            <h1 className={"text-dark-grey text-[36px]"}>СПБГЭТУ "ЛЭТИ"</h1>
            <h2 className="mt-[18px] text-[26px]">{data.title}</h2>
            <div className="mt-[-12px]">
                <Labels labelsList={[data.title, data.department, data.faculty]}/>
            </div>
            <SemestersList URL={data.URL}/>
        </div>
    )
}

export default SpecPage