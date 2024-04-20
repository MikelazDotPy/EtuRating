import { makeAutoObservable } from "mobx";
import axios from "axios";

import {FacultiesDATA, SPECIALITIES} from "./dataStubs";
import {faCalculator} from "@fortawesome/free-solid-svg-icons";
const qs= require("qs")

const URL = "http://localhost:8000/api/faculties";

// Создаем соответствие между русскими и английскими названиями предметов

// Функция для получения английского названия предмета

// Используем функцию для получения английского названия предмета

class FacultiesStore {
    selectedFacultyId = null;
    selectedSpeciality = null;
    selectedFacultyName = null;
    searchText = null;
    facultyData = null;
    specialitiesFilter = null;
    mainPageInfo = null;
    examPoints = [{type: null, points: null}, {type: null, points: null}, {type: null, points: null}]

    constructor() {
        makeAutoObservable(this);
        // this.loadStateFromStorage();
    }

    async getMainPageInfo() {
        try {
            const response = await axios.get(URL);
            this.mainPageInfo = response.data;
            return this.mainPageInfo;
        } catch (error) {
            if (error.response) {
                console.error('Ошибка при получении данных: ', error.response.data);
                console.error('Статус ошибки: ', error.response.status);
            } else if (error.request) {
                console.error('Ошибка сети: ', error.request);
            } else {
                console.error('Ошибка при настройке запроса: ', error.message);
            }
            throw error;
        }
    }

    changeActiveFaculty(faculty) {
        if (faculty !== null) {
            this.selectedFacultyId = faculty.id;
            this.selectedFacultyName = faculty.title;
        } else {
            this.selectedFacultyId = null;
            this.selectedFacultyName = null;
        }
    }

    changeActiveSpeciality(speciality) {
        this.selectedSpeciality = speciality.id;
    }

    changeSearchText(text) {
        this.searchText = text
    }

    getSearchData(){
        this.searchText = null;
    }

    async fetchFacultiesData(id, body) {
        if (body) {
            try {
                const res = await axios.post(URL + `/${id}`, body)
                this.facultyData = res.data;
                console.log(res)
                return this.facultyData;
            } catch (error) {
                console.error('Ошибка при отправке данных: ', error);
                throw error;
            }
        }
        const res = await axios.get(URL + `/${id}`)
        this.facultyData = res.data;
        return this.facultyData;
    }


    changeFilter(filter) {
        this.specialitiesFilter = filter;
    }

    async getSpecialityInfo(URL) {
        return await SPECIALITIES.find(spec => spec.URL === URL)
    }

    changeExamPoints = (id, amount) => {
        this.examPoints[id-1].points = amount
    }

    changeExamType = (id, type) => {
        this.examPoints[id-1].type = type.not_russian
    }

    getEnglishName(russianName) {
        const discipline = DispciplinesExams.find(d => d.russian === russianName);
        return discipline ? discipline.not_russian : null;
    }

}

export const FacultiesData = new FacultiesStore();


export const DispciplinesExams = [
    {russian: "Русский язык", not_russian: "russian"},
    {russian: "Математика", not_russian: "maths"},
    {russian: "Литература", not_russian: "literatura"},
    {russian: "География", not_russian: "geography"},
    {russian: "Информатика", not_russian: "informatics"},
    {russian: "Физика", not_russian: "physics"},
    {russian: "История", not_russian: "history"},
    {russian: "Биология", not_russian: "biology"},
    {russian: "Химия", not_russian: "breaking_bad"},
    {russian: "Обществознание", not_russian: "society"},
    {russian: "Иностранный язык", not_russian: "english"},
]