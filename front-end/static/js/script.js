$(document).ready(function () {
    // Function to fetch and display reports
    function fetchReports() {
        fetch('/api/reports')  // Assuming /api/reports is the correct endpoint
            .then(response => response.json())
            .then(data => {
                const reportsContainer = $('#reports');
                reportsContainer.empty();
                data.forEach(report => {
                    const reportItem = `<a href="#" class="list-group-item list-group-item-action">
                        <h5 class="mb-1">${report.client_name || 'N/A'}</h5>
                        <p class="mb-1">${report.accident_description || 'No Description'}</p>
                        <small>${report.time || 'No Time'} - ${report.street_name || 'No Street'}, ${report.city_name || 'No City'}</small>
                    </a>`;
                    reportsContainer.append(reportItem);
                });
            })
            .catch(error => console.error('Error fetching reports:', error));
    }

    // Fetch reports on page load
    fetchReports();

    // Handle form submission to add a new report
    $('#add-report-form').submit(function (event) {
        event.preventDefault();

        const reportData = {
            client_name: $('#client_name').val(),
            contact_number: $('#contact_number').val(),
            accident_description: $('#accident_description').val(),
            street_name: $('#street_name').val(),
            surburb_name: $('#surburb_name').val(),
            city_name: $('#city_name').val(),
            time: $('#time').val(),
            police_station_address: $('#police_station_address').val(),
            ar_number: $('#ar_number').val()
        };

        fetch('/api/reports', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(reportData)
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            $('#add-report-form')[0].reset();
            fetchReports();
        })
        .catch(error => console.error('Error adding report:', error));
    });
});
