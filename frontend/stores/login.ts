import {defineStore} from "pinia";
import {IUser} from "@/types";
const BASE_URL = 'http://localhost:8000/api/v1/';

export const useLoginStore = defineStore('login', {
	state: () => ({
		token: '',
		pendingUser: false,
	}),
	getters: {},
	actions: {
		async createUser(user: IUser) {
			console.log(user)
			this.pendingUser = true;
			try {
				const {pending, data} = await useLazyFetch(`${BASE_URL}auth/users/`, {
					method: 'POST',
					body: JSON.stringify({username: user.username, password: user.password})
				});
				if (pending) {
					console.log(data)
					this.pendingUser = true;
				}
			} catch (error) {
				console.log(error);
			}
		},
		async loginUser(user: IUser) {
			this.pendingUser = true;
			try {
				const {pending, data: token} = await useLazyFetch(`${BASE_URL}auth/token/login/`, {
					method: 'POST',
					body: JSON.stringify({username: user.username, password: user.password})
				});
				if (pending) {
					console.log(token.value)
				}
			} catch (e) {
				console.log(e)
			}
		}
	},
})
