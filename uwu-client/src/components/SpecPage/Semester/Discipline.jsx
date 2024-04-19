const Discipline = ({discipline}) => {
    return (
        <div className="flex justify-between items-center w-full">
            <div>{discipline.title}</div>
            <div className={"flex"}>
                <div className="ml-10">Зачетных единиц: {discipline.creditUnit}</div>
                <div className="ml-10">Часов: {discipline.hours}</div>
            </div>
        </div>
    )
}

export default Discipline