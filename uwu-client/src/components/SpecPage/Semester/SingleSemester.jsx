import Discipline from "@/components/SpecPage/Semester/Discipline";

const SingleSemester = ({data}) => {

    console.log(data)

    return (
        <div className="w-full">
            {data.title}
            {data.disciplines.map(discipline => {
                return <Discipline discipline={discipline} />
            })}
        </div>
    )
}

export default SingleSemester