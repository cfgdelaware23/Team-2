function apiLayer() {
  fetch("/getSchedule").then((res) =>
      res.json().then((data) => {
          console.log(data);
      })
  );
}

export default apiLayer;