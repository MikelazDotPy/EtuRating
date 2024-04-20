import Filter from "@/components/specialitiesList/Filter";
import SpecInList from "@/components/specialitiesList/SpecInList";
import {FacultiesData} from "../../../stores/FacultiesStore";
import {observer} from "mobx-react";

const SpecList = observer(({ specialitiesData }) => {
    return (
        <>
        <Filter/>
        <div className="space-y-10 mt-8">
            {/*{specialitiesData.map((spec, index) => {*/}
            {/*    if (FacultiesData.specialitiesFilter !== null && spec.type === FacultiesData.specialitiesFilter) {*/}
            {/*        return <SpecInList {...specialitiesData[index]}/>*/}
            {/*    }*/}
            {/*    if (FacultiesData.specialitiesFilter === null) {*/}
            {/*        return <SpecInList {...specialitiesData[index]}/>*/}
            {/*    }*/}
            {/*})}*/}
        </div>
    </>)
})

export default SpecList