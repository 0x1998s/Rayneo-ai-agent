import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { Layout } from 'antd';
import AppHeader from './components/AppHeader';
import AppSidebar from './components/AppSidebar';
import Dashboard from './pages/Dashboard';
import Models from './pages/Models';
import Documents from './pages/Documents';
import Workflows from './pages/Workflows';
import Prompts from './pages/Prompts';
import Finetune from './pages/Finetune';
import Chat from './pages/Chat';
import Settings from './pages/Settings';
import Login from './pages/Login';
import { useAuthStore } from './stores/authStore';
import './App.css';

const { Content, Sider } = Layout;

function App() {
  const { isAuthenticated } = useAuthStore();

  if (!isAuthenticated) {
    return <Login />;
  }

  return (
    <Layout className="app-layout">
      <AppHeader />
      <Layout>
        <Sider width={240} className="app-sidebar">
          <AppSidebar />
        </Sider>
        <Layout>
          <Content className="app-content">
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/models" element={<Models />} />
              <Route path="/documents" element={<Documents />} />
              <Route path="/workflows" element={<Workflows />} />
              <Route path="/prompts" element={<Prompts />} />
              <Route path="/finetune" element={<Finetune />} />
              <Route path="/chat" element={<Chat />} />
              <Route path="/settings" element={<Settings />} />
            </Routes>
          </Content>
        </Layout>
      </Layout>
    </Layout>
  );
}

export default App;
