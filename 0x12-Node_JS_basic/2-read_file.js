const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n');
    const headers = lines[0].split(',');

    if (headers[0] !== 'firstname' || headers[1] !== 'lastname' || headers[2] !== 'age' || headers[3] !== 'field') {
      throw new Error('Invalid CSV format');
    }

    const studentsByField = {};

    // eslint-disable-next-line no-plusplus
    for (let i = 1; i < lines.length; i++) {
      const fields = lines[i].split(',');

      if (fields.length === 4 && fields[0] !== '' && fields[1] !== '' && fields[2] !== '' && fields[3] !== '') {
        const field = fields[3];

        if (!studentsByField[field]) {
          studentsByField[field] = {
            count: 1,
            list: [fields[0]],
          };
        } else {
          // eslint-disable-next-line indent, no-plusplus
                    studentsByField[field].count++;
          studentsByField[field].list.push(fields[0]);
        }
      }
    }

    let totalCount = 0;

    // eslint-disable-next-line guard-for-in
    for (const field in studentsByField) {
      const { count } = studentsByField[field];
      const { list } = studentsByField[field];

      console.log(`Number of students in ${field}: ${count}. List: ${list.join(', ')}`);
      totalCount += count;
      // eslint-disable-next-line indent
            // eslint-disable-next-line indent
        }

    console.log(`Number of students: ${totalCount}`);
  } catch (err) {
    console.error(`Cannot load the database: ${err}`);
  }
}

module.exports = countStudents;
