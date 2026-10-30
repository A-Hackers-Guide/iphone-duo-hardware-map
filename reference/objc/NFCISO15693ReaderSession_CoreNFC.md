# `NFCISO15693ReaderSession`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NFCReaderSession`
- Protocols: `NFReaderSessionCallbacks`
- 0 instance variables, 4 properties, 3 instance methods, 1 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[NFCISO15693ReaderSession readingAvailable];
```

## Instance methods

```
-[NFCISO15693ReaderSession initWithDelegate:queue:];
-[NFCISO15693ReaderSession didDetectTags:connectedTagIndex:];
-[NFCISO15693ReaderSession restartPolling];
```
