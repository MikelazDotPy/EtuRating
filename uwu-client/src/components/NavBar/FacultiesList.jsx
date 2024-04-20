import React, { useEffect, useState } from 'react';
import { Faculty } from "@/components/NavBar/NavBarFaculty";
import { FacultiesData } from "../../../stores/FacultiesStore";

const FacultiesList = React.memo(() => {
    const [navBarData, setNavBarData] = useState(null);

    useEffect(() => {
        const getData = async () => {
            const data = await FacultiesData.getMainPageInfo();
            setNavBarData(data);
        }
        getData();
    }, []);

    return (
        <>
            {navBarData && navBarData.map(faculty => (
                <Faculty
                    key={faculty.id}
                    faculty={faculty}
                />
            ))}
        </>
    );
});

export default FacultiesList;