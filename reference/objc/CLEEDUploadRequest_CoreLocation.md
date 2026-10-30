# `CLEEDUploadRequest`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CLEEDRequest`
- Protocols: `NSSecureCoding`
- 7 instance variables, 8 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"NSMutableSet" _mediaList;
@"NSString" _baseURL;
@"NSString" _relativePath;
@"NSString" _token;
@"NSData" _sessionID;
@"NSData" _combinedSecret;
q _numDuplicateMediaSelections;
```

## Properties

```
@property (T@"NSString",&,N,V_baseURL) baseURL;
@property (T@"NSString",&,N,V_relativePath) relativePath;
@property (T@"NSString",&,N) uploadURL;
@property (T@"NSString",R,&,N,V_token) token;
@property (T@"NSData",R,&,N,V_sessionID) sessionID;
@property (T@"NSData",&,N,V_combinedSecret) combinedSecret;
@property (T@"NSMutableSet",&,N,V_mediaList) mediaList;
@property (Tq,N,V_numDuplicateMediaSelections) numDuplicateMediaSelections;
```

## Class methods

```
+[CLEEDUploadRequest supportsSecureCoding];
```

## Instance methods

```
-[CLEEDUploadRequest initWithDictionary:error:];
-[CLEEDUploadRequest baseURL];
-[CLEEDUploadRequest setBaseURL:];
-[CLEEDUploadRequest sessionID];
-[CLEEDUploadRequest dealloc];
-[CLEEDUploadRequest setRelativePath:];
-[CLEEDUploadRequest relativePath];
-[CLEEDUploadRequest encodeWithCoder:];
-[CLEEDUploadRequest description];
-[CLEEDUploadRequest initWithCoder:];
-[CLEEDUploadRequest token];
-[CLEEDUploadRequest setUploadURL:];
-[CLEEDUploadRequest uploadURL];
-[CLEEDUploadRequest mediaList];
-[CLEEDUploadRequest setMediaList:];
-[CLEEDUploadRequest setNumDuplicateMediaSelections:];
-[CLEEDUploadRequest updateRequestWithMediaItemList:];
-[CLEEDUploadRequest combinedSecret];
-[CLEEDUploadRequest getRequestDict];
-[CLEEDUploadRequest initWithDictionary:decryptedRequestData:baseURL:error:];
-[CLEEDUploadRequest initWithID:psapID:partnerID:geofenceID:requestDate:state:baseURL:relativePath:token:sessionID:combinedSecret:mediaList:];
-[CLEEDUploadRequest numDuplicateMediaSelections];
-[CLEEDUploadRequest setCombinedSecret:];
```
