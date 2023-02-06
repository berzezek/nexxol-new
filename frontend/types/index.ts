export interface ICategory {
  id: number;
  name: string;
  description: string;
  parent: number;
  image: string;
  date_created: string;
  date_updated: string;
}

export interface IProduct {
  id: number;
  name: string;
  description: string;
  price: number;
  category: number;
  date_created: string;
  date_updated: string;
  is_active: boolean;
}

export interface IImage {
  id: number;
  product: number;
  image: string;
  date_created: string;
  date_updated: string;
}
