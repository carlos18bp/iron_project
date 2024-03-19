import Swal from "sweetalert2";
import { useUserStore } from "@/stores/user";

/**
 * Show a success message for create or edit request.
 * @param {object} formData - form data to create or edit a record.
 * @param {string} text_response - text success message.
 * @param {string} redirectUrl - Redirect endpoint.
 */
export async function submitHandler(formData, text_response) {
  const userStore = useUserStore();

  await userStore.createRequest(formData);

  if (userStore.getRequestStatus === 200) {
    const swal = Swal.mixin({
      customClass: {
        confirmButton: "btn bg-gray_p hover:bg-black p-4 font-regular text-white",
      },
      buttonsStyling: false
    });

    swal.fire({
      icon: "success",
      title: "Success",
      text: text_response,
      confirmButtonText: 'OK!'
    }).then((result) => {
      if (result.isConfirmed) {
        return true;
      }
    });
  } else {
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "Algo salió mal!",
      footer: "<a>Vuelve a intentar o intenta más tarde.</a>",
    });
    return false;
  }
}