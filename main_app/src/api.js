function apiLayer(data) {
  console.log(data);
  // const formattedData = data.map((d) => {
  //   return {

  //   }
  // })
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  };
  fetch("/getSchedule", requestOptions).then((res) =>
      res.json().then((d) => {
          console.log(d);
      })
  );
}

export default apiLayer;