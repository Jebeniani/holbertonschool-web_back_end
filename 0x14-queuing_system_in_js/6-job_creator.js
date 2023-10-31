const kue = require('kue');
const queue = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a notification message.',
};

const job = queue.create('push_notification_code', jobData);

job.on('enqueue', () => {
  console.log('Notification job created:', job.id);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

job.save((err) => {
  if (!err) {
  } else {
    console.error('Error creating the job:', err);
  }
});
