const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/') res.end('Hello Holberton School!');

  if (req.url === '/students') {
    try {
      const data = await countStudents(process.argv[2]);
      res.statusCode = 200;
      res.write('This is the list of our students\n');
      res.write(`Number of students: ${data.numberOfStudents}\n`);
      for (const [field, students] of Object.entries(data.studentByField)) {
        if (field !== 'undefined') {
          res.write(`Number of students in ${field}: ${students.count}. List: ${students.list.join(', ')}\n`);
        }
      }
      res.end();
    } catch (error) {
      res.statusCode = 404;
      res.end(error.message);
    }
  }
});
app.listen(1245);
module.exports = app;
