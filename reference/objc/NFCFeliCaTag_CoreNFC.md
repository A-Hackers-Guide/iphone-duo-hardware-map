# `NFCFeliCaTag`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NFCTag`
- Protocols: `NFCFeliCaTag`
- 0 instance variables, 9 properties, 13 instance methods, 0 class methods

## Properties

```
@property (T@"NSData",R,&,N) currentSystemCode;
@property (T@"NSData",R,&,N) currentIDm;
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
-[NFCFeliCaTag copyWithZone:];
-[NFCFeliCaTag resetModeWithCompletionHandler:];
-[NFCFeliCaTag currentIDm];
-[NFCFeliCaTag currentSystemCode];
-[NFCFeliCaTag pollingWithSystemCode:requestCode:timeSlot:completionHandler:];
-[NFCFeliCaTag readWithoutEncryptionWithServiceCodeList:blockList:completionHandler:];
-[NFCFeliCaTag requestResponseWithCompletionHandler:];
-[NFCFeliCaTag requestServiceV2WithNodeCodeList:completionHandler:];
-[NFCFeliCaTag requestServiceWithNodeCodeList:completionHandler:];
-[NFCFeliCaTag requestSpecificationVersionWithCompletionHandler:];
-[NFCFeliCaTag requestSystemCodeWithCompletionHandler:];
-[NFCFeliCaTag sendFeliCaCommandPacket:completionHandler:];
-[NFCFeliCaTag writeWithoutEncryptionWithServiceCodeList:blockList:blockData:completionHandler:];
```
