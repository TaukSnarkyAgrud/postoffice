const newman = require('newman');
const fs = require('fs');
var util = require('util');


newman.run({
    reporters: 'cli',
    collection: require('./Alerts 2.7.postman_collection.json'),
    environment: require('./QA ATL - Message Envy General Hospital.postman_environment.json'),
    folder: 'Contract Tests'
}).on('start', function (err, args) { // on start of run, log to console
    console.log('running a collection...');
}).on('done', function (err, summary) {
    if (err || summary.error) {
        console.error('collection run encountered an error.');
    }
    else {
        console.log('Collection run completed. Exporting Contract Responses to file: ./ResponseBodies.json');
        const filteredRequest = summary.run.executions.map(function (req){
            return {
                "name": req['item']['name'],
                "body": JSON.parse(req.response.text())
                };
            });
        fs.writeFileSync("ResponseBodies.json", JSON.stringify(filteredRequest));
    }
});