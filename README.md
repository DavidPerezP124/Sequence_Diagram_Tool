# Sequence Diagram Tool
A tool to help create sequence diagrams for system documentation and debugging

## What does this do?

This helps visualizing, sharing and timing object interaction in a system.

The system may vary from the backend, the frontend, middleware, etc.

And the resulting diagram can be shared with others, for documentation or reporting.

## How to use this?

This creates a local server to send events from any system.

The port that this will use can be specified in the `Set New Port` section on the bottom left.

The default port that this uses is `8282`.

You can create a new process to collect the events, either with a POST to the local server.

example:

```console
curl --location 'http://localhost:8220/create-process' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'id=New_Process'
```

Or with the `+` sign at the top left, just give it a name and create the process to send to.


Now you can send any event to the websocket and the application will order it according to the timestamp, the events must have the following values:

{
    "type": "", // The layer calling this
    "data": "", // The interaction name
    "date": ""  // A Unix timestamp in seconds since epoch
}

For the current example you would send the message to the following socket: `ws://localhost:8282/process?id=New_Process`

If you have not worked with websockets before, you may start [here](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications) 

## I have the diagrama now, so what?

You can better visualize interactions between your systems.

You can share an image of the diagram.

You can measure time between events.

## Examples

An example to get started using Postman to understand the flow of the application.

You can create a tab to collect events with a POST request, as mentioned above:

![POST](https://user-images.githubusercontent.com/32963483/220938149-fa229b53-4862-49a3-a41a-75eefdfc30d9.png)

Now you need to connect to the websocket:

![WS Connect](https://user-images.githubusercontent.com/32963483/220938976-ed5039ef-f6d9-4e30-96bd-601308846163.png)

Now send a JSON message with the required properties: type, data, date:

![Message](https://user-images.githubusercontent.com/32963483/220939237-9f824214-2dbd-4896-947f-4e4ecc9216bf.png)

And the app will update with the message that was sent:

![App shows message](https://user-images.githubusercontent.com/32963483/220939339-41eb49cf-f998-456c-b712-e60252958ab5.png)

When you are happy with your diagram:

![Screenshot 2023-02-23 at 8 27 58](https://user-images.githubusercontent.com/32963483/220939532-178f0fba-93b1-41f6-a0d6-103609eb6739.png)

NOTE: Only available if you are using MacOS Ventura or above.

When you click share:
A preview of the image will appear, you may either cancel or share the image:

![Screenshot 2023-02-23 at 8 28 07](https://user-images.githubusercontent.com/32963483/220939793-97d8f718-1b2f-40da-9912-3eefd65628c3.png)




