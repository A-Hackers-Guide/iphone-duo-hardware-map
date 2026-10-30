# `SBDisplayScaleMapping`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSString" _displayHardwareIdentifier;
d _nativePPI;
{CGSize="width"d"height"d} _referenceSize;
Q _scaleMethod;
Q _supportedScales;
@"NSDictionary" _displayScaleToLogicalScale;
```

## Properties

```
@property (T@"NSString",R,C,N,V_displayHardwareIdentifier) displayHardwareIdentifier;
@property (TQ,R,N,V_supportedScales) supportedScales;
@property (T{CGSize=dd},R,N,V_referenceSize) referenceSize;
```

## Class methods

```
+[SBDisplayScaleMapping withDisplay:];
```

## Instance methods

```
-[SBDisplayScaleMapping referenceSize];
-[SBDisplayScaleMapping description];
-[SBDisplayScaleMapping displayHardwareIdentifier];
-[SBDisplayScaleMapping supportedScales];
-[SBDisplayScaleMapping _defaultScale];
-[SBDisplayScaleMapping createDefaultSettings];
-[SBDisplayScaleMapping initWithDisplayHardwareIdentifier:nativePPI:referenceSize:scaleMethod:supportedScales:displayScaleToLogicalScale:];
-[SBDisplayScaleMapping logicalScaleForDisplayScale:];
-[SBDisplayScaleMapping ppiForDisplayScale:];
```
