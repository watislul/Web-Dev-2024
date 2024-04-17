
import { Company } from "./company";
import {NumberFormatStyle} from "@angular/common";

export interface Vacancy {
    id: number;
    name: string;
    description: string;
    salary : number

    formated_salary : String;
    company: Company;
  }
