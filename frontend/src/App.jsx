import { useState, useRef, useEffect } from 'react';
import GlassCard from './components/GlassCard';
import ChatBubble from './components/ChatBubble';
import './styles/globals.css';

export default function App(){
  const [messages,setMessages]=useState([]);
  const [input,setInput]=useState("");
  const endRef=useRef(null);
  useEffect(()=>{ endRef.current?.scrollIntoView({behavior:"smooth"}); },[messages]);

  async function send(){
    if(!input.trim()) return;
    const userMsg={role:"user",text:input};
    setMessages(m=>[...m,userMsg]);
    try{
      const resp=await fetch("http://127.0.0.1:8000/api/ask",{method:"POST",headers:{"Content-Type":"application/json"},body: JSON.stringify({message:input})});
      const data=await resp.json();
      const botMsg={role:"bot",text:data.reply};
      setMessages(m=>[...m,botMsg]);
    }catch(e){
      setMessages(m=>[...m,{role:'bot',text:'Error contacting backend'}]);
    }
    setInput("");
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-700 to-blue-600 flex items-center justify-center p-4">
      <GlassCard>
        <div className="mb-4 flex items-center gap-3">
          <img src="/avatars/bot.png" alt="MindLink AI Logo" className="w-10 h-10 rounded-full object-cover shadow-sm"/>
          <div>
            <div className="text-white text-xl font-semibold">MindLink AI</div>
            <div className="text-white/70 text-xs">Your friendly assistant</div>
          </div>
        </div>
        <div className="h-96 overflow-y-auto pr-2">
          {messages.map((m,i)=>(<ChatBubble key={i} role={m.role} text={m.text}/>))}
          <div ref={endRef}></div>
        </div>
        <div className="flex gap-2 mt-4">
          <input className="flex-grow bg-white/10 backdrop-blur-md px-3 py-2 rounded-xl outline-none chat-input placeholder-gray-400"
            value={input} onChange={e=>setInput(e.target.value)} onKeyDown={e=>e.key==="Enter"&&send()} placeholder="Type a message..."/>
          <button onClick={send} className="px-4 py-2 bg-white/30 text-white rounded-xl">Send</button>
        </div>
      </GlassCard>
    </div>
  );
}
