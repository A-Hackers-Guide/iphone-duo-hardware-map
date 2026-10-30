# `FBSOrientationObserver`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 2 instance variables, 5 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"FBSActiveInterfaceOrientationObserver" _observer;
@? _handler;
```

## Properties

```
@property (T@?,C,N,V_handler) handler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSOrientationObserver activeInterfaceOrientation];
```

## Instance methods

```
-[FBSOrientationObserver _initWithObserver:];
-[FBSOrientationObserver init];
-[FBSOrientationObserver setHandler:];
-[FBSOrientationObserver invalidate];
-[FBSOrientationObserver activeInterfaceOrientation];
-[FBSOrientationObserver handler];
-[FBSOrientationObserver activeInterfaceOrientationWithCompletion:];
```
