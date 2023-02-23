## Flask Examples

This example uses a truncated Flask backend and a React frontend.

Then only method that calls to the server is the Orders.js component.

When it loads for the first time it requests the orders from the backend.

When it loads it sends an event to the websocket, using the port `8282`.

When the backend receives the calls it also sends a message to the websocket on `8282`.

The time that it uses must be similar between them. It uses a unix time stamp in seconds after 1970 * 1000.

On JS the `new Date().getTime()` returns this format out of the box. 
On python you would need to multiply the current value of `timestamp()` by 1000.

They need to be on the same timezone, or else you will get very different results and organization.