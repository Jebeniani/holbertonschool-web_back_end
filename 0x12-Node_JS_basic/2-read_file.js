const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n');
    const headers = lines[0].split(',');

    if (
      headers[0] !== 'firstname'
      || headers[1] !== 'lastname'
      || headers[2] !== 'age'
      || headers[3] !== 'field'
    ) {
      throw new Error('Invalid CSV format');
    }

    const studentsByField = {
      CS: { count: 0, list: [] },
      SWE: { count: 0, list: [] },
    };

    for (let i = 1; i < lines.length; i += 1) {
      const fields = lines[i].split(',');

      if (fields.length === 4 && fields[0] !== '' && fields[1] !== '' && fields[2] !== '' && fields[3] !== '') {
        const field = fields[3];
        const name = fields[0];

        if (field === 'CS' || field === 'SWE') {
          studentsByField[field].count += 1;
          studentsByField[field].list.push(name);
        }
      }
    }

    console.log(`Number of students: ${studentsByField.CS.count + studentsByField.SWE.count}`);
    console.log(`Number of students in CS: ${studentsByField.CS.count}. List: ${studentsByField.CS.list.join(', ')}`);
    console.log(`Number of students in SWE: ${studentsByField.SWE.count}. List: ${studentsByField.SWE.list.join(', ')}`);
  } catch (err) {
    console.error(`Cannot load the database: ${err}`);
  }
}

module.exports = countStudents;
