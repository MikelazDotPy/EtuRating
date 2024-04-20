"use client"

import {FacultiesData} from "../../stores/FacultiesStore";
import {observer} from "mobx-react";

const Home = observer(() => {
    const selectedFaculty = FacultiesData.selectedFacultyName
    let title = "Пожалуйста, выберите факультет"

    if (selectedFaculty) {
        title = `Страница факультета ${selectedFaculty}`
    }

    return (
        <div>
            {title}
        </div>
    );
})

export default Home
