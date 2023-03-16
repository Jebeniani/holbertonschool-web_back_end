export default function createIteratorObject(report) {
  return Object.values(report.allEmployees).join().split(',');
}
