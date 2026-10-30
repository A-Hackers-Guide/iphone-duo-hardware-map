# `NFCTagReaderSession`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NFCReaderSession`
- Protocols: `NFReaderSessionCallbacks`
- 2 instance variables, 5 properties, 10 instance methods, 2 class methods

## Instance variables

```
@ _swiftDelegateWrapper;
@"<NFCTag>" _connectedTag;
```

## Properties

```
@property (T@"<NFCTag>",R,&,N,V_connectedTag) connectedTag;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[NFCTagReaderSession readingAvailable];
+[NFCTagReaderSession isPaymentSession];
```

## Instance methods

```
-[NFCTagReaderSession didDetectTags:connectedTagIndex:];
-[NFCTagReaderSession restartPolling];
-[NFCTagReaderSession connectToTag:completionHandler:];
-[NFCTagReaderSession _callbackDidBecomeActive];
-[NFCTagReaderSession _restartPollingWithConfig:];
-[NFCTagReaderSession connectedTag];
-[NFCTagReaderSession initWithConfiguration:delegate:queue:];
-[NFCTagReaderSession initWithPollConfig:swiftDelegate:sessionType:queue:];
-[NFCTagReaderSession initWithPollingOption:delegate:queue:];
-[NFCTagReaderSession restartPollingWithConfiguration:];
```
