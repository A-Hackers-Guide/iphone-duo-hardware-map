# `FBSActiveInterfaceOrientationState`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `BSXPCSecureCoding`, `NSCopying`
- 2 instance variables, 6 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"FBSDisplayIdentity" _displayIdentity;
q _interfaceOrientation;
```

## Properties

```
@property (T@"FBSDisplayIdentity",R,N,V_displayIdentity) displayIdentity;
@property (Tq,R,N,V_interfaceOrientation) interfaceOrientation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSActiveInterfaceOrientationState supportsBSXPCSecureCoding];
```

## Instance methods

```
-[FBSActiveInterfaceOrientationState interfaceOrientation];
-[FBSActiveInterfaceOrientationState hash];
-[FBSActiveInterfaceOrientationState description];
-[FBSActiveInterfaceOrientationState appendDescriptionToStream:];
-[FBSActiveInterfaceOrientationState encodeWithBSXPCCoder:];
-[FBSActiveInterfaceOrientationState initWithBSXPCCoder:];
-[FBSActiveInterfaceOrientationState copyWithZone:];
-[FBSActiveInterfaceOrientationState isEqual:];
-[FBSActiveInterfaceOrientationState displayIdentity];
-[FBSActiveInterfaceOrientationState _initWithDisplayIdentity:interfaceOrientation:];
```
