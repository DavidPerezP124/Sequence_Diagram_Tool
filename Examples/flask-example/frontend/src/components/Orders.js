import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Title from './Title';
import { useEffect, useState } from 'react';
import Network from '../services/Network';
import useWebSocket from 'react-use-websocket';

export default function Orders() {
  const [rows, setRows] = useState([]);
  const ws_url = 'ws://localhost:8282/process?id=python_example';
  const { sendMessage } = useWebSocket(ws_url);


  useEffect(() => {
    let network = new Network()
    let time = new Date().getTime()
    time = Math.round((time))
    console.log(time)
    sendMessage(`{"type":"Client","data":"requesting rows","date":"${time}"}`)
    network.getRows().then((res) => {
      if (res) {
        setRows(res)
      }
    })
  },[sendMessage])


  return (
    <React.Fragment>
      <Title>Recent Orders</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>Date</TableCell>
            <TableCell>Name</TableCell>
            <TableCell>Ship To</TableCell>
            <TableCell>Payment Method</TableCell>
            <TableCell align="right">Sale Amount</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id}>
              <TableCell>{row.date}</TableCell>
              <TableCell>{row.name}</TableCell>
              <TableCell>{row.shipTo}</TableCell>
              <TableCell>{row.paymentMethod}</TableCell>
              <TableCell align="right">{`$${row.amount}`}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </React.Fragment>
  );
}
