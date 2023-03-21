import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser(userData, photoData) {
  try {
    const photo = await uploadPhoto(photoData);
    const user = await createUser(userData);
    return { photo, user };
  } catch (error) {
    console.error(error);
    return { photo: null, user: null };
  }
}
