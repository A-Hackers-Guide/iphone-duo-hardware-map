# `NFCVASCommandConfiguration`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
q _mode;
@"NSString" _passTypeIdentifier;
@"NSURL" _url;
```

## Properties

```
@property (Tq,N,V_mode) mode;
@property (T@"NSString",&,N,V_passTypeIdentifier) passTypeIdentifier;
@property (T@"NSURL",&,N,V_url) url;
```

## Instance methods

```
-[NFCVASCommandConfiguration init];
-[NFCVASCommandConfiguration setMode:];
-[NFCVASCommandConfiguration mode];
-[NFCVASCommandConfiguration description];
-[NFCVASCommandConfiguration setUrl:];
-[NFCVASCommandConfiguration copyWithZone:];
-[NFCVASCommandConfiguration url];
-[NFCVASCommandConfiguration passTypeIdentifier];
-[NFCVASCommandConfiguration setPassTypeIdentifier:];
-[NFCVASCommandConfiguration initWithVASMode:passTypeIdentifier:url:];
```
