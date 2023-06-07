import React, { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './main';
import CityChart from './CityChart';

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/city-chart" element={<CityChart />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
