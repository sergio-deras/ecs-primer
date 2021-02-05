import express from 'express';

const app = express();
const port = 80;

app.get('/', (req, res) => {
    res.send('Hola nuevo mundo');
});

app.listen(port, () => {
    console.log( 'Server started at http://localhost:${ port }' );
} );