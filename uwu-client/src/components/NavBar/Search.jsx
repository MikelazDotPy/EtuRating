import {FacultiesData} from "../../../stores/FacultiesStore";
import {observer} from "mobx-react";

const Search = observer(() => {

    const handleChange = (event) => {
        FacultiesData.changeSearchText(event.target.value);
    }

    const submitSearch = (event) => {
        if (event.key === "Enter")
        FacultiesData.getSearchData()
    }

    return (
        <>
            <input type='text'
                   placeholder='Найти специальность'
                   className='w-[230px] h-9 py-2 px-4 border-none bg-white rounded-lg outline-none text-gray-500'
                   onChange={handleChange}
                   value={FacultiesData.searchText || ''}
                   onKeyPress={submitSearch}
            />
        </>
    )
})

export default Search