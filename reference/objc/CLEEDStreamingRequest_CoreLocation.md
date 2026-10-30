# `CLEEDStreamingRequest`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CLEEDRequest`
- Protocols: `NSSecureCoding`
- 3 instance variables, 4 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSString" _token;
@"NSString" _baseURL;
@"NSString" _relativePath;
```

## Properties

```
@property (T@"NSString",&,N,V_baseURL) baseURL;
@property (T@"NSString",&,N,V_relativePath) relativePath;
@property (T@"NSString",&,N) streamingURL;
@property (T@"NSString",R,&,N,V_token) token;
```

## Class methods

```
+[CLEEDStreamingRequest supportsSecureCoding];
```

## Instance methods

```
-[CLEEDStreamingRequest initWithDictionary:error:];
-[CLEEDStreamingRequest baseURL];
-[CLEEDStreamingRequest setBaseURL:];
-[CLEEDStreamingRequest dealloc];
-[CLEEDStreamingRequest setRelativePath:];
-[CLEEDStreamingRequest relativePath];
-[CLEEDStreamingRequest encodeWithCoder:];
-[CLEEDStreamingRequest description];
-[CLEEDStreamingRequest initWithCoder:];
-[CLEEDStreamingRequest token];
-[CLEEDStreamingRequest getRequestDict];
-[CLEEDStreamingRequest initWithDictionary:decryptedRequestData:baseURL:error:];
-[CLEEDStreamingRequest initWithID:psapID:partnerID:geofenceID:requestDate:state:baseURL:relativePath:token:];
-[CLEEDStreamingRequest setStreamingURL:];
-[CLEEDStreamingRequest streamingURL];
```
