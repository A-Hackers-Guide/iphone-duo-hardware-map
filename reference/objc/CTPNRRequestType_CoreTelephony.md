# `CTPNRRequestType`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"NSData" _pushToken;
@"NSString" _embedded;
@"NSNumber" _attemptCount;
@"NSArray" _pnrReqList;
@"NSString" _sessionToken;
@"NSString" _requestID;
```

## Properties

```
@property (T@"NSData",&,N,V_pushToken) pushToken;
@property (T@"NSString",&,N,V_embedded) embedded;
@property (T@"NSNumber",&,N,V_attemptCount) attemptCount;
@property (T@"NSArray",&,N,V_pnrReqList) pnrReqList;
@property (T@"NSString",&,N,V_sessionToken) sessionToken;
@property (T@"NSString",&,N,V_requestID) requestID;
```

## Class methods

```
+[CTPNRRequestType supportsSecureCoding];
```

## Instance methods

```
-[CTPNRRequestType pushToken];
-[CTPNRRequestType setPushToken:];
-[CTPNRRequestType setRequestID:];
-[CTPNRRequestType requestID];
-[CTPNRRequestType init];
-[CTPNRRequestType encodeWithCoder:];
-[CTPNRRequestType sessionToken];
-[CTPNRRequestType description];
-[CTPNRRequestType initWithCoder:];
-[CTPNRRequestType setAttemptCount:];
-[CTPNRRequestType copyWithZone:];
-[CTPNRRequestType isEqual:];
-[CTPNRRequestType setSessionToken:];
-[CTPNRRequestType attemptCount];
-[CTPNRRequestType pnrReqList];
-[CTPNRRequestType setEmbedded:];
-[CTPNRRequestType setPnrReqList:];
-[CTPNRRequestType embedded];
-[CTPNRRequestType isEqualToCTPNRRequestType:];
```
