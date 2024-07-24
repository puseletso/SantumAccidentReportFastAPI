import React, { useState } from 'react';
import apiClient from '../api/apiClient';

function AccidentReportForm() {
    const [formData, setFormData] = useState({
        client_name: '',
        contact_number: '',
        accident_description: '',
        street_name: '',
        surburb_name: '',
        city_name: '',
        time: '',
        images: [],
        police_station_address: '',
        ar_number: ''
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await apiClient.post('/', formData);
            alert('Accident report submitted successfully');
            setFormData({
                client_name: '',
                contact_number: '',
                accident_description: '',
                street_name: '',
                surburb_name: '',
                city_name: '',
                time: '',
                images: [],
                police_station_address: '',
                ar_number: ''
            });
        } catch (error) {
            console.error('Error submitting report:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            {/* Include form fields here */}
            <button type="submit">Submit</button>
        </form>
    );
}

export default AccidentReportForm;
