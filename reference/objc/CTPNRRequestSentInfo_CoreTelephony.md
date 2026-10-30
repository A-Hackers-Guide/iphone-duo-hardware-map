# `CTPNRRequestSentInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _success;
@"NSString" _token;
@"NSNumber" _timeout;
@"NSString" _requestID;
```

## Properties

```
@property (TB,N,V_success) success;
@property (T@"NSString",&,N,V_token) token;
@property (T@"NSNumber",&,N,V_timeout) timeout;
@property (T@"NSString",&,N,V_requestID) requestID;
```

## Class methods

```
+[CTPNRRequestSentInfo supportsSecureCoding];
```

## Instance methods

```
-[CTPNRRequestSentInfo setSuccess:];
-[CTPNRRequestSentInfo setRequestID:];
-[CTPNRRequestSentInfo success];
-[CTPNRRequestSentInfo requestID];
-[CTPNRRequestSentInfo init];
-[CTPNRRequestSentInfo timeout];
-[CTPNRRequestSentInfo setTimeout:];
-[CTPNRRequestSentInfo encodeWithCoder:];
-[CTPNRRequestSentInfo description];
-[CTPNRRequestSentInfo initWithCoder:];
-[CTPNRRequestSentInfo token];
-[CTPNRRequestSentInfo setToken:];
-[CTPNRRequestSentInfo copyWithZone:];
-[CTPNRRequestSentInfo isEqual:];
-[CTPNRRequestSentInfo isEqualToCTPNRRequestSentInfo:];
```
