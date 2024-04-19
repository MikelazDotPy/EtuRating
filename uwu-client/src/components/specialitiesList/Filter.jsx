import { FacultiesData } from "../../../stores/FacultiesStore";
import { observer } from "mobx-react";

const Filter = observer(() => {
    const filters = ["Магистратура", "Бакалавриат", "Специалитет"];
    const inActiveClass = "cursor-pointer text-[20px] text-overall-gray";
    const activeClass = "cursor-pointer text-[20px] text-overall-purple";

    const isActive = (filter) => {
        return FacultiesData.specialitiesFilter === filter;
    }

    return (
        <div className="mt-8 flex space-x-9">
            {filters.map((filter, index) => (
                <div
                    key={index}
                    className={`${isActive(filter) ? activeClass : inActiveClass} text-[20px]`}
                    onClick={() => FacultiesData.changeFilter(filter)}
                >
                    {filter}
                </div>
            ))}
        </div>
    );
});

export default Filter;