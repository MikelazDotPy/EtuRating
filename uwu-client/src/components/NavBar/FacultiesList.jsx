import React, { useState } from 'react';
import {Faculty} from "@/components/NavBar/NavBarFaculty";

const stub = [
    {id: 1, title: "ФКТИ", specialities: [{id: 3344, title: 'Программная инженерия', URL: "programming_engineering"}, {id: 3381, title: "Приматы", URL: "pmi"}]},
    {id: 2, title: "ФИБС", specialities: [{id: 1234, title: "Говнари"}]},
    {id: 3, title: "ФЭА"},
];

const FacultiesList = React.memo(() => {
    return (
        <>
            {stub.map(faculty => (
                <Faculty
                    key={faculty.id}
                    faculty={faculty}
                />
            ))}
        </>
    );
});

export default FacultiesList;