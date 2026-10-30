# `MSTimestampResponse`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 12 instance variables, 12 properties, 44 instance methods, 1 class methods

## Instance variables

```
@"NSData" _timestampResponse;
@"MSPKIStatusInfo" _status;
@"MSMessageImprint" _messageImprint;
@"NSDate" _timestamp;
@"NSData" _nonce;
@"NSArray" _certificates;
@"NSData" _timeStampTokenData;
@"NSData" _serialNumber;
@"NSString" _tsa;
@"MSOID" _tsaPolicyID;
q _version;
@"MSCMSSignedData" _timeStampToken;
```

## Properties

```
@property (T@"MSMessageImprint",&,V_messageImprint) messageImprint;
@property (T@"NSData",&,V_serialNumber) serialNumber;
@property (T@"NSString",&,V_tsa) tsa;
@property (T@"MSOID",&,V_tsaPolicyID) tsaPolicyID;
@property (Tq,V_version) version;
@property (T@"MSPKIStatusInfo",&,V_status) status;
@property (T@"NSDate",&,V_timestamp) timestamp;
@property (T@"NSData",&,V_nonce) nonce;
@property (T@"MSCMSSignedData",&,V_timeStampToken) timeStampToken;
@property (T@"NSData",&,V_timeStampTokenData) timeStampTokenData;
@property (T@"NSData",&,V_timestampResponse) timestampResponse;
@property (T@"NSArray",&,V_certificates) certificates;
```

## Class methods

```
+[MSTimestampResponse supportsSecureCoding];
```

## Instance methods

```
-[MSTimestampResponse certificates];
-[MSTimestampResponse nonce];
-[MSTimestampResponse setSerialNumber:];
-[MSTimestampResponse setTimestamp:];
-[MSTimestampResponse debugDescription];
-[MSTimestampResponse setCertificates:];
-[MSTimestampResponse timestamp];
-[MSTimestampResponse status];
-[MSTimestampResponse serialNumber];
-[MSTimestampResponse version];
-[MSTimestampResponse encodeWithCoder:];
-[MSTimestampResponse init:];
-[MSTimestampResponse hash];
-[MSTimestampResponse description];
-[MSTimestampResponse initWithCoder:];
-[MSTimestampResponse setVersion:];
-[MSTimestampResponse setStatus:];
-[MSTimestampResponse isEqual:];
-[MSTimestampResponse setNonce:];
-[MSTimestampResponse timestampResponse];
-[MSTimestampResponse signingCertificate];
-[MSTimestampResponse verifyWithMessageImprint:error:];
-[MSTimestampResponse setTsa:];
-[MSTimestampResponse setTsaPolicyID:];
-[MSTimestampResponse tsa];
-[MSTimestampResponse certificateHasTimeStampingEKU:];
-[MSTimestampResponse initWithTimestampToken:];
-[MSTimestampResponse isEqualToTimestampResponse:error:];
-[MSTimestampResponse messageImprint];
-[MSTimestampResponse parseFailureInfo:];
-[MSTimestampResponse parseTSAFromGeneralName:];
-[MSTimestampResponse parseTSTInfo:error:];
-[MSTimestampResponse parseTimeStampToken:error:];
-[MSTimestampResponse parseTimestampResponse:];
-[MSTimestampResponse setMessageImprint:];
-[MSTimestampResponse setTimeStampToken:];
-[MSTimestampResponse setTimeStampTokenData:];
-[MSTimestampResponse setTimestampResponse:];
-[MSTimestampResponse timeStampToken];
-[MSTimestampResponse timeStampTokenData];
-[MSTimestampResponse tsaPolicyID];
-[MSTimestampResponse verifyWithMessageImprint:policies:error:];
-[MSTimestampResponse verifyWithRequest:error:];
-[MSTimestampResponse verifyWithRequest:policies:error:];
```
