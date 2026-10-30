# `SBFDisplayProxy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 16 instance methods, 4 class methods

## Instance variables

```
B _external;
@"NSString" _identifier;
q _surfaceType;
q _appliedContentMode;
q _targetContentMode;
```

## Properties

```
@property (T@"NSString",C,N,V_identifier) identifier;
@property (Tq,N,V_surfaceType) surfaceType;
@property (TB,N,GisExternal,V_external) external;
@property (Tq,N,V_appliedContentMode) appliedContentMode;
@property (Tq,N,V_targetContentMode) targetContentMode;
```

## Class methods

```
+[SBFDisplayProxy coverIntegratedDisplayWithIdentifier:];
+[SBFDisplayProxy defaultIntegratedDisplayWithIdentifier:];
+[SBFDisplayProxy externalDisplayWithIdentifier:];
+[SBFDisplayProxy innerIntegratedDisplayWithIdentifier:];
```

## Instance methods

```
-[SBFDisplayProxy isExternal];
-[SBFDisplayProxy debugDescription];
-[SBFDisplayProxy surfaceType];
-[SBFDisplayProxy identifier];
-[SBFDisplayProxy succinctDescription];
-[SBFDisplayProxy setIdentifier:];
-[SBFDisplayProxy setExternal:];
-[SBFDisplayProxy hash];
-[SBFDisplayProxy description];
-[SBFDisplayProxy appendDescriptionToStream:];
-[SBFDisplayProxy setSurfaceType:];
-[SBFDisplayProxy isEqual:];
-[SBFDisplayProxy appliedContentMode];
-[SBFDisplayProxy setAppliedContentMode:];
-[SBFDisplayProxy setTargetContentMode:];
-[SBFDisplayProxy targetContentMode];
```
