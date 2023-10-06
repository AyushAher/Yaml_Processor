import { createSlice } from "@reduxjs/toolkit";


export interface UserState {
    token: string | null
}

var userState: UserState = {
    token: null
}


const AppStateSlice = createSlice({
    name: "UserState",
    initialState: userState,
    reducers: {
        setToken: (state: UserState, payload) => {
            state.token = payload.payload
        }
    }
});

export const {
    setToken
} = AppStateSlice.actions;

export default AppStateSlice.reducer;