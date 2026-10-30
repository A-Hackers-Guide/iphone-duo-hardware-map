# `CAMOverlayServiceToggle`

- Image: [`/System/Library/PrivateFrameworks/CameraOverlayServices.framework/CameraOverlayServices`](../userland/System__Library__PrivateFrameworks__CameraOverlayServices.framework__CameraOverlayServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMAbstractOverlayServiceControl`
- 5 instance variables, 5 properties, 16 instance methods, 1 class methods

## Instance variables

```
q _toggleType;
@"NSString" _onImageName;
@"NSString" _offImageName;
@"NSString" _onTitle;
@"NSString" _offTitle;
```

## Properties

```
@property (Tq,R,N,V_toggleType) toggleType;
@property (T@"NSString",&,N,V_onImageName) onImageName;
@property (T@"NSString",&,N,V_offImageName) offImageName;
@property (T@"NSString",R,N,V_onTitle) onTitle;
@property (T@"NSString",R,N,V_offTitle) offTitle;
```

## Class methods

```
+[CAMOverlayServiceToggle supportsSecureCoding];
```

## Instance methods

```
-[CAMOverlayServiceToggle isContentEqual:];
-[CAMOverlayServiceToggle controlType];
-[CAMOverlayServiceToggle encodeWithCoder:];
-[CAMOverlayServiceToggle initWithCoder:];
-[CAMOverlayServiceToggle copyWithZone:];
-[CAMOverlayServiceToggle toggleType];
-[CAMOverlayServiceToggle initWithIdentifier:title:imageName:onImageName:offImageName:];
-[CAMOverlayServiceToggle updateWithBooleanValue:];
-[CAMOverlayServiceToggle onTitle];
-[CAMOverlayServiceToggle offTitle];
-[CAMOverlayServiceToggle setOnImageName:];
-[CAMOverlayServiceToggle initWithIdentifier:toggleType:];
-[CAMOverlayServiceToggle offImageName];
-[CAMOverlayServiceToggle onImageName];
-[CAMOverlayServiceToggle persistentlyVisible];
-[CAMOverlayServiceToggle setOffImageName:];
```
