function apiLayer(volunteerAvailability, eventSchedule) {
  const formattedVolunteerData = volunteerAvailability.map((d) => {
    return (
      {
        "name": d.Name,
        "skills": d.Roles?.split(", ") ?? ['Host'],
        "monday": convertTimes(d.Monday),
        "tuesday": convertTimes(d.Tuesday),
        "wednesday": convertTimes(d.Wednesday),
        "thursday": convertTimes(d.Thursday),
        "friday": convertTimes(d.Friday),
        "saturday": convertTimes(d.Saturday),
        "sunday": convertTimes(d.Sunday)
      }
    );
  });
  const formattedEventData = eventSchedule.map((e) => {
    return (
      {
        "eventName": e.Event,
        "skillsNeeded": e["Skills Needed"]?.split(", ") ?? ["Host"],
        "day": e.Day,
        "meetingID": e["Meeting ID"] ?? "Not Available",
        "organizer": e.Organizer ?? "Not Available",
        "account": e.Account,
        "recurrence": e.Recurring,
        "time": [parseInt(parseFloat(e.Time) * 24)]
      }
    );
  })
  console.log(formattedVolunteerData);
  console.log(formattedEventData);
  const json = {
    "volunteerData": formattedVolunteerData,
    "eventData": formattedEventData
  }
  console.log(json);
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(json)
  };
  fetch("/getSchedule", requestOptions).then((res) =>
      res.json().then((d) => {
          const blob = new Blob([d.schedule], { type: 'text/csv' });
          const url = window.URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.style.display = 'none';
          a.href = url;
          a.download = "filename";
        
          document.body.appendChild(a);
          a.click();
        
          window.URL.revokeObjectURL(url);
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
        return [];
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