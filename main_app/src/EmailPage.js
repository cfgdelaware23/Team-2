import React from 'react'
import EmailComponent from './EmailComponent'

function EmailPage() {

    // const [events, setEvents] = useState([]) // set state data

    // get tomorrow's date
    const today = new Date()
    const tomorrow = new Date(today)
    tomorrow.setDate(tomorrow.getDate() + 1)

    // // fetch data from backend
    // useEffect(() => {
    //   fetch("/getSchedule").then(
    //     res => res.json()
    //   ).then( 
    //     data => {
    //       setEvents(data)
    //       console.log(data)
    //     }
    //   )
    // }, [])

  const events = [
    {
      title: "ACB Presents The Daily Schedule",
      description: "Join your Community Morning Crew for the question of the day; reading of the daily schedule; and sharing time.",
      acb_link: "http://www.acbmedia.org/5",
      acb_desc: "Listen on ACB Media 5",
      amazon_call: "Say to your Amazon device, “ask ACB Media to play 5.”",
      clubhouse_link: "https://www.clubhouse.com/event/M49bp8Km?utm_medium=ch_event&utm_campaign=kkfdqoZtTwqyp7nuMjDeTQ-573858",
      clubhouse_desc: "Join in Clubhouse",
      zoom_link: "https://acb-org.zoom.us/j/83900771734",
      zoom_title: "ACB Presents The Daily Schedule",
      onetap: "+13126266799,,83900771734#",
      phone: "312-626-6799",
      meeting_id: "839 0077 1734",
    },
    {
      title: "The Breakfast Bunch",
      description: "Join Tom and the gang for an hour of free-flowing conversation.",
      acb_link: "",
      acb_desc: "",
      amazon_call: "",
      clubhouse_link: "",
      clubhouse_desc: "",
      zoom_link: "https://acb-org.zoom.us/j/87608122562?pwd=ZENhZnE2dk9xREJxb2UvaDBxcFVsZz09",
      zoom_title: "The Breakfast Bunch",
      onetap: "+13126266799,,87608122562#",
      phone: "312-626-6799",
      meeting_id: "876 0812 2562",
    },
    {
      title: "Spiritual Sanctuary",
      description: "Come one, come all to a place where we can relax and discuss all things spiritual with an open mind and acceptance. All faiths are welcome.",
      acb_link: "",
      acb_desc: "",
      amazon_call: "",
      clubhouse_link: "",
      clubhouse_desc: "",
      zoom_link: "https://acb-org.zoom.us/j/86926851687?pwd=czRNMFd2NXNVUGR0ZWtBTjk3V0JYdz09",
      zoom_title: "Spiritual Sanctuary",
      onetap: "+13126266799,,86926851687#",
      phone: "312-626-6799",
      meeting_id: "869 2685 1687"
    },
    {
      title: "Sunday Edition",
      description: "This Sunday Anthony and the Sunday Edition Crew welcomes Everette Bacon the new Vice President of Blindness Initiatives, AIRA. Everette who is a prominent Board member of the National Federation of the Blind and passionate Advocator will share his journey with us and give us a look into the realm of advocating for Visual Interpretation.",
      acb_link: "http://www.acbmedia.org/1",
      acb_desc: "Listen on ACB Media 1",
      amazon_call: "Say to your Amazon device, “ask ACB Media to play 1.”",
      clubhouse_link: "https://www.clubhouse.com/event/mJwvrqVV?utm_medium=ch_event&utm_campaign=kkfdqoZtTwqyp7nuMjDeTQ-654237",
      clubhouse_desc: "Join in Clubhouse",
      zoom_link: "https://zoom.us/j/93847707647?pwd=Snc4TG1QdEh5dXRUNFNjU1U4dHM0dz09",
      zoom_title: "Sunday Edition",
      onetap: "+13126266799,,93847707647#,,,,*893509#",
      phone: "312-626-6799",
      meeting_id: "938 4770 7647"
    },
    {
      title: "Ask the Pastor",
      description: "Ask Pastor Bill your questions about the Bible or the Christian life. A teaching will be followed by your questions. Prayer requests can then be shared if desired. This event is open to anyone regardless of their denomination.",
      acb_link: "",
      acb_desc: "",
      amazon_call: "",
      clubhouse_link: "",
      clubhouse_desc: "",
      zoom_link: "https://acb-org.zoom.us/j/81543193834?pwd=eWV0dW9QY2c4U0pGS0F6bmVQTWwrdz09",
      zoom_title: "Ask the Pastor",
      onetap: "13126266799,,81543193834#",
      phone: "312-626-6799",
      meeting_id: "815 4319 3834"
    }
  ]

  // maps through all events and renders EmailComponent for each
  return (
    <>
      <h1>Sunday September 17, 2023</h1>
      {events.map((event) => {
        return (
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
        />)
      })}
    </>
  )
}

export default EmailPage