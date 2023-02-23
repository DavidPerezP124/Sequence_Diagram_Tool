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


Now you can send any evnt to it and the application will order it according to the timestamp, the events must have the following values:

{
    "type": "", // The layer calling this
    "data": "", // The interaction name
    "date": ""  // A Unix timestamp in seconds since epoch
}

## I have the diagrama now, so what?

You can better visualize interactions between your systems.

You can share an image of the diagram.

You can measure time between events.

## Examples

WIP
