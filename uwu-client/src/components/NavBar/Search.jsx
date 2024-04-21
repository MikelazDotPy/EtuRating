import { useRouter } from 'next/navigation';
import {observer} from "mobx-react";
import {FacultiesData} from "../../../stores/FacultiesStore";

const Search = observer(() => {
    const router = useRouter();

    const handleChange = (event) => {
        FacultiesData.changeSearchText(event.target.value);
    }

    const submitSearch = async (event) => {
        if (event.key === "Enter") {
            const res = await FacultiesData.getSearchData();
            console.log("res" + res);
            if (res) {
                await router.push(`/faculties/specialities/${res}`);
            }

        }
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
});

export default Search;