# `NFCTag` (protocol)

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `NSSecureCoding`, `NSCopying`
- 0 instance variables, 3 properties, 7 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) type;
@property (T@"<NFCReaderSession>",R,W,N) session;
@property (TB,R,N,GisAvailable) available;
```

## Instance methods

```
-[NFCTag isAvailable];
-[NFCTag type];
-[NFCTag session];
-[NFCTag asNFCISO7816Tag];
-[NFCTag asNFCFeliCaTag];
-[NFCTag asNFCISO15693Tag];
-[NFCTag asNFCMiFareTag];
```
