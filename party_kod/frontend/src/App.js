// src/App.js

import React, { useState } from 'react';
import Chat from './Chat';

const App = () => {
    const [chatName, setChatName] = useState('');
    const [isChatStarted, setIsChatStarted] = useState(false);

    const handleStartChat = () => {
        setIsChatStarted(true);
    };

    return (
        <div>
            {!isChatStarted ? (
                <div>
                    <h1>Введите название чата</h1>
                    <input type="text" onChange={(e) => setChatName(e.target.value)} />
                    <button onClick={handleStartChat}>Начать чат</button>
                </div>
            ) : (
                <Chat chatName={chatName} />
            )}
        </div>
    );
};

export default App;
