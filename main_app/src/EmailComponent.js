import React, { useState } from 'react'

function EmailComponent(props) {
  return (
    <>
      <h2>{props.title}</h2>
      <h2>{props.description}</h2>
      {props.acb_link != "" && <a href={props.acb_link}>{props.acb_desc}</a>}
      {props.amazon_call != "" && <h2>{props.amazon_call}</h2>}
      {props.clubhouse_link != "" && <a href={props.clubhouse_link}>{props.clubhouse_desc}</a>}
      <h2>Join the call:</h2>
      <a href={props.zoom_link}>{props.zoom_title}</a>
      <h3>One tap mobile: </h3>
      <p>{"1" + props.onetap}</p>
      <h3>Phone: </h3>
      <p>{props.phone}</p>
      <h3>Webinar ID: </h3>
      <p>{props.meeting_id}</p>
    </>
  )
}

export default EmailComponent