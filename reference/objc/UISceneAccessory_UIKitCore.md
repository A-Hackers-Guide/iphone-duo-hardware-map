# `UISceneAccessory`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`
- 2 instance variables, 4 properties, 7 instance methods, 9 class methods

## Instance variables

```
@"<_UISceneCompanionImpl>" _impl;
@"NSString" _typeDescription;
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
+[UISceneAccessory externalNonInteractiveSceneAccessoryWithConfiguration:userInfo:];
+[UISceneAccessory _cameraCaptureSceneAccessoryWithConfiguration:];
+[UISceneAccessory _cameraCaptureSceneAccessoryWithConfiguration:userInfo:];
+[UISceneAccessory _highlightSceneAccessoryWithColor:];
+[UISceneAccessory _reservedSceneAccessoryWithConfiguration:];
+[UISceneAccessory _reservedSceneAccessoryWithConfiguration:userInfo:];
+[UISceneAccessory cameraCaptureSceneAccessoryWithConfiguration:];
+[UISceneAccessory cameraCaptureSceneAccessoryWithConfiguration:userInfo:];
+[UISceneAccessory externalNonInteractiveSceneAccessoryWithConfiguration:];
```

## Instance methods

```
-[UISceneAccessory debugDescription];
-[UISceneAccessory succinctDescription];
-[UISceneAccessory hash];
-[UISceneAccessory description];
-[UISceneAccessory appendDescriptionToStream:];
-[UISceneAccessory isEqual:];
-[UISceneAccessory initWithTypeDescription:impl:];
```
