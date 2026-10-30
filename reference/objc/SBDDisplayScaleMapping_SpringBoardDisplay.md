# `SBDDisplayScaleMapping`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardDisplay.framework/SpringBoardDisplay`](../userland/System__Library__PrivateFrameworks__SpringBoardDisplay.framework__SpringBoardDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 2 properties, 4 instance methods, 1 class methods

## Instance variables

```
Q supportedScales;
nativeResolution;
displayHardwareIdentifier;
nativePPI;
scaleMethod;
displayScaleToLogicalScale;
```

## Properties

```
@property (T@"NSString",N,R) description;
@property (TQ,N,VsupportedScales) supportedScales;
```

## Class methods

```
+[SBDDisplayScaleMapping withDisplay:];
```

## Instance methods

```
-[SBDDisplayScaleMapping init];
-[SBDDisplayScaleMapping description];
-[SBDDisplayScaleMapping supportedScales];
-[SBDDisplayScaleMapping setSupportedScales:];
```
