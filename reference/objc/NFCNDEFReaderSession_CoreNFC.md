# `NFCNDEFReaderSession`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NFCReaderSession`
- Protocols: `NFReaderSessionCallbacks`
- 2 instance variables, 4 properties, 7 instance methods, 1 class methods

## Instance variables

```
B _invalidateAfterFirstRead;
Q _tagsRead;
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
+[NFCNDEFReaderSession readingAvailable];
```

## Instance methods

```
-[NFCNDEFReaderSession didDetectNDEFMessages:fromTags:connectedTagIndex:updateUICallback:];
-[NFCNDEFReaderSession didTerminate:];
-[NFCNDEFReaderSession restartPolling];
-[NFCNDEFReaderSession connectToTag:completionHandler:];
-[NFCNDEFReaderSession _callbackDidBecomeActive];
-[NFCNDEFReaderSession initWithDelegate:queue:invalidateAfterFirstRead:];
-[NFCNDEFReaderSession initWithDelegate:queue:pollMethod:];
```
