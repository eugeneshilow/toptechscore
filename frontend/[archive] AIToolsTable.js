import React, { useState, useEffect } from 'react';
import { Table } from 'antd';
import './AIToolsTable.css';

function AIToolsTable() {
  const [tools, setTools] = useState([]);

  useEffect(() => {
    fetch('/api/tools/')
      .then(response => response.json())
      .then(data => setTools(data));
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
      dataIndex: 'es_score',
      key: 'es_score',
    },
    {
      title: 'Popularity',
      dataIndex: 'popularity',
      key: 'popularity',
    },
    {
      title: 'Engagement',
      dataIndex: 'engagement',
      key: 'engagement',
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

  return <Table className="ai-tools-table" columns={columns} dataSource={tools} rowKey="id" />;
}

export default AIToolsTable;

