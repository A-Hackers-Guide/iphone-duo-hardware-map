# `NFCNDEFTag` (protocol)

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `NSSecureCoding`, `NSCopying`
- 0 instance variables, 1 properties, 5 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisAvailable) available;
```

## Instance methods

```
-[NFCNDEFTag isAvailable];
-[NFCNDEFTag writeLockWithCompletionHandler:];
-[NFCNDEFTag queryNDEFStatusWithCompletionHandler:];
-[NFCNDEFTag readNDEFWithCompletionHandler:];
-[NFCNDEFTag writeNDEF:completionHandler:];
```
