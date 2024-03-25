import { defineStore } from "pinia";
import { create_request, get_request } from "./services/request_http";

export const useUserStore = defineStore("user", {
  state: () => ({
    users: [],
    areUpdateUsers: false,
    requestStatus: "",
  }),
  getters: {
    /**
     *
     * @param {object} state - State.
     * @returns {number} - status request.
     */
    getRequestStatus: (state) => {
      return state.requestStatus;
    },
    /**
     * Get user by id.
     * @param {object} state - State.
     * @returns {array} - user by id occurrence.
     */
    userById: (state) => (userId) => {
      return state.users.find((user) => user.id === userId);
    },
  },
  actions: {
    /**
     * Fetch data from backend.
     */
    async init() {
      if (!this.areUpdateUsers) this.fetchUsersData();
    },
    /**
     * Fetch users from backend.
     */
    async fetchUsersData() {
      if (this.areUpdateusers) return;

      let response = await get_request("users/");
      let jsonData = response.data;

      if (jsonData && typeof jsonData === "string") {
        try {
          jsonData = JSON.parse(jsonData);
        } catch (error) {
          console.error(error.message);
          jsonData = [];
        }
      }

      this.users = jsonData ?? [];
      console.log("Source: users, count: " + this.users.length);
      console.log(this.users);

      this.areUpdateusers = true;
    },
    /**
     * Call creation userrequest.
     * @param {object} formData - Form data.
     */
    async createRequest(formData) {
      let response = await create_request(
        "/create_user/",
        JSON.stringify(formData)
      );

      this.requestStatus = response.status;
      this.areUpdateUsers = false;
      this.fetchUsersData();
    },
  },
});
