# `NFCReaderSession` (protocol)

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 6 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisReady) ready;
@property (T@"NSString",C,N) alertMessage;
```

## Instance methods

```
-[NFCReaderSession isReady];
-[NFCReaderSession alertMessage];
-[NFCReaderSession setAlertMessage:];
-[NFCReaderSession invalidateSession];
-[NFCReaderSession beginSession];
-[NFCReaderSession invalidateSessionWithErrorMessage:];
```
