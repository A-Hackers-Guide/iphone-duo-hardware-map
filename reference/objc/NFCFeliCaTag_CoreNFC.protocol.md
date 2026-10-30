# `NFCFeliCaTag` (protocol)

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NFCTag`, `NFCNDEFTag`
- 0 instance variables, 2 properties, 12 instance methods, 0 class methods

## Properties

```
@property (T@"NSData",R,&,N) currentSystemCode;
@property (T@"NSData",R,&,N) currentIDm;
```

## Instance methods

```
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
