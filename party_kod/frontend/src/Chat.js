// src/Chat.js

import React, { useState, useEffect } from 'react';

const Chat = ({ chatName }) => {
    const [username, setUsername] = useState('');
    const [message, setMessage] = useState('');
    const [messages, setMessages] = useState([]);
    const [ws, setWs] = useState(null);

    useEffect(() => {
        const webSocket = new WebSocket(ws://localhost:8000/ws/chat/${chatName}/);
        
        webSocket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            setMessages((prevMessages) => [...prevMessages, { username: data.username, message: data.message }]);
        };

        setWs(webSocket);

        return () => {
            webSocket.close();
        };
    }, [chatName]);

    const sendMessage = () => {
        if (ws) {
            ws.send(JSON.stringify({ message, username }));
            setMessage('');
        }
    };

    return (
        <div>
            <h2>Chat: {chatName}</h2>
            <input type="text" placeholder="Ваше имя" onChange={(e) => setUsername(e.target.value)} />
            <div>
                {messages.map((msg, index) => (
                    <div key={index}><strong>{msg.username}:</strong> {msg.message}</div>
                ))}
            </div>
            <input type="text" value={message} onChange={(e) => setMessage(e.target.value)} />
            <button onClick={sendMessage}>Отправить</button>
        </div>
    );
};

export default Chat;
