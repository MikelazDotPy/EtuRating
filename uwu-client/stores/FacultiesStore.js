import { makeAutoObservable } from "mobx";

import {FacultiesDATA, SPECIALITIES} from "./dataStubs";


class FacultiesStore {
    selectedFacultyId = null;
    selectedSpeciality = null;
    selectedFacultyName = null;
    searchText = null;
    facultyData = null;
    specialitiesFilter = null;

    constructor() {
        makeAutoObservable(this);
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