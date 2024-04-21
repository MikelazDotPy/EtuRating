import Labels from "@/components/specialitiesList/labels";
import SemestersList from "@/components/SpecPage/Semester/SemestersList";

const SpecPage = ({data}) => {

    return (
        <div className="mt-6">
            <h1 className={"text-dark-grey text-[36px]"}>СПБГЭТУ "ЛЭТИ"</h1>
            <h2 className="mt-[0px] text-[26px]">{data[0].name}</h2>
            <div className="mt-[14px]">
                    <Labels labelsList={[data[0].departament, data[0].faculty, data[0].study_form]}/>
            </div>
            <SemestersList data={data.slice(1, 10)}/>
        </div>
    )
}

export default SpecPage