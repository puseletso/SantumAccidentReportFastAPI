import React, { useEffect, useState } from 'react';
import apiClient from '../api/apiClient';

function AccidentReportList() {
    const [reports, setReports] = useState([]);

    useEffect(() => {
        const fetchReports = async () => {
            try {
                const response = await apiClient.get('/');
                setReports(response.data);
            } catch (error) {
                console.error('Error fetching reports:', error);
            }
        };

        fetchReports();
    }, []);

    const handleDelete = async (id) => {
        try {
            await apiClient.delete(`/${id}`);
            setReports(reports.filter(report => report.id !== id));
        } catch (error) {
            console.error('Error deleting report:', error);
        }
    };

    return (
        <div>
            <h2>Accident Reports</h2>
            <ul>
                {reports.map(report => (
                    <li key={report.id}>
                        <div>{report.client_name}</div>
                        <button onClick={() => handleDelete(report.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default AccidentReportList;
