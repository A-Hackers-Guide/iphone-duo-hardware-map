# `NFCTagCommandConfiguration`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 2 instance variables, 2 properties, 5 instance methods, 0 class methods

## Instance variables

```
Q _maximumRetries;
d _retryInterval;
```

## Properties

```
@property (TQ,N,V_maximumRetries) maximumRetries;
@property (Td,N,V_retryInterval) retryInterval;
```

## Instance methods

```
-[NFCTagCommandConfiguration setRetryInterval:];
-[NFCTagCommandConfiguration copyWithZone:];
-[NFCTagCommandConfiguration retryInterval];
-[NFCTagCommandConfiguration maximumRetries];
-[NFCTagCommandConfiguration setMaximumRetries:];
```
