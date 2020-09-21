// customized antd

import React from 'react';
import 'antd/dist/antd.css';
import './NavBar.css';
import { Menu } from 'antd';
import { HomeOutlined, SelectOutlined, CalculatorOutlined } from '@ant-design/icons';

class NavBar extends React.Component {
  state = {
    current: 'Home',
  };

  handleClick = e => {
    // console.log('click ', e);
    this.setState({ current: e.key });
  };

  render() {
    const { current } = '';
    return (
      <Menu onClick={this.handleClick} selectedKeys={[current]} mode="horizontal">
        <Menu.Item key="Home" icon={<HomeOutlined />}>
        <a href="/">Home</a>
        </Menu.Item>

        <Menu.Item key="Analysis" icon={<CalculatorOutlined />}>
        <a href="/search">Analysis</a>
        </Menu.Item>

        <Menu.Item key="code" icon = {<SelectOutlined />}>
          <a href="https://github.com/" target="_blank" rel="noopener noreferrer">
            code
          </a>
        </Menu.Item>
      </Menu>
    );
  }
}

export default NavBar;