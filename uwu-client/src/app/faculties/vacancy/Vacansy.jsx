import { useState } from "react";

const Vacancy = ({ skills }) => {
    const [vacancyShown, setVacancyShown] = useState(null);

    const toggleVacancy = (index) => {
        setVacancyShown(vacancyShown === index ? null : index);
    };

    return (
        <div>
            <h4 className="text-[20px] mt-3">{skills.title}</h4>
            <div className="ml-4 mt-3 text-gray-700">Вакансии в этой профессии:</div>
            {skills.vacansions && skills.vacansions.map((vacancy, index) => {
                return (
                    <div key={index} onClick={() => toggleVacancy(index)}>
                        <h6 className="ml-8 mt-4 text-gray-800">{vacancy.name}</h6>
                        {vacancyShown === index && (
                            <>
                                <div className="mt-2 ml-12 text-gray-700">
                                    Необходимый опыт работы: {vacancy.exp}
                                </div>
                                <div className="mt-2 ml-12 text-gray-700">Необходимый скиллы:</div>
                                {vacancy.skills && vacancy.skills.map((skill, skillIndex) => {
                                    return (
                                        <div key={skillIndex} className="mt-3 ml-16">
                                            <span className="text-overall-purple">{skill}</span>
                                        </div>
                                    );
                                })}
                            </>
                        )}
                    </div>
                );
            })}
        </div>
    );
};

export default Vacancy;