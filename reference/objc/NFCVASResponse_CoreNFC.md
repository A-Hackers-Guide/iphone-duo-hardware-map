# `NFCVASResponse`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
q _status;
@"NSData" _vasData;
@"NSData" _mobileToken;
```

## Properties

```
@property (Tq,R,N,V_status) status;
@property (T@"NSData",R,&,N,V_vasData) vasData;
@property (T@"NSData",R,&,N,V_mobileToken) mobileToken;
```

## Instance methods

```
-[NFCVASResponse init];
-[NFCVASResponse status];
-[NFCVASResponse copyWithZone:];
-[NFCVASResponse vasData];
-[NFCVASResponse mobileToken];
-[NFCVASResponse initWithStatus:data:mobileToken:];
```
