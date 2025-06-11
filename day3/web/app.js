const express = require('express');
const { Pool } = require('pg');
const app = express();
const port = 3000;

// Database configuration from environment variables
const dbConfig = {
  user: process.env.DATABASE_USER,
  password: process.env.DATABASE_PASSWORD,
  host: process.env.DATABASE_HOST,
  port: process.env.DATABASE_PORT,
  database: process.env.DATABASE_NAME,
};

// Create a new database pool
const pool = new Pool(dbConfig);

// Connect to the database and log result
async function testDbConnection() {
  let client;
  try {
    console.log('Attempting to connect to database with config:', {
      host: dbConfig.host,
      port: dbConfig.port,
      database: dbConfig.database,
      user: dbConfig.user,
    });
    
    client = await pool.connect();
    console.log('Successfully connected to database!');
    return true;
  } catch (err) {
    console.error('Database connection error:', err.message);
    return false;
  } finally {
    if (client) client.release();
  }
}

// Root endpoint
app.get('/', async (req, res) => {
  const isConnected = await testDbConnection();
  
  let html;
  if (isConnected) {
    try {
      // Query data from the database
      const result = await pool.query('SELECT * FROM items');
      const items = result.rows;
      
      // Generate HTML with the items
      html = `
        <!DOCTYPE html>
        <html>
        <head>
            <title>Docker Debugging - Day 3</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    text-align: center;
                }
                .success {
                    color: green;
                    font-size: 24px;
                    margin: 20px 0;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }
                th, td {
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }
                th {
                    background-color: #f2f2f2;
                }
            </style>
        </head>
        <body>
            <h1>Docker Debugging Assignment</h1>
            <h2>Day 3 - Multi-Container Communication</h2>
            <div class="success">
                Success! You've fixed all the issues!
            </div>
            <p>
                You successfully fixed the connection between the web service and the database.
            </p>
            <h3>Items from Database:</h3>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Description</th>
                </tr>
                ${items.map(item => `
                    <tr>
                        <td>${item.id}</td>
                        <td>${item.name}</td>
                        <td>${item.description}</td>
                    </tr>
                `).join('')}
            </table>
        </body>
        </html>
      `;
    } catch (err) {
      console.error('Error querying database:', err);
      html = `
        <!DOCTYPE html>
        <html>
        <head>
            <title>Docker Debugging - Day 3</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    text-align: center;
                }
                .error {
                    color: red;
                    font-size: 24px;
                    margin: 20px 0;
                }
            </style>
        </head>
        <body>
            <h1>Docker Debugging Assignment</h1>
            <h2>Day 3 - Multi-Container Communication</h2>
            <div class="error">
                Connected to database but failed to query data: ${err.message}
            </div>
            <p>
                You've fixed the connection, but there might still be an issue with the database schema.
            </p>
        </body>
        </html>
      `;
    }
  } else {
    html = `
      <!DOCTYPE html>
      <html>
      <head>
          <title>Docker Debugging - Day 3</title>
          <style>
              body {
                  font-family: Arial, sans-serif;
                  max-width: 800px;
                  margin: 0 auto;
                  padding: 20px;
                  text-align: center;
              }
              .error {
                  color: red;
                  font-size: 24px;
                  margin: 20px 0;
              }
              pre {
                  background-color: #f5f5f5;
                  padding: 15px;
                  border-radius: 5px;
                  text-align: left;
                  overflow-x: auto;
              }
          </style>
      </head>
      <body>
          <h1>Docker Debugging Assignment</h1>
          <h2>Day 3 - Multi-Container Communication</h2>
          <div class="error">
              Failed to connect to the database!
          </div>
          <p>
              Check the connection settings and make sure the database is running.
          </p>
          <h3>Database Configuration:</h3>
          <pre>
Host: ${dbConfig.host}
Port: ${dbConfig.port}
Database: ${dbConfig.database}
User: ${dbConfig.user}
          </pre>
          <p>
              Look at the logs for more information.
          </p>
      </body>
      </html>
    `;
  }
  
  res.send(html);
});

// Start the server
app.listen(port, () => {
  console.log(`Web service listening at http://localhost:${port}`);
  console.log('Environment variables:');
  console.log(`DATABASE_HOST: ${process.env.DATABASE_HOST}`);
  console.log(`DATABASE_PORT: ${process.env.DATABASE_PORT}`);
  console.log(`DATABASE_USER: ${process.env.DATABASE_USER}`);
  console.log(`DATABASE_NAME: ${process.env.DATABASE_NAME}`);
  
  testDbConnection();
}); 