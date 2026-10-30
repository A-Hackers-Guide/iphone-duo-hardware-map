# `MSCMSTimestampAttribute`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MSCMSAttributeCoder`
- 6 instance variables, 8 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _certChainRequested;
@"NSURL" _serverURL;
@"MSCMSSignerInfo" _signerInfo;
@"NSArray" _certificates;
@"MSOID" _digestAlgorithm;
@"MSCMSTimestampAttributeInternal" _timestampAttribute;
```

## Properties

```
@property (T@"MSCMSTimestampAttributeInternal",&,V_timestampAttribute) timestampAttribute;
@property (T@"NSURL",&,V_serverURL) serverURL;
@property (TB,V_certChainRequested) certChainRequested;
@property (T@"MSCMSSignerInfo",R,V_signerInfo) signerInfo;
@property (T@"NSArray",R,V_certificates) certificates;
@property (T@"MSOID",R,V_digestAlgorithm) digestAlgorithm;
@property (T@"NSDate",R) timestampTime;
@property (T@"MSOID",R,&) attributeType;
```

## Instance methods

```
-[MSCMSTimestampAttribute certificates];
-[MSCMSTimestampAttribute attributeType];
-[MSCMSTimestampAttribute digestAlgorithm];
-[MSCMSTimestampAttribute serverURL];
-[MSCMSTimestampAttribute verifyTimestamps:error:];
-[MSCMSTimestampAttribute initWithAttribute:error:];
-[MSCMSTimestampAttribute setServerURL:];
-[MSCMSTimestampAttribute initWithServerURL:];
-[MSCMSTimestampAttribute certChainRequested];
-[MSCMSTimestampAttribute encodeAttributeWithError:];
-[MSCMSTimestampAttribute initWithServerURL:chainRequested:];
-[MSCMSTimestampAttribute initWithTimestampToken:];
-[MSCMSTimestampAttribute setCertChainRequested:];
-[MSCMSTimestampAttribute setTimestampAttribute:];
-[MSCMSTimestampAttribute signerInfo];
-[MSCMSTimestampAttribute timestampAttribute];
-[MSCMSTimestampAttribute timestampTime];
```
