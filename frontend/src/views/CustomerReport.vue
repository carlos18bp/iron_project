<template>
  <Header></Header>
  <section class="overflow-x-auto mt-16 p-4">
    <table class="w-full text-sm text-left rtl:text-right text-gray-400 overflow-hidden rounded-lg">
        <thead class="text-xs uppercase bg-gray-700 text-gray-400">
            <tr class="rounded-lg">
                <th scope="col" class="px-6 py-3">
                    #
                </th>
                <th scope="col" class="px-6 py-3">
                    User full name
                </th>
                <th scope="col" class="px-6 py-3">
                    Email
                </th>
                <th scope="col" class="px-6 py-3">
                    contact
                </th>
                <th scope="col" class="px-6 py-3">
                    Subject
                </th>
                <th scope="col" class="px-6 py-3">
                    Description
                </th>
                <th scope="col" class="px-6 py-3">
                    Projects of interest
                </th>
                <th scope="col" class="px-6 py-3">
                    Profession(s)
                </th>
                <th scope="col" class="px-6 py-3">
                    Where hear about us
                </th>
            </tr>
        </thead>
        <tbody>
            <tr 
                v-for="(user, index) in users" :key="user.id"
                class="border-b bg-gray-800 border-gray-700 hover:bg-gray-600">
                <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap text-white">
                    {{ index + 1 }}
                </th>
                <td class="px-6 py-4">
                    {{ user.firstName + ' ' + user.lastName }}
                </td>
                <td class="px-6 py-4">
                    {{ user.email }}
                </td>
                <td class="px-6 py-4">
                    {{ user.contact }}
                </td>
                <td class="px-6 py-4">
                    {{ user.subject }}
                </td>
                <td class="px-6 py-4">
                    {{ user.description }}
                </td>
                <td class="py-4">
                    <ul>
                        <li v-for="project in user.projects" :key="project">
                            - {{ project }}
                        </li>
                    </ul>
                </td>
                <td class="py-4">
                    <ul>
                        <li v-for="profession in user.professions" :key="profession">
                            - {{ profession }}
                        </li>
                    </ul>
                </td>
                <td class="px-6 py-4">
                    {{ user.hear_about_us }}
                </td>
            </tr>
        </tbody>
    </table>
  </section>
  <Footer></Footer>
</template>

<script setup>
  import { onMounted, ref } from 'vue';
  import { initFlowbite } from 'flowbite';
  import { useUserStore } from '@/stores/user';
  import Header from "@/components/layouts/Header.vue";
  import Footer from "@/components/layouts/Footer.vue";

  const userStore = useUserStore();
  const users = ref([]);

  onMounted(async () => {
    initFlowbite();
    await userStore.init();
    users.value = userStore.users;
  });
</script>