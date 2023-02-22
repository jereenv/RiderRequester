# RiderRequester
 Django Rider Requester 
 
	For the below problem statement, I implemented the backend structure for it
	
*** Project Description ***

There will be 2 persons one is a Rider and the other is an Asset Transportation Requester (will be referred as requester from now on). 
A Rider is a person who travels from one place to another and is willing to carry some assets(packages/luggages) along with him. 
A Requester is a person who wants his assets to be carried by someone else from one place to another. 
Requesters can create transportation requests and Riders can share their rides independently
.
Features	
A Rider can share his travel info with details like from and to locations, the number of assets he can take with him etc. 
Requesters can request to carry their assets, with details like from and to locations, the type of assets, number of assets that need to be carried.
A Requester should be able to see all the asset transportation requests requested by him. 
A Requester should be able to see all the matching travel info shared by Riders based on his asset transportation requests locations. 
A Requester can apply to carry his assets by a Rider.

APIs

Write an API to create an asset transport request by using the reference screen mentioned below and return valid response with respective status code (For Requester)
Requester should be able to request an asset transport
Valid asset types are LAPTOP, TRAVEL_BAG, PACKAGE
Valid sensitivities are HIGHLY_SENSITIVE, SENSITIVE, NORMAL
	

Write an API to share the travel info of the Rider by using the reference screen mentioned below and return valid response (For Rider)
Valid travel mediums are BUS, CAR, TRAIN

Write an API to get asset transport requests created by the Requester following the reference screen and get the response details as shown in the screen.(For Requester)
This API should also support
sorting on datetime 
filtering on status and asset type.
3. Api should support pagination
 If no filter is applied, all requests should be shown by default. 


Note: 
Here NO.OF PEOPLE  in the reference screen means NO.OF ASSETS
The initial status of the request should be Pending.
When the request’s end datetime is completed then the status should be Expired.
You can ignore the accepted person details column
Possible statuses are Expired and Pending. Ignore the “Confirm” status shown in the reference image.


Write an API to get the matching rides by Riders based on the requests applied by the Requester. The API should support pagination.

Example of matched requests criteria.
If a requester creates a transportation request from hyderabad to bangalore on a specific date, the matched rides should be of the same locations and date. Multiple rides can be matched to a single request.

The above criteria applies for all the transportation requests of a Requester

Note: 
Here NO.OF PEOPLE in the reference screen means NO.OF ASSETS
The initial status of the matched Asset Transportation request should be NOT_APPLIED & gets changed to APPLIED once the requester applies for it


 As a Requester, I should be able to apply for the travel info shared by a Rider. Once applied the status should be shown as applied in matched rides api. 

