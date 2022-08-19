const inshorts = require('inshorts-news-api');
let str;
var fs=require('fs');


function c1(){
	var options = {
		lang: 'en',
		category: 'business'
	  }
	  
	  inshorts.getNews(options ,function(result, news_offset){
		console.log(news_offset);
		ADD(result);
        //console.log(result);
	  });
	}

function countDown(ne1) {	
	  var options = {
		lang: 'en',
		category: 'business',
		news_offset: ne1
	  }
	inshorts.getMoreNews(options ,function(result, news_offset1){
		if(a==0){
			const output=str;
			//console.log(str);
			fs.writeFile('/Users/yashkharade/Desktop/javascript/OUTPUT.json',str,function(err){
				if(err) throw err;
				console.log('Doneee');
			});		
		}
		
		if(a>0){
            ADD(result);
            console.log(news_offset1);
			console.log(a+"\n")
			a = a-1;
			return countDown(news_offset1);
		}
	  });
}

function ADD(result){
	if(str==undefined){
		str=JSON.stringify(result);
	}else{
		str=str+JSON.stringify(result);
	}
}
let a = 100;
c1();
countDown('7pkh3bm5-1');