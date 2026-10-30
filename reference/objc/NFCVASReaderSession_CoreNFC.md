# `NFCVASReaderSession`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NFCReaderSession`
- Protocols: `NFReaderSessionCallbacks`
- 2 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NFTimer" _presenceCheckTimer;
@"NSArray" _vasConfig;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[NFCVASReaderSession readingAvailable];
```

## Instance methods

```
-[NFCVASReaderSession dealloc];
-[NFCVASReaderSession beginSession];
-[NFCVASReaderSession didDetectTags:connectedTagIndex:];
-[NFCVASReaderSession didTerminate:];
-[NFCVASReaderSession _callbackDidBecomeActive];
-[NFCVASReaderSession _convertVASConfigToInternalRequest:];
-[NFCVASReaderSession _convertVASResponseToExternal:];
-[NFCVASReaderSession _sendVASRequests:error:];
-[NFCVASReaderSession initWithVASCommandConfigurations:delegate:queue:];
```
