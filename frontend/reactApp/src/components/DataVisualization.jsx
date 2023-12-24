import React, {useEffect, useState} from "react";

const DataVisualization = () => {
    const [data, setData] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch('http://localhost:8000/enemies/dragons/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to fetch.');
                }
                return response.json();
            })
            .then(data =>{
                setData(data);
                setIsLoading(false);
            })
            .catch(error => {
                setError(error.message);
                setIsLoading(false);
            });

    }, []);

    if (isLoading) {
        return <p>Loading...</p>;
    }
    if (error) {
        return <p>Error: {error}</p>;
    }
        
    return (
        <div>
            <h1>DRAGONS</h1>
            {data.map(dragon =>(
                <div key={dragon.id}>
                    <h2>{dragon.name}</h2>
                    <p>{dragon.element}</p>
                    <p>{dragon.attack}</p>
                    <p>{dragon.defense}</p>
                    <p>{dragon.hp}</p>
                    <p>{dragon.speed}</p>
                </div>
            ))}
        </div>
    );
};

export default DataVisualization;