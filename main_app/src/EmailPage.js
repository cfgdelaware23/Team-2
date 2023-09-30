import React from 'react'
import EmailComponent from './EmailComponent'

function EmailPage() {

    const [events, setEvents] = useState([]) // set state data

    // get tomorrow's date
    const today = new Date()
    const tomorrow = new Date(today)
    tomorrow.setDate(tomorrow.getDate() + 1)

    // fetch data from backend
    useEffect(() => {
      fetch("/getSchedule").then(
        res => res.json()
      ).then(
        data => {
          setEvents(data)
          console.log(data)
        }
      )
    }, [])

  return (
    <>
      <h1>{tomorrow.getDay + " " + tomorrow.getMonth + " " + tomorrow.getDate + ", " + tomorrow.getFullYear}</h1>
      {events.map((event) => {
        <EmailComponent 
          title={event.title}
          description={event.description}
          acb_link={event.acb_link}
          acb_desc={event.acb_desc}
          amazon_call={event.amazon_call}
          clubhouse_link={event.clubhouse_link}
          clubhouse_desc={event.clubhouse_desc}
          zoom_link={event.zoom_link}
          zoom_title={event.zoom_title}
          onetap={event.onetap}
          phone={event.phone}
          meeting_id={event.meeting_id}
        />
      })}
    </>
  )
}

export default EmailPage