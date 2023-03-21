import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promises = [
    signUpUser(firstName, lastName).then((value) => ({ status: 'resolved', value })).catch((error) => ({ status: 'rejected', value: error })),
    uploadPhoto(fileName).then((value) => ({ status: 'resolved', value })).catch((error) => ({ status: 'rejected', value: error })),
  ];

  return Promise.all(promises);
}
