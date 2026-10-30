# `MSCMSAppleTimestampAttribute`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MSCMSTimestampAttribute`
- 3 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"MSTimestampResponse" _cachedTimestampResponse;
B _timestampResponseParsed;
@"NSData" _rawTimestampTokenData;
```

## Properties

```
@property (T@"NSData",&,N,V_rawTimestampTokenData) rawTimestampTokenData;
@property (T@"MSTimestampResponse",R) timestampResponse;
```

## Instance methods

```
-[MSCMSAppleTimestampAttribute certificates];
-[MSCMSAppleTimestampAttribute digestAlgorithm];
-[MSCMSAppleTimestampAttribute verifyTimestamps:error:];
-[MSCMSAppleTimestampAttribute initWithAttribute:error:];
-[MSCMSAppleTimestampAttribute timestampResponse];
-[MSCMSAppleTimestampAttribute encodeAttributeWithError:];
-[MSCMSAppleTimestampAttribute initWithTimestampToken:];
-[MSCMSAppleTimestampAttribute rawTimestampTokenData];
-[MSCMSAppleTimestampAttribute setRawTimestampTokenData:];
-[MSCMSAppleTimestampAttribute verifyWithSignerInfo:policies:error:];
```
