import { makeAutoObservable } from "mobx";
import axios from "axios";

import {FacultiesDATA, SPECIALITIES} from "./dataStubs";

class FacultiesStore {
    selectedFacultyId = null;
    selectedSpeciality = null;
    selectedFacultyName = null;
    searchText = null;
    facultyData = null;
    specialitiesFilter = null;
    mainPageInfo = null;

    constructor() {
        makeAutoObservable(this);
    }

    async getMainPageInfo() {
        try {
            const response = await axios.get("http://25.17.147.15:8000/api/faculties");
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
        console.log(this.searchText)
        this.searchText = null;
    }

    async fetchFacultiesData(id) {
        this.facultyData = await FacultiesDATA;
        return this.facultyData;
    }

    changeFilter(filter) {
        this.specialitiesFilter = filter;
        console.log(this.specialitiesFilter)
    }

    async getSpecialityInfo(URL) {
        return await SPECIALITIES.find(spec => spec.URL === URL)
    }

}

export const FacultiesData = new FacultiesStore();