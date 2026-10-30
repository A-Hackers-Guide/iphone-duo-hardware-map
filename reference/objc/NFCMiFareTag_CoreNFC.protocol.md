# `NFCMiFareTag` (protocol)

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NFCTag`, `NFCNDEFTag`
- 0 instance variables, 3 properties, 5 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) mifareFamily;
@property (T@"NSData",R,C,N) identifier;
@property (T@"NSData",R,C,N) historicalBytes;
```

## Instance methods

```
-[NFCMiFareTag identifier];
-[NFCMiFareTag historicalBytes];
-[NFCMiFareTag mifareFamily];
-[NFCMiFareTag sendMiFareCommand:completionHandler:];
-[NFCMiFareTag sendMiFareISO7816Command:completionHandler:];
```
