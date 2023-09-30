function apiLayer() {
  const sampleData = [
    {
      "name": "Jane Doe",
      "monAvailability": "4pm-6pm",
      "tuesAvailability": "4pm-6pm",
      "wedAvailability": "4pm-6pm",
      "thuAvailability": "4pm-6pm",
      "friAvailability": "4pm-6pm",
    }
  ];
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(sampleData)
  };
  fetch("/getSchedule", requestOptions).then((res) =>
      res.json().then((data) => {
          console.log(data);
      })
  );
}

export default apiLayer;