# `TUContactImageResponse`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSData" _imageData;
q _imageType;
```

## Properties

```
@property (T@"NSData",R,N,V_imageData) imageData;
@property (Tq,R,N,V_imageType) imageType;
```

## Class methods

```
+[TUContactImageResponse supportsSecureCoding];
```

## Instance methods

```
-[TUContactImageResponse imageType];
-[TUContactImageResponse imageData];
-[TUContactImageResponse encodeWithCoder:];
-[TUContactImageResponse description];
-[TUContactImageResponse initWithCoder:];
-[TUContactImageResponse initWithImageData:type:];
```
