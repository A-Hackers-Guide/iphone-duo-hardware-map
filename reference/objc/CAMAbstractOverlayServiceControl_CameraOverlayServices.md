# `CAMAbstractOverlayServiceControl`

- Image: [`/System/Library/PrivateFrameworks/CameraOverlayServices.framework/CameraOverlayServices`](../userland/System__Library__PrivateFrameworks__CameraOverlayServices.framework__CameraOverlayServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 5 properties, 15 instance methods, 2 class methods

## Instance variables

```
@"NSString" _title;
@"NSString" _imageName;
B _enabled;
B _persistentlyVisible;
@"NSString" _identifier;
q _controlType;
```

## Properties

```
@property (T@"NSString",R,N,V_identifier) identifier;
@property (Tq,R,N,V_controlType) controlType;
@property (T@"NSString",R,N,V_title) title;
@property (T@"NSString",R,N,V_imageName) imageName;
@property (TB,R,N,V_persistentlyVisible) persistentlyVisible;
```

## Class methods

```
+[CAMAbstractOverlayServiceControl supportsSecureCoding];
+[CAMAbstractOverlayServiceControl _preferredLocale];
```

## Instance methods

```
-[CAMAbstractOverlayServiceControl identifier];
-[CAMAbstractOverlayServiceControl isContentEqual:];
-[CAMAbstractOverlayServiceControl isEnabled];
-[CAMAbstractOverlayServiceControl imageName];
-[CAMAbstractOverlayServiceControl title];
-[CAMAbstractOverlayServiceControl setEnabled:];
-[CAMAbstractOverlayServiceControl controlType];
-[CAMAbstractOverlayServiceControl encodeWithCoder:];
-[CAMAbstractOverlayServiceControl description];
-[CAMAbstractOverlayServiceControl initWithCoder:];
-[CAMAbstractOverlayServiceControl copyWithZone:];
-[CAMAbstractOverlayServiceControl updateWithEnabled:];
-[CAMAbstractOverlayServiceControl validateUpdate:];
-[CAMAbstractOverlayServiceControl _initWithIdentifier:title:imageName:];
-[CAMAbstractOverlayServiceControl persistentlyVisible];
```
