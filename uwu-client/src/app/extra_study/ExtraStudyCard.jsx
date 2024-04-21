import {useState} from "react";
import Image from "next/image";
import Link from "next/link";

const ExtraStudyCard = ({data}) => {

    console.log(data)

    return (
        <div className="bg-white px-8 py-9 w-[1200px] mt-[50px]">
            <div className={"flex justify-between items-top"}>
                <h5 className={"text-[18px] w-[750px]"}>{data && data.title}</h5>
                <div className="price">
                    <p className={"text-[20px]"}>{data && data.cost} руб</p>
                    <p>цена</p>
                </div>
                <div className="price">
                    <p className={"text-[18px]"}>{data && data.duration || "Нет информации"}</p>
                    <p>Продолжительность</p>
                </div>
            </div>
            <div className={"flex justify-between mt-3 mb-7"}>
                <div>
                    <h3 className={"text-[24px] text-[#3B434E]"}>Об обучении</h3>
                    <div className={"flex w-[500px] justify-between mt-4"}>
                        <div>Дата начала обучения</div>
                        <div>{data && data.starts}</div>
                    </div>
                    <div className={"flex w-[500px] justify-between text-[16px] mt-2"}>
                        <div>Форма обучения</div>
                        <div>{data && data.edu_form}</div>
                    </div>
                    <div className={"flex w-[500px] justify-between text-[16px] mt-2"}>
                        <div>Длительность обучения</div>
                        <div>{data && data.long || "Нет информации"}</div>
                    </div>
                    <div className={"flex w-[500px] justify-between text-[16px] mt-2"}>
                        <div>Тип обучения</div>
                        <div>{data && data.type || "Нет информации"}</div>
                    </div>
                </div>
                <div className={"w-[2px] bg-black h-auto"}></div>
                <div>
                    <h3 className={"text-[24px] text-[#3B434E]"}>Об организации</h3>
                    <div className={"flex w-[500px] justify-between mt-4"}>
                        <div className="pr-5">Название</div>
                        <div className={"items-right"}>{data && data.org_name}</div>
                    </div>
                    <div className={"flex w-[500px] justify-between text-[16px] mt-2"}>
                        <div>Адрес</div>
                        <div>{data && data.org_address}</div>
                    </div>
                    <div className={"flex w-[500px] justify-between text-[16px] mt-2"}>
                        <div>Номер Телефона</div>
                        <div>{data && data.phone || "Нет информации"}</div>
                    </div>
                    <div className={"flex w-[500px] justify-between text-[16px] mt-2"}>
                        <div>Почта</div>
                        <div>{data && data.email || "Нет информации"}</div>
                    </div>
                </div>
            </div>
            <Link href={`${data && data.site || "#"}`}
            className={"mt-5 text-overall-purple"}
            >Узнать больше</Link>
        </div>
    )
}

export default ExtraStudyCard