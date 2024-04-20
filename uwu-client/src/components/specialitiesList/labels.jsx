const Labels = ({labelsList}) => {

    return (
        <div className="mt-5 space-x-3">
            {labelsList.length > 0 && labelsList.map((label, index) => {
                return <span
                    key={index}
                    className="text-gray-700 px-2 text-[12px]
                    py-[3px] border-solid border-2 border-overall-grey rounded-[50px]">
                    {label}
                </span>
            })}
        </div>
    )
}

export default Labels;