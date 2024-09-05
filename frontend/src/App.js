import React, { useState, useEffect } from 'react';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import SendIcon from '@mui/icons-material/Send';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [type, setType] = useState(null);
  const [item, setItem] = useState([]);
  const [selectedItem, setSelectedItem] = useState([]);
  const [message, setMessage] = useState('');

  useEffect(() => {
    const fetchItem = async () => {
      try {
        const response = await axios.get('/file');
        setItem(response.data);
      } catch (error) {
        console.error('Error:', error);
      }
    };

    fetchItem();
  }, []);

  const handleUpload = () => {
    const formData = new FormData();
    formData.append('file', file);

    fetch('/upload', {
      method: 'POST',
      body: formData,
    })
      .then(response => response.json())
      .then(data => {
        window.location.reload();
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };

  const handleText = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/send_message', { message });
      console.log('Resposta da API:', response.data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleItem = async (event) => {
    event.preventDefault();
    var response = null
    try {
      if (type === 'document')
        response = await axios.post('/send_document', { selectedItem });
      else if (type === 'media')
        response = await axios.post('/send_media', { selectedItem });
      console.log('Resposta da API:', response.data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="App">
      <div>
        <form onSubmit={handleText}>
          <label>Mensagem</label>
          <TextField
            id="outlined-multiline-flexible"
            label="Multiline"
            value={message}
            multiline
            maxRows={4}
            onChange={(e) => setMessage(e.target.value)}
          />
          <Button variant="contained" type="submit" endIcon={<SendIcon />}> Enviar </Button>
        </form>
      </div>
      <div>
        <label>Importar Arquivo</label>
        <Button variant="contained" component="label">
          Upload
          <input type="file" hidden onChange={(e) => setFile(e.target.files[0])} />
        </Button>
        {file && (
          <label>{file.name} </label>
        )}
        <Button variant="contained" onClick={handleUpload} endIcon={<SendIcon />}> Enviar </Button>
      </div>
      <div>
        <label>Enviar Arquivo</label>
        <FormControl component="fieldset">
          <RadioGroup
            aria-label="type"
            defaultValue="document"
            name="type"
            value={type}
            onChange={(e) => setType(e.target.value)}
          >
            <FormControlLabel value="document" control={<Radio />} label="Documento" />
            <FormControlLabel value="media" control={<Radio />} label="Fotos e vídeos" />
          </RadioGroup>
          <RadioGroup
            aria-label="items"
            name="items"
            value={selectedItem}
            onChange={(e) => setSelectedItem(e.target.value)}
          >
            {item.map((item, index) => (
              <FormControlLabel
                key={index}
                value={item.fileaddress}
                control={<Radio />}
                label={item.filename}
              />
            ))}
          </RadioGroup>
          <Button variant="contained" onClick={handleItem} endIcon={<SendIcon />}>Enviar</Button>
        </FormControl>
      </div>
    </div>
  );
}

export default App;
