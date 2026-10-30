# `NFCISO7816Tag` (protocol)

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NFCTag`, `NFCNDEFTag`
- 0 instance variables, 6 properties, 7 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,&,N) initialSelectedAID;
@property (T@"NSData",R,C,N) identifier;
@property (T@"NSData",R,C,N) historicalBytes;
@property (T@"NSData",R,C,N) applicationData;
@property (TB,R,N) proprietaryApplicationDataCoding;
@property (TB,R,N) supportsPACE;
```

## Instance methods

```
-[NFCISO7816Tag identifier];
-[NFCISO7816Tag applicationData];
-[NFCISO7816Tag historicalBytes];
-[NFCISO7816Tag supportsPACE];
-[NFCISO7816Tag initialSelectedAID];
-[NFCISO7816Tag proprietaryApplicationDataCoding];
-[NFCISO7816Tag sendCommandAPDU:completionHandler:];
```
