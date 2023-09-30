function apiLayer(volunteerAvailability, eventSchedule) {
  const formattedVolunteerData = volunteerAvailability.map((d) => {
    return (
      {
        "name": d.Name,
        "details": {
          "skills": d.Roles?.split(", "),
          "monday": convertTimes(d.Monday),
          "tuesday": convertTimes(d.Tuesday),
          "wednesday": convertTimes(d.Wednesday),
          "thursday": convertTimes(d.Thursday),
          "friday": convertTimes(d.Friday),
          "saturday": convertTimes(d.Saturday),
          "sunday": convertTimes(d.Sunday)
        }
      }
    );
  });
  console.log(eventSchedule);
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(formattedVolunteerData)
  };
  fetch("/getSchedule", requestOptions).then((res) =>
      res.json().then((d) => {
          console.log(d);
      })
  );
}

function convertTimes(times) {
  if (times === "None")
    return [];
  else if (times === "all day")
    return Array.from(Array(24).keys());
  else {
    const allTimes = times?.split(", ");
    const timeArr = new Set();
    for (const time of allTimes) {
      const left = time.split("-")[0];
      const right = time.split("-")[1];
      if (!left || !right)
        return "";
      let leftTime;
      let rightTime;
      if (left.includes("am")) {
        leftTime = parseInt(left.substring(0, left.indexOf("am")));
      }
      else if (left.includes("pm")) {
        leftTime = parseInt(left.substring(0, left.indexOf("pm"))) + 12;
      }
      if (right.includes("am")) {
        rightTime = parseInt(right.substring(0, right.indexOf("am")));
      }
      else if (right.includes("pm")) {
        rightTime = parseInt(right.substring(0, right.indexOf("pm"))) + 12;
      }
      for (let i = leftTime; i < rightTime; i++) {
        timeArr.add(i);
      }
    }
    return Array.from(timeArr);
  }
}

export default apiLayer;