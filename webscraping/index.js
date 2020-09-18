// import { createObjectCsvWriter } from 'csv-writer'
// import { createClient } from 'pexels'
import pexels from 'pexels';
const { createClient } = pexels;
import csv_writer from 'csv-writer';
const { createObjectCsvWriter } = csv_writer;
// require('csv-writer')
// const createObjectCsvWriter = createObjectCsvWriter;

const csvWriter = createObjectCsvWriter({
    path: 'wrinkle_dataset_2xlarge.csv',
    header: [
        { id: 'No', title: 'No' },
        { id: 'URL', title: 'URL' },
        { id: 'Author', title: 'Author' },
        { id: 'AuthorURL', title: 'AuthorURL' },
        { id: 'Condition', title: 'Condition' }
    ]
})



const API_KEY = '563492ad6f917000010000013feb856c52d94c9cbc8fe530332693e2'
const client = createClient(API_KEY)


const query = 'wrinkles'


var callback = new Promise((resolve,reject)=>{
    let counter = 0
    let records = []
    for (let i = 1; i < 4; i++) {
        client.photos.search({
            query,
            page: i,
            per_page: 80
        }).then(result => {
    
            result.photos.forEach((photo, index) => {
                counter++
                let temp = {
                    "No": counter,
                    "URL": photo.src.large2x,
                    "Author": photo.photographer,
                    "AuthorURL": photo.photographer_url,
                    "Condition": query
                }
                records.push(temp)
                console.log("Finished scraping pg "+i)
                if (counter===239) resolve(records)
            });       
           
        }
        )
    }
})
    

callback.then(result=>{
    csvWriter.writeRecords(result).then(() => {
                console.log("Done!")
            })
})

// if(i===3){
//     
// }