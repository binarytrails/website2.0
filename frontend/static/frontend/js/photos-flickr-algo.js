/*
	Resize photos by rows to fit in client window without losing proportions.
	Status: Development
*/

window.onload=Resize();

function Resize()
{
	var photosUl  = document.getElementById("photos_ul");
	// points -> html objects
	var photos = photosUl.getElementsByTagName("img");
	// html object proprieties in array, used for slice() etc.
	var photosData = Array.prototype.slice.call(photos);
	
	var row = 1;
	var rowTotalWidth = 0;
	var firstRowPhotoIndex = 0;
	for(i = 0; i < photosData.length; i++)
	{
		rowTotalWidth += photos[i].width;
		if (rowTotalWidth > window.innerWidth)
		{
			// on more than 35 px from right border it makes a new line
			rowTotalWidth -= photos[i].width - 35;
				
			// returns portion copy of array & points to the same object
			var rowPhotosData = photosData.slice(firstRowPhotoIndex, i);
			ResizeRowImagesToFitInnerWidth(photos, rowPhotosData, rowTotalWidth);
			
			row += 1;
			rowTotalWidth = 0;
			firstRowPhotoIndex = i;
		} 
		else if (i == photosData.length - 1)
		{
			//rowTotalWidth -= 35;
			//var rowPhotosData = photosData.slice(firstRowPhotoIndex, i);
                        //ResizeRowImagesToFitInnerWidth(photos, rowPhotosData, rowTotalWidth);	
		}
	}
	console.log("End, rows done: " + row);
	
	
	//alert(windowWidth);
}

function ResizeRowImagesToFitInnerWidth(images, imagesData, totalWidth)
{
	console.log("tw:" + window.innerWidth + " \n tiw:" +  totalWidth);

	var index = 0,
	newTiw = 0;
	for(var imageData in imagesData)
	{
		proportion = imagesData[index].width / totalWidth;
		newWidth = window.innerWidth * proportion;
		// not sure
		//newHeight = newWidth / proportion;
		
		newTiw += newWidth;
		console.log("w: " + imagesData[index].width + " x " + proportion + " = " + newWidth)

		images[index].style.width = newWidth.toString() + "px";
		//images[index].style.height = newHeight;
		index += 1;
	}
	console.log("ntiw:" + newTiw);

}

