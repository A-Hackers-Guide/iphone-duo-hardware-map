# `NFCMiFareTag`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NFCTag`
- Protocols: `NFCMiFareTag`
- 1 instance variables, 10 properties, 6 instance methods, 0 class methods

## Instance variables

```
Q _mifareFamily;
```

## Properties

```
@property (TQ,N,V_mifareFamily) mifareFamily;
@property (T@"NSData",R,C,N) identifier;
@property (T@"NSData",R,C,N) historicalBytes;
@property (TQ,R,N) type;
@property (T@"<NFCReaderSession>",R,W,N) session;
@property (TB,R,N,GisAvailable) available;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[NFCMiFareTag copyWithZone:];
-[NFCMiFareTag initWithSession:tag:startupConfig:];
-[NFCMiFareTag mifareFamily];
-[NFCMiFareTag sendMiFareCommand:completionHandler:];
-[NFCMiFareTag sendMiFareISO7816Command:completionHandler:];
-[NFCMiFareTag setMifareFamily:];
```
