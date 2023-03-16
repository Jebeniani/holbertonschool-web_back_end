export default function createReportObject(employeesList) {
  return {
    allEmployees: {
      ...employeesList,
    },
    GetNumberOfDepartments(employeesList) {
      return Object.keys(employeesList).length;
    },
  };
}
