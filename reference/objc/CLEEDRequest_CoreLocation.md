# `CLEEDRequest`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 14 instance variables, 14 properties, 32 instance methods, 15 class methods

## Instance variables

```
B _metricSubmitted;
@"NSUUID" _ID;
@"NSString" _psapID;
@"NSDate" _requestDate;
q _type;
q _state;
@"NSString" _partnerID;
@"NSString" _geofenceID;
q _requestStatusAtFirstUserResponse;
q _requestTransmissionTime;
d _requestReceivedTime;
d _receivedTimeToFirstUserResponse;
d _receivedTimeToAcceptTime;
q _numMediaSelectIterations;
```

## Properties

```
@property (T@"NSString",R,&,N,V_partnerID) partnerID;
@property (T@"NSString",R,&,N,V_geofenceID) geofenceID;
@property (Tq,N,V_state) state;
@property (Tq,N,V_requestStatusAtFirstUserResponse) requestStatusAtFirstUserResponse;
@property (Tq,N,V_requestTransmissionTime) requestTransmissionTime;
@property (Td,N,V_requestReceivedTime) requestReceivedTime;
@property (Td,N,V_receivedTimeToFirstUserResponse) receivedTimeToFirstUserResponse;
@property (Td,N,V_receivedTimeToAcceptTime) receivedTimeToAcceptTime;
@property (Tq,N,V_numMediaSelectIterations) numMediaSelectIterations;
@property (TB,N,V_metricSubmitted) metricSubmitted;
@property (T@"NSUUID",R,&,N,V_ID) ID;
@property (T@"NSString",R,&,N,V_psapID) psapID;
@property (T@"NSDate",R,&,N,V_requestDate) requestDate;
@property (Tq,R,N,V_type) type;
```

## Class methods

```
+[CLEEDRequest supportsSecureCoding];
+[CLEEDRequest createRequestFromCachedDict:error:];
+[CLEEDRequest createRequestFromDict:baseURL:sessionID:partnerAdrPublicKeyData:deviceSessionPrivateKey:deviceSessionSecret:error:];
+[CLEEDRequest getCallIDFromDict:];
+[CLEEDRequest getDecryptedControlRequestData:sessionID:partnerAdrPublicKeyData:deviceSessionPrivateKey:deviceSessionSecret:combinedSecret:error:];
+[CLEEDRequest getDecryptedPartnerSessionSecret:sessionID:partnerID:partnerAdrPublicKeyData:deviceSessionPrivateKey:];
+[CLEEDRequest getDecryptedRequestDict:requestID:combinedSecret:sharedInfoPrefix:];
+[CLEEDRequest getPartnerIDFromDict:];
+[CLEEDRequest getSessionStartTimeFromDict:];
+[CLEEDRequest getSharedInfoPrefixFromSessionID:partnerID:partnerAdrPublicKeyData:deviceSessionPrivateKey:];
+[CLEEDRequest requestTypeFromDict:];
+[CLEEDRequest toCLEEDRequestString:];
+[CLEEDRequest toCLEEDRequestType:];
+[CLEEDRequest toEEDControlResponseStatus:];
+[CLEEDRequest validateDerivedSessionSecrets:sharedInfoPrefix:partnerKeyConfirmation:];
```

## Instance methods

```
-[CLEEDRequest requestDate];
-[CLEEDRequest initWithDictionary:error:];
-[CLEEDRequest setState:];
-[CLEEDRequest ID];
-[CLEEDRequest dealloc];
-[CLEEDRequest type];
-[CLEEDRequest encodeWithCoder:];
-[CLEEDRequest description];
-[CLEEDRequest initWithCoder:];
-[CLEEDRequest state];
-[CLEEDRequest metricSubmitted];
-[CLEEDRequest receivedTimeToFirstUserResponse];
-[CLEEDRequest updateDurationInformationForCA:];
-[CLEEDRequest geofenceID];
-[CLEEDRequest getRequestDict];
-[CLEEDRequest getResponseDataDictionary];
-[CLEEDRequest initWithDictionary:decryptedRequestData:baseURL:error:];
-[CLEEDRequest initWithID:psapID:partnerID:geofenceID:requestDate:requestType:state:];
-[CLEEDRequest numMediaSelectIterations];
-[CLEEDRequest partnerID];
-[CLEEDRequest psapID];
-[CLEEDRequest receivedTimeToAcceptTime];
-[CLEEDRequest requestReceivedTime];
-[CLEEDRequest requestStatusAtFirstUserResponse];
-[CLEEDRequest requestTransmissionTime];
-[CLEEDRequest setMetricSubmitted:];
-[CLEEDRequest setNumMediaSelectIterations:];
-[CLEEDRequest setReceivedTimeToAcceptTime:];
-[CLEEDRequest setReceivedTimeToFirstUserResponse:];
-[CLEEDRequest setRequestReceivedTime:];
-[CLEEDRequest setRequestStatusAtFirstUserResponse:];
-[CLEEDRequest setRequestTransmissionTime:];
```
