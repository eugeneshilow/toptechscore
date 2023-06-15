import './Table.css';
import React, { useState, useEffect } from 'react';
import { Table, Popover } from 'antd';

function App() {
  const [tools, setTools] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/tools/')
        .then(response => response.json())
        .then(data => {
            console.log(data); // add console log to check if data is fetched correctly
            setTools(data);
        });
  }, []);

  const columns = [
    {
      title: '#',
      key: 'index',
      render: (text, record, index) => index + 1,
    },
    {
      title: 'Name',
      dataIndex: 'name',
      key: 'name',
    },
    {
      title: 'ES Score',
      dataIndex: 'tts',
      key: 'tts',
      sorter: (a, b) => a.tts - b.tts, 
      render: tts => (
        <span style={{backgroundColor: '#13C783', padding: '5px 10px', borderRadius: '5px', color: 'white'}}>
          {tts}
        </span>
      ),
    },
    {
      title: 'Popularity',
      dataIndex: 'popularity',
      key: 'popularity',
      sorter: (a, b) => a.tts - b.tts, 
      render: popularity => (
        <Popover content={`Popularity score: ${"test"}`}>
          <span>{popularity}</span>
        </Popover>
      )
    },
    {
      title: 'Engagement',
      dataIndex: 'engagement',
      key: 'engagement',
      sorter: (a, b) => a.tts - b.tts,
      render: engagement => (
        <Popover content={`Engagement score: ${"test2"}`}>
          <span>{engagement}</span>
        </Popover>
      )
    },
    {
      title: 'Category',
      dataIndex: 'category',
      key: 'category',
    },
    {
      title: 'Sub-category',
      dataIndex: 'sub_category',
      key: 'sub_category',
    },
    {
      title: 'Description',
      dataIndex: 'description',
      key: 'description',
    },
  ];

  console.log(tools); // add console log to check if tools state is updated correctly

  return (
    <Table
      columns={columns}
      dataSource={tools}
      rowKey="id"
      pagination={{ pageSize: 100, showSizeChanger: false }}
    />
  );
}

export default App;