# `AHFManager`

- Image: [`/System/Library/PrivateFrameworks/AppleHIDFeedback.framework/AppleHIDFeedback`](../userland/System__Library__PrivateFrameworks__AppleHIDFeedback.framework__AppleHIDFeedback.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"AHFTrackpadController" _trackpadController;
@"AHFPencilController" _pencilController;
```

## Properties

```
@property (T@"AHFTrackpadController",&,N,V_trackpadController) trackpadController;
@property (T@"AHFPencilController",&,N,V_pencilController) pencilController;
```

## Class methods

```
+[AHFManager sharedInstance];
```

## Instance methods

```
-[AHFManager init];
-[AHFManager pencilController];
-[AHFManager playFeedback:powerSourceID:timestamp:error:];
-[AHFManager playFeedback:senderID:timestamp:error:];
-[AHFManager setPencilController:];
-[AHFManager setTrackpadController:];
-[AHFManager trackpadController];
```
