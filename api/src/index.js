const fs = require('fs');
const pdfjs = require('pdfjs-dist');

const PDF_PATH = './AthleticsNIFixtures.pdf';
const PAGE_NUMBER = 1;
const RACES_START_INDEX = 82;
const NUMBER_RACE_COLUMNS = 4;

const race = {
  event: '',
  date: '',
  venue: '',
  time: '',
  contact: ''
};

async function parsePdfText(pdf) {
  const page = await pdf.getPage(PAGE_NUMBER);
  return page.getTextContent();
}

//function buildRaceObjects(pdfStrings) {
  //const result = [];
  //let raceArr = [];
  //pdfStrings.forEach((pdfString, index) => {
    //const nextString = pdfStrings[index + 1];
    //const nextNextString = pdfStrings[index + 2];
    //if (nextString === undefined || nextNextString === undefined) return;
    //const nextTwoEmpty = !nextString.trim() && !nextNextString.trim();
    //if (nextTwoEmpty) {
      //result.push(raceArr);
      //raceArr = [];
    //} else {
      //raceArr.push(pdfString);
    //}
  //})
  //return result;
//}

async function parsePdf(pdf) {
  const textContent = await parsePdfText(pdf);
  console.log(textContent)
  const raceItems = textContent.items.slice(RACES_START_INDEX);
  const pdfStrings = raceItems.map(pdfItem => pdfItem.str);
  //const raceObjects = buildRaceObjects(pdfStrings);
}

pdfjs.getDocument({ url: PDF_PATH }).then(parsePdf);

