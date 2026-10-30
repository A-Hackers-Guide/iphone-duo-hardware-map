# `NFCISO7816Tag`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NFCTag`
- Protocols: `NFCISO7816Tag`
- 0 instance variables, 11 properties, 4 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,&,N) initialSelectedAID;
@property (T@"NSData",R,C,N) identifier;
@property (T@"NSData",R,C,N) historicalBytes;
@property (T@"NSData",R,C,N) applicationData;
@property (TB,R,N) proprietaryApplicationDataCoding;
@property (TB,R,N) supportsPACE;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N,GisAvailable) available;
```

## Instance methods

```
-[NFCISO7816Tag copyWithZone:];
-[NFCISO7816Tag supportsPACE];
-[NFCISO7816Tag initialSelectedAID];
-[NFCISO7816Tag sendCommandAPDU:completionHandler:];
```
