<template>
	<MainLogin @loginUser="loginUser" />
</template>

<script setup>
import { useLoginStore } from "@/stores/login";

const loginStore = useLoginStore();
const loginUser = (user) => {
	loginStore.loginUser(user)
};
</script>

<style scoped></style>
