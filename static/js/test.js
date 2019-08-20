function buildcomparisonData(Year) {
    d3.selectAll("p").remove();
    // @TODO: Complete the following function that builds the metadata panel
    var comparisonURL = `/comparison/${Year}`;
    var input = d3.select("#female-year"); 
    d3.json(comparisonURL).then((data) => {
      // console.log(data)
      data.forEach((Help) => {
        // var row = d3.select("#female-year").append("p");
        //   row.text(`${Help.Name}`);  
        })
    })
}
            // if (Character != null){
            //         Character.forEach((data) =>{
            //             Character.replace(/Mr.|Mrs.|Ms.|Miss|Ms|Mrs|Mr|Dr|Dr.|Atty.|Gov|Gen.|Sgt.|.|(|)|voice|Voice|/g, "")
            //         })
            //         console.log(Character)
                    // CharacterClean.push(char)   
                // }
                // return CharacterClean}
            // console.log(CharacterClean)
function charReplace(data){
    if (data != null){
    var Individchar = str(data).split(", ")
    var Individualchar = Individchar.replace(/Mr.|Mrs.|Ms.|Miss|Ms|Mrs|Mr|Dr|Dr.|Atty.|Gov|Gen.|Sgt.|.|(|)|voice|Voice|(voice)|/g, "")
    return Individualchar
}
return data}
function CharacterVSBaby(Year) {
    var Names = []
    var Rank = []
    var Character = []
    var ID = []
    var CharacterClean = []
    // @TODO: Complete the following function that builds the metadata panel
    var comparisonURL = `/comparison/${Year}`;
    d3.json(comparisonURL).then((data) => {
        // console.log(Mdata)
        data.forEach((Help) => {
        var charname = charReplace(Help.Characters)
            Character.push(charname)
            ID.push(Help.imdbID)
            Names.push(Help.Names)
            Rank.push(Help.Rank)})
            console.log(Character)
        var trace1 = {
            x: Rank,
            y: Names,
            mode: "markers",
            text: Names,
            marker: { size: 3,
            color: Names,
            colorscale: 'Earth'}
        } 
      var data1 = [trace1]   
      Plotly.newPlot("bubble", data1);
         
        })
    
}
    // var filterlist = []
    // for (i=0; i<BabyNamesPopular.length; i++){
    //     Character.filter(function(Characterfilter) { Character[i] == BabyNamesPopular[0]
    //     filterlist.push(Characterfilter)
    //     return Character})
    // }
    // console.log(filterlist)           
 

function init() {
    // Grab a reference to the dropdown select element
    var selector = d3.select("#selDataset");
    console.log(selector);
    // Use the list of sample names to populate the select options
    d3.json("/female/years").then((compareYears) => {
      console.log(compareYears)
        compareYears.forEach((Year) => {
        selector
        .append("option")
        .text(Year)
        .property("value", Year)
      });
  
      // Use the first sample from the list to build the initial plots
      const firstYear = compareYears;
      buildcomparisonData(firstYear);
      CharacterVSBaby(firstYear);
    });
}  
  
function optionChanged(newYear) {
// Fetch new data each time a new sample is selected
    buildcomparisonData(newYear);
    CharacterVSBaby(newYear);
}

  // Initialize the dashboard
init();
